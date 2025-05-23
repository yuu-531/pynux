import os
import sys

DATA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

def resolve_path(virtual_path):
    if not virtual_path.startswith('/'):
        print("パスは必ず / で始めてね！")
        return None
    full_path = os.path.abspath(os.path.join(DATA_ROOT, virtual_path.lstrip('/')))
    if not full_path.startswith(DATA_ROOT):
        print("dataフォルダの外にはアクセスできないよ！")
        return None
    return full_path

def load_commands():
    commands_dir = resolve_path('/system/Commands')
    commands = {}
    if not commands_dir:
        return commands

    for fname in os.listdir(commands_dir):
        if fname.endswith('.py'):
            cmd_name = fname[:-3]
            path = os.path.join(commands_dir, fname)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    code = compile(f.read(), fname, 'exec')
                    cmd_globals = {}
                    exec(code, cmd_globals)
                    if 'run' in cmd_globals:
                        commands[cmd_name] = cmd_globals['run']
            except Exception as e:
                print(f"コマンド{cmd_name}の読み込みエラー: {e}")
    return commands

def main():
    print("Welcome to Pynux!")
    commands = load_commands()
    current_dir = '/user'

    while True:
        try:
            inp = input(f"Pynux:{current_dir}$ ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n終了します。")
            break

        if inp == '':
            continue
        if inp == 'exit':
            print("Bye!")
            break

        parts = inp.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd in commands:
            try:
                result = commands[cmd](args, current_dir, resolve_path)
                if isinstance(result, str):
                    current_dir = result  # cdコマンド用
            except Exception as e:
                print(f"コマンド実行中にエラー: {e}")
        else:
            print(f"コマンド '{cmd}' は見つかりません。")

if __name__ == '__main__':
    main()