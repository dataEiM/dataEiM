import csv
import dearpygui.dearpygui as dpg

import os
from datetime import datetime

file_path = os.path.join(os.path.dirname(__file__), "1.csv")

temp_slect_data=[]

#########################
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






########################




def fnc_setValue():
    pass    
    tmp_new_data=dpg.get_value("popup_input_field")

    global temp_slect_data
    tmp_row_col="row_"+str(temp_slect_data[0])+"_4"
    print("after click ok ",tmp_new_data,tmp_row_col)
 
    #print("xxxxxxx=",tmp_row_col)
    dpg.set_item_label(tmp_row_col, tmp_new_data)

def on_row_selected(sender, app_data, user_data):
    print("Row selected:", user_data)
    dpg.set_value("my_text", user_data)
    #popup_input_field
    dpg.set_value("popup_input_field", user_data[3])  
    global temp_slect_data
    temp_slect_data=user_data   
    print("temp_slect_data=",  temp_slect_data)


    #tag_id="row_"+str(row_idx + 1)+"_"+str(cnt_cell)
    #tmp_row_col="row_"+str(user_data[0])+"_"+str(user_data[4]) # dynamic cell
    tmp_row_col="row_"+str(user_data[0])+"_4"
     # get only last column

    cell_value = dpg.get_value(tmp_row_col)
    cell_label = dpg.get_item_label(tmp_row_col)


    print("cell_value=",cell_value)
    print("cell_label=",cell_label)
    def show_window():
        x, y = dpg.get_item_rect_min(tmp_row_col)
        
        dpg.delete_item("New_Window_popup") if dpg.does_item_exist("New_Window_popup") else None
        with dpg.window(label="New_Window_popup", tag="New_Window_popup", pos=(x, y)):
            dpg.add_input_text(label="Input Text")
            dpg.add_input_int(label="Input Integer")

    

    show_window()

def load_csv_callback():
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
    except Exception as e:
        print("Error:", e)
        return

    # ล้างตารางก่อนใส่ใหม่
    dpg.delete_item("csv_table", children_only=True)
    for row in data:
        #print(len(row))  column counter
        #print(row)

    # คำนวณจำนวนคอลัมน์มากที่สุด
        max_cols = max(len(row) for row in data)+1

    # สร้าง header ถ้ายังไม่มี
    for i in range(max_cols):
        dpg.add_table_column(label=f"Col {i+1}", parent="csv_table")

    # เพิ่มแถวในตาราง
    for row_idx, row in enumerate(data): #  
        tmp_data=[]
        with dpg.table_row(parent="csv_table"): 
            cnt_cell=0
            # Add row number first
           # dpg.add_selectable(label=str(row_idx + 1), callback=on_row_selected, user_data=[row_idx + 1]+row)
            dpg.add_selectable(label=str(row_idx + 1))
           # dpg.add_selectable(label="row_"+str(row_idx + 1)+"_"+str(cnt_cell))
           
           
            for cell in row:
                cnt_cell=cnt_cell+1
              #  print("xxxx",cell,len(row))
              #  print()
                tmp_data = [row_idx + 1] + row  # Include row number in the data
              #  dpg.add_selectable(label="row_"+str(row_idx + 1)+"_"+str(cnt_cell), callback=on_row_selected, user_data=tmp_data,tag="row_"+str(row_idx + 1)+"_"+str(cnt_cell))  
                tag_id="row_"+str(row_idx + 1)+"_"+str(cnt_cell)
                dpg.add_selectable(label=cell, callback=on_row_selected, user_data=tmp_data+[cnt_cell],tag=tag_id)    
               # print("row_"+str(row_idx + 1)+"_"+str(cnt_cell))
               
              #  dpg.add_text(cell)

            for _ in range(max_cols - len(row)):
                cnt_cell=cnt_cell+1
               #dpg.add_text("-")  # เติมช่องว่างหากแถวสั้น
            #   dpg.add_selectable(label="row_"+str(row_idx + 1)+"_"+str(cnt_cell), callback=on_row_selected, user_data=tmp_data,tag="row_"+str(row_idx + 1)+"_"+str(cnt_cell)) 
                tag_id="row_"+str(row_idx + 1)+"_"+str(cnt_cell)

                dpg.add_selectable(label="" , callback=on_row_selected, user_data=tmp_data+[cnt_cell],tag=tag_id)     
              


dpg.create_context()
dpg.create_viewport(title="CSV Viewer (Dear PyGui)", width=900, height=600)

with dpg.window(label="CSV Table Window", width=850, height=590):
    dpg.add_button(label="Load CSV", callback=load_csv_callback)
    with dpg.table(header_row=True, resizable=True, borders_innerH=True, borders_outerH=True,
                   borders_innerV=True, borders_outerV=True, policy=dpg.mvTable_SizingStretchProp, tag="csv_table", callback=on_row_selected):
        pass
    ###########
    dpg.add_button(label="Show Table Data", callback=get_all_table_data)
    dpg.add_button(label="Save Table", callback=save_table_to_file)
    ###########



with dpg.window(label="Result", width=20, height=20,pos=[800,20],tag="result_table"):
    dpg.add_input_text(label="Result", width=20, height=20,tag="result")
    dpg.add_text("Result")

with dpg.window(label="Right click window", show=True, id="right_click_menu", no_title_bar=False,tag="popup_window",pos=[800,100],):
    dpg.add_text("default Hello", tag="my_text")
    dpg.add_input_text(tag="popup_input_field", hint="xxxx")
    dpg.add_button(label="Set", callback=fnc_setValue)
    pass


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()