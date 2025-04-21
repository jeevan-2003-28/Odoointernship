from odoo import models, fields, api

class BicycleOrder(models.Model):
    _name = 'bicycle.order'
    _description = 'Bicycle Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('bicycle.order'))
    customer_name = fields.Char(string='Customer Name', required=True)
    customer_phone = fields.Char(string='Customer Phone')
    customer_email = fields.Char(string='Customer Email')
    order_date = fields.Date(string='Order Date', default=fields.Date.today)
    delivery_date = fields.Date(string='Delivery Date')
    product_id = fields.Many2one('bicycle.product', string='Bicycle Model', required=True)
    quantity = fields.Integer(string='Quantity', default=1)
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ], string='Status', default='draft')

    @api.depends('product_id', 'quantity')
    def _compute_total_price(self):
        for order in self:
            order.total_price = order.product_id.price * order.quantity