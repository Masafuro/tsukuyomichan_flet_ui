import flet as ft
from core import CustomContainer

def main(page: ft.Page):
    # ウィンドウサイズを微調整
    page.window.width = 835
    page.window.height = 660
    page.window_resizable = False

    custom_container = CustomContainer()
    page.add(custom_container)
    custom_container.update_message_text("from main.pyなのだ。")

ft.app(target=main)
