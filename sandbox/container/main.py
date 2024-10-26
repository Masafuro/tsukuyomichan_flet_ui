import flet as ft
from core import CustomContainer

def main(page: ft.Page):
    # ウィンドウサイズを微調整
    page.window.width = 835
    page.window.height = 660
    page.window.resizable = False  # 最新バージョンに対応

    # カスタムコンテナのインスタンスを作成
    custom_container = CustomContainer()

    # ページにカスタムコンテナを追加
    page.add(custom_container)

    # UI部にアクセス
    ui_area = custom_container.get_ui_area()

    # ボタン1を作成してUI部に追加
    button1 = ft.ElevatedButton(
        text="ボタン1",
        on_click=lambda e: custom_container.update_message_text("ボタン1がクリックされました")
    )

    # クリアボタンを作成してUI部に追加
    clear_button = ft.ElevatedButton(
        text="クリア",
        on_click=lambda e: custom_container.clear_ui_area()
    )

    # ボタンをUI部に追加
    ui_area.controls.extend([button1, clear_button])
    ui_area.update()

ft.app(target=main)
