# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _

class Request(models.Model):
    _name = 'siimsa.request'

    name = fields.Char('Descripción')
    can_mat = fields.Integer('Cantidad')
    uni_mat = fields.Char('Unidad')


class Tool(models.Model):
    _name = 'siimsa.tool'

    name = fields.Char('Descripción')
    can_mat = fields.Integer('Cantidad')
    uni_mat = fields.Char('Unidad')
