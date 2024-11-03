import flet as ft
from multiprocessing import Process, Event
import time
import sys
import os

# サブプロセスで実行するバックグラウンドタスク
def background_task(stop_event):
    while not stop_event.is_set():  # 定期的に終了フラグを確認
        print("Background task running...")
        time.sleep(1)  # 1秒間スリープ（割り込みを受けるため）
    print("Background task stopping...")

def main(page: ft.Page):
    # サブプロセスを制御するためのイベント
    stop_event = Event()
    # サブプロセスを作成して開始
    process = Process(target=background_task, args=(stop_event,))
    process.start()

    # ウィンドウが閉じられたときに実行される関数
    def on_window_close(e):
        print("Window is closing...")
        stop_event.set()           # サブプロセスに終了シグナルを送信
        process.join(timeout=1)     # サブプロセスが1秒以内に終了するのを待機
        if process.is_alive():
            process.terminate()     # サブプロセスがまだ動いている場合、強制終了
        process.join()              # 強制終了が完了するのを待機
        os._exit(0)                 # プロセスを強制終了

    # ウィンドウが閉じられたときに on_window_close を呼び出す
    page.on_window_close = on_window_close

    # GUI要素のセットアップ
    input_field = ft.TextField(label="Enter your name")
    output_text = ft.Text(value="")

    # ボタンのクリックイベント
    def on_button_click(e):
        output_text.value = f"Hello, {input_field.value}!"
        page.update()  # ページを更新して変更を反映

    # ボタンを作成
    button = ft.ElevatedButton(text="Say Hello", on_click=on_button_click)

    # ページに要素を追加
    page.add(input_field, button, output_text)

if __name__ == '__main__':
    ft.app(target=main)
