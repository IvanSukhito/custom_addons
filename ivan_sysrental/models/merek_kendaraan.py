from odoo import api, fields, models


class RentalMerekKendaraan(models.Model):
    _name = 'sysrental.merek_kendaraan'
    _description = 'Merek Kendaraan'
    _rec_name = 'merek_kendaraan'

    merek_kendaraan = fields.Char(
        string="merek_kendaraan",
        required=True,
        store=True,
        )
    type_kendaraan_id = fields.Many2one(
        "sysrental.type_kendaraan",
        string="type_kendaraan",
        store=True,
    )

    @api.model
    def create(self, vals):
        """Jika merek kendaraan dibuat dari form kendaraan, otomatis assign type_kendaraan_id"""
        print("Context:", self.env.context)  # Debugging
    
        kendaraan_id = self.env.context.get('active_id')
        
        if kendaraan_id and 'type_kendaraan_id' not in vals:
            kendaraan = self.env['sysrental.kendaraan'].browse(kendaraan_id)
            print("Kendaraan ID:", kendaraan.id)  # Debugging
            print("Tipe Kendaraan ID:", kendaraan.type_kendaraan_id.id)  # Debugging
            
            if kendaraan.type_kendaraan_id:
                vals['type_kendaraan_id'] = kendaraan.type_kendaraan_id.id
                
        return super(RentalMerekKendaraan, self).create(vals)


    # def create(self, vals):
    #     """Jika merek kendaraan dibuat dari form kendaraan, otomatis assign type_kendaraan_id"""
    #     if 'type_kendaraan_id' not in vals and self.env.domain.get('type_kendaraan_id'):
    #         vals['type_kendaraan_id'] = self.env.domain['type_kendaraan_id']
    #     return super(RentalMerekKendaraan, self).create(vals)
    
    # def default_get(self, fields_list):
        # """Set default type_kendaraan_id jika dibuat dari form kendaraan"""
        # defaults = super(RentalMerekKendaraan, self).default_get(fields_list)
        # if self.env.context.get('active_model') == 'sysrental.kendaraan' and self.env.context.get('active_id'):
            # kendaraan = self.env['sysrental.kendaraan'].browse(self.env.context['active_id'])
            # defaults['type_kendaraan_id'] = kendaraan.type_kendaraan_id.id
        # return defaults