from odoo import models, fields, api

class MySecondModel(models.Model):
    _name = "my_second_model"

    name = fields.Char(string="First Name")
    phone = fields.Char()
    active = fields.Boolean(default=True)
    my_model_ids = fields.One2many('my_model', 'my_second_model_id')