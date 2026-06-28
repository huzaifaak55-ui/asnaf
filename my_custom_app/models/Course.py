# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
   name = 'gf.course'
   description = 'Course'

   name = fields.Char(string="Name", required=True) 
   