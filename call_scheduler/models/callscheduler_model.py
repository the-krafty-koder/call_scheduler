from odoo import fields,api,models

class call_scheduler(models.Model):
    _name = "call_scheduler.model"
    _description = "A module for scheduling calls"

    contact = fields.Many2one("res.partner",string="Customer")
    subject = fields.Char(string="Subject",size=50)
    call_purpose = fields.Char(string="Call Purpose",size=100)
    call_type = fields.Char(string="Call type",size=10)
    call_result = fields.Text(string="Call Result")
    call_time = fields.Datetime(string="Time")

    is_done = fields.Boolean(string="Is Done")

    @api.multi
    def convert_to_lead(self):
        self.ensure_one()
        return {
            'type':'ir.actions.act_window',
            'res_model':'crm.lead',
            'view_type':'form',
            'view_mode':'form',
            'target':'current',
        }