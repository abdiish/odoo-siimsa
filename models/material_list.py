# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

class Material(models.Model):
     _name = 'siimsa.material'

     name    = fields.Char('Requisición de compra')
     tpo_com = fields.Selection([
                                ('Papeleria','Papelería'),
                                ('Limpieza','Limpieza'),
                                ('Produccion','Producción'),
                                ('Computo','Cómputo'),
                                ('Otro','Otro')],'Tipo de compra')
     fec_sol = fields.Datetime(string='Fecha')
     material = fields.Many2many('siimsa.request', string="Lista de Material")
     herramienta = fields.Many2many('siimsa.tool',string="Lista de Herramienta")
     solicitud = fields.Many2one('res.partner',ondelete='set null', string="Empleado",index=True)
     orden = fields.Many2one('siimsa.work',string="Orden de trabajo")




