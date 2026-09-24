-- statement
create table if not exists SandboxMetadata(Key text primary key,Value text not null);
-- statement
create table if not exists ProductCategory(CategoryId integer primary key,CategoryName text not null unique,Active integer not null);
-- statement
create table if not exists Customer(CustomerId integer primary key,CompanyName text not null,Email text not null,Phone text,Active integer not null,Description text,CreatedOn text not null);
-- statement
create table if not exists Product(ProductId integer primary key,ProductName text not null,CategoryId integer not null references ProductCategory(CategoryId),UnitPrice numeric not null,Discontinued integer not null,Sku text not null unique);
-- statement
create table if not exists Employee(EmployeeId integer primary key,DisplayName text not null,Email text not null,HireDate text not null,Active integer not null);
-- statement
create table if not exists Warehouse(WarehouseId integer primary key,WarehouseName text not null,City text not null,Active integer not null);
-- statement
create table if not exists Orders(OrderId integer primary key,CustomerId integer not null references Customer(CustomerId),EmployeeId integer references Employee(EmployeeId),OrderDate text not null,Status integer not null,Reference text,Total numeric not null);
-- statement
create table if not exists OrderDetail(OrderDetailId integer primary key,OrderId integer not null references Orders(OrderId),ProductId integer not null references Product(ProductId),Quantity integer not null,UnitPrice numeric not null,LineTotal numeric not null);
-- statement
create table if not exists Inventory(InventoryId integer primary key,WarehouseId integer not null references Warehouse(WarehouseId),ProductId integer not null references Product(ProductId),QuantityOnHand integer not null,ReorderLevel integer not null,unique(WarehouseId,ProductId));
-- statement
insert or ignore into SandboxMetadata values('SeedIdentity','SaySolSandboxSeed/v1');
-- statement
with recursive n(i) as(values(1) union all select i+1 from n where i<6) insert or ignore into ProductCategory select i,printf('Category %02d',i),1 from n;
-- statement
with recursive n(i) as(values(1) union all select i+1 from n where i<30) insert or ignore into Customer select i,printf('Customer %03d',i),printf('customer%03d@example.test',i),printf('+1-555-%04d',i),case when i%9=0 then 0 else 1 end,case when i%5=0 then null else printf('Account %03d',i) end,printf('2026-01-%02d',i%28+1) from n;
-- statement
with recursive n(i) as(values(1) union all select i+1 from n where i<30) insert or ignore into Product select i,printf('Product %03d',i),(i-1)%6+1,5+i*2.25,case when i%13=0 then 1 else 0 end,printf('SKU-%04d',i) from n;
-- statement
with recursive n(i) as(values(1) union all select i+1 from n where i<8) insert or ignore into Employee select i,printf('Employee %02d',i),printf('employee%02d@example.test',i),printf('2024-%02d-15',(i-1)%12+1),1 from n;
-- statement
insert or ignore into Warehouse values(1,'Warehouse 01','Austin',1),(2,'Warehouse 02','Reno',1),(3,'Warehouse 03','Columbus',1),(4,'Warehouse 04','Savannah',1);
-- statement
with recursive n(i) as(values(1) union all select i+1 from n where i<100) insert or ignore into Orders select i,(i-1)%30+1,(i-1)%8+1,printf('2026-%02d-%02d',(i-1)%9+1,(i-1)%28+1),i%4+1,case when i%6=0 then null else printf('PO-%04d',i) end,0 from n;
-- statement
with recursive o(i) as(values(1) union all select i+1 from o where i<100),l(j) as(values(1) union all select j+1 from l where j<3) insert or ignore into OrderDetail select (i-1)*3+j,i,(i*3+j-2)%30+1,(i+j)%7+1,5+((i*3+j-2)%30+1)*2.25,((i+j)%7+1)*(5+((i*3+j-2)%30+1)*2.25) from o cross join l;
-- statement
update Orders set Total=(select sum(LineTotal) from OrderDetail where OrderDetail.OrderId=Orders.OrderId);
-- statement
with recursive w(i) as(values(1) union all select i+1 from w where i<4),p(j) as(values(1) union all select j+1 from p where j<30) insert or ignore into Inventory select (i-1)*30+j,i,j,(i*17+j*3)%101,10+j%8 from w cross join p;
