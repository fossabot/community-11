# Copyright (C) 2023 Eye Security (yasin.tas@eye.security)
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

class BinaryTriggeredYARA(Signature):
    name = "binary_yara"
    description = "Binary file triggered YARA rule"
    severity = 3
    confidence = 50
    weight = 1
    categories = ["static"]
    authors = ["Yasin Tas",  "Eye Security"]
    minimum = "1.3"

    def run(self):
        if self.results["target"]["file"]["yara"]:
            self.description = "Binary file triggered YARA rule(s)"
            yara_triggered = self.results["target"]["file"]["yara"]
            if len(yara_triggered) > 1:
                self.description = "Binary file triggered multiple YARA rule(s)"
            for yara in yara_triggered:
                self.data.append({"Binary triggered YARA rule": yara["name"]})
            return True

        return False