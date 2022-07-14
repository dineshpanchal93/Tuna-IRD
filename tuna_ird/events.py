import frappe

def update_sales_invoice_oncancel(doc,method =None):
    frappe.db.set_value("Sales Invoice",doc.name,{"title":"Cancelled","customer_name":"Cancelled","customer":"Cancelled","total_qty":0,"total":0,"grand_total":0,"rounded_total":0,"in_words":"NA","rounding_adjustment":0,"total_taxes_and_charges":0,"outstanding_amount":0,"base_net_total":0,"base_rounded_total":0,"outstanding_amount":0})
    frappe.db.commit()
    for i in doc.items:
        db_update = frappe.db.set_value("Sales Invoice Item",i.name,{"qty":0,"rate":0,"amount":0,"base_rate":0,"base_amount":0,
                                                      "net_rate":0,
                                                      "net_amount":0,
                                                      "base_net_rate":0,
                                                      "base_net_amount":0})
        frappe.db.commit()
    for j in doc.payment_schedule:
        db_update_pay = frappe.db.set_value("Payment Schedule",j.name,{"payment_amount":0,"base_payment_amount":0})
        frappe.db.commit()
