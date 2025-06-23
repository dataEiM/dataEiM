import dearpygui.dearpygui as dpg

def key_press_callback(sender, app_data, user_data):
    key = user_data
    print(f"Key pressed: {key}")

dpg.create_context()
dpg.create_viewport(title='Custom Keyboard Layout', width=600, height=400)

keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.']
]

# สร้างธีมสำหรับปุ่ม
with dpg.theme() as button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 128, 255), category=dpg.mvThemeCat_Core)  # สีพื้นหลัง
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 180, 255), category=dpg.mvThemeCat_Core)  # สีเมื่อ hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 100, 200), category=dpg.mvThemeCat_Core)  # สีเมื่อกด

with dpg.window(label="Keyboard"):
    for row in keyboard_layout:
        with dpg.group(horizontal=True):
            for key in row:
                btn = dpg.add_button(label=key, callback=key_press_callback, user_data=key)
                dpg.bind_item_theme(btn, button_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()