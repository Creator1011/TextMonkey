import random
import pickle
import argparse
import os


def generate_text(markov_dict, order=2, length=50):
    current_state = random.choice(list(markov_dict.keys()))
    generated_text = list(current_state)

    while len(generated_text) < length:
        if current_state in markov_dict:
            next_word = random.choice(markov_dict[current_state])
            generated_text.append(next_word)
            current_state = tuple(generated_text[-order:])

            if next_word.endswith('.') or next_word.endswith('!') or next_word.endswith('?'):
                break
        else:
            current_state = random.choice(list(markov_dict.keys()))

    generated_text = ' '.join(generated_text)
    if len(generated_text.split(".")) <= 1:
        return generated_text + "."
    return generated_text


# 从文件中加载字典
with open("markov_dict.pickle", "rb") as file:
    loaded_dict = pickle.load(file)

parser = argparse.ArgumentParser(description="Generate English Text")

# 添加参数
parser.add_argument("-o", "--order", type=str, help="Order of Markov chain", default=2)
parser.add_argument("-l", "--length", type=str, help="length of generated text", default=50)

# 解析命令行参数
args = parser.parse_args()

order = int(args.order)
length = int(args.length)

generated_text = generate_text(loaded_dict, order=order, length=length)
print(generated_text)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(generated_text)

os.system("pause")
