import flet as ft
import subprocess

def main(page: ft.Page):
    page.title = "Flet Console Application"
    page.scroll = "always"  # 縦方向にスクロール可能に設定

    # コンソール出力を表示するリストビュー
    console_output = ft.ListView(height=400, spacing=5, auto_scroll=True)

    # 入力フィールド
    input_field = ft.TextField(
        label="Enter command",
        autofocus=True,
        on_submit=lambda e: execute_command(e.control.value),
    )

    # コンソール出力を追加するためのコンテナ
    page.controls.append(console_output)
    page.controls.append(input_field)

    # コマンド実行関数
    def execute_command(command):
        if command.strip().lower() == "exit":
            page.window_close()  # 「exit」と入力でアプリケーションを終了

        else:
            try:
                # コマンドを実行し、結果を取得
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                # 標準出力とエラー出力を結合して表示
                output = result.stdout + result.stderr
            except Exception as e:
                output = f"Error: {str(e)}"

            # コマンドと出力をリストビューに追加
            console_output.controls.append(ft.Text(f"> {command}"))
            console_output.controls.append(ft.Text(output))

            # 20行を超えたら古い行を削除
            if len(console_output.controls) > 40:  # コマンドとその出力で2行なので40
                console_output.controls = console_output.controls[2:]

            page.update()
        
        # コマンド実行後、入力フィールドをクリア
        input_field.value = ""
        page.update()

    page.update()

# Fletアプリを起動
ft.app(target=main)
