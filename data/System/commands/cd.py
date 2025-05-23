def run(args, current_dir, resolve_path):
    if len(args) != 1:
        print("使い方: cd <ディレクトリ>")
        return current_dir

    new_path = args[0]
    if not new_path.startswith('/'):
        # 相対パス扱いにするならここで実装可能（省略）
        new_path = current_dir.rstrip('/') + '/' + new_path

    full_path = resolve_path(new_path)
    if full_path is None or not os.path.isdir(full_path):
        print(f"ディレクトリが存在しません: {new_path}")
        return current_dir

    return new_path.rstrip('/')