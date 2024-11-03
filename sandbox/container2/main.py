# main.py
import flet as ft
from core import MyApp

def main(page: ft.Page):
    # ウィンドウのサイズを設定
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False

    app = MyApp()
    page.add(app)

    # クラスの内容を更新する例
    app.update_header("New Header Content")
    app.update_left_upper_content("Updated Left Upper Content")
    app.update_left_lower_content("Updated Left Lower Content")
    app.update_right_content("Updated Right Content")
    app.update_footer("Modified Footer Content")

ft.app(target=main)
