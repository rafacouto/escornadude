#!/usr/bin/python2

# escornadude.py
#
# Copyright (C) 2017 Rafa Couto <caligari@treboada.net> 
#                                                                                  
# This program is free software; you can redistribute it and/or                    
# modify it under the terms of the GNU General Public License                      
# as published by the Free Software Foundation; either version 2                   
# of the License, or (at your option) any later version.                           
#                                                                                  
# This program is distributed in the hope that it will be useful,                  
# but WITHOUT ANY WARRANTY; without even the implied warranty of                   
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                    
# GNU General Public License for more details.                                     
#                                                                                  
# You should have received a copy of the GNU General Public License                
# along with this program; if not, write to the Free Software                      
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,       
# USA.                                                                             
#                                                                                  
# See LICENSE file for details                                                      
#                                                                                  

import os
import sys
import urllib
import subprocess

def get_avrdude():
    uname = os.uname()
    exe = "%s-%s/avrdude" % (uname[0], uname[4])
    if uname == "Windows":
        exe += ".exe"
    cfg = "avrdude-%s.conf" % (uname[0])
    return (exe, cfg)

# ToDo
def get_version():
    # in testing
    return "v1.4.1"

# ToDo
def get_micro():
    # in testing
    return "nano"

# ToDo
def get_port():
    # in testing
    return "/dev/ttyUSB0"

# firmware repository
urlbase = "https://github.com/escornabot/arduino/raw/testing/binaries"

# avrdude
avrdude_exe, avrdude_cfg = get_avrdude()
if not os.path.isfile(avrdude_exe):
    print("avrdude binary not found (please report): %s" % avrdude_exe)
    sys.exit()

# chose version and microcontroller
hexfile = "escornabot-%s-%s.hex" % (get_version(), get_micro())

# download the firmware
url = urlbase + "/" + hexfile
print("Downloading %s" % url)
try:
    firmware = urllib.urlretrieve(url)[0]
except:
    print("Firmware not downloaded (please report): " % url)
    sys.exit()

# upload to microcontroller
subprocess.call(
    "%s -p atmega328p -C %s -c arduino -b 57600 -P ""%s"" -U ""flash:w:%s:i"" -D" %
    (avrdude_exe, avrdude_cfg, get_port(), firmware), 
    shell=True)

# remove downloads
os.remove(firmware)


