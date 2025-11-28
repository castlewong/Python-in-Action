import re
import os


def remove_bracket_pairs_sequential(content):
    """
    按顺序一组一组删除[和)之间的内容

    参数:
        content: 文本内容

    返回:
        处理后的文本内容和被删除的内容列表
    """
    result = []
    remaining = content
    changes = []

    while True:
        # 找到第一个 [
        start_idx = remaining.find('[')
        if start_idx == -1:
            # 没有找到更多的 [，添加剩余内容
            result.append(remaining)
            break

        # 找到第一个 [ 之后的第一个 )
        end_idx = remaining.find(')', start_idx)
        if end_idx == -1:
            # 没有找到对应的 )，添加剩余内容
            result.append(remaining)
            break

        # 添加 [ 之前的内容
        result.append(remaining[:start_idx])

        # 记录被删除的内容
        deleted_content = remaining[start_idx:end_idx + 1]
        changes.append(deleted_content)

        # 更新剩余内容（跳过已删除的部分）
        remaining = remaining[end_idx + 1:]

    return ''.join(result), changes


def process_markdown_file(file_path, create_backup=True):
    """
    处理Markdown文件，按顺序删除[和)之间的内容

    参数:
        file_path: 文件路径
        create_backup: 是否创建备份
    """
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 创建备份
        if create_backup:
            backup_path = file_path + '.bak'
            with open(backup_path, 'w', encoding='utf-8') as backup_file:
                backup_file.write(content)
            print(f"备份已创建: {backup_path}")

        # 处理内容
        processed_content, changes = remove_bracket_pairs_sequential(content)

        # 写入处理后的内容
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(processed_content)

        # 输出处理信息
        print(f"成功处理文件: {file_path}")
        print(f"共删除 {len(changes)} 组内容:")
        for i, change in enumerate(changes, 1):
            print(f"  第{i}组: {change}")

        return len(changes)

    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 不存在")
        return 0
    except Exception as e:
        print(f"处理文件时出错: {e}")
        return 0


def preview_changes(file_path):
    """
    预览将要进行的更改
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        processed_content, changes = remove_bracket_pairs_sequential(content)

        if changes:
            print(f"在文件 {file_path} 中找到 {len(changes)} 组内容将被删除:")
            for i, change in enumerate(changes, 1):
                print(f"{i}. {change}")

            print("\n处理后预览:")
            print("-" * 50)
            print(processed_content[:500] + "..." if len(processed_content) > 500 else processed_content)
            print("-" * 50)
        else:
            print(f"在文件 {file_path} 中未找到匹配的内容")

    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 不存在")


# 在这里填写你的文件路径
FILE_PATH = "/zh.md"  # 请将这里替换为你的实际文件路径

# 主程序
if __name__ == "__main__":
    # 检查文件是否存在
    if not os.path.exists(FILE_PATH):
        print(f"错误: 文件 {FILE_PATH} 不存在")
        print("请检查 FILE_PATH 变量是否正确设置")
        exit(1)

    # 询问用户想要执行的操作
    print(f"要处理的文件: {FILE_PATH}")
    print("请选择操作:")
    print("1. 预览更改 (不修改文件)")
    print("2. 执行处理 (会创建备份)")
    print("3. 执行处理 (不创建备份)")

    choice = input("请输入选择 (1/2/3): ").strip()

    if choice == "1":
        preview_changes(FILE_PATH)
    elif choice == "2":
        process_markdown_file(FILE_PATH, create_backup=True)
    elif choice == "3":
        process_markdown_file(FILE_PATH, create_backup=False)
    else:
        print("无效的选择")