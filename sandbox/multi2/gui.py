import flet as ft
import multiprocessing
import subprocess
import queue
import asyncio

# メイン関数
def main(page: ft.Page):
    page.title = "GUI Application"
    
    # Queueを作成
    gui_to_system_queue = multiprocessing.Queue()
    system_to_gui_queue = multiprocessing.Queue()
    
    # Text表示部分とボタンを設置
    display_text = ft.Text(value="Waiting for response...")
    send_button = ft.ElevatedButton(text="Send to system.py", on_click=lambda e: send_message())

    page.controls.append(display_text)
    page.controls.append(send_button)
    
    # system.pyをサブプロセスとして起動
    system_process = subprocess.Popen(
        ["python", "system.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # メッセージ送信関数
    def send_message():
        gui_to_system_queue.put("clicked")
    
    # メッセージ受信チェック関数（非同期で実行）
    async def check_response():
        while True:
            message = None
            try:
                # system_to_gui_queueからメッセージを受信
                message = system_to_gui_queue.get_nowait()
                display_text.value = message
                page.update()
            except queue.Empty:
                pass
            
            # メッセージが"close"ならsystem.pyを終了
            if message == "close":
                system_process.terminate()
                page.close()
                break

            # 0.1秒待機して再度チェック
            await asyncio.sleep(0.1)

    # 非同期タスクとしてcheck_responseを開始
    asyncio.ensure_future(check_response())
    page.update()

ft.app(target=main)
