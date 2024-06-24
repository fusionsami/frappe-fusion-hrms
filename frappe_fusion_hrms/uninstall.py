import frappe

def before_uninstall():
    delete_custom_doctype()

def delete_custom_doctype():
    if frappe.db.exists("DocType", "Custom DocType"):
        frappe.delete_doc("DocType", "Custom DocType", ignore_permissions=True)
        frappe.db.commit()

