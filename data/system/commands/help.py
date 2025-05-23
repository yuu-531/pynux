# help.py

import os

def run(args, commands, USER_DIR):
    print("使用可能なコマンド一覧：")
    for name in sorted(commands.keys()):
        print(f" - {name}")