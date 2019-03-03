# -*- coding: utf-8 -*-
from datetime import timedelta
from openerp import models, fields, api, exceptions, _

class Work(models.Model):
     _name = 'siimsa.work'

     name = fields.Char(string='N° Orden de trabajo', size=4, required=True)
     ord_com = fields.Char(string='N° Orden de compra', size=4)
     num_cot = fields.Char(string='N° de cotización', size=4)
     num_fac = fields.Char(string='N° de factura', size=4)
     num_rem = fields.Char(string='N° de remisión', size=4)
     num_pza = fields.Char(string='N° de piezas', size=4,required=True)
     num_pte = fields.Char(string='N° de parte',required=True)
     fec_sol = fields.Date(string='Fecha de solicitud',required=True)
     fec_ent = fields.Date(string='Fecha de entrega',required=True)
     fec_rea = fields.Date(string='Fecha de entrega real')
     des_act = fields.Text(string='Descripción')
     color = fields.Integer()
     con_cto = fields.Many2one('res.partner',ondelete='set null',string="Contacto",index=True)
     con_cte = fields.Many2one('res.partner',ondelete='set null',string="Cliente",index=True)

     priority = fields.Selection([
                                 ('0','Low'),
                                 ('1','Normal'),
                                 ('2','High')],'Priority',default='0')

     kanban_state = fields.Selection([
                                     ('normal','In Progress'),
                                     ('blocked','Blocked'),
                                     ('done','Ready for next stage')],'Kanban State', default='normal')

     @api.depends('fec_sol','fec_ent')
     def _get_end_date(self):
          for r in self:
               if not(r.fec_sol and r.fec_ent):
                    r.fec_ent = r.fec_sol
                    continue
                    start = fields.Datetime.from_string(r.fec_sol)
                    duration = timedelta(days=r.duration,seconds=-1)
     def _set_end_date(self):
          for r in self:
               if not(r.fec_sol and r.fec_ent):
                    continue
                    fec_sol = fields.Datetime.from_string(r.fec_sol)
                    fec_ent = fields.Datetime.from_string(r.fec_ent)
                    r.duration = (fec_ent-fec_sol).days+1





