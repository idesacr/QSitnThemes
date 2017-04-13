# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sitnThemes
                                 A QGIS plugin
 Load QGIS projects witth themes likes in online geoportal
                             -------------------
        begin                : 2017-04-13
        copyright            : (C) 2017 by om/sitn
        email                : olivier.monod@ne.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load sitnThemes class from file sitnThemes.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sitnTheme import sitnThemes
    return sitnThemes(iface)
