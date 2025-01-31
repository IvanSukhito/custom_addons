from odoo import models, fields, api
import logging


_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    
    _inherit = "purchase.order"


    num_total_product = fields.Integer(
        string= "Total Product",
        compute= "_compute_total_products",
        store= True
    )
    num_total_product_qty = fields.Integer(
        string= "Total Qty",
        compute= "_compute_total_products",
        store= True
    )
    num_total_invoices = fields.Integer(
        string= "Total Invoices",
        compute= "_compute_total_products",
        store= True
    )
    num_total_invoices_paid = fields.Integer(
        string= "Total Invoices Paid",
        compute= "_compute_total_products",
        store= True
    )

    hide_customize = fields.Boolean(string="Hide")
    update_state = fields.Boolean(default=False)  # contoh custom field
    company_is_to_show = fields.Boolean(string="Is To SHow", related="company_id.is_to_show", store=False)
    
    @api.depends('order_line.product_qty','order_line.product_id','invoice_ids','invoice_ids.payment_state')
    def _compute_total_products(self):

        _logger.info("This is an INFO log message.%s")
        _logger.warning("This is a WARNING log message.")
        _logger.error("This is an ERROR log message.")
        for o in self:

            total_qty = sum(o.order_line.mapped('product_qty'))
            total_product = len(o.order_line.mapped('product_id'))
            paid_invoices = o.invoice_ids.filtered(lambda inv: inv.payment_state == 'paid')
            total_invoices = len(o.invoice_ids)
            o.num_total_product_qty = total_qty
            o.num_total_product = total_product
            o.num_total_invoices = total_invoices
            o.num_total_invoices_paid = len(paid_invoices)
            
    
    # fungsion update masal tambah button
    def to_draft(self):
        for record in self:
            if record.state != 'draft':
                record.state = 'draft'
 
    # @api.depends(num_total_product,num_total_product_qty, num_total_invoices,num_total_invoices_paid)
    # def to_show_customize(self):
    #       for record in self:
    #         #   # Perform action based on toggle state
    #         if record.is_to_show and self.env.company.root_id:
    #             record.is_to_show = False; 
    #         else:
    #             record.is_to_show = True;
    
    #def action_toggle_function(self):
    #    # Logic for toggling action
    #    for order in self:
    #        if order.toggle_button:
    #            # Action when the toggle is ON
    #            print("Toggle ON")
    #        else:
    #            # Action when the toggle is OFF
    #            print("Toggle OFF")