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

import urllib
import os
import subprocess

import sys

def avrdude_binary():
    uname = os.uname()
    avrdude = "%s-%s/avrdude" % (uname[0], uname[4])
    if uname == "Windows":
        avrdude += ".exe"
    return avrdude

def get_version():
    # in testing
    return "v1.4.1"

def get_micro():
    # in testing
    return "nano"

# firmware repository
urlbase = "https://github.com/escornabot/arduino/raw/testing/binaries"

# avrdude
avrdude = avrdude_binary()
if not os.path.isfile(avrdude):
    print("avrdude binary not found (please report): %s" % avrdude)
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
#subprocess.call([avrdude, "-U", "flash:w:" + firmware+ ":i", "-C",
#    "avrdude.conf", "-v", "-p", "atmega328", "-b", "115200", "-c", "stk500v2", 
#    "-P", "/dev/ttyUSB0"])

# remove downloads
os.remove(firmware)


