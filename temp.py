import os

file_path = ".\\images\\fukidashi\\fukidashi1.png"  # パスを適切に変更してください

if os.path.isfile(file_path):
    print("ファイルは存在します。")
else:
    print("ファイルが見つかりません。")
