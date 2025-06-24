frappe.listview_settings['Lead'] = {
    onload: function(listview) {
        listview.page.add_inner_button(__('Bulk Actions'), () => {}, 'Actions');
        
        listview.page.add_inner_button(__('Convert to Customer'), async () => {
            let selected = listview.get_checked_items();
            if (!selected.length) {
                frappe.msgprint(__('Please select leads.'));
                return;
            }

            frappe.call({
                method: "custom_crm.custom_crm.doctype.lead.bulk_convert.convert_to_customer",
                args: { leads: selected.map(lead => lead.name) },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.msgprint(__('Converted {0} leads successfully.', [r.message]));
                        listview.refresh();
                    }
                }
            });
        }, 'Bulk Actions');
    }
};

