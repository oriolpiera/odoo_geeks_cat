# -*- coding: utf-8 -*-
from odoo import models


class WizardAssignNumberToMember(models.TransientModel):

    _name = 'wizard.assign.number.to.member'

    def assign_number_to_member(self):
        Partner = self.env['res.partner']
        active_ids = self.env.context.get('active_ids')
        for partner_id in active_ids:
            partner_obj = Partner.browse(partner_id)
            if not partner_obj.member_code:
                partner_obj.member_code = self.env['ir.sequence'].next_by_code('member.code')
