import flet as ft
import sys

def main(page: ft.Page):
    # ウィンドウが閉じられたときに実行される関数
    def on_window_close(e):
        print("Window is closing...")
        sys.exit()  # プログラムを終了

    # ウィンドウが閉じられたときに on_window_close を呼び出す
    page.on_window_close = on_window_close

    # ボタンを設置
    button = ft.ElevatedButton(text="Click me!", on_click=lambda e: print("Button clicked"))
    page.add(button)

if __name__ == '__main__':
    ft.app(target=main)
