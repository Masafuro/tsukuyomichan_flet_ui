# system.py
from multiprocessing import Queue, Event
import time

def run_system(to_gui_queue, from_gui_queue, stop_event):
    while not stop_event.is_set():
        # main.py（GUI）からのデータをチェック
        if not from_gui_queue.empty():
            input_text = from_gui_queue.get()  # main.pyからのメッセージを取得
            print(f"Received from main.py: {input_text}")  # コンソールに表示

            # 受け取った内容をそのまま to_gui_queue に返す
            to_gui_queue.put(f"Echo from system.py: {input_text}")

        # 少し待機してから次のループへ
        time.sleep(0.5)  # 0.5秒に短縮
