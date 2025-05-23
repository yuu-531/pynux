import os

# === 絶対パスで安全にアクセス ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))           # pynux/
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))        # 親フォルダ
DATA_DIR = os.path.join(ROOT_DIR, "data")                       # data/
SYSTEM_DIR = os.path.join(DATA_DIR, "system")                   # data/system/
COMMANDS_DIR = os.path.join(SYSTEM_DIR, "commands")             # data/system/Commands/
USER_DIR = os.path.join(DATA_DIR, "user")                       # data/user/

def init_directories():
    os.makedirs(COMMANDS_DIR, exist_ok=True)
    os.makedirs(USER_DIR, exist_ok=True)

def load_commands():
    commands = {}
    if not os.path.exists(COMMANDS_DIR):
        print(f"[ERROR] コマンドディレクトリが存在しません: {COMMANDS_DIR}")
        return commands

    for fname in os.listdir(COMMANDS_DIR):
        if fname.endswith(".py"):
            cmd_name = fname[:-3]
            with open(os.path.join(COMMANDS_DIR, fname), "r", encoding="utf-8") as f:
                commands[cmd_name] = f.read()
    return commands

def execute_command(commands, name, args):
    if name not in commands:
        print(f"[!] コマンド '{name}' は見つかりません")
        return

    scope = {
        "__name__": "__main__",
        "__args__": args,
        "USER_DIR": USER_DIR,
        "commands": commands
    }

    try:
        exec(commands[name], scope)
        if "run" in scope and callable(scope["run"]):
            scope["run"](args, commands, USER_DIR)
    except Exception as e:
        print(f"[ERROR] コマンド '{name}' 実行中にエラー: {e}")

def main():
    init_directories()
    commands = load_commands()

    print("=== Pynux Terminal ===")
    print("終了するには 'exit' を入力")

    while True:
        try:
            cmd = input("pynux$ ").strip()
            if cmd == "":
                continue
            if cmd.lower() in ["exit", "quit"]:
                print("Pynux を終了します")
                break

            parts = cmd.split()
            cmd_name = parts[0]
            cmd_args = parts[1:]
            execute_command(commands, cmd_name, cmd_args)

        except KeyboardInterrupt:
            print("\n[!] 強制終了 (Ctrl+C)")
        except Exception as e:
            print(f"[ERROR] メインループ中にエラー: {e}")

if __name__ == "__main__":
    main()