import flet as ft

def main(page: ft.Page):
    # 画面の設定
    page.title = "吹き出しのようなデザイン"
    page.bgcolor = ft.colors.WHITE
    page.padding = 20

    # 画像ウィジェット
    image = ft.Image(
        src="./fukidashi1.png",  # 画像URL（変更可能）
        width=512,
        height=306,
        fit=ft.ImageFit.COVER
    )

    # テキストエリア（複数行）
    text_area = ft.TextField(
        multiline=True,
        # label="吹き出しテキスト",
        value="ここにテキストを入力してください...",
        width=400,
        height=250,
        bgcolor=ft.colors.WHITE,
        border=ft.InputBorder.NONE, 
        border_radius=10,
    )

    # Stackでレイヤーを重ねる
    stack = ft.Stack(
        [
            image,
            ft.Container(
                content=text_area,
                padding=50,
                bgcolor=ft.colors.with_opacity(0.8, ft.colors.WHITE),
                border_radius=10,
                alignment=ft.alignment.top_center,
            ),
        ],
        width=512,
        height=306,
    )

    # ページに追加
    page.add(stack)

# Fletアプリの起動
ft.app(target=main)
