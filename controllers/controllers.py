# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json, request

class Odoocalc(http.Controller):
    @http.route('/odoocalc', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('odoocalc.index')

    @http.route('/odoocalc/calculate', type='json', auth='public', website=True, cors="*")
    def calculate(self, **kw):
        print(request)
        return json.dump({"result":  1 + 5 })