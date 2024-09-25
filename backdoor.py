import os
# ユーザーからコマンドを受け取る
user_input = input("Enter a command: ")
# ユーザーの入力をそのままOSコマンドとして実行（危険）
os.system(user_input)
