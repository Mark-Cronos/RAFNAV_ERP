import frappe


def execute():
    frappe.reload_doctype("Project Task")

    # add "Completed" if customized
    property_setter_name = frappe.db.exists(
        "Property Setter",
        dict(doc_type="Project Task", field_name="status", property="options"),
    )
    if property_setter_name:
        property_setter = frappe.get_doc("Property Setter", property_setter_name)
        if "Completed" not in property_setter.value:
            property_setter.value = property_setter.value + "\nCompleted"
            property_setter.save()

    # renamed default status to Completed as status "Closed" is ambiguous
    frappe.db.sql(
        'update `tabProject Task` set status = "Completed" where status = "Closed"'
    )
