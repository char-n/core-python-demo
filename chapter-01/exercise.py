# encoding: utf-8

import re


# 封装输出方法
def my_print(re_obj):
    if re_obj is not None:
        print(re_obj.group())
    else:
        print("not match")


# 1.识别后续的字符串：“bat”、“bit”、“but”、“hat”、“hit”或者“hut”。

pattern = '[bh][aiu]t'

re_match = re.match(pattern, 'bit')
my_print(re_match)

# 2.匹配由单个空格分隔的任意单词对，也就是姓和名。

pattern = '[A-Z][a-z]+\s[A-Z][a-z]+'
data = "Mark Zuckerberg"
re_match = re.match(pattern, data)
my_print(re_match)

# 3.匹配由单个逗号和单个空白符分隔的任何单词和单个字母，如姓氏的首字母。
pattern = '[a-zA-Z]+,\s[a-zA-Z]'
data = 'word, Idd'
re_match = re.match(pattern, data)
my_print(re_match)

# 4.匹配所有有效 Python 标识符的集合
# 所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。
pattern = '[a-zA-Z_]\w*'
data = '__init__'
re_search = re.search(pattern, data)
my_print(re_search)

'''
5. 根据读者当地的格式，匹配街道地址（使你的正则表达式足够通用，来匹配任意数
量的街道单词，包括类型名称）。例如，美国街道地址使用如下格式：1180 Bordeaux
Drive。使你的正则表达式足够灵活，以支持多单词的街道名称，如 3120 De La Cruz
Boulevard。
'''

pattern = '\d{4}\s([A-Z][a-z]+\s)+[A-Z][a-z]+'
data = '3120 De La Cruz Boulevard'
re_search = re.search(pattern, data)
my_print(re_search)

'''
6. 匹配以“www”起始且以“.com”结尾的简单Web 域名；例如，www://www. yahoo.com/。
选做题：你的正则表达式也可以支持其他高级域名，如.edu、.net 等（例如，
http://www.foothill.edu）。
'''
pattern = 'https*://www\.\w+\.(edu|com|org|net)'
data = 'http://www.github.net'
re_search = re.search(pattern, data)
my_print(re_search)

# 7.匹配所有能够表示 Python 整数的字符串集
pattern = '-*\d+'
data = '-15dfd2'   # 打印出来是-15 ,匹配到了前面的数字.
re_search = re.search(pattern, data)
my_print(re_search)

findall = re.findall(pattern, data)
print(findall)
for find in findall:
    print(find)

