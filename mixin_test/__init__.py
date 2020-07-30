from odoo import models, fields


class TestMixin(models.AbstractModel):
    _name = 'test.mixin'

    test_field = fields.Boolean("Test field")
    test_field_selection = fields.Selection("Test selection field")


class TestModel(models.Model):
    _name = "test.model"

    _inherit = 'test.mixin'
