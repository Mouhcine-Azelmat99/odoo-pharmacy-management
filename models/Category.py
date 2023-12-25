from odoo import models, fields, api

class Category(models.Model):
    _name = 'pharmacy.product.category'
    _description = 'Product Category'
    name = fields.Char('Category Name', required=True)
    desc = fields.Text("Description")
