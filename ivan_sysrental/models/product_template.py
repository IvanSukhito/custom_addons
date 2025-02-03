from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    rental_price = fields.Float(string="Rental Price")
    is_rental = fields.Boolean(string="Is SysRental Product", default=False)
    # is_sysrental = fields.Boolean(string="Sys rental ?")
    # rental_count = fields.Float(string="Rental Count", compute="_compute_rental_count")


    def action_product_sysrental(self):
        self.ensure_one()
        ptl_id = self.id
        domain = [('is_rental_line', '=', True), ('product_template_id', '=', ptl_id)]
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rental Product Timeline',
            'view_mode': 'timeline',
            'view_id': self.env.ref('ivan_sysrental.sol_rental_timeline_action').id,
            'res_model': 'sale.order.line',
            'context': "{'create': False}",
            'domain': domain
        }
    
    # def _compute_rental_count(self):
        # for rec in self:
            # if rec.is_rental:
                # rented_product = self.env["sale.order.line"].search([('is_rental_line', '=', True), ('product_template_id', '=', rec.id)])
                # delivered_count = sum(rented_product.mapped('qty_delivered'))
                # returned_count = sum(rented_product.mapped('qty_returned'))
                # rec.rental_count = delivered_count - returned_count
            # else:
                # rec.rental_count = 0.0