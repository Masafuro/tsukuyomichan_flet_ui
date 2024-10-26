import flet as ft
from core import CustomContainer

def main(page: ft.Page):
    # ウィンドウサイズを微調整
    page.window.width = 835
    page.window.height = 660
    page.window.resizable = False

    # カスタムコンテナのインスタンスを作成
    custom_container = CustomContainer()

    # ページにカスタムコンテナを追加
    page.add(custom_container)

    # UI部にアクセス
    ui_area = custom_container.get_ui_area()

    # ボタン領域 (高さ230) - 縦横中央揃え
    button_area = ft.Container(
        width=500,
        height=230,
        content=ft.Column(
            [
                ft.Container(
                    content=ft.ElevatedButton(
                        text="画像を変更",
                        on_click=lambda e: custom_container.change_character_image("good_luck.png")
                    ),
                    alignment=ft.alignment.center  # 縦横中央揃え
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER  # 縦方向の中央揃え
        ),
        alignment=ft.alignment.top_left  # 左上に揃える
    )

    # タイトル領域 (高さ50)
    title_text = ft.Text(
        "タイトルテキスト",
        color=ft.colors.BLACK,
        size=20
    )
    title_area = ft.Container(
        content=title_text,
        width=500,
        height=50,
        alignment=ft.alignment.center_left  # 左揃えに設定
    )

    # UI部を分割して配置
    ui_area.controls.extend([button_area, title_area])
    ui_area.update()

ft.app(target=main)
