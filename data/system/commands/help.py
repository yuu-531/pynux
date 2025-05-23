import os

def run(args, system_path, user_path):
    help_file = os.path.join(system_path, "help.txt")
    commands_dir = os.path.join(system_path, "commands")

    # commandsフォルダ内の.pyファイルを取得
    try:
        all_commands = [f[:-3] for f in os.listdir(commands_dir) if f.endswith(".py")]
    except FileNotFoundError:
        print("コマンドフォルダが見つかりません。")
        return

    # help.txtの読み込み
    descriptions = {}
    if os.path.isfile(help_file):
        with open(help_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    cmd, desc = parts
                    descriptions[cmd] = desc

    # 各コマンドに対して表示
    for cmd in sorted(all_commands):
        desc = descriptions.get(cmd, "情報なし")
        print(f"{cmd} - {desc}")