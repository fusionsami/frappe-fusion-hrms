import frappe
from frappe.core.doctype.doctype.doctype import validate_permissions_for_doctype

def after_install():
    create_custom_doctype()
    add_permissions_to_employee()

def create_custom_doctype():
    if not frappe.db.exists("DocType", "Custom DocType"):
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": "Custom DocType",
            "module": "Frappe Fusion Hrms",
            "custom": 1,
            "fields": [
                {"fieldname": "custom_field", "label": "Custom Field", "fieldtype": "Data"}
            ],
            "permissions": [
                {"role": "Employee", "read": 1, "write": 1, "create": 1, "delete": 1}
            ]
        })
        doc.insert()
        frappe.db.commit()

def add_permissions_to_employee():
    doc = frappe.get_doc("DocType", "Custom DocType")
    if not any(perm.role == "Employee" for perm in doc.permissions):
        doc.append("permissions", {
            "role": "Employee",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1
        })
        doc.save()
        validate_permissions_for_doctype("Custom DocType")
        frappe.db.commit()
