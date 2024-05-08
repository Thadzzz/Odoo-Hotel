# -*- coding: utf-8 -*-

#charges.py

from odoo import models, fields, api

class charges(models.Model):
    _name = 'hotel.charges'
    _description = 'hotel charges master list'
    _order="name"

    name = fields.Char("Charge Name")
    description = fields.Char("Charge Description")