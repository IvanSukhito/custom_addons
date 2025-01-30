from odoo import models, api, fields


class IvanCustomize(models.Model):
    _name = 'ivan.customize'
    _description = 'Ivan Coba Custom'
    _inherit = "mail.thread"
    
    nama = fields.Char(
        string="Nama",
        required=True,
        active=True, 
        store=True,
        tracking=True,
        )
    tanggal_lahir = fields.Date(
        string="TTL",
        required=True,
        active=True, 
        store=True,
        tracking=True,
        )
    pekerjaan = fields.Char(
        string="Pekerjaan",
        required=True,
        tracking=True,
        )
    kota = fields.Selection(
        [('jakarta','Jakarta'),
         ('bali','Bali')])
    
