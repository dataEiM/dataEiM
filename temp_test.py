import dearpygui.dearpygui as dpg

dpg.create_context()

# สร้าง theme สำหรับ widget ต่างๆ
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)

with dpg.window(label="System Dashboard", pos=(20, 50), width=1000, height=600):
    # แบ่งหน้าจอเป็น 2 ส่วน
    with dpg.group(horizontal=True):
        # ส่วนซ้าย - แสดงสถานะ
        with dpg.child_window(width=300, height=550):
            dpg.add_text("System Status", color=(52, 152, 219))
            dpg.add_separator()
            
            # สถานะต่างๆ
            with dpg.group():
                dpg.add_text("Power Status:")
                dpg.add_radio_button(["ON", "OFF"], horizontal=True)
                
                dpg.add_text("Temperature:")
                dpg.add_slider_float(default_value=25.0, min_value=0, max_value=100, format="%.1f °C")
                
                dpg.add_text("Connection:")
                dpg.add_combo(["Connected", "Disconnected", "Error"])

        # ส่วนขวา - แสดงผลการทดสอบ
        with dpg.child_window(width=650, height=550):
            dpg.add_text("Test Results", color=(52, 152, 219))
            dpg.add_separator()
            
            # ตารางผลการทดสอบ
            with dpg.table(header_row=True):
                dpg.add_table_column(label="Test ID")
                dpg.add_table_column(label="Description")
                dpg.add_table_column(label="Status")
                dpg.add_table_column(label="Time")
                
                # ข้อมูลตัวอย่าง
                for i in range(5):
                    with dpg.table_row():
                        dpg.add_text(f"TEST_{i+1}")
                        dpg.add_text("System Check")
                        dpg.add_text("PASS" if i % 2 == 0 else "FAIL")
                        dpg.add_text("10:30:45")

            # กราฟแสดงผล
            dpg.add_text("Test Progress")
            dpg.add_progress_bar(default_value=0.75, width=-1)

    # ปุ่มควบคุมด้านล่าง
    with dpg.group(horizontal=True):
        dpg.add_button(label="Start Test", width=150)
        dpg.add_button(label="Stop Test", width=150)
        dpg.add_button(label="Reset", width=150)
        dpg.add_button(label="Export Report", width=150)

dpg.bind_theme(global_theme)
dpg.create_viewport(title='System Dashboard', width=1050, height=700)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()