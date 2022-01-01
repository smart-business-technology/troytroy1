from odoo import api, fields, models


class PayrollsarkReport(models.TransientModel):
    _name = 'sales.diff.report.wiz'


    def print_report(self):
        data = {'model': 'payroll.sark.report.wiz', 'form': self.read()[0]}
        lll=[]
        baghdad_priclist = self.env['product.pricelist'].search([("name",'=','بغداد')])

        basra_priclist = self.env['product.pricelist'].search([("name",'=','بصره')])
        print(baghdad_priclist)
        for rec in baghdad_priclist.item_ids:
            print(rec.product_tmpl_id)
            for rec1 in basra_priclist.item_ids:
                print(rec.product_tmpl_id.name,'        ',rec1.product_tmpl_id.name)
                if rec.product_tmpl_id.name==rec1.product_tmpl_id.name:

                    lll.append({"product":rec.product_tmpl_id.name ,'baghdad_price':rec.fixed_price ,'basra_price':rec1.fixed_price,'diff':rec1.fixed_price-rec.fixed_price})

        # print(lll)
        summ1 = 0
        summ2 = 0
        summ3 = 0
        for i in lll:
            summ1 += i['baghdad_price']
            summ2 += i['basra_price']
            summ3 += i['diff']
        print(summ1)
        print(summ2)
        print(summ3)

        lll.append(
            {"product": 'المجموع', 'baghdad_price':summ1, 'basra_price': summ2,
             'diff': summ3})

        data['lines'] = lll
        # print(data)
        # print(basra_priclist)
        return self.env.ref('invoice_fields.sales_diff_report').report_action(self, data)
