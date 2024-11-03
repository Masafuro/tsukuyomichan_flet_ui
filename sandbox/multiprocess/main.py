import flet as ft
from multiprocessing import Process, Queue, Event
import system
import time
import threading
import sys
import os

def main(page: ft.Page):
    # system.pyとの通信に使用するキューとイベント
    to_gui_queue = Queue()
    from_gui_queue = Queue()
    stop_event = Event()

    # system.pyを別プロセスで開始
    system_process = Process(target=system.run_system, args=(to_gui_queue, from_gui_queue, stop_event))
    system_process.start()

    # GUI要素のセットアップ
    output_area = ft.TextField(value="", multiline=True, width=400, height=200, read_only=True)
    input_field = ft.TextField(label="Send to system.py", width=300)
    send_button = ft.ElevatedButton(text="Send", on_click=lambda e: send_to_system())

    page.add(output_area, input_field, send_button)

    # system.py にテキストフィールドの内容を送信
    def send_to_system():
        user_input = input_field.value
        from_gui_queue.put(user_input)  # 入力内容をsystem.pyに送信
        input_field.value = ""  # テキストフィールドをクリア
        page.update()

    # system.py からのメッセージをテキストエリアに表示
    def update_output_area():
        while True:
            if not to_gui_queue.empty():
                message = to_gui_queue.get()  # system.pyからのメッセージを取得
                output_area.value += f"{message}\n"  # テキストエリアに追加
                page.update()
            time.sleep(0.5)

    # ウィンドウが閉じられたときにサブプロセスとmain.pyを終了
    def on_window_close(e):
        print("Closing application...")
        stop_event.set()           # サブプロセスに終了シグナルを送信
        system_process.join(timeout=1)  # サブプロセスが1秒以内に終了するのを待機
        if system_process.is_alive():
            system_process.terminate()  # サブプロセスがまだ動いている場合、強制終了
        system_process.join()  # 強制終了が完了するのを待機
        os._exit(0)  # プロセスを強制終了

    # ウィンドウが閉じられたときに on_window_close を呼び出す
    page.on_window_close = on_window_close

    # system.py からのメッセージを更新するスレッドを開始
    threading.Thread(target=update_output_area, daemon=True).start()

if __name__ == '__main__':
    ft.app(target=main)
