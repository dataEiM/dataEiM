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
_cnt_key=0
_cntInput=0
_cntBigtext=0
_cntSmalltext=0
_log=dict()     #not use
_log_text=set() #change from dict to set
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
keyboard_layout_num_cmp=[]

keyboard_layout_num_BIG=[81, 87, 69, 82, 84, 89, 85, 73, 79, 80, 91, 93, 92,
65, 83, 68, 70, 71, 72, 74, 75, 76, 59, 39, 90, 88, 
67, 86, 66, 78, 77, 44, 46, 47,32]

#TOP NUMBER [1-0 ,- ,= ]IS 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 61
 
number_skip=[49,50,51,52,53,54,55,56,57]    
keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P','[',']','\\'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';',"'"],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.','/']    
]


#current char to num
'''
32, 39, 44, 46, 47, 59, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93}
'''


def chekbtn1(sender, app_data, user_data):
    print(f"setkb->sender:{sender},app_data:{app_data},user_data:{user_data}")
    

_last_tempKB=()
def check_kb():
    global _log_text
    global _last_tempKB
    global keyboard_layout_num_BIG
    global keyboard_layout_num_cmp
    global _cnt_key
   
    intersection = list()
    char_input=dpg.get_value("input1")
    
    _cnt_key=0
    cnt_i=35
    ii=0
    char_to_num_=set() 
    if len(char_input)>0:
        char_input_to_set_=set(char_input)
        
        print("input = ",char_input) 
    
        for i in char_input_to_set_: #conv. char set to number
            if ord(i) in {32, 39, 44, 46, 47, 59, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93}: #32,39,44
                ii=ii+1
                char_to_num_.add(ord(i))
                # add [A-Z] into char_to_num_{}
                #print("------------"):
                print("current char to num",char_to_num_)
                #print("------------")
                _cnt_key+=1
                _log_text.add(ord(i))
                print("num exist in set=",char_to_num_.issubset(set(keyboard_layout_num_BIG)))
                dpg.bind_item_theme("btn_"+str(ord(i)), button_theme)                
                #cnt_x=dpg.get_value("count_ABC")               
                dpg.set_value("count_ABC",str(cnt_i-ii))
                

    char_input=dpg.get_value("input1")
    print("current kb=",char_input)
    print("last_kb=",_last_tempKB)
    if len(char_input)>0:    
        #----check update current character input
        #----update last add or delete stage
        #----only use delete stage 
        
        if len(_last_tempKB)>len(char_input):
            print("deleted")
            reset_me_=(set(_last_tempKB)-set(char_input))
            print(reset_me_)
            for ix in reset_me_:
                #print( dpg.does_item_exist(dpg.add_button(label=key, tag="btn_"+str(ord(key)))))
                if dpg.does_item_exist("btn_"+str(ord(ix))):
                #if ix.upper():
                    dpg.bind_item_theme("btn_"+str(ord(ix)), "empty_theme")
                    _log_text.remove(ord(ix))
                #dpg.bind_item_theme("btn_"+str(ord(last_char_BIG)), button_theme)
        elif len(char_input)>len(_last_tempKB):
            print("add")
            print(set(char_input)-set(_last_tempKB))
        else:
            pass 
        _last_tempKB=char_input
    else:
        pass
        #---clear last set if user select all and delete
        print("found last command")
        print("last_kb=",_last_tempKB)
        for ix in _last_tempKB:
            if dpg.does_item_exist("btn_"+str(ord(ix))):
                dpg.bind_item_theme("btn_"+str(ord(ix)), "empty_theme")
                _log_text.remove(ord(ix))
                
        #clear all and reset set()
        #dpg.add_text(tag="count_ABC",default_value="35")
        dpg.set_value("count_ABC","35")
    print(">>>>",_cnt_key)
 
    print("keypress log is ", str(_log_text))
        




def setkb(sender, app_data, user_data):
    check_kb()
    #dpg.add_button(label=key, tag="btn_"+str(ord(key)),callback=chekbtn1,user_data=key,width=30, height=20)
    print(f"setkb->sender:{sender},app_data:{app_data},user_data:{user_data}")
    global keyboard_layout_num_cmp
    char_input=dpg.get_value("input1")
    print("check me")
    if len(char_input)>0:
        pass

    print("end check")
    
    #numerical_value.clear()
    
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


with dpg.theme(tag="border_widget"):
    with dpg.theme_component(dpg.mvGroup): # <--- เป้าหมายคือ dpg.group
        dpg.add_theme_color(dpg.mvThemeCol_Border, (20, 80, 10), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0.1, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 5, 5, category=dpg.mvThemeCat_Core) # Padding ภายในกรอบ group
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 5, 5, category=dpg.mvThemeCat_Core) # Spacing ระหว่างปุ่มในแถว













with dpg.theme() as border_me:
    with dpg.theme_component(dpg.mvButton):        
        dpg.add_theme_color(dpg.mvThemeCol_Border, (100, 80, 255), category=dpg.mvThemeCat_Core) # Red Border
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0.2, category=dpg.mvThemeCat_Core) # IMPORTANT: Set border thickness!
        
       
        
with dpg.theme() as button_theme:
    with dpg.theme_component(dpg.mvButton):        
        dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 80, 255), category=dpg.mvThemeCat_Core)  # สีพื้นหลัง
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 180, 255), category=dpg.mvThemeCat_Core)  # สีเมื่อ hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 100, 200), category=dpg.mvThemeCat_Core)  # สีเมื่อกด
        #dpg.add_theme_color(dpg.mvThemeCol_Border, (255, 0, 0, 255), category=dpg.mvThemeCat_Core)
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
    #dpg.set_value("readPos1_text","")
    #dpg.set_value("readPos2_text","")
    dpg.set_value("comparePOS12","") 

    dpg.set_value("sn","")
    dpg.set_value("big_text","")
    dpg.set_value("small_text","")   
    #dpg.set_value("readPos1_text","")
    #dpg.set_value("readPos2_text","")
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
_newPOS=0
def  check_pos1and2():
    global _readData
    global _newPOS
       
    #print("_readData[0][0]=",_readData[1][0])

    if len(_readData)>1:
        if _readData[1][0]==_readData[2][0] and _readData[1][1]==_readData[2][1]:
            _newPOS=0 #same position
            print("Move to new position")
        else:
            _newPOS=1 #different position = pass
            print("Mouse move = pass")
            dpg.bind_item_theme("readPos1", border_me)
            dpg.bind_item_theme("readPos2", border_me) 
   
 
#{1: [201, 67], 2: [579, 85]} 
def readPos1(sender, app_data, user_data):  
    global  _readData
    dpg.bind_item_theme("readPos1", "empty_theme")
    dpg.bind_item_theme("readPos2", "empty_theme")      
    #readwindow()
    #check_box1 = dpg.get_item_pos("child_box")
    _readData[1]=dpg.get_item_pos("child_box")
    check_pos1and2()    

    # ดึงค่า (values) ทั้งหมดออกมาจาก dictionary
    #all_values = _readData.values()   
    #print(set(tuple(all_values)) )
    #_newPOS=set(tuple(all_values))


    #print(_newPOS)
    #dpg.set_value("readPos1_text",_readData[1])
    dpg.set_item_label("readPos1", f"readPos1\n{_readData[1]}")
    #check_pos1and2()  









 
def readPos2(sender, app_data, user_data): 
    global _readData
    dpg.bind_item_theme("readPos1", "empty_theme")
    dpg.bind_item_theme("readPos2", "empty_theme")
    
    #check_box2 = dpg.get_item_pos("child_box")
    _readData[2]=dpg.get_item_pos("child_box")

    check_pos1and2()
    

    # ดึงค่า (values) ทั้งหมดออกมาจาก dictionary
    #all_values = _readData.values()   
     
   # _newPOS=set(tuple(all_values))
    #print(_newPOS)
   
    #dpg.set_value("readPos2_text",_readData[2])
    dpg.set_item_label("readPos2", f"readPos2\n{_readData[2]}")
    #print("_readData[2]",_readData[2])
    #check_pos1and2()  
    #print(_readData)
    
     
  

##########################
# Process

def checkProcess():
    global _pass
    global _cnt_key
    #------
    print("def checkProcess():")
    #--check sn    
    sn=dpg.get_value("sn")
    sn_len=len(sn)     
    if sn.isdigit() and sn_len==11:
        #sn pass
        _pass["sn"]=1
        _log["sn"]=sn
    else:         
        dpg.focus_item("sn")
        _pass["sn"]=0
        _log["sn"]="none"
        
    
    #--check key press value 35 is passed
    auto_cnt_key=dpg.get_value("count_ABC")
    print("count_keypress=",str(_cnt_key)+"="+str(auto_cnt_key))
    if _cnt_key==auto_cnt_key:
        #keypresss pass
        _pass["keypress"]=1
        _log["keypress"]="xxxxx"
    else:
        _pass["keypress"]=0



    print(_pass)
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

with dpg.window(label="-HID Testing-", show=True, id="child_box",
                no_title_bar=False,tag="child_box",pos=[400,30],width=468,height=300):
    #dpg.configure_item(item_tag, label="New Label Text")
    #Default value is
    
    count_sn=0 
  
    with dpg.group(horizontal=True):
        dpg.add_input_text(label="Sn: " ,tag="sn",width=130,callback=chkInputlength)
        dpg.add_text(tag="count_sn",default_value=f"{count_sn} digit")
    
    dpg.add_spacer(height=2)    
    
    with dpg.group(horizontal=True):
        #dpg.add_input_text(label="ABCDEF" ,tag="input1",width=130,height=100, callback=setkb)
        dpg.add_input_text(label="ABCDEF" ,tag="input1",width=130,height=100, callback=check_kb)
        #check_kb 
        dpg.add_text(tag="count_ABC",default_value="35")
       
  #  global _template_bigText     

  #  dpg.add_text(tag="show_bigText",default_value="")
    dpg.add_spacer(height=2) 
    i=0
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    with dpg.group(tag="kb_layout"):
        for row in keyboard_layout:
            i+=1 
            with dpg.group(horizontal=True):
                for key in row:            
                    dpg.add_button(label=key, tag="btn_"+str(ord(key)),callback=chekbtn1,user_data=key,width=30, height=20)
                if i==2:    
                    dpg.add_button(label="Enter",  width=66, height=20,tag="glx-enter")
                    dpg.bind_item_theme("glx-enter", button_theme)
                    
                    
                elif i==3:
                    dpg.add_button(label="Shift",  width=103, height=20,tag="glx-shift")
                    dpg.bind_item_theme("glx-shift", button_theme) 
        dpg.add_button(label=" Space bar ", tag="btn_32",callback=chekbtn1,user_data=32,width=450, height=20)
        dpg.bind_item_theme("kb_layout", "border_widget") 
        
        
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    dpg.add_spacer(height=2) 
    dpg.add_separator()
    dpg.add_spacer(height=2) 
    with dpg.group(horizontal=True):
       # dpg.add_spacer(width=5)
        dpg.add_button(label="readPos1", callback=readPos1,width=100, height=40,tag="readPos1") 
        #dpg.add_text(tag="readPos1_text",default_value="")
        
    #with dpg.group(horizontal=True):         
        dpg.add_button(label="readPos2", callback=readPos2,width=100, height=40,tag="readPos2") 
        #dpg.add_text(tag="readPos2_text",default_value="")
        dpg.add_spacer(width=17)
        dpg.add_button(label="Process",width=100, height=40, callback=checkProcess)
        dpg.add_button(label="Reset",width=100, height=40)
        
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
