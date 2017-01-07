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

urlbase = "https://github.com/escornabot/arduino/raw/testing/binaries"
hexfile = "escornabot-v1.4.1-nano.hex"

url = urlbase + "/" + hexfile

print("Downloading %s" % url)
filename = urllib.urlretrieve(url)[0]

subprocess.call([ "avrdude", "-U", "flash:w:" + filename + ":i", "-C",
    "avrdude.conf", "-v", "-p", "atmega328", "-b", "115200", "-c", "stk500v2", 
    "-P", "/dev/ttyUSB0"])

os.remove(filename)


