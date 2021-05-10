#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

def btnm_event_handler(e,ta):

    obj = lv.btnmatrix.__cast__(e.get_target())
    txt = obj.get_btn_text(obj.get_selected_btn())
    if txt == lv.SYMBOL.BACKSPACE:
        ta.del_char()
    elif txt == lv.SYMBOL.NEW_LINE:
        ta.set_text("")
    else:
        ta.add_text(txt)

'''
    if(strcmp(txt, LV_SYMBOL_BACKSPACE) == 0) lv_textarea_del_char(ta);
    else if(strcmp(txt, LV_SYMBOL_NEW_LINE) == 0) lv_textarea_add_char(ta, '\n');
    else lv_textarea_add_text(ta, txt);
'''


ta = lv.textarea(lv.scr_act())
ta.set_one_line(True)
ta.align(lv.ALIGN.TOP_MID, 0, 10)

ta.add_state(lv.STATE.FOCUSED)   # To be sure the cursor is visible

btnm_map = ["1", "2", "3", "\n",
            "4", "5", "6", "\n",
            "7", "8", "9", "\n",
            lv.SYMBOL.BACKSPACE, "0", lv.SYMBOL.NEW_LINE, ""]
         
btnm = lv.btnmatrix(lv.scr_act())
btnm.set_size(200, 150)
btnm.align(lv.ALIGN.BOTTOM_MID, 0, -10)
btnm.add_event_cb(lambda e: btnm_event_handler(e,ta), lv.EVENT.VALUE_CHANGED, None)
btnm.clear_flag(lv.obj.FLAG.CLICK_FOCUSABLE)    # To keep the text area focused on button clicks
btnm.set_map(btnm_map)

