import flet as ft

class InterfaceA:
    def __init__(self):
        # InterfaceAで使うコンテナを定義
        self.container = ft.Container(
            content=ft.Text("インターフェース A"),
            width=200,
            height=200,
            bgcolor=ft.colors.LIGHT_BLUE_100,
            alignment=ft.alignment.center
        )

    def get_container(self):
        # Containerを返すメソッド
        return self.container

class InterfaceB:
    def __init__(self):
        # InterfaceBで使うコンテナを定義
        self.container = ft.Container(
            content=ft.Text("インターフェース B"),
            width=200,
            height=200,
            bgcolor=ft.colors.LIGHT_GREEN_100,
            alignment=ft.alignment.center
        )

    def get_container(self):
        return self.container

class InterfaceC:
    def __init__(self):
        # InterfaceCで使うコンテナを定義
        self.container = ft.Container(
            content=ft.Text("インターフェース C"),
            width=200,
            height=200,
            bgcolor=ft.colors.PINK_100,
            alignment=ft.alignment.center
        )

    def get_container(self):
        return self.container
