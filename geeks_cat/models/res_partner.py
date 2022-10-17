# Copyright 2022 Oriol Piera
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    member_code = fields.Integer(string="Member code", unique=True)
