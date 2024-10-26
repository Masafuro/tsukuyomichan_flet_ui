import time
from flet import Page, Text
from tsukuyomichan_ui.core import TsukuyomiUI

def main(page: Page):
    # TsukuyomiUIのインスタンスを作成（初期画像サイズを設定）
    tsukuyomi = TsukuyomiUI(initial_expression="normal", image_width=150, image_height=150)

    # テキストパーツを作成してメッセージハンドラとして設定
    message_text = Text()
    page.add(message_text)
    tsukuyomi.set_message_handler(message_text)

    # TsukuyomiUIをPageに追加
    page.add(tsukuyomi)


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
