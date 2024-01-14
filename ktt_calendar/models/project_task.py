from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    is_committed = fields.Boolean(string="Committed", default=False)
    
    # @api.onchange('include_customer')
    # def _onchange_include_customer(self):
    #     if(self.include_customer):
    #         pass

