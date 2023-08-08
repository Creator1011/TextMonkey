import subprocess
import argparse


def generate_markov_dict(order):
    subprocess.run(["python", "generate_markov_dict.py", "-o", str(order)])


def generate_text(order, length):
    subprocess.run(["python", "generate_text.py", "-o", str(order), "-l", str(length)])


# 创建命令行解析器
parser = argparse.ArgumentParser(description="Generate English Text")

# 添加子命令
subparsers = parser.add_subparsers(dest="command")

# 创建生成马尔科夫链字典的子命令解析器
dict_parser = subparsers.add_parser("dict")
dict_parser.add_argument("-o", "--order", type=int, help="Order of Markov chain", required=True)

# 创建生成文本的子命令解析器
text_parser = subparsers.add_parser("text")
text_parser.add_argument("-o", "--order", type=int, help="Order of Markov chain", required=True)
text_parser.add_argument("-l", "--length", type=int, help="Length of generated text")

# 解析命令行参数
args = parser.parse_args()

if args.command == "dict":
    generate_markov_dict(args.order)
elif args.command == "text":
    if args.length:
        generate_text(args.order, args.length)
    else:
        print("Please provide the length of generated text")
else:
    print("Please enter a valid command")
