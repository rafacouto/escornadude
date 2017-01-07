# EscornaDUDE

This applicaton is the __Escornabot Firmware Downloader/UloaDEr__ based on [AVRDUDE][AVR01].

It provides an easy way to obtain the [Escornabot Firmware][ESC01] and upload it to your [Escornabot][ESC02].


## License

_EscornaDUDE_ is licensed, like _AVRDUDE_, under __GNU General Public License v2__.

Please, read and respect [LICENSE][LIC01].


## Installation

-ToDo-


## Usage

-ToDo-

    $ ./escornadude.py 
    Downloading https://github.com/escornabot/arduino/raw/testing/binaries/escornabot-v1.4.1-nano.hex
    
    avrdude: AVR device initialized and ready to accept instructions
    
    Reading | ################################################## | 100% 0.00s
    
    avrdude: Device signature = 0x1e950f (probably m328p)
    avrdude: reading input file "/tmp/tmp5mKqbG.hex"
    avrdude: writing flash (9220 bytes):
    
    Writing | ################################################## | 100% 2.92s
    
    avrdude: 9220 bytes of flash written
    avrdude: verifying flash memory against /tmp/tmp5mKqbG.hex:
    avrdude: load data flash data from input file /tmp/tmp5mKqbG.hex:
    avrdude: input file /tmp/tmp5mKqbG.hex contains 9220 bytes
    avrdude: reading on-chip flash data:
    
    Reading | ################################################## | 100% 2.29s
    
    avrdude: verifying ...
    avrdude: 9220 bytes of flash verified
    
    avrdude: safemode: Fuses OK (E:00, H:00, L:00)
    
    avrdude done.  Thank you.




<!-- links -->
[AVR01]: http://savannah.nongnu.org/projects/avrdude
[ESC01]: https://github.com/escornabot/arduino
[ESC02]: http://escornabot.com
[LIC01]: blob/stable/LICENSE
