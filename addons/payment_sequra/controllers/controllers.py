# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/paymentSequra(http.Controller):
#     @http.route('//mnt/extra-addons/payment_sequra//mnt/extra-addons/payment_sequra', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/payment_sequra//mnt/extra-addons/payment_sequra/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/payment_sequra.listing', {
#             'root': '//mnt/extra-addons/payment_sequra//mnt/extra-addons/payment_sequra',
#             'objects': http.request.env['/mnt/extra-addons/payment_sequra./mnt/extra-addons/payment_sequra'].search([]),
#         })

#     @http.route('//mnt/extra-addons/payment_sequra//mnt/extra-addons/payment_sequra/objects/<model("/mnt/extra-addons/payment_sequra./mnt/extra-addons/payment_sequra"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/payment_sequra.object', {
#             'object': obj
#         })

