# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

class Production(models.Model):
     _name = 'siimsa.production'

     name = fields.Char(string='Orden de producción')
     ord_pro    = fields.Many2one('siimsa.work',ondelete='set null',string="Orden de trabajo",index=True, required=True)
     ldm_mat = fields.Many2one('siimsa.material',string="Requisición")
     actividades = fields.One2many('siimsa.planning','produccion',string="Actividad")
     color = fields.Integer()