# -*- coding:utf-8 -*-
import re


def regex_demo():
    regex_str = "hello world"
    pattern = "hello"
    # compile

    re_compile = re.compile(pattern)
    print(re_compile)

    # match 从字符串的其实部分开始匹配

    match = re.match(pattern, regex_str)  # 返回正则表达式对象

    print(match)

    group = match.group()  # 匹配对象，返回整个匹配对象
    print(group)

    # search 只会搜索第一个匹配的
    search = re.search(pattern, "hello world hello")
    if search is not None:
        print("search: " + search.group())

    # 择一匹配
    pattern = "bat|bet|bit"
    re_match = re.match(pattern, "bat")
    if re_match is not None:
        print("择一匹配：" + re_match.group())

    re_search = re.search(pattern, "i bat it")
    if re_search is not None:
        print("择一匹配search: " + re_search.group())

    # 匹配单个字符
    pattern = ".end"
    re_match = re.match(pattern, "bend")
    if re_match is not None:
        print("匹配单个字符：" + re_match.group())

    # 创建子字符集([])
    pattern = "[cr][23][dp][o2]"
    re_match = re.match(pattern, "c3p2")
    if re_match is not None:
        print(re_match.group())

    # 重复、特殊字符和分组
    pattern = "\w+@(\w+\.)?\w+\.com"
    # 不能匹配
    re_match = re.match(pattern, "123@xxx.yyy.zzz.com")
    if re_match is not None:
        print(re_match.group())

    # 可以匹配
    re_match = re.match(pattern, "123@xxx.yyy.com")
    if re_match is not None:
        print(re_match.group())

    # 匹配多个子域名
    pattern = "\w+@(\w+\.)*\w+\.com"
    re_match = re.match(pattern, "123@qq.www.xxx.yyy.com")
    if re_match is not None:
        print(re_match.group())

    # 是否可以这样写(这样也可以)
    pattern = "\w+@(\w+\.)+com"
    re_match = re.match(pattern, "111@qq.www.sss.ddd.com")
    if re_match is not None:
        print(re_match.group())

    # group 和 groups
    pattern = "(\w\w\w)-(\d\d\d)"
    re_match = re.match(pattern, "abc-123")
    if re_match is not None:
        print(re_match.group())
        print(re_match.group(1))
        print(re_match.group(2))
        print(re_match.groups())

    # findall
    s = "This and that."
    findall = re.findall(r'(th\w+) and (th\w+)', s, re.I)
    print(findall)

    # finditer (AttributeError: 'callable_iterator' object has no attribute 'next')
    finditer = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
    print(type(finditer))
    # finditer.next()
    # finditer_next = finditer.next()
    # print(finditer_next.groups())

    # sub
    sub = re.sub("x", "w", "hexo")
    print(sub)

    sub = re.sub('[xw]','z','hexo world')
    print(sub)


    # subn
    subn = re.subn(r"x", r"w", r"hexo xi")
    print(subn)

    # \N的使用
    re_sub = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')
    # {1,2} 出现1到2次
    print(re_sub)


if __name__ == '__main__':
    regex_demo()
