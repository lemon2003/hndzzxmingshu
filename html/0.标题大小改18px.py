import os
import re


def modify_html_font_size(file_path):
    """修改HTML文件中.nav-menu li a标签的字体大小"""
    try:
        # 尝试多种编码打开文件
        encodings = ['utf-8', 'gbk', 'latin-1']
        content = None

        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue

        if content is None:
            print(f"⚠️ 无法解码文件: {file_path}")
            return False

        # 查找<head>到</head>部分
        head_pattern = r'<head>(.*?)</head>'
        head_match = re.search(head_pattern, content, re.DOTALL)

        if not head_match:
            print(f"🔍 未找到<head>标签: {file_path}")
            return False

        head_content = head_match.group(1)

        # 检查是否已存在.nav-menu li a样式
        nav_menu_pattern = r'\.nav-menu\s+li\s+a\s*{[^}]*}'
        existing_style = re.search(nav_menu_pattern, head_content, re.DOTALL)

        if existing_style:
            # 修改现有样式
            old_style = existing_style.group(0)

            # 替换或添加font-size属性
            if 'font-size' in old_style:
                new_style = re.sub(r'font-size\s*:\s*[^;]+;', 'font-size: 18px;', old_style)
            else:
                new_style = old_style.rstrip('}') + ' font-size: 18px; }'

            # 更新head内容
            new_head_content = head_content.replace(old_style, new_style)
        else:
            # 添加新样式
            new_style = '<style>.nav-menu li a { font-size: 18px; }</style>'
            new_head_content = head_content + new_style

        # 替换原始head内容
        new_content = content.replace(
            f'<head>{head_content}</head>',
            f'<head>{new_head_content}</head>'
        )

        # 如果内容有变化才写入
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 已更新: {file_path}")
            return True
        else:
            print(f"🔍 无需修改: {file_path}")
            return False

    except Exception as e:
        print(f"❌ 处理文件出错 {file_path}: {str(e)}")
        return False


def main():
    # 获取当前工作目录
    current_dir = os.getcwd()
    print(f"🔍 正在扫描目录: {current_dir}")
    print("-" * 50)

    # 统计变量
    total_files = 0
    modified_files = 0

    # 遍历当前目录所有HTML文件
    for filename in os.listdir(current_dir):
        if not filename.lower().endswith('.html'):
            continue

        file_path = os.path.join(current_dir, filename)

        # 跳过目录
        if os.path.isdir(file_path):
            continue

        total_files += 1
        if modify_html_font_size(file_path):
            modified_files += 1

    # 输出统计结果
    print("-" * 50)
    print(f"📊 扫描完成! 共检查 {total_files} 个HTML文件")
    print(f"✨ 成功修改 {modified_files} 个文件")
    print(f"ℹ️ 未修改 {total_files - modified_files} 个文件")


if __name__ == "__main__":
    main()