#!/opt/bin/lv_micropython -i
import sys
import lvgl as lv
import display_driver
import fs_driver

fs_drv = lv.fs_drv_t()
fs_driver.fs_register(fs_drv, 'S')

img = lv.gif(lv.scr_act())
# The File system is attached to letter 'S'

img.set_src("S:bulb.gif")
img.center()
