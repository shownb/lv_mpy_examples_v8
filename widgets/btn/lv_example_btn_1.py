#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

def event_handler(evt):
    code = evt.get_code()

    if code == lv.EVENT.CLICKED:
            print("Clicked event seen")
    elif code == lv.EVENT.VALUE_CHANGED:
        print("Value changed seen")
        
level= 4
log_level=["Trace", "Info", "Warning", "Error", "User"]
#lv.log_register_print_cb(lambda level,filename,func,msg: print('LOG: %s, file: %s in %s, line %d: %s' % (log_level[level], filename, func,  msg)))           
lv.log_register_print_cb(lambda lvl,msg: print("LOG: " + log_level[lvl] + msg))

lv.log(4,"Hello")

# log = lv.log((lambda level,filename,line,func,msg: print('LOG: %s, file: %s in %s, line %d: %s' % (log_level[level], filename, func, line, msg)))
#lv.log_add("User","Hello")
# create a simple button
btn1 = lv.btn(lv.scr_act())

# attach the callback
btn1.add_event_cb(event_handler,lv.EVENT.ALL, None)

btn1.align(lv.ALIGN.CENTER,0,-40)
label=lv.label(btn1)
label.set_text("Button")

# create a toggle button
btn2 = lv.btn(lv.scr_act())

# attach the callback
#btn2.add_event_cb(event_handler,lv.EVENT.VALUE_CHANGED,None)
btn2.add_event_cb(event_handler,lv.EVENT.ALL, None)

btn2.align(lv.ALIGN.CENTER,0,40)
btn2.add_flag(lv.obj.FLAG.CHECKABLE)
btn2.set_height(lv.SIZE.CONTENT)

label=lv.label(btn2)
label.set_text("Toggle")
label.center()
