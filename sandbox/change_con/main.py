import flet as ft
from interfaces import InterfaceA, InterfaceB, InterfaceC

def main(page: ft.Page):
    # インターフェースインスタンスの作成
    interfaces = {
        "A": InterfaceA(),
        "B": InterfaceB(),
        "C": InterfaceC(),
    }

    # 初期インターフェースをAに設定
    current_interface = interfaces["A"]
    container = current_interface.get_container()

    def switch_interface(e):
        # 押されたボタンのテキストに応じてインターフェースを切り替え
        selected_interface = interfaces[e.control.text]
        page.controls.remove(container)  # 現在のコンテナを削除
        new_container = selected_interface.get_container()  # 新しいコンテナを取得
        page.controls.insert(0, new_container)  # 新しいコンテナを追加
        page.update()  # ページ更新

    # ボタンを作成し、クリックでインターフェースを切り替え
    button_a = ft.ElevatedButton("A", on_click=switch_interface)
    button_b = ft.ElevatedButton("B", on_click=switch_interface)
    button_c = ft.ElevatedButton("C", on_click=switch_interface)

    # ページにコンテナとボタンを追加
    page.add(container, button_a, button_b, button_c)

ft.app(target=main)
