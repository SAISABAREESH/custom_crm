import frappe
from frappe.utils import now_datetime, add_to_date
from frappe.core.doctype.communication.email import make
from frappe.core.doctype.user.user import get_user_fullname

def send_event_reminders():
    now = now_datetime()

    time_frames = {
        "1_hour": add_to_date(now, hours=1),
        "1_day": add_to_date(now, days=1),
        "1_week": add_to_date(now, weeks=1),
    }

    for label, time_point in time_frames.items():
        events = frappe.get_all("Event", filters={
            "send_reminder": 1,
            "starts_on": ["between", [now, time_point]]
        }, fields=["name", "subject", "starts_on", "owner"])

        for event in events:
            owner_email = frappe.db.get_value("User", event.owner, "email")
            frappe.sendmail(
                recipients=[owner_email],
                subject=f"Reminder: Upcoming Event - {event.subject}",
                message=f"Event **{event.subject}** is scheduled on {event.starts_on}."
            )
