import dearpygui.dearpygui as dpg

selected_cell = {"tag": None}

# สร้างธีมพื้นหลังสีฟ้า
with dpg.theme() as blue_bg_theme:
    with dpg.theme_component(dpg.mvSelectable):
        dpg.add_theme_color(dpg.mvThemeCol_Header, (0, 150, 255, 100))  # สีพื้นหลัง
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (0, 150, 255, 150))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (0, 150, 255, 200))

# ฟังก์ชันเลือก cell
def on_cell_click(sender, app_data, user_data):
    # ล้างธีมเดิม
    if selected_cell["tag"]:
        dpg.bind_item_theme(selected_cell["tag"], 0)

    # ใส่ธีมใหม่
    dpg.bind_item_theme(user_data, blue_bg_theme)
    selected_cell["tag"] = user_data

with dpg.window(label="Table"):
    with dpg.table(header_row=False):
        dpg.add_table_column()
        dpg.add_table_column()

        for i in range(3):
            with dpg.table_row():
                for j in range(2):
                    tag = f"cell_{i}_{j}"
                    dpg.add_selectable(label=f"Cell {i},{j}", tag=tag, callback=on_cell_click, user_data=tag)
