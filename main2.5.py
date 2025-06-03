import csv
import dearpygui.dearpygui as dpg

import os

file_path = os.path.join(os.path.dirname(__file__), "1.csv")

def fnc_setValue():
    pass
    tmpdata=dpg.get_value("popup_input_field")
    print("xxxxxxx=",tmpdata)

def on_row_selected(sender, app_data, user_data):
    print("Row selected:", user_data)
    dpg.set_value("my_text", user_data)
    #popup_input_field
    dpg.set_value("popup_input_field", user_data[2])  
    
def load_csv_callback():
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
    except Exception as e:
        print("Error:", e)
        return

    # ล้างตารางก่อนใส่ใหม่
    dpg.delete_item("table", children_only=True)
    for row in data:
        print(len(row))
        print(row)

    # คำนวณจำนวนคอลัมน์มากที่สุด
    max_cols = max(len(row) for row in data)

    # สร้าง header ถ้ายังไม่มี
    for i in range(max_cols+1):
        dpg.add_table_column(label=f"Col {i+1}", parent="csv_table")

    # เพิ่มแถวในตาราง
    for row in data:
        
        with dpg.table_row(parent="csv_table"):
            for cell in row:
                dpg.add_selectable(label=cell, callback=on_row_selected, user_data=row)    
              
              #  dpg.add_text(cell)

            for _ in range(max_cols - len(row)):
                dpg.add_text("")  # เติมช่องว่างหากแถวสั้น

dpg.create_context()
dpg.create_viewport(title="CSV Viewer (Dear PyGui)", width=900, height=600)

with dpg.window(label="CSV Table Window", width=850, height=590):
    dpg.add_button(label="Load CSV", callback=load_csv_callback)
    with dpg.table(header_row=True, resizable=True, borders_innerH=True, borders_outerH=True,
                   borders_innerV=True, borders_outerV=True, policy=dpg.mvTable_SizingStretchProp, tag="csv_table", callback=on_row_selected):
        pass


with dpg.window(label="Result", width=20, height=20,pos=[800,20],tag="result_table"):
    dpg.add_input_text(label="Result", width=20, height=20,tag="result")
    dpg.add_text("Result")

with dpg.window(label="Right click window", show=True, id="right_click_menu", no_title_bar=False,tag="popup_window"):
    dpg.add_text("default Hello", tag="my_text")
    dpg.add_input_text(tag="popup_input_field", hint="xxxx")
    dpg.add_button(label="Set", callback=fnc_setValue)
    pass


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
