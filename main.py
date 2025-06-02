import csv
import dearpygui.dearpygui as dpg

import os

file_path = os.path.join(os.path.dirname(__file__), "1.csv")

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
    for i in range(max_cols):
        dpg.add_table_column(label=f"Col {i+1}", parent="table")

    # เพิ่มแถวในตาราง
    for row in data:
        with dpg.table_row(parent="table"):
            for cell in row:
                dpg.add_text(cell)
            for _ in range(max_cols - len(row)):
                dpg.add_text("")  # เติมช่องว่างหากแถวสั้น

dpg.create_context()
dpg.create_viewport(title="CSV Viewer (Dear PyGui)", width=800, height=600)

with dpg.window(label="CSV Table Window", width=790, height=590):
    dpg.add_button(label="Load CSV", callback=load_csv_callback)
    with dpg.table(header_row=True, resizable=True, borders_innerH=True, borders_outerH=True,
                   borders_innerV=True, borders_outerV=True, policy=dpg.mvTable_SizingStretchProp, tag="table"):
        pass


 
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
