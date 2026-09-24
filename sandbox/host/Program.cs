using Microsoft.Data.Sqlite;
var builder=WebApplication.CreateBuilder(args);var app=builder.Build();
var database=Path.Combine(app.Environment.ContentRootPath,"App_Data","SaySolSandbox.sqlite");
Directory.CreateDirectory(Path.GetDirectoryName(database)!);
using(var c=new SqliteConnection($"Data Source={database};Pooling=False")){c.Open();using var tx=c.BeginTransaction();foreach(var sql in File.ReadAllText(Path.Combine(AppContext.BaseDirectory,"Migrations","DefaultDB","baseline.sql")).Split("-- statement",StringSplitOptions.RemoveEmptyEntries)){using var cmd=c.CreateCommand();cmd.Transaction=tx;cmd.CommandText=sql;cmd.ExecuteNonQuery();}tx.Commit();}
var expected=new Dictionary<string,long>{{"ProductCategory",6},{"Customer",30},{"Product",30},{"Employee",8},{"Warehouse",4},{"Orders",100},{"OrderDetail",300},{"Inventory",120}};
object Inspect(){using var c=new SqliteConnection($"Data Source={database};Mode=ReadOnly;Pooling=False");c.Open();var counts=new Dictionary<string,long>();foreach(var item in expected){using var cmd=c.CreateCommand();cmd.CommandText=$"select count(*) from {item.Key}";counts[item.Key]=Convert.ToInt64(cmd.ExecuteScalar());}using var seed=c.CreateCommand();seed.CommandText="select Value from SandboxMetadata where Key='SeedIdentity'";var identity=Convert.ToString(seed.ExecuteScalar());return new{passed=counts.All(x=>x.Value==expected[x.Key])&&identity=="SaySolSandboxSeed/v1",counts,seedIdentity=identity,serenityVersion="10.5.2"};}
app.MapGet("/health/baseline",Inspect);
app.MapGet("/api/customers",()=>Query("select CustomerId,CompanyName,Email,Phone,Active from Customer order by CustomerId"));
app.MapGet("/api/products",()=>Query("select ProductId,ProductName,CategoryId,UnitPrice,Discontinued from Product order by ProductId"));
app.MapGet("/api/orders",()=>Query("select OrderId,CustomerId,EmployeeId,OrderDate,Status,Total from Orders order by OrderId"));
List<Dictionary<string,object?>> Query(string sql){using var c=new SqliteConnection($"Data Source={database};Mode=ReadOnly;Pooling=False");c.Open();using var cmd=c.CreateCommand();cmd.CommandText=sql;using var r=cmd.ExecuteReader();var rows=new List<Dictionary<string,object?>>();while(r.Read()){var row=new Dictionary<string,object?>();for(var i=0;i<r.FieldCount;i++)row[r.GetName(i)]=r.IsDBNull(i)?null:r.GetValue(i);rows.Add(row);}return rows;}
if(args.Contains("--validate-baseline")){var json=System.Text.Json.JsonSerializer.Serialize(Inspect());Console.WriteLine(json);var pass=json.Contains("\"passed\":true");Console.WriteLine(pass?"SAYSOL SANDBOX DATABASE: PASS":"SAYSOL SANDBOX DATABASE: FAIL");return pass?0:1;}
app.Run();return 0;
