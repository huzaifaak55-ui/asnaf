# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
   name = 'gf.Student'
   description = 'Student'

   name = fields.Char(string="Name", required=True) 
   roll_no = fields.Char(string="Roll Number")
   Father_Name = fields.Char(string="Father Name")
   Mother_Name = fields.Char(string="Mother Name")
   dob=fields.Date(string="Birth Date")
   gender=fields.Selection(
      [("male","Male"),("female","Female"),("other","Other")],
      string="Gender"
   )
   active=fields.Boolean()
   address=fields.Char()
   admisson_no=fields.Integer(string="Admisson No")
   course_id=fields.Many2one("gf.course",string="Course")
#   @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

