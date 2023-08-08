import pickle
import argparse
import os


def generate_markov_chain(corpus, order=2):
    markov_dict = {}

    # 遍历语料库，建立马尔科夫链模型
    for sentence in corpus:
        words = sentence.split()
        for i in range(len(words) - order):
            key = tuple(words[i:i + order])
            value = words[i + order]

            if key in markov_dict:
                markov_dict[key].append(value)
            else:
                markov_dict[key] = [value]

    return markov_dict


# 读取多个文件
file_paths = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        temp = file.split(".")
        if temp[len(temp) - 1] == "txt":
            file_paths.append(os.path.join(root, file))
corpus = []

for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            sentences = line.split(".")
            corpus.extend(sentences)

# 创建命令行解析器
parser = argparse.ArgumentParser(description="Generate Markov chain dict")
# 添加参数
parser.add_argument("-o", "--order", type=int, help="Order of Markov chain", default=2)

# 解析命令行参数
args = parser.parse_args()
order = args.order

markov_dict = generate_markov_chain(corpus, order=order)

# 将字典保存为文件
with open("markov_dict.pickle", "wb") as file:
    pickle.dump(markov_dict, file)
