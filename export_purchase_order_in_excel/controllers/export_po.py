# -*- coding: utf-8 -*-
import base64
from odoo import http, SUPERUSER_ID
from odoo.http import request
# from odoo.addons.web.controllers.main import binary_content
import logging

_logger = logging.getLogger(__name__)


class POExcelReportDetail(http.Controller):

    @http.route([
        "/web/binary/download_po_excel_report/<model('purchase.order.excel.report'):file>"],
        type='http', auth="public", website=True)
    def download_po_excel_report(self, file=None, **post):
        if file:
            status, headers, content = request.env['ir.http'].sudo().binary_content(model='purchase.order.excel.report', id=file.id, field='excel_file', filename_field=file.file_name)
            content_base64 = base64.b64decode(content) if content else ''
            headers.append(('Content-Type', 'application/vnd.ms-excel'))
            headers.append(('Content-Disposition', 'attachment;filename=' + file.file_name + ' ; '))
            return request.make_response(content_base64, headers)
        return False
