# -*- coding: utf-8 -*-
# Copyright © 2015-2019 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/

# Get values of the ignoressl option of the rss section
'''Get values of the ignoressl option of the rss section'''

# standard library imports
import ssl

def parseignoressl(config, ignore_ssl_from_cli):
    '''Parse configuration values and get values of the feedparser section'''
    section = 'rss'
    option = 'ignore_ssl'
    if config.has_option(section, option):
        ignoressl = config.getboolean(section, option)
    else:
        ignoressl = ignore_ssl_from_cli
    return ignoressl
