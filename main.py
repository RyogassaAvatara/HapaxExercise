import re


def hapax():
    f = open('dotd.txt', 'r', encoding='utf8')
    word_list = re.findall('\w+', f.read().lower())
    dict = {}

    for word in word_list:
        if word not in dict:
            dict[word] = 1
        elif word in dict:
            dict[word] += 1

    for word in dict:
        if dict[word] == 1:

            print(word)


if __name__ == "__main__":

    hapax()
