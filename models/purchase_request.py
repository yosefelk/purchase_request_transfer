# -*- coding: utf-8 -*-

from odoo import _, api, exceptions, fields, models
from odoo.exceptions import UserError

_STATES = [
    ("draft", "Draft"),
    ("to_approve", "To be approved"),
    ("approved", "Approved"),
    ('transferred', 'Transferred'),
    ("rejected", "Rejected"),
    ("done", "Done"),
]

class PurchaseRequest(models.Model):
    _inherit = "purchase.request"
   
    inter_company_transfer_id = fields.Many2one('inter.company.transfer.ept', string="Inter Company Transfer",
                                                copy=False, help="Reference of ICT.")
    recuperation = fields.Char(string="Récupérée par", required="1")
       
    state = fields.Selection(
        selection=_STATES,
        string="Status",
        index=True,
        track_visibility="onchange",
        required=True,
        copy=False,
        default="draft",
    )

    def button_create_inter_company_transfer(self):
      transfer_line_ids = []
      
      if not self.recuperation:
        raise UserError(_("SVP choisir les valeurs pour Récupérée par"))
      for each in self.line_ids:
        transfer_line_ids.append((0,0, {'product_id': each.product_id.id,
                                        'quantity': each.product_qty,}))
        vals = {
                
                'x_recuperation': self.recuperation,
                'type': 'ict',
                'inter_company_transfer_line_ids': transfer_line_ids,}
      inter_company_transfer_id = self.env['inter.company.transfer.ept'].create(vals)
      if inter_company_transfer_id:
        self.state = 'transferred'
        self.inter_company_transfer_id = inter_company_transfer_id.id
        template_id = self.env.ref('purchase_request_transfer.approver_ict_email_template')
        self.env['mail.template'].browse(template_id.id).send_mail(self.id)