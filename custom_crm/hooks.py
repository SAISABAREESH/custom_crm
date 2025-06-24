app_name = "Bulk and "
app_title = "Custom CRM"
app_publisher = "Your Name or Company"
app_description = "A custom CRM built with Frappe"
app_email = "your@email.com"
app_license = "MIT"  # Or the license you are using
app_version = "1.0.0"

# Include JS in Lead doctype
doctype_js = {
    "Lead": "public/js/lead_bulk_action.js"
}

# Scheduler event for hourly reminders
scheduler_events = {
    "hourly": [
        "custom_crm.custom_crm.doctype.event.event.send_event_reminders"
    ]
}

# Patch for adding reminder field (optional, if used)
# Add this only if using frappe patches
# fixtures = ["Custom Field"]   # optional if you're exporting fields
