# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class KttMeeting(models.Model):
    _inherit = 'calendar.event'

    task_ids = fields.Many2many(
        comodel_name='project.task', relation='calendar_project_tasks', column1='calendar_event_id', column2='task_id', string='Tasks')

    def write(self, vals):
        # If the task is deleted then switch task stage to 'backlog'
        # And if add task then check status task is committed ?
        if(vals['task_ids']):
            for item in vals['task_ids']:
                task_id = item[1]
                task_record = self.env['project.task'].browse(task_id)
                stages = task_record.project_id.type_ids
                if(item[0] == 3):
                    self._switch_task_stage(task_record, stages, item[0])
                if(item[0] == 4 and task_record.is_committed):
                    raise ValidationError("Task code '%s' are committed. Please choose another task." % task_record.task_code)
        # Switch stage 'print backlog' of the all task valid in the meeting
        res = super(KttMeeting, self).write(vals)
        tasks = self.task_ids
        if(tasks):
            for task in tasks:
                if(not task.is_committed):
                    stages = task.project_id.type_ids
                    self._switch_task_stage(task, stages, 4)
                
        return res
    
    def unlink(self):
        if(self.task_ids):
            raise ValidationError('The meeting has tasks. Meetings cannot be deleted.')
        return super(KttMeeting, self).unlink()
    
    def _switch_task_stage(self, task, stages, action):
        for stage in stages:
            if(stage.sequence == 0 and action == 3):
                task.stage_id = stage
                task.is_committed = False
            if(stage.sequence == 1 and action == 4):
                task.stage_id = stage
                task.is_committed = True
        