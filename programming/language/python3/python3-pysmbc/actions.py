#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-implicit-function-declaration -Wno-deprecated-declarations")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")