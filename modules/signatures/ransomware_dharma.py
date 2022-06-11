# Copyright (C) 2020 bartblaze
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature


class DharmaMutexes(Signature):
    name = "dharma_mutexes"
    description = "Creates a known Dharma/Crysis ransomware variant mutex"
    severity = 3
    categories = ["ransomware"]
    families = ["Dharma", "Crysis", "Wadhrama"]
    authors = ["bartblaze"]
    minimum = "0.5"
    evented = True
    ttps = ["T1486"]

    def run(self):
        indicators = [
            "syncronize_[A-Z0-9]{6,7}$",
        ]

        for indicator in indicators:
            if self.check_mutex(pattern=indicator, regex=True):
                return True

        return False
