from odoo import api, fields, models


class RentalTypeKendaraan(models.Model):
    _name = 'sysrental.type_kendaraan'
    _description = 'Type Kendaraan'
    _rec_name = 'type_kendaraan'

    type_kendaraan = fields.Char(
        string="type_kendaraan",
        required=True,
        store=True,
        )
    