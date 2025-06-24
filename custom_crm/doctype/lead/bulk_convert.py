import frappe
from frappe import _

@frappe.whitelist()
def convert_to_customer(leads):
    leads = frappe.parse_json(leads)
    converted = 0

    for lead_name in leads:
        lead = frappe.get_doc("Lead", lead_name)

        # Check if customer already exists with this lead
        if not frappe.db.exists("Customer", {"lead_name": lead.name}):
            customer = frappe.get_doc({
                "doctype": "Customer",
                "customer_name": lead.lead_name or lead_name,
                "customer_type": "Individual",
                "lead_name": lead.name
            })
            customer.insert(ignore_permissions=True)
            frappe.db.commit()  # Commit after insert
            converted += 1

    return {"converted": converted}

