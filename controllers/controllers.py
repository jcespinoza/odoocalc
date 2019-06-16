# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json, request
import src.calculator
class Odoocalc(http.Controller):
    @http.route('/odoocalc', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('odoocalc.index')

    @http.route('/odoocalc/calculate', type='json', auth='none', website=True, cors="http://localhost,http://localhost:4200,*", csrf=False)
    def calculate(self, **kw):
        print(request)
        calculator = Calculator()
        return json.dumps(
            calculator.
            # {
            #     "sucess": True,
            #     "errorMessage": None,
            #     "output":  1 + 5 
            # }
            )