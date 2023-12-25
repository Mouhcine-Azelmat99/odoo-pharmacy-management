from odoo import models, fields

class Customer(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer'
    
    orders = fields.One2many('pharmacy.product.order', 'customer', string='Orders')
