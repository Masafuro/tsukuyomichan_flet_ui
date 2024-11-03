# core.py
import flet as ft

# ヘッダーのクラス
class Header(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container = ft.Container(
            width=800,
            height=80,
            bgcolor=ft.colors.BLUE_200,
            content=ft.Text("Header", size=20, color=ft.colors.WHITE)
        )

    def build(self):
        return self.container

    def update_content(self, new_text):
        self.container.content = ft.Text(new_text, size=20, color=ft.colors.WHITE)
        self.update()

# 左上コンテンツのクラス
class LeftUpperContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container = ft.Container(
            width=465,
            height=200,
            bgcolor=ft.colors.GREEN_400,
            content=ft.Text("Left Upper Content", size=20, color=ft.colors.WHITE)
        )

    def build(self):
        return self.container

    def update_content(self, new_text):
        self.container.content = ft.Text(new_text, size=20, color=ft.colors.WHITE)
        self.update()

# 左下コンテンツのクラス
class LeftLowerContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container = ft.Container(
            width=465,
            height=200,
            bgcolor=ft.colors.GREEN_200,
            content=ft.Text("Left Lower Content", size=20, color=ft.colors.WHITE)
        )

    def build(self):
        return self.container

    def update_content(self, new_text):
        self.container.content = ft.Text(new_text, size=20, color=ft.colors.WHITE)
        self.update()

# 左コンテンツのクラス
class LeftContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.left_upper = LeftUpperContent()
        self.left_lower = LeftLowerContent()

    def build(self):
        return ft.Column(
            controls=[
                self.left_upper,
                self.left_lower,
            ],
            width=465,
            height=400,
            spacing=0  # 要素間の隙間をなくす
        )

    def update_upper_content(self, new_text):
        self.left_upper.update_content(new_text)

    def update_lower_content(self, new_text):
        self.left_lower.update_content(new_text)

# 右コンテンツのクラス
class RightContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container = ft.Container(
            width=300,
            height=400,
            bgcolor=ft.colors.YELLOW_200,
            content=ft.Text("Right Content", size=20, color=ft.colors.BLACK)
        )

    def build(self):
        return self.container

    def update_content(self, new_text):
        self.container.content = ft.Text(new_text, size=20, color=ft.colors.BLACK)
        self.update()

# メイン領域のクラス
class MainContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.left_content = LeftContent()
        self.right_content = RightContent()

    def build(self):
        return ft.Row(
            controls=[
                self.left_content,
                self.right_content,
            ],
            width=800,
            height=400,
            spacing=0  # 要素間の隙間をなくす
        )

    def update_left_upper_content(self, new_text):
        self.left_content.update_upper_content(new_text)

    def update_left_lower_content(self, new_text):
        self.left_content.update_lower_content(new_text)

    def update_right_content(self, new_text):
        self.right_content.update_content(new_text)

# フッターのクラス
class Footer(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container = ft.Container(
            width=800,
            height=80,
            bgcolor=ft.colors.RED_200,
            content=ft.Text("Footer", size=20, color=ft.colors.WHITE)
        )

    def build(self):
        return self.container

    def update_content(self, new_text):
        self.container.content = ft.Text(new_text, size=20, color=ft.colors.WHITE)
        self.update()

# メインアプリケーションクラス
class MyApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.header = Header()
        self.main_content = MainContent()
        self.footer = Footer()

    def build(self):
        return ft.Column(
            controls=[
                self.header,
                self.main_content,
                self.footer,
            ],
            width=800,
            height=600,
            alignment=ft.MainAxisAlignment.START,
            spacing=0  # 要素間の隙間をなくす
        )

    # 各セクションの内容を変更するメソッド
    def update_header(self, new_text):
        self.header.update_content(new_text)

    def update_left_upper_content(self, new_text):
        self.main_content.update_left_upper_content(new_text)

    def update_left_lower_content(self, new_text):
        self.main_content.update_left_lower_content(new_text)

    def update_right_content(self, new_text):
        self.main_content.update_right_content(new_text)

    def update_footer(self, new_text):
        self.footer.update_content(new_text)
