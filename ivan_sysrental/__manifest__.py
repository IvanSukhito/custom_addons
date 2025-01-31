{
    "name" : "System Rental",
    "author" : "Ivan S",
    "license" : "LGPL-3",
    "version" : "18.0.1.1",
    "depends" : ['mail'],
    "data" : [
        "security/security.xml",
        "security/ir.model.access.csv", 
        "views/merek_kendaraan.xml",
        "views/type_kendaraan.xml",
        "views/kendaraan.xml",
        "views/menu.xml",
    ],
    "installable" : True,
    "application" : True,
    "images" : [
        'static/description/icon.png',
        # 'static/img/default_icon_app.png',
    ]
}