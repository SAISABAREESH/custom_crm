
# Custom CRM

A Frappe-based custom CRM extension that includes:

- ✅ Bulk lead conversion to customers from the Lead list view
- 📧 Automatic email reminders for upcoming Events
- 🧩 A custom field (`send_reminder`) added to Event for toggle-based reminders

---

## 🚀 Features

### 1. Bulk Convert Leads
- Adds a **"Convert to Customer"** button in the Lead list view.
- Converts selected Leads into Customers.
- Prevents duplicate Customers by checking `lead_name`.

> Location: `lead_bulk_action.js`, `bulk_convert.py`

### 2. Auto Event Reminders
- Sends email reminders for upcoming Events that have `send_reminder` checked.
- Timeframes: **1 hour**, **1 day**, **1 week**.
- Scheduled to run **hourly** using Frappe's scheduler.

> Location: `event.py`, `hooks.py`

### 3. Custom Field: `send_reminder`
- Automatically added to the Event doctype using a patch script.
- Default is **checked** (1).

> Location: `add_reminder_field.py`

---

## 🛠️ Installation

1. Clone this repo into your Frappe bench:
    ```bash
    bench get-app custom_crm
    bench --site yoursite install-app custom_crm
    ```

2. Run the custom field patch (optional if you're not using fixtures):
    ```bash
    bench --site yoursite execute custom_crm.add_reminder_field.execute
    ```

3. Make sure the scheduler is enabled:
    ```bash
    bench --site yoursite enable-scheduler
    ```

4. Restart the bench:
    ```bash
    bench restart
    ```

---

## 🔄 File References

| File | Purpose |
|------|---------|
| `lead_bulk_action.js` | JS code to inject custom button in Lead list |
| `bulk_convert.py` | Python backend logic to convert Leads |
| `event.py` | Python logic to send email reminders |
| `hooks.py` | App metadata, doctype JS injection, scheduler hook |
| `add_reminder_field.py` | Patch to create custom checkbox field on Event |

---

## 📬 Email Configuration

Ensure email is properly set up in your site for reminders to work:

```bash
Email Account > SMTP Settings > Enable Outgoing
```

---

## 📄 License

MIT License

---

## 👤 Author

Your Name or Company  
Email: your@email.com
