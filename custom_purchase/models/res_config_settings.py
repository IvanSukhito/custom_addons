from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_to_show = fields.Boolean(
        string="Show Customization",
        help="Toggle to show or hide the Total Product, Total Qty, Total Invocies, Total Invoices Paid .",
    )

    