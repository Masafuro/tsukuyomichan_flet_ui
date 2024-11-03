import multiprocessing
import queue
import time
import sys

def system_process(gui_to_system_queue, system_to_gui_queue):
    while True:
        try:
            # GUIからのメッセージを取得
            message = gui_to_system_queue.get_nowait()
            if message == "clicked":
                # メッセージを返す
                system_to_gui_queue.put("Message received!")
            elif message == "close":
                system_to_gui_queue.put("close")
                break
        except queue.Empty:
            pass

        time.sleep(0.1)

if __name__ == "__main__":
    # Queueの作成
    gui_to_system_queue = multiprocessing.Queue()
    system_to_gui_queue = multiprocessing.Queue()
    
    # プロセスの起動
    system_process(gui_to_system_queue, system_to_gui_queue)
