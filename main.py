from flet import Page, Text
from tsukuyomichan_ui.core import TsukuyomiUI

def main(page: Page):
    # 1. メッセージ表示用のTextパーツを作成
    message_text = Text()

    # 2. TsukuyomiUIのインスタンスを作成
    tsukuyomi = TsukuyomiUI(initial_expression="normal")

    # 3. PageにTextパーツを追加してから、メッセージハンドラとして設定
    page.add(message_text)
    tsukuyomi.set_message_handler(message_text)

    # 4. TsukuyomiUIをPageに追加
    page.add(tsukuyomi)

    # 5. 表情を「happy」に変更し、メッセージを表示
    tsukuyomi.change_expression("thank_you")
    tsukuyomi.say("ありがとうございます。")

if __name__ == "__main__":
    from flet import app
    app(target=main)
