from odoo import models, fields, api


class PharmacyProduct(models.Model):
    _name = 'pharmacy.product'
    _description = 'product'
    name = fields.Char('name', required=True)
    desc = fields.Text('Description', required=True)
    qte = fields.Integer(string='Quantity')
    EXP_Date = fields.Date(string="Expiration date")
    price = fields.Float(string="Price", required=True)
    image = fields.Binary(string="Image", attachment=True)
    category_id = fields.Many2one('pharmacy.product.category', string='Category')
    order_lines=fields.One2many('pharmacy.product.orderlines','product')