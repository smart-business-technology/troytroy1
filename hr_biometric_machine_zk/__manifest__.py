{
    "name" : "ZK Biometric Device Integration Kware (ZKTECO) 13",
    "version" : "14.01",
    "author" : "",
    "category" : "HR",
    "website" : "",
    "description": "Module for the integration between ZK Biometric Machines and Odoo.",
    'license': 'AGPL-3',
    "depends" : ["base","hr",'hr_attendance'],
    "data" : [
				"wizard/zk_create_users_wizard.xml",
				"views/biometric_machine_view.xml",
				"secuirty/res_groups.xml",
				"secuirty/ir.model.access.csv",
        "data/download_dat.xml"
			],
	'images': ['static/images/zk_screenshot.gif'],
    "active": True,
    "installable": True,
    'currency': 'EUR',
    'price': 0,
}
