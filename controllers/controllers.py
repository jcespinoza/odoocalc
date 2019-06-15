# -*- coding: utf-8 -*-
from odoo import http

class Odoocalc(http.Controller):
    @http.route('/odoocalc', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('odoocalc.index')