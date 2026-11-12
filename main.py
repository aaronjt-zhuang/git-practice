"""一个只有命令行的小待办程序，用来练 Git 协作。

用法：
    python main.py                    列出全部
    python main.py add "交实验报告"    添加一项
    python main.py list               列出全部
    python main.py done 1             把第 1 项标记为完成
"""

import json
import sys
from pathlib import Path

DATA = Path(__file__).with_name("todos.json")


def load():
    if not DATA.exists():
        return []
    return json.loads(DATA.read_text(encoding="utf-8"))


def save(items):
    DATA.write_text(
        json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def cmd_add(text):
    items = load()
    items.append({"text": text, "done": False})
    save(items)
    print(f"已添加: {text}")


def cmd_list():
    items = load()
    if not items:
        print("(空空如也，用 add 加一条)")
        return
    for i, item in enumerate(items, 1):
        mark = "x" if item["done"] else " "
        print(f"{i}. [{mark}] {item['text']}")


def cmd_done(index):
    items = load()
    if not 1 <= index <= len(items):
        print(f"没有第 {index} 项")
        return
    items[index - 1]["done"] = True
    save(items)
    print(f"已完成: {items[index - 1]['text']}")


def main(argv):
    if not argv:
        cmd_list()
        return

    action, rest = argv[0], argv[1:]

    if action == "add" and rest:
        cmd_add(" ".join(rest))
    elif action == "list":
        cmd_list()
    elif action == "done" and rest:
        try:
            cmd_done(int(rest[0]))
        except ValueError:
            print("done 后面要跟一个数字")
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
