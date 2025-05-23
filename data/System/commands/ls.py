import os

def run(args, current_dir, resolve_path):
    target = args[0] if args else current_dir
    full_path = resolve_path(target)
    if full_path is None or not os.path.isdir(full_path):
        print(f"ディレクトリが存在しません: {target}")
        return

    for f in os.listdir(full_path):
        print(f)