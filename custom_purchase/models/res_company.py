from odoo import models, fields


class res_company(models.Model):
    _inherit = "res.company"

    is_to_show= fields.Boolean(
        string="Toggle Button", 
        default= True
    ) 