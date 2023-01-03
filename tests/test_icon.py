"""
 Copyright 2022 Philip Mai - philip.mai@accenture.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from pyiconlibrary import *

lib = IconLibrary()
colors = ["black", "white"]
types = ["outlined", "round", "sharp", "twotone", "normal"]
sizes = ["1x", "2x"]
names = ["add_alert", "wrong_location", "hourglass_bottom", "hotel"]
for color in colors:
    for type in types:
        for size in sizes:
            for name in names:
                img = lib.get_icon(color=color, name=name, icon_type=type, size=size)
