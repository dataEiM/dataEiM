import dearpygui.dearpygui as dpg
import cv2
import datetime
_program_title="GLX Input Check"

_last_tempKB=set()
_last_tempKB_DEL=set()
_last_tempKB_ADD=set()

keyboard_layout_num_BIG=[
81, 87, 69, 82, 84, 89, 85, 73, 79, 80, 91, 93, 92,
65, 83, 68, 70, 71, 72, 74, 75, 76, 59, 39, 90, 88, 
67, 86, 66, 78, 77, 44, 46, 47,32
]

keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P','[',']','\\'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';',"'"],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.','/']    
]

#small key 1-0 -= is [61, 56, 51, 48, 50, 55, 45, 52, 53, 54, 49, 57]
#small key
def chkInputlength(sender, app_data, user_data):
    pass

def set_kb_bg():
    global _last_tempKB
    for i in _last_tempKB:
        ii=str(ord(i))
        if dpg.does_item_exist("btn_"+ii):
            dpg.bind_item_theme("btn_"+ii,button_theme)
            print("new addX=",ii)

def clear_kb_bg():
    global _last_tempKB_DEL
    global _last_tempKB
    print("delXXX=",_last_tempKB_DEL)
    for i in _last_tempKB_DEL:
        ii=str(ord(i))
        if dpg.does_item_exist("btn_"+ii):
            dpg.bind_item_theme("btn_"+ii,"empty_theme")
            print("delX=",ii,"current=",_last_tempKB)

def set_kb_ADD():
    global _last_tempKB_ADD
    for i in _last_tempKB_ADD:
        ii=str(ord(i))
        if dpg.does_item_exist("btn_"+ii):
            dpg.bind_item_theme("btn_"+ii,button_theme)
            print("addX=",ii)
        

#ddddddddddd
# #input1
#ddddddddddd
a=()
def check_kb():
    global a
    global _last_tempKB
    global _last_tempKB_ADD
    global _last_tempKB_DEL

   
    
    kb_txt_conv_2set=set(dpg.get_value("input1"))
    print("check proces=",kb_txt_conv_2set)
    a=[ord(i) for i in kb_txt_conv_2set]
    print(a)

   
    for i in kb_txt_conv_2set: #conv. char set to number
        if ord(i) in {32, 39, 44, 46, 47, 59, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93}: #32,39,44    
            if len(_last_tempKB)==0:
                #--initial _last_tempKB
                #--input value to _last_tempKB
                _last_tempKB=kb_txt_conv_2set
                print("_last_tempKB 1=",_last_tempKB) 
                set_kb_bg()
            elif len(_last_tempKB)<len(kb_txt_conv_2set):
                _last_tempKB_ADD=kb_txt_conv_2set-set(_last_tempKB)
                _last_tempKB=kb_txt_conv_2set
                print("add new=",_last_tempKB_ADD," _last_tempKB=",_last_tempKB)
                set_kb_ADD()
            elif len(_last_tempKB)>len(kb_txt_conv_2set):
                print("del mode")
                _last_tempKB_DEL=_last_tempKB-set(kb_txt_conv_2set)
                _last_tempKB=kb_txt_conv_2set
                print("del_me =",_last_tempKB_DEL," _last_tempKB=",_last_tempKB)
                clear_kb_bg()
            elif len(_last_tempKB)==len(kb_txt_conv_2set):
                print("=loop")
                print("_last_tempKB=",_last_tempKB,"kb_txt_conv_2set=",kb_txt_conv_2set)
            else:
                #equal 
                _last_tempKB=kb_txt_conv_2set
                print("hear")
    if  len(kb_txt_conv_2set)==0:
        #clear all
        print("text last",_last_tempKB)
        _last_tempKB_DEL=_last_tempKB
        clear_kb_bg()
        _last_tempKB.clear()
    else:
        pass
    ##Aasdfasldk;fklf;
    if  len(kb_txt_conv_2set)>0:
     for i in kb_txt_conv_2set:
            if ord(i) in {32, 39, 44, 46, 47, 59, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93}:
                pass

 
def clickKey(sender, app_data, user_data):
    print(f"setkb->sender:{sender},app_data:{app_data},user_data:{user_data}")

#####    main  box #######
##########################
dpg.create_context()
dpg.create_viewport(title=_program_title, width=1000, height=500)


#==== start theme
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
#==== endd theme



with dpg.window(label="Mainbox", width=600, height=400,tag="Mainbox"):     
    with dpg.table(header_row=True, resizable=True, borders_innerH=True, borders_outerH=True,
                   borders_innerV=True, borders_outerV=True,tag="main_tb"):
        dpg.add_table_column(label="ID", width_fixed=True, init_width_or_weight=50)
        dpg.add_table_column(label="Serial")
        dpg.add_table_column(label="Value") # Corrected constant
        dpg.add_table_column(label="Status")    
    dpg.add_separator()    

     
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

    #-------- start input keyboard
    with dpg.group(horizontal=True):
        dpg.add_input_text(label="ABCDEF" ,tag="input1",width=130,height=100, callback=check_kb)
        dpg.add_text(tag="input1_text",default_value="xx")       
    #-------- end  read keyboard
        
 
    dpg.add_spacer(height=2) 
    i=0
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    with dpg.group(tag="kb_layout"):
        for row in keyboard_layout:
            i+=1 
            with dpg.group(horizontal=True):
                for key in row:            
                    dpg.add_button(label=key, tag="btn_"+str(ord(key)),callback=clickKey,user_data=key,width=30, height=20)
                if i==2:    
                    dpg.add_button(label="Enter",  width=66, height=20,tag="glx-enter")
                    #dpg.bind_item_theme("glx-enter", button_theme)
                    
                    
                elif i==3:
                    dpg.add_button(label="Shift",  width=103, height=20,tag="glx-shift")
                    #dpg.bind_item_theme("glx-shift", button_theme) 
        dpg.add_button(label=" Space bar ", tag="btn_32",callback=clickKey,user_data=32,width=450, height=20)
        dpg.bind_item_theme("kb_layout", "border_widget") 
        
        
    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    dpg.add_spacer(height=2) 
    dpg.add_separator()
    dpg.add_spacer(height=2) 
    with dpg.group(horizontal=True):
       # dpg.add_spacer(width=5)
        #dpg.add_button(label="readPos1", callback=readPos1,width=100, height=40,tag="readPos1") 
        dpg.add_button(label="readPos1",width=100, height=40,tag="readPos1") 
       
    #with dpg.group(horizontal=True):         
        #dpg.add_button(label="readPos2", callback=readPos2,width=100, height=40,tag="readPos2") 
        dpg.add_button(label="readPos2",width=100, height=40,tag="readPos2") 

        dpg.add_spacer(width=17)
        #dpg.add_button(label="Process",width=100, height=40, callback=checkProcess)
        dpg.add_button(label="Reset",width=100, height=40)
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()