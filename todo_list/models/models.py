from odoo import models, fields


class TodoTask(models.Model):
    _name = 'todo_list.task'
    _description = 'Todo Task'
    _order = 'is_done asc, id desc'

    name = fields.Char(string='Task', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string='Done', default=False)
    user_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
