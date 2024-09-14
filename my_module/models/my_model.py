from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MyModel(models.Model):
    _name = "my_model"
    _description = 'my model description'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'f_name'

    ref = fields.Char(default="New", readonly=1)
    f_name = fields.Char(string="First Name")
    date_field = fields.Date(string="test date")
    expected_done_date = fields.Date(tracking=1)
    is_late = fields.Boolean(default=False)
    price = fields.Float(digits='0, 2', tracking=1)
    price2 = fields.Float()
    diff_price = fields.Float(compute='_compute_diff', store=1)
    bool = fields.Boolean()
    active = fields.Boolean(default=True)

    my_second_model_id = fields.Many2one('my_second_model')

    my_second_model_name = fields.Char(related='my_second_model_id.name', readonly=0, stord=1)
    my_second_model_phone = fields.Char(related='my_second_model_id.phone')

    my_model_line_ids = fields.One2many('my_model_line', 'my_model_id')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('done', 'Done'),
    ], default='draft')

    @api.constrains('price')
    def _check_price_greater_zero(self):
        for rec in self:
            if rec.price <= 0:
                raise ValidationError('please add valid number of price')


    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(MyModel, self).create(vals)
    #
    #     return res

    @api.model
    def create(self, vals):
        res = super(MyModel, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('my_model_seq')
        return res

    @api.depends('price2', 'price')
    def _compute_diff(self):
        for rec in self:
            rec.diff_price = rec.price2 - rec.price

    @api.onchange('price')
    def _onchange_price(self):
        for rec in self:
            if rec.price <= 0:
                return {
                    'warning':{'title': 'warning', 'message': 'negative value', 'type': 'notification'}
                }

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def check_expected_done_date(self):
        my_model_ids = self.search([])
        for rec in my_model_ids:
            if rec.expected_done_date and rec.expected_done_date < fields.date.today():
                rec.is_late = True
        # print("inside check_expected_done_date")





class MyModelLine(models.Model):
    _name = "my_model_line"
    _description = 'my model line'

    my_model_id = fields.Many2one('my_model')

    area = fields.Float()
    vol = fields.Float()



