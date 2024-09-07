from frappe import _


def get_data():
    return {
        "fieldname": "bank_account",
        "transactions": [
            {
                "label": _("Payments"),
                "items": ["Payment Record"],
            },
            {"label": _("Contacts"), "items": ["Person Contact", "Company Contact"]},
        ],
    }
