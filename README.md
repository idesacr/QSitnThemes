# QSitnThemes

A QGIS plugin that loads QGIS projets that set up gmf-like stylin from a gmf-like theme panel (dock widget)

Configuration (temporary solution):
- Create a themesConfig.py file that contains a themes variable defined as imbricated lists:

themes = [ 
    ['theme_name', 'icon_name', 'path_to_qgis_project_file_with_foward_slashes.qgs'],
#example    ['mensuration', 'cadastre.png', '//blablafileserver/plan_cadastral_couleur.qgs'],
]

