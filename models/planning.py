# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

class Planning(models.Model):
     _name = 'siimsa.planning'

     num_pza = fields.Integer(string='N° de piezas')
     tpo_ser = fields.Selection([
                                ('Maquinado','Maquinado'),
                                ('Fresado','Fresado'),
                                ('Soldadura','Soldadura'),
                                ('Corte','Corte'),
                                ('Rectificado','Rectificado'),
                                ('Medicion','Medición')],'Tipo de servicio')

     tie_pla = fields.Float(digits=(6,2),string='Tiempo planeado')
     tie_rea = fields.Float(digits=(6,2),string='Tiempo real')

     dato = fields.Integer(string="Porcentaje",compute='_time')

     produccion = fields.Many2one('siimsa.production',string="Orden de producción")
     id_maquinaria = fields.Many2one('maintenance.equipment',string="Maquinaria")
     id_empleado = fields.Many2one('res.partner',string="Operador")

     color = fields.Integer()

     kanban_state = fields.Selection([
         ('normal', 'In Progress'),
         ('blocked', 'Blocked'),
         ('done', 'Ready for next stage')], 'Kanban State', default='normal')

     state = fields.Selection([
                              ('draft',_("Borrador")),
                              ('confirmed',_("En proceso")),
                              ('done',_("Hecho")),
                            ],'Estado',default='draft')

     @api.multi
     @api.onchange('dato')
     def action_draft(self):
         self.state = 'draft'

     @api.multi
     def action_confirmed(self):
         self.state = 'confirmed'

     @api.multi
     def action_done(self):
         self.state = 'done'

     @api.depends('tie_pla','tie_rea')
     def _time(self):

         for r in self:
             if not r.tie_rea:
                 r.dato = 0.0
             else:
                 r.dato = 100 * r.tie_rea / r.tie_pla

