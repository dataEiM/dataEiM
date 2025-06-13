import dearpygui.dearpygui as dpg

current_row = {"index": 0}  # ตำแหน่งแถวที่เลือก

def highlight_row(index):
    for i in range(5):
        dpg.set_value(f"row_{i}_cell", i == index)  # True = เลือก, False = ไม่เลือก

def next_row_callback():
    current_row["index"] = (current_row["index"] + 1) % 5
    highlight_row(current_row["index"])

dpg.create_context()

with dpg.window(label="ตัวอย่าง Table"):
    with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingFixedFit):
        dpg.add_table_column(label="ชื่อ")
        dpg.add_table_column(label="อายุ")

        for i in range(5):
            with dpg.table_row():
                dpg.add_selectable(label=f"ชื่อ {i}", tag=f"row_{i}_cell")
                dpg.add_text(f"{20+i} ปี")

    dpg.add_button(label="เลือกแถวถัดไป", callback=next_row_callback)

dpg.create_viewport(title="เลือกแถวถัดไป", width=500, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()

highlight_row(current_row["index"])  # เริ่มต้นเลือกแถวแรก
dpg.start_dearpygui()
dpg.destroy_context()
