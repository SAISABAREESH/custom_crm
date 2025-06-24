import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def execute():
    create_custom_field("Event", {
        "fieldname": "send_reminder",
        "label": "Send Reminder",
        "fieldtype": "Check",
        "insert_after": "subject",
        "default": 1
    })
