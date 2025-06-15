'''#
#
#
#
#
#

7.52 
add enter in popup input box
show path template
7.5 add status caption
add test percent
add auto copy




'''



import csv
import dearpygui.dearpygui as dpg

import os
from datetime import datetime

file_path = os.path.join(os.path.dirname(__file__), "1.csv")

temp_slect_data=[]
_progress=0
_max_list=0
_current_list=0

_inputForm={}
_program_title=""
#########################
'''def set_msg(data):
    old_msg=dpg.get_value("log_field")
    data=data+"\n"+old_msg
    dpg.set_value("log_field", data)
'''
 
def get_all_table_data():

    table_data = []
    try:
        # ดึงข้อมูลทุกแถวจากตาราง
        rows = dpg.get_item_children("csv_table", slot=1)  # slot=1 คือ child slots
        if rows:
            for row_idx, row in enumerate(rows):
                row_data = []
                # ดึงข้อมูลแต่ละเซลล์ในแถว
                cells = dpg.get_item_children(row, slot=1)
                for cell in cells:
                    cell_value = dpg.get_item_label(cell)
                    row_data.append(cell_value)
                table_data.append(row_data)
        return table_data
    except Exception as e:
        print("Error getting table data:", e)
        return []

def save_table_to_file():
    # ดึงข้อมูลจากตาราง
    table_data = get_all_table_data()
    if table_data:
        try:
            # บันทึกลงไฟล์ CSV
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"export_table_data_{timestamp}.csv"
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(table_data)
            print(f"Saved table data to {output_file}")
        except Exception as e:
            print("Error saving to file:", e)








#def fun_next_row():
 #   print("next row")
 #   #on_row_selected, user_data=tmp_data+[cnt_cell],tag=tag_id)  



########################
#check data and will set PASS/FAIL word in the last column
def chk_val_limit(lex_limit,lex_click_data):
    #call from on_row_selected
        #chk_val_limit(lex_limit=temp_slect_data[-2],lex_click_data=temp_slect_data)

    print("********************************")
    print(lex_limit,"lex_click_data=",lex_click_data)
    print("********************************")
    

def fnc_setValue():
     
    global _inputForm
    global _max_list
    #tmp_new_data=dpg.get_value("popup_input_field")
    tmp_new_data=dpg.get_value("popUpWindow_input_text")
    global temp_slect_data
    tmp_row_col="row_"+str(temp_slect_data[0])+"_5"
    print("after click ok ",tmp_new_data,tmp_row_col)
 
    #print("xxxxxxx=",tmp_row_col)
    dpg.set_item_label(tmp_row_col, tmp_new_data)
    
    _inputForm[temp_slect_data[0]]=1 #keep row number  key  for  check current add input to table form  \\\ only colum 3 \\\ add adding by set input box 
    print("current input ",_inputForm)
    dpg.set_value("input_form_text",sum(_inputForm.values()))
    dpg.set_value("input_form_progress",sum(_inputForm.values())/_max_list)
    dpg.set_value("percent_text",sum(_inputForm.values())/_max_list*100)   
    #DELETE POPUP
    dpg.delete_item("New_Window_popup") if dpg.does_item_exist("New_Window_popup") else None
    print(f"maxlist={_max_list}")
    print(f"currentlist={_current_list}")
    #print(f"key is{dpg.mvKey_Return}") 525 is key enter 
    #if enter active will call fun_next_row
   # fun_next_row()






def show_popInput():
    global temp_slect_data
    tmp_row_col="row_"+str(temp_slect_data[0])+"_5"
    x, y = dpg.get_item_rect_min(tmp_row_col)

    dpg.delete_item("New_Window_popup") if dpg.does_item_exist("New_Window_popup") else None
    with dpg.window(label="Enter Value", tag="New_Window_popup", pos=(x, y+21)):
        with dpg.group(horizontal=False,tag="container_popup_Input_text"):
            
            ##################################################################################################
            #pop up input box for setting new value 
            #create new window for input data to table      
            dpg.add_input_text(label="Input Text", tag="popUpWindow_input_text",on_enter=True,callback=fnc_setValue)                  
            #dpg.add_text("")  # สร้างบรรทัดว่าง
            dpg.add_spacing(count=2)  # เพิ่มระยะห่าง 5 pixels
            with dpg.group(horizontal=True, tag="container_popup_New"):
                pass
            dpg.add_spacing(count=5)  # เพิ่มระยะห่าง 5 pixels
            dpg.add_button(label="Set Value", callback=fnc_setValue,tag="Set Value")
            ##################################################################################################


    


def on_row_selected(sender, app_data, user_data):
    global _inputForm 
    global _max_list
    print("============================================")
    print("Row selected:", user_data)
    
    dpg.set_value("my_text", user_data)

    #popup_input_field deatil windows  for input data
    dpg.set_value("popup_input_field", user_data[3])  
    global temp_slect_data
  
    
    #################################################
    
    temp_slect_data=user_data   
    print("temp_slect_data=",  temp_slect_data)
    
    #after click a row
    #Row selected: [40, '15.2.1', 'SYSTEM STATUS', 'OFF', 'option', 3]
    #temp_slect_data= [40, '15.2.1', 'SYSTEM STATUS', 'OFF', 'option', 3]

    if len(user_data)>5:
        #Row selected: [15, '8.2', 'Visual check EMO RELAY LED.', 'ON GREEN', 'option', 2]
        #print("select column",temp_slect_data[5])
        if(temp_slect_data[5]==3):
            print("select column 3") 
            ########################################################
            
            _inputForm[temp_slect_data[0]]=1 #keep row number  key  for  check current add input to table form  \\\ only colum 3 \\\ add adding by set input box 
            print("current input ",_inputForm)
            dpg.set_value("input_form_text",sum(_inputForm.values()))   
            dpg.set_value("input_form_progress",sum(_inputForm.values())/_max_list)
            #dpg.set_value("percent_text",sum(_inputForm.values())/_max_list*100)    
            percentx=f"{(sum(_inputForm.values())/_max_list*100):.2f}%"
            dpg.set_value("percent_text",percentx)
            #####################
            #show pop up input box
            #####################            
            show_popInput()
            dpg.set_value("popUpWindow_input_text",temp_slect_data[-3])
            dpg.focus_item("popUpWindow_input_text")


            #####################
            #copy from 3 to 5 
            #####################
            #if  temp_slect_data[-3] has two value will split and make a new select 
            tmp_row_col="row_"+str(temp_slect_data[0])+"_5"  #link to column 5 where i need to copy
 
            
            #####################
            #create butn  if col4 has two data  with "|" this section is working
            #####################
            temp_split=temp_slect_data[-3].split("|")
            if(len(temp_split)>1):
                for x in temp_split:
                    dpg.add_button(label=x,tag="input_"+x,  parent="container_popup_New")#add to popup window 
                    # ย้ายปุ่ม input_btnx ให้อยู่เหนือปุ่ม Set
                    #dpg.move_item("input_btnx", parent="container_popup_Input_text", before="Set Value")       
                #dpg.set_item_label("popUpWindow_input_text", "temp_split[0]") #default value    
                dpg.set_value("popUpWindow_input_text", temp_split[0])   #set input text by first list[0]


            else:
                #if value has only one word this loop will work
                for x in temp_split:
                    # เปลี่ยน ON เป็น OFF
                    #button_value_change = "OFF" if "ON" in x else x
                    # เปลี่ยน ON เป็น OFF โดยใช้ replace
                    if "ON" in x:
                        button_value = x.replace("ON", "OFF")
                        dpg.add_button(label=x,tag="input_"+x,  parent="container_popup_New")#add default text to popup window 
                        dpg.add_button(label=button_value,tag="input_"+button_value,  parent="container_popup_New")#add new text to popup window 
                        button_label = dpg.get_item_label("input_"+x)  # อ่าน label ของปุ่ม
                        dpg.set_item_label(tmp_row_col, button_label) #default value    

                    elif "OFF" in x:
                        button_value = x.replace("OFF", "ON")
                        dpg.add_button(label=x,tag="input_"+x,  parent="container_popup_New")#add default text to popup window 
                        dpg.add_button(label=button_value,tag="input_"+button_value,  parent="container_popup_New")#add new text to popup window 
                        button_label = dpg.get_item_label("input_"+x)  # อ่าน label ของปุ่ม
                        dpg.set_item_label(tmp_row_col, button_label) #default value    

                    #opposite word autogen and add a new button
                    #dpg.add_button(label=button_value_change,tag="input_"+button_value_change,  parent="container_popup_New")#add to popup window 
                    # ย้ายปุ่ม input_btnx ให้อยู่เหนือปุ่ม Set
                    #dpg.move_item("input_btnx", parent="container_popup_Input_text", before="Set Value")                     
 
            print("55555555555555555555555555555555555555555555")
            print("temp_slect_data[-2]=",temp_slect_data[-2])
            print("lex_click_data=",temp_slect_data)
            print("55555555555555555555555555555555555555555555")
            #########################################################
            chk_val_limit(lex_limit=temp_slect_data[-2],lex_click_data=temp_slect_data)
            ##########################################################

            ##################################################
            #check data before show pass or  fail 
            ##################################################
            tmp_row_col_limit="row_"+str(temp_slect_data[0])+"_4"  #link to column 4
            print("tmp_row_col_limit",tmp_row_col_limit)
            tmp_row_col_limit_text=dpg.get_item_label(tmp_row_col_limit)    
            print("tmp_row_col_limit_text",tmp_row_col_limit_text)


        else:    
            print("temp_slect_data=",  temp_slect_data)
    else:#[14, '8.1', 'SYSTEM STATUS', 'ON', 2]
        if(temp_slect_data[-1]==3):
            print(temp_slect_data[-1])
            _inputForm[temp_slect_data[0]]=1 #keep row number  key  for  check current add input to table form  \\\ only colum 3 \\\ add adding by set input box 
            # print("select column<5",temp_slect_data)
            dpg.set_value("input_form_text",sum(_inputForm.values()))   
            dpg.set_value("input_form_progress",sum(_inputForm.values())/_max_list)        
            #dpg.set_value("percent_text",sum(_inputForm.values())/_max_list*100)    
            percentx=f"{(sum(_inputForm.values())/_max_list*100):.2f}%"

            dpg.set_value("percent_text",percentx) 
            show_popInput()

    #tag_id="row_"+str(row_idx + 1)+"_"+str(cnt_cell)
    #tmp_row_col="row_"+str(user_data[0])+"_"+str(user_data[4]) # dynamic cell
    tmp_row_col="row_"+str(user_data[0])+"_5"
     # get only last column

    cell_value = dpg.get_value(tmp_row_col)
    cell_label = dpg.get_item_label(tmp_row_col)

    print("cell_value=",cell_value)
    print("cell_label=",cell_label)
        

def load_csv_callback():
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
    except Exception as e:
        print("Error:", e)
        return
    #set title bar
    global _program_title
    _program_title=""
    _program_title+="  Reading=>"+file_path

    
    #not use dpg.set_main_window_name(_program_title)
    dpg.set_viewport_title(_program_title)

                             
    #set value for progress bar 0 % and counter 0
    global _inputForm
    _inputForm={}
    global _max_list
    _max_list=0
    dpg.set_value("input_form_text",0)   
    dpg.set_value("input_form_progress",0)
    percentx=f"{(0):.2f}%"
    dpg.set_value("percent_text",percentx)


    # ล้างตารางก่อนใส่ใหม่
    dpg.delete_item("csv_table", children_only=True)
    for row in data:
        #print(len(row))  column counter
        #print(row)

    # คำนวณจำนวนคอลัมน์มากที่สุด
        max_cols = max(len(row) for row in data)+3

    # สร้าง header ถ้ายังไม่มี
    for i in range(max_cols):
        dpg.add_table_column(label=f"Col {i+1}", parent="csv_table")

    # เพิ่มแถวในตาราง
    for row_idx, row in enumerate(data): #  
        _max_list=_max_list+1
        tmp_data=[]
        with dpg.table_row(parent="csv_table"): 
            cnt_cell=0
            # Add row number first
           # dpg.add_selectable(label=str(row_idx + 1), callback=on_row_selected, user_data=[row_idx + 1]+row)
            #dpg.add_selectable(label=str(row_idx + 1))
            dpg.add_text(str(row_idx + 1))
           # dpg.add_selectable(label="row_"+str(row_idx + 1)+"_"+str(cnt_cell))
           
           
            for cell in row:                 
                cnt_cell=cnt_cell+1
                #print("xxxx",cell,len(row))               
                tmp_data = [row_idx + 1] + row  # Include row number in the data
                #  dpg.add_selectable(label="row_"+str(row_idx + 1)+"_"+str(cnt_cell), 
                # callback=on_row_selected, user_data=tmp_data,tag="row_"+str(row_idx + 1)+"_"+str(cnt_cell))  
                tag_id="row_"+str(row_idx + 1)+"_"+str(cnt_cell)
                
                #dpg.add_selectable(label=cell, callback=on_row_selected, user_data=tmp_data+[cnt_cell],tag=tag_id)

                ######## only col 3 can click ########
                #if cnt_cell==3:
                dpg.add_selectable(label=cell, callback=on_row_selected, user_data=tmp_data+[cnt_cell],tag=tag_id)    
 
                 

               # print("row_"+str(row_idx + 1)+"_"+str(cnt_cell))
               
              #  dpg.add_text(cell)

            for _ in range(max_cols - len(row)):
                cnt_cell=cnt_cell+1
               #dpg.add_text("-")  # เติมช่องว่างหากแถวสั้น
            #   dpg.add_selectable(label="row_"+str(row_idx + 1)+"_"+str(cnt_cell), callback=on_row_selected, user_data=tmp_data,tag="row_"+str(row_idx + 1)+"_"+str(cnt_cell)) 
                tag_id="row_"+str(row_idx + 1)+"_"+str(cnt_cell)

                dpg.add_selectable(label="" , callback=on_row_selected, user_data=tmp_data+[cnt_cell],tag=tag_id)     
             
              


############################################################################################################
#####                                           MAIN                                                    ####
############################################################################################################
dpg.create_context()

_program_title="GLX:KTestListx01"
dpg.create_viewport(title=_program_title, width=1200, height=600)

 
        

############################
# sub window
############################
#with dpg.window(label="CSV Table Window", width=850, height=800):
with dpg.window(label="Test list", width=850, height=800):
    dpg.add_button(label="Load CSV", callback=load_csv_callback)
       
    dpg.add_text("Test Progress")
    dpg.add_text("0",tag="percent_text")

    dpg.add_progress_bar(default_value=0, width=-1,tag="input_form_progress")
    with dpg.table(header_row=True, resizable=True, borders_innerH=True, borders_outerH=True,
                   borders_innerV=True, borders_outerV=True, policy=dpg.mvTable_SizingStretchProp, tag="csv_table", 
                   callback=on_row_selected) as selectablecells:
        pass
    
     

    
############################
    dpg.add_button(label="Show Table Data", callback=get_all_table_data)
    dpg.add_button(label="Save Table", callback=save_table_to_file)
############################ 





### show data after click a table row 

with dpg.window(label="Test Details", show=True, id="right_click_menu", no_title_bar=False,tag="popup_window",pos=[900,100],width=500,height=100):
    dpg.add_text("GLX-Testlist", tag="my_text")
    dpg.add_text("Input Data", tag="input_form_text")
    dpg.add_input_text(tag="popup_input_field", hint="Gtext")
    #dpg.add_button(label="About", callback=fnc_setValue)

'''
with dpg.window(label="Terminal",tag="Terminal",id="Terminal",pos=[900,300],width=480,height=200):
    dpg.add_text("App loging")
    with dpg.child_window(width=490,height=500):
        # autoscroll is turned on by default as tracked = True
        dpg.add_input_text(
            tag="log_field", multiline=True, readonly=True, tracked=True, track_offset=1, width=-1, height=0)
'''



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()