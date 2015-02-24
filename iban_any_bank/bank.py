# -*- coding: utf-8 -*-

##############################################################################
#
# IBAN Field for any bank
# Copyright (C) 2015 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api

class PartnerBankIBAN(models.Model):
    _inherit = 'res.partner.bank'

    iban_any = fields.Char(
        # I had to call this iban_any because 'iban' was already taken in base_iban
        string='IBAN',
        help='For a "Normal" bank account, you can also put in an IBAN here as an alternative',
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
