frappe.listview_settings['Lead'] = {
    onload: function (listview) {
        listview.page.add_inner_button(__('Convert to Customer'), function () {
            const selected = listview.get_checked_items();

            if (!selected.length) {
                frappe.msgprint(__('Please select at least one lead to convert.'));
                return;
            }

            const lead_names = selected.map(item => item.name);

            frappe.call({
                method: "custom_crm.custom_crm.doctype.lead.bulk_convert.convert_to_customer",
                args: {
                    leads: lead_names
                },
                callback: function (response) {
                    if (!response.exc) {
                        frappe.msgprint(__("{0} leads converted successfully.", [response.message]));
                        listview.refresh();
                    }
                }
            });
        }, __('Actions'));
    }
};
