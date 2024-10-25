import os
from flet import UserControl, Image

class TsukuyomiUI(UserControl):
    def __init__(self, initial_expression="normal", image_width=200, image_height=200):
        super().__init__()

        # モジュール内のimagesフォルダへのパスを取得
        self.images_dir = os.path.join(os.path.dirname(__file__), "images")

        self.expression = initial_expression
        self.message_handler = None

        # 画像のサイズを設定
        self.image_width = image_width
        self.image_height = image_height

        # 表情画像の辞書を定義
        self.expressions_dict = {
            "please": os.path.join(self.images_dir, "please.png"),
            "thank_you": os.path.join(self.images_dir, "thank_you.png"),
            "good_luck": os.path.join(self.images_dir, "good_luck.png"),
            "prayer": os.path.join(self.images_dir, "prayer.png"),
            "may_i_ask": os.path.join(self.images_dir, "may_i_ask.png"),
            "look_right": os.path.join(self.images_dir, "look_right.png"),
            "look_left": os.path.join(self.images_dir, "look_left.png"),
            "not_good": os.path.join(self.images_dir, "not_good.png"),
            "goodbye": os.path.join(self.images_dir, "goodbye.png")
        }

        # 初期のキャラクター画像を設定
        self.character_image = Image(
            src=self.expressions_dict.get(self.expression, self.expressions_dict["please"]),
            width=self.image_width,
            height=self.image_height
        )

        # クラスのコントロールにキャラクター画像を追加
        self.controls.append(self.character_image)

    def change_expression(self, new_expression):
        """キャラクターの表情を変更するメソッド"""
        if new_expression in self.expressions_dict:
            self.expression = new_expression
            self.character_image.src = self.expressions_dict[self.expression]
            self.update()  # 画像を更新
        else:
            print(f"Error: {new_expression} is not a valid expression.")

    def set_image_size(self, width, height):
        """画像サイズを変更するメソッド"""
        self.image_width = width
        self.image_height = height
        self.character_image.width = width
        self.character_image.height = height
        self.update()

    def set_message_handler(self, handler):
        """メッセージ表示用のUIパーツを設定するメソッド"""
        self.message_handler = handler

    def say(self, message):
        """メッセージを表示するメソッド"""
        if self.message_handler:
            # カスタムメッセージパーツにメッセージを表示
            self.message_handler.value = message
            self.message_handler.update()
        else:
            # メッセージパーツが設定されていない場合のエラーメッセージ
            print("Error: No message handler is set. Use set_message_handler() to set one.")
