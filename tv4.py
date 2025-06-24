import dearpygui.dearpygui as dpg
import cv2
import datetime

"""


        _pass["sn"]=0
        _log["sn"]="none"

        _log["pos1"]=_readData[1]
        _log["pos2"]=_readData[2]

        _pass["big_text"]=1
        _log["big_text"]=dpg.get_value("big_text")

        _pass["small_text"]=0
        _log["small_text"]=dpg.get_value("small_text")
"""        

#
_program_title="GLX Input Check"
_readData=dict()
_pass=dict()
_cntInput=0
_cntBigtext=0
_cntSmalltext=0
_log=dict()
_status="FAIL"
tmpbit="0000"
_template_bigText=set("QWERTYUIOP[]\SADFGHJKL;'ZXCVBNM,./")
_template_small_text=set("qwertyuiop[]\sadfghjkl;'zxcvbnm,./")

#---Start set keyboard
#numerical_value=[]
'''ord('0') = 48
ord('1') = 49
ord('2') = 50
ord('3') = 51
ord('4') = 52
ord('5') = 53
ord('6') = 54
ord('7') = 55
ord('8') = 56
ord('9') = 57
'''
keyboard_layout_num_BIG=[81, 87, 69, 82, 84, 89, 85, 73, 79, 80, 91, 93, 92,
65, 83, 68, 70, 71, 72, 74, 75, 76, 59, 39, 90, 88, 
67, 86, 66, 78, 77, 44, 46, 47,32]
 
number_skip=[49,50,51,52,53,54,55,56,57]    
keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P','[',']','\\'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';',"'"],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.','/']
    
]


def chekbtn1(sender, app_data, user_data):
    print(f"setkb->sender:{sender},app_data:{app_data},user_data:{user_data}")




def setkb(sender, app_data, user_data):
    #dpg.add_button(label=key, tag="btn_"+str(ord(key)),callback=chekbtn1,user_data=key,width=30, height=20)
    print(f"setkb->sender:{sender},app_data:{app_data},user_data:{user_data}")
     
    #numerical_value.clear()
    char_input=dpg.get_value("input1")
    if len(char_input)>0:
        print(keyboard_layout_num_BIG)
        #input > 0
        last_char_BIG=char_input[-1].upper()
        if  ord(last_char_BIG) in keyboard_layout_num_BIG:
            #print(last_char_BIG,"+",ord(last_char_BIG))
            dpg.bind_item_theme("btn_"+str(ord(last_char_BIG)), button_theme) 
    else:
        #input <0
        pass


        
    #print(char_input[-1])
   # dpg.bind_item_theme(char_input[-1], button_theme)
    '''if char_input!="":
        print("last key is ",ord(char_input[-1]))
        if(len(char_input))>0:          
            for char_inputABC in char_input:
                dpg.bind_item_theme(ord(char_inputABC), button_theme)
            #print(A)
          #  dpg.bind_item_theme(A, button_theme)
          #  print("a=",a)
          #  if a=="A":
          #      dpg.bind_item_theme("A", button_theme)
          #      print("found=a")
          #  print(f"setkb->sender:{sender},app_data:{app_data},user_data:{user_data}")
          #  dpg.bind_item_theme(btn, "empty_theme")
    else:
        global keyboard_layout_num_BIG
        print(keyboard_layout_num_BIG)
        for num in keyboard_layout_num_BIG:
            dpg.bind_item_theme(num, "empty_theme")
          
                #numerical_value.append(ord(char_inputABC))
                #numerical_value.append(ord(char_inputABC))
    #print(ord(char_input))
    '''       
dpg.create_context()
dpg.create_viewport(title='Custom Keyboard Layout', width=600, height=400)


 

with dpg.theme(tag="empty_theme"):
        # ไม่มีการตั้งค่าใดๆ ในธีมนี้
        pass
      # สร้างธีมสำหรับปุ่ม
      
with dpg.theme() as button_theme:
    with dpg.theme_component(dpg.mvButton):        
        dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 80, 255), category=dpg.mvThemeCat_Core)  # สีพื้นหลัง
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 180, 255), category=dpg.mvThemeCat_Core)  # สีเมื่อ hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 100, 200), category=dpg.mvThemeCat_Core)  # สีเมื่อกด
#---end set keyboard 



#####################################################################################################################################################################
# PASS FAIL Process

def writeTable():
    global _log
    global _status
    global tmpbit
    rows = dpg.get_item_children("main_tb", 1)
   
    with dpg.table_row(parent="main_tb"):
        dpg.add_text(len(rows)+1)
        dpg.add_text(_log["sn"])
        dpg.add_text(tmpbit)
        dpg.add_text(_status)
        
def setbit():
    global _pass
    global tmpbit
    tmpbit=(f"{str(_pass['sn'])}{str(_pass['big_text'])}{str(_pass['small_text'])}{str(_pass['pos'])}")
    #dpg.set_value("comparePOS12",tmpbit) 

###########################
# Export  PASS?FAIL 
def exportLOG():
    global _log
    global _status
    global tmpbit
    setbit()
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S") # Format without microseconds       
    #print("export file.....")
    print(_log)
    print("")
    print("Plexus (Thailand) Co., Ltd.")
    #{'pos1': [470, 30], 'pos2': [158, 107], 'sn': '11111111111',
    # 'big_text': "QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,....",
    # 'small_text': "qwertyuiopasdfghjkl;'zxcvbnm,.vfgb"}
    print(f"SN:{_log['sn']}")
    print(f"{formatted_datetime}")  
    print("-"*20)
    
   
    
        
        
    print(f"Mouse movement from {_log['pos1']} to {_log['pos2']}        ")    
    print("Keyboard capital data")
    print(f"\t{_log['big_text']}")    
    print("Keyboard nomal data")
    print(f"\t{_log['small_text']}")
    print("")
    print(f"Test resutl :\t{_status}  \tBit set: {tmpbit}")
    
    
###########################
# Show PASS?FAIL 
    
def showResult(resultme):  
    if resultme=="PASS":
        pass_ImageAddress = 'pass.png'
        img = cv2.imread(pass_ImageAddress)
        cv2.imshow("GLX Result", img)
        cv2.moveWindow("GLX Result", 900, 200)
    else:
        fail_ImageAddress = 'fail.png'
        img = cv2.imread(fail_ImageAddress)
        cv2.imshow("GLX Result", img)
        cv2.moveWindow("GLX Result", 900, 200)
    cv2.waitKey(0) # เพิ่มบรรทัดนี้: รอจนกว่าจะมีการกดปุ่มใดๆ บนหน้าต่าง OpenCV
    cv2.destroyAllWindows() # เพิ่มบรรทัดนี้: ปิดหน้าต่าง OpenCV ทั้งหมด
#################################################################### upper def for pass fail process ####################################################################

###########################
# clear all gui
###########################
# Reset 
def clsGUI():
    global _status
    _status="FAIL"    
    dpg.configure_item("big_text", enabled=True)
    dpg.configure_item("small_text", enabled=True)
    dpg.configure_item("sn", enabled=True)
    cv2.destroyAllWindows() # เพิ่มบรรทัดนี้: ปิดหน้าต่าง OpenCV ทั้งหมด
    global _readData
    global _pass
    global _cntInput
    global _cntBigtext
    global _cntSmalltext
    global _log
    _log.clear()
    _readData.clear()
    _pass.clear()
    _cntInput=0
    _cntBigtext=0
    _cntSmalltext=0

    #_template_bigText=set("QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./") 

    dpg.set_value("count_sn","0 digit")
    dpg.set_value("count_ABC","0")
    dpg.set_value("show_bigText","")
    dpg.set_value("count_abc","0")
    dpg.set_value("show_small_text","")
    dpg.set_value("readPos1_text","")
    dpg.set_value("readPos2_text","")
    dpg.set_value("comparePOS12","") 

    dpg.set_value("sn","")
    dpg.set_value("big_text","")
    dpg.set_value("small_text","")   
    dpg.set_value("readPos1_text","")
    dpg.set_value("readPos2_text","")
    dpg.set_value("comparePOS12","")

    

###########################
# Reset 
def resetInput():
    global _status
    _status="FAIL"    
    dpg.configure_item("big_text", enabled=True)
    dpg.configure_item("small_text", enabled=True)
    dpg.configure_item("sn", enabled=True)
    cv2.destroyAllWindows() # เพิ่มบรรทัดนี้: ปิดหน้าต่าง OpenCV ทั้งหมด
    global _readData
    global _pass
    global _cntInput
    global _cntBigtext
    global _cntSmalltext
    global _log
    _log.clear()
    _readData.clear()
    _pass.clear()
    _cntInput=0
    _cntBigtext=0
    _cntSmalltext=0

   # _template_bigText=set("QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./") 


    #dpg.set_value("sn","")
    #dpg.set_value("big_text","")
    #dpg.set_value("small_text","")   
    dpg.set_value("readPos1_text","")
    dpg.set_value("readPos2_text","")
    dpg.set_value("comparePOS12","")
     
###########################
# Read Windows    
def readwindow():
    readwindow = dpg.get_item_pos("Mainbox")
    viewport_width = dpg.get_viewport_width()
    viewport_height = dpg.get_viewport_height()
    print("mianbox",readwindow)
    print("viewport_w=",viewport_width)
    print("viewport_h=",viewport_height)


###########################
# Check Input length
def chkInputlength(sender, app_data, user_data):
    global _template_bigText
    if sender=="sn"    :
        _cntInput=0
        _cntInput=len(app_data)
        if _cntInput==11:
           dpg.configure_item(sender, enabled=False) 
        else:
            dpg.configure_item(sender, enabled=True)
        dpg.set_value("count_sn",f"{_cntInput} digit") # เปลี่ยนตรงนี้    
    elif sender=="big_text":
        _cntInput=0
        _cntInput=len(app_data)        
        input_bigText=set(dpg.get_value("big_text"))
        input_bigText_missing=_template_bigText-input_bigText
        dpg.set_value("count_ABC",_cntInput)
        if(len(input_bigText_missing)==0):
            dpg.set_value("show_bigText","-> Capital Key capture : PASSED") 
            dpg.configure_item(sender, enabled=False) 
        else:
            dpg.set_value("show_bigText",input_bigText_missing)  
            dpg.configure_item(sender, enabled=True)

        '''print(len(input_bigText_missing))
        dpg.set_value("show_bigText",input_bigText_missing)  
        _cntInput=0
        _cntInput=len(app_data)
        dpg.set_value("count_ABC",_cntInput)
        if _cntInput==68:
            print(app_data)
            _cntBigtext=1
            dpg.configure_item(sender, enabled=False)
        else:
            dpg.configure_item(sender, enabled=True)
            _cntBigtext=0'''

    elif sender=="small_text":
        _cntInput=0
        _cntInput=len(app_data)        
        input_small_text=set(dpg.get_value("small_text"))
        input_small_text_missing=_template_small_text-input_small_text
        dpg.set_value("count_abc",_cntInput)
        if(len(input_small_text_missing)==0):
            dpg.set_value("show_small_text","-> Small Key capture : PASSED") 
            dpg.configure_item(sender, enabled=False) 
        else:
            dpg.set_value("show_small_text",input_small_text_missing)  
            dpg.configure_item(sender, enabled=True)













        '''_cntInput=0
        _cntInput=len(app_data)
        dpg.set_value("count_abc",_cntInput)
        
        if _cntInput==68:
            print(app_data)
            _cntSmalltext=1
            dpg.configure_item(sender, enabled=False)
        else:
            dpg.configure_item(sender, enabled=True)
            _cntSmalltext=0
        '''
    else:
        pass

###########################
# Read POS
def  check_pos1and2():
    global  _readData
    print(_readData[1],_readData[2])
 
 
def readPos1(sender, app_data, user_data):  
    global  _readData
    #readwindow()
    check_box1 = dpg.get_item_pos("child_box")
    _readData[1]=check_box1
    #dpg.set_value("readPos1_text",_readData[1])

    dpg.set_item_label("readPos1", f"readPos1\n{_readData[1]}")
    check_pos1and2()  
 
def readPos2(sender, app_data, user_data): 
    global  _readData
    check_box2 = dpg.get_item_pos("child_box")
    _readData[2]=check_box2
    #dpg.set_value("readPos2_text",_readData[2])
    dpg.set_item_label("readPos2", f"readPos2\n{_readData[2]}")
    #print("_readData[2]",_readData[2])
    check_pos1and2()  
     
    
     
  

##########################
# Process
def Process():
    global _pass
    global _readData
    global _status

    _status="FAIL"
    
    cv2.destroyAllWindows() # เพิ่มบรรทัดนี้: ปิดหน้าต่าง OpenCV ทั้งหมด
    # Postition
    #print("len=",len(_readData))
    #print("data=",len(_readData))
    
    if "pos1" not in _log:
        _log['pos1']="-99"
        
    if "pos2" not in _log:
        _log['pos2']="-99"

 
        
    if len(_readData)<=0:
        dpg.set_value("comparePOS12","Blank data")         
    else:
        if _readData[1]==_readData[2]:
            _pass["pos"]=0
            dpg.set_value("comparePOS12","Same POS isn't Accepted")
            log["pos1"]="Unaccepted"
            _log["pos2"]="Unaccepted"                      
        else:
            _pass["pos"]=1
            _log["pos1"]=_readData[1]
            _log["pos2"]=_readData[2]
            
    # SN        
    sn=dpg.get_value("sn")
    sn_len=len(sn)     
    if sn.isdigit() and sn_len==11:        
        _pass["sn"]=1
        _log["sn"]=sn
    else:
        #error dpg.set_item_activated("sn")
        dpg.focus_item("sn")
        #dpg.set_value("sn","Error")
        _pass["sn"]=0
        _log["sn"]="none"
        
    #big_text 34char
    if dpg.get_value("big_text").isupper():
        _pass["big_text"]=1
        _log["big_text"]=dpg.get_value("big_text")
    else:
        dpg.focus_item("big_text")
        dpg.set_value("big_text","Error,saved...")
        _pass["big_text"]=0
        _log["big_text"]=dpg.get_value("big_text")

    #SMALL 34char
    if dpg.get_value("small_text").islower():               
        _pass["small_text"]=1
        _log["small_text"]=dpg.get_value("small_text")
    else:
        dpg.focus_item("small_text")
        dpg.set_value("small_text","Error,saved...")
        _pass["small_text"]=0
        _log["small_text"]=dpg.get_value("small_text")

    if len(_readData)>0:        
        if _readData[1]==_readData[2]:               
            _pass["pos"]=0
            _log["pos1"]=_readData[1]
            _log["pos2"]=_readData[2]
        else:
            _pass["pos"]=1
            _log["pos1"]=_readData[1]
            _log["pos2"]=_readData[2]
    else:
        _pass["pos"]=0
        
    #     dpg.focus_item("small_text")
    #    dpg.set_value("small_text","Error,saved...")
    #    _pass["small_text"]=0
    #    _log["small_text"]=dpg.get_value("small_text")

      
    
    # show PASS / FAIL poopup
    if _pass["sn"]==1:
        if 0 in _pass.values():
            exportLOG()
            #print("input -data=",_pass)
            dpg.set_value("comparePOS12",f"Test flag number is {sum(_pass.values())}")
            setbit()
            writeTable()        
            showResult("FAIL")
            _status="FAIL"
            resetInput()
        else:
            exportLOG()
            _status="PASS"
            print("input -data=",_pass)
            dpg.set_value("comparePOS12",f"Test flag number is {sum(_pass.values())}")
            setbit()
            writeTable()
            showResult("PASS")
            resetInput()
             
        

dpg.create_context()
dpg.create_viewport(title=_program_title, width=1000, height=500)

#####    main  box #######
##########################
        
with dpg.window(label="Mainbox", width=600, height=400,tag="Mainbox"):       
    #dpg.add_text("Test Progress")
    #dpg.add_text("0",tag="percent_text")
    with dpg.table(header_row=True, resizable=True, borders_innerH=True, borders_outerH=True,
                   borders_innerV=True, borders_outerV=True,tag="main_tb"):
        dpg.add_table_column(label="ID", width_fixed=True, init_width_or_weight=50)
        dpg.add_table_column(label="Serial")
        dpg.add_table_column(label="Value") # Corrected constant
        dpg.add_table_column(label="Status")    
    dpg.add_separator()    
    #dpg.add_progress_bar(default_value=0, width=-1,tag="input_form_progress")
    #dpg.add_button(label="Save Table", ) 
     
#####    Sub  box #######
##########################

with dpg.window(label="Test Windows", show=True, id="child_box",
                no_title_bar=False,tag="child_box",pos=[470,30],width=500,height=280):
    #dpg.configure_item(item_tag, label="New Label Text")
    #Default value is
    
    count_sn=0 
  
    with dpg.group(horizontal=True):
        dpg.add_input_text(label="Sn: " ,tag="sn",width=130,callback=chkInputlength)
        dpg.add_text(tag="count_sn",default_value=f"{count_sn} digit")
    
    dpg.add_spacer(height=2)    
    
    with dpg.group(horizontal=True):
        dpg.add_input_text(label="ABCDEF" ,tag="input1",width=130,height=100, callback=setkb)
     #   dpg.add_text(tag="count_ABC",default_value="0")
  #  global _template_bigText     

  #  dpg.add_text(tag="show_bigText",default_value="")
    dpg.add_spacer(height=2) 
    i=0
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    
    for row in keyboard_layout:
        i+=1 
        with dpg.group(horizontal=True):
            for key in row:            
                dpg.add_button(label=key, tag="btn_"+str(ord(key)),callback=chekbtn1,user_data=key,width=30, height=20)
            if i==2:    
                dpg.add_button(label="Enter",  width=69, height=20,tag="glx-enter")
                dpg.bind_item_theme("glx-enter", button_theme) 
            elif i==3:
                dpg.add_button(label="Shift",  width=108, height=20,tag="glx-shift")
                dpg.bind_item_theme("glx-shift", button_theme) 

    dpg.add_button(label=" Space bar ", tag="btn_32",callback=chekbtn1,user_data=32,width=489, height=20) 
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    dpg.add_spacer(height=2) 
    dpg.add_separator()
    with dpg.group(horizontal=True): 
        dpg.add_button(label="readPos1", callback=readPos1,width=100, height=40,tag="readPos1") 
        dpg.add_text(tag="readPos1_text",default_value="")

    with dpg.group(horizontal=True):         
        dpg.add_button(label="readPos2", callback=readPos2,width=100, height=40,tag="readPos2") 
        dpg.add_text(tag="readPos2_text",default_value="")

















#    with dpg.group(horizontal=True): 
#        dpg.add_input_text(label="abcdef",tag="small_text" ,width=130,callback=chkInputlength)
     #   dpg.add_text(tag="count_abc",default_value="0")
#show_small_text
    #dpg.add_text(tag="show_small_text",default_value="")

#    dpg.add_spacer(height=2)        
    #dpg.add_checkbox(label="checkbox1", default_value=True)
#    with dpg.group(horizontal=True): 
#        dpg.add_button(label="readPos1", callback=readPos1)
#        dpg.add_text(tag="readPos1_text",default_value="")

   # with dpg.group(horizontal=True):         
        #dpg.add_button(label="readPos2", callback=readPos2)
        #dpg.add_text(tag="readPos2_text",default_value="")
        
    #dpg.add_dummy(width=2)  error
    # dpg.add_hspacer(width=2) error
    #dpg.add_spacer(width=10)
    #dpg.add_text(tag="comparePOS12",default_value="Same POS.")    
    #dpg.add_spacer(height=2) 
        
    #dpg.add_separator()
    #dpg.add_button(label="Process", callback=Process)
    #dpg.add_button(label="Reset", callback=clsGUI)
     
############################

############################ 

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()