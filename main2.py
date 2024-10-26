import time
import flet as ft
from tsukuyomichan_ui.core import TsukuyomiUI

def main(page: ft.Page):
    page.window.width = 800  # ウィンドウの幅を800ピクセルに設定
    page.window.height = 600
    # TsukuyomiUIのインスタンスを作成（初期画像サイズを設定）
    tsukuyomi = TsukuyomiUI(initial_expression="normal", image_width=200, image_height=200)

    page.title = "吹き出しのようなデザイン"
    page.bgcolor = ft.colors.WHITE
    page.padding = 20

    # 画像ウィジェット
    image = ft.Image(
        src="./tsukuyomichan_ui/images/fukidashi/fukidashi1.png",  # 画像URL（変更可能）
        width=512,
        height=306,
        fit=ft.ImageFit.COVER
    )

    # ft.Text を使った読み取り専用の複数行表示
    text_display = ft.Text(
        value="こんにちは",
        width=300,
        height=200,
        bgcolor=ft.colors.WHITE
    )

    # Container 内に ft.Text を配置
    text_container = ft.Container(
        content=text_display,
        width=380,
        height=200,
        # bgcolor=ft.colors.with_opacity(0.8, ft.colors.WHITE),
        padding=10,
        top=40,
        left=50,
        border_radius=10,
        bgcolor=ft.colors.GREY_200

    )
    stack = ft.Container(
        ft.Stack(
            [
                image,
                text_container,
            ],
            width=500,
            height=300,
        ),
        bgcolor=ft.colors.BLUE_100
    )

    # UI部（左下）
    button1 = ft.ElevatedButton("ボタン1")
    button2 = ft.ElevatedButton("ボタン2")
    ui_column = ft.Column(
        [button1, button2],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    # 左側の部分（吹き出しとUI）
    left_column = ft.Container(
        ft.Column(
            [
                stack,  # 吹き出し部
                ui_column  # UI部
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
        ),
        bgcolor=ft.colors.YELLOW_100
    )
    # Tsukuyomi部分（右側）
    tsukuyomi = TsukuyomiUI()

    # 全体のレイアウト（左と右）
    main_row = ft.Container(
        ft.Row(
            [
                left_column,  # 左側の部分
                tsukuyomi  # Tsukuyomi部分
            ],
            width=800,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=20
        ),
        bgcolor=ft.colors.GREEN_100,
    )

    page.add(main_row)
    tsukuyomi.set_image_size(200, 200)



    tsukuyomi.set_message_handler(text_display)
    tsukuyomi.say("新しいメッセージがここに表示されます！")



    # 5秒間待機
    time.sleep(3)
    # 表情を「happy」に変更し、メッセージを表示
    tsukuyomi.change_expression("thank_you")
    tsukuyomi.say("ありがとうございます。")
    # 画像サイズを動的に変更（200x200）
    tsukuyomi.set_image_size(200, 200)

    

if __name__ == "__main__":
    from flet import app
    app(target=main)
