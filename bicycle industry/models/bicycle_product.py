from odoo import models, fields, api

class BicycleProduct(models.Model):
    _name = 'bicycle.product'
    _description = 'Bicycle Product'

    name = fields.Char(string='Model Name', required=True)
    product_type = fields.Selection([
        ('road', 'Road Bike'),
        ('mountain', 'Mountain Bike'),
        ('hybrid', 'Hybrid Bike'),
        ('electric', 'Electric Bike'),
    ], string='Type', required=True)
    frame_size = fields.Char(string='Frame Size')
    wheel_size = fields.Char(string='Wheel Size')
    price = fields.Float(string='Price')
    in_stock = fields.Integer(string='Quantity in Stock')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)