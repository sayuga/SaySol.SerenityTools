import {readFileSync} from "node:fs";
const source=readFileSync(new URL("../Modules/Business/Domain.ts",import.meta.url),"utf8");
for(const expected of ["CustomerGrid","ProductGrid","OrderGrid","OrderDetailRow","OrderStatus"])
 if(!source.includes(expected)) throw new Error("Missing frontend artifact: "+expected);
console.log("Sandbox frontend artifacts: PASS");
