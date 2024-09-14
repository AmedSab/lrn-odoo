from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    my_model_id = fields.Many2one('my_model')

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print("inside action_confirm")
        return res



