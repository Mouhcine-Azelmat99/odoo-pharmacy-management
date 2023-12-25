from odoo import models, fields, api



class Order(models.Model):
    _name = 'pharmacy.product.order'
    _description = 'Product Order'

    name = fields.Char('Order Reference', required=True)
    orderlines = fields.One2many('pharmacy.product.orderlines','order')
    customer=fields.Many2one('pharmacy.customer',string='Customer')
    created_at=fields.Datetime(default=fields.Datetime.now)
    total_price=fields.Float(compute='calc_total',store=True)
    
    
    @api.depends('orderlines.subtotal')
    @api.onchange('orderlines')
    def calc_total(self):
        for order in self:
            for record in order.orderlines:
                order.total_price += record.subtotal
