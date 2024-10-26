import flet as ft
import os

class CustomContainer(ft.UserControl):
    def __init__(self):
        super().__init__()

        # メッセージ部の背景画像 (fukidashi1.png)
        self.message_image = ft.Image(
            src=os.path.join(os.path.dirname(__file__), "fukidashi1.png"),
            width=500,
            height=300,
            fit=ft.ImageFit.COVER
        )

        # メッセージテキスト
        self.message_text = ft.Text(
            "メッセージテキスト",
            color=ft.colors.BLACK,
            size=20
        )

        # メッセージテキストのコンテナ (指定されたサイズと位置)
        self.text_container = ft.Container(
            content=self.message_text,
            width=380,
            height=200,
            bgcolor=ft.colors.PINK_100,
            border_radius=10,
            padding=10
        )

        # メッセージ部で画像とテキストを重ねる
        self.message_area = ft.Stack(
            [
                self.message_image,
                ft.Container(
                    content=self.text_container,
                    top=40,
                    left=50
                )
            ],
            width=500,
            height=300
        )

        # UI部 (下側, 高さ300)
        self.ui_area = ft.Container(
            bgcolor=ft.colors.YELLOW,
            width=500,
            height=300,
            content=ft.Text("UI部", color=ft.colors.BLACK),
            alignment=ft.alignment.center,
            padding=0
        )

        # インターフェース部 (左側, 幅500)
        self.interface_area = ft.Column(
            [
                self.message_area,
                self.ui_area
            ],
            spacing=0,
            width=500,
            height=600
        )

        # キャラクター部 (右側, 幅300)
        self.character_area = ft.Container(
            bgcolor=ft.colors.LIGHT_BLUE,
            width=300,
            height=600,
            content=ft.Text("キャラクター部", color=ft.colors.BLACK),
            alignment=ft.alignment.center,
            padding=0
        )

    def build(self):
        return ft.Row(
            [
                self.interface_area,
                self.character_area
            ],
            spacing=0,
            width=800,
            height=600
        )

    def update_message_text(self, new_text):
        """メッセージテキストを更新するメソッド"""
        self.message_text.value = new_text
        self.message_text.update()  # 画面に変更を反映
