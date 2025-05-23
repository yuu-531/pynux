import os

def run(args, current_dir, resolve_path):
    if len(args) != 1:
        print("使い方: cat <ファイル>")
        return

    file_path = args[0]
    if not file_path.startswith('/'):
        file_path = current_dir.rstrip('/') + '/' + file_path

    full_path = resolve_path(file_path)
    if full_path is None or not os.path.isfile(full_path):
        print(f"ファイルがありません: {file_path}")
        return

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print(f"ファイル読み込みエラー: {e}")