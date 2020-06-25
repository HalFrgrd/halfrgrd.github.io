## Flashing blackmagic firmware on ST-Link
This is guide on how to make a Black Magic Probe using two ST-Link V2 programmers using MinGW64. 
The guide is based on:

http://blog.linuxbits.io/2016/02/15/cheap-chinese-st-link-v-2-programmer-converted-to-black-magic-probe-debugger/

I only cover the differences between that guide and my experience
### Connecting one ST-Link to another
The pinout on my board was different to the one in the above guide.
I had: GND, SWCLK, SWDIO, VCC in that order. VCC was closest to the male USB port of the programmer.


### Installing openocd on MinGW64
https://www.playembedded.org/blog/building-openocd-under-windows-using-msys2/v
https://packages.msys2.org/package/mingw-w64-x86_64-openocd-git?repo=mingw64

Run: `pacman -S mingw-w64-i686-openocd-git`


### Installing stlink tools (st-flash) on MinGW64

```
git clone https://github.com/stlink-org/stlink
cd stlink/
cmake -G "MinGW Makefiles"
mingw32-make
```