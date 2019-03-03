# -*- coding: utf-8 -*-
from openerp.report import report_sxw
from openerp.osv import osv

class list_activity(report_sxw.rml_parse):

    def __init__(self,cr,uid,name,context):
        super(list_activity,self).__init__(cr,uid,name,context)

class list_a(osv.AbstractModel):
    _name = 'report.siimsa.list_activity'
    _inherit = 'report.abstract_report'
    _template = 'siimsa.list_activity'
    _wrapped_report_class = list_activity


