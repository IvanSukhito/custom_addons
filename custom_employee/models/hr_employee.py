from odoo import models, fields, api


class HrEmployeePrivate(models.Model):
    _inherit = 'hr.employee'

    column_static = fields.Char(string="Custom Field Static", compute="_compute_custom_backend_fields", store=False)
    company_custom = fields.Char(string="company_custom", compute="_compute_filter_list_bycompany", store=False)
    is_column_visible = fields.Boolean(
        string='Show Column For Company',
        default = False,
        help = "Toogle to show or hide the column",
    )
    list_company_active = fields.Many2one(
         'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
    )

    @api.depends()
    def _compute_custom_backend_fields(self):
        for r in self:
            r.column_static = f'Emp-{r.mobile_phone or 'kosong'}'
    
   
    @api.onchange(list_company_active)
    def _compute_filter_listcustom(self):
        for r in self:
            if r.list_company_active:
                print(f"Company Aktif: {r.list_company_active}")
    # @api.model
    # def default_get(self, fields_list):
    #     res =  super().default_get(fields_list)
    #     if self.env.user.company_id.id == 1:
    #         res['is_column_visible'] = True
    #     else:
    #         res['is_column_visible'] = False
        
    #     return res
