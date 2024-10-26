import os
from flet import UserControl, Image, Column

class TsukuyomiUI(UserControl):
    def __init__(self, initial_expression="normal", image_width=50, image_height=50):
        super().__init__()

        self.images_dir = os.path.join(os.path.dirname(__file__), "images/tsukuyomichan")
        self.expression = initial_expression
        self.image_width = image_width
        self.image_height = image_height

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

        self.character_image = Image(
            src=self.expressions_dict.get(self.expression, self.expressions_dict["please"]),
            width=self.image_width,
            height=self.image_height
        )

    def build(self):
        return Column(
            [self.character_image],
            width=self.image_width,
            height=self.image_height
        )

    def change_expression(self, new_expression):
        if new_expression in self.expressions_dict:
            self.expression = new_expression
            self.character_image.src = self.expressions_dict[self.expression]
            self.character_image.update()
        else:
            print(f"Error: {new_expression} is not a valid expression.")

    def set_image_size(self, width, height):
        self.image_width = width
        self.image_height = height
        self.character_image.width = width
        self.character_image.height = height
        self.character_image.update()

    def set_message_handler(self, handler):
        if hasattr(handler, "value"):
            self.message_handler = handler
        else:
            print("Error: Invalid message handler provided.")

    def say(self, message):
        if self.message_handler:
            self.message_handler.value = message
            self.message_handler.update()
        else:
            print("Error: No message handler is set. Use set_message_handler() to set one.")