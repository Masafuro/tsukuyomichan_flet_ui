import flet as ft

class CustomContainer(ft.UserControl):
    def __init__(self):
        super().__init__()

        # メッセージ部 (上側, 高さ300)
        self.message_area = ft.Container(
            bgcolor=ft.colors.LIGHT_GREEN,
            width=500,
            height=300,
            content=ft.Text("メッセージ部", color=ft.colors.BLACK),
            alignment=ft.alignment.center,
            padding=0
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

# main.pyでの使用
def main(page: ft.Page):
    # ウィンドウサイズと位置を設定
    page.window.width = 835
    page.window.height = 660
    page.window_resizable = False  # ウィンドウをリサイズ不可にする
    page.window_top = 0  # ウィンドウの上側を0に設定
    page.window_left = 0  # ウィンドウの左側を0に設定

    # カスタムコンテナのインスタンスを作成
    custom_container = CustomContainer()

    # ページにカスタムコンテナを追加
    page.add(custom_container)

ft.app(target=main)
