import flet as ft

def print_to_console(text):
    """指定されたテキストをコンソールに表示する関数"""
    print(text)

def main(page: ft.Page):
    page.title = "FletFlow Pi Calculator"

    # UI要素の定義
    precision_input = ft.TextField(label="Precision Level (Digits)", width=200)
    progress_bar = ft.ProgressBar(width=300, value=0)
    message_label = ft.Text(value="Enter a precision level and click 'Calculate' to approximate π.")

    # 計算開始ボタンの処理
    def start_calculation(e):
        # precision_inputの内容を取得し、データテーブル形式に整形
        precision = precision_input.value
        data_table = {
            "type": "request",
            "command": "calculate",
            "status": "initial",
            "data": {"precision": precision},
            "details": "Starting π calculation"
        }
        print_to_console((data_table,))  # タプル形式で出力
        message_label.value = f"Calculating π to {precision} decimal places... (Backend not implemented)"
        progress_bar.value = 0
        page.update()

    # 停止ボタンの処理（仮の関数）
    def stop_calculation(e):
        message_label.value = "Calculation stopped. (Backend not implemented)"
        progress_bar.value = 0
        page.update()

    # リセットボタンの処理
    def reset(e):
        precision_input.value = ""
        progress_bar.value = 0
        message_label.value = "Enter a precision level and click 'Calculate' to approximate π."
        page.update()

    # ボタンの定義
    calculate_button = ft.ElevatedButton(text="Calculate", on_click=start_calculation)
    stop_button = ft.ElevatedButton(text="Stop", on_click=stop_calculation)
    reset_button = ft.ElevatedButton(text="Reset", on_click=reset)

    # レイアウト
    page.add(
        ft.Column([
            ft.Text("FletFlow Pi Calculator", style="headlineMedium"),
            message_label,
            precision_input,
            ft.Row([calculate_button, stop_button, reset_button]),
            progress_bar
        ])
    )

# Fletアプリケーションの実行
if __name__ == "__main__":
    ft.app(target=main)
