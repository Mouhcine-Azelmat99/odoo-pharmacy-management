from odoo import models, fields, api

class OrderLines(models.Model):
    _name="pharmacy.product.orderlines"
    _description="pharmacy.product.orderlines"

    product = fields.Many2one('pharmacy.product')
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price', related='product.price', readonly=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal')
    order=fields.Many2one('pharmacy.product.order',string='order')

    @api.depends('quantity', 'price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price
