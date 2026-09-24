import { Decorators, EntityGrid } from "@serenity-is/corelib";
export enum OrderStatus { Draft=1, Submitted=2, Shipped=3, Cancelled=4 }
export interface CustomerRow { customerId?:number; companyName?:string; email?:string; phone?:string; active?:boolean; }
export interface ProductRow { productId?:number; productName?:string; categoryId?:number; unitPrice?:number; discontinued?:boolean; }
export interface OrderRow { orderId?:number; customerId?:number; employeeId?:number; orderDate?:string; status?:OrderStatus; total?:number; }
export interface OrderDetailRow { orderDetailId?:number; orderId?:number; productId?:number; quantity?:number; unitPrice?:number; lineTotal?:number; }
@Decorators.registerClass("SaySolSandbox.Business.CustomerGrid")
export class CustomerGrid extends EntityGrid<CustomerRow> {}
@Decorators.registerClass("SaySolSandbox.Business.ProductGrid")
export class ProductGrid extends EntityGrid<ProductRow> {}
@Decorators.registerClass("SaySolSandbox.Business.OrderGrid")
export class OrderGrid extends EntityGrid<OrderRow> {}
