import logging
from odoo import fields, api, models


_logger = logging.getLogger(__name__)


class RentalKendaraan(models.Model):
    _name = 'sysrental.kendaraan'
    _description = 'Model Kendaraan'
    _inherit = 'mail.thread'
    _rec_name = 'nama'
    
    nama = fields.Char(
        string="Nama",
        required=True,
        store=True,
        tracking=True,
        )
    plat_nomor = fields.Char(
        string="Plat Nomor",
        store=True,
        tracking=True,
        )
    tahun_keluaran = fields.Date(
        string="Tahun Keluaran",
        required=True,
        active=True, 
        store=True,
        tracking=True,
        )
    type_kendaraan_id = fields.Many2one(
        "sysrental.type_kendaraan",
        string="type_kendaraan",
        store=True,
    )
    merek_kendaraan_id = fields.Many2one(
        "sysrental.merek_kendaraan",
        string="merek_kendaraan",
        domain="[('type_kendaraan_id', '=', type_kendaraan_id)]",
        store=True,
        # context="{'default_type_kendaraan_id': type_kendaraan_id}",

    )
    status = fields.Selection(
        [('available','Available'),
         ('not available','Not Available')])
    

    # @api.onchange('type_kendaraan_id')
    # def _onchange_type_kendaraan(self):
    #   
        # self.merek_kendaraan_id = False
    # harga, 
    