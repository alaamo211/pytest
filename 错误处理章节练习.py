# -*- coding: utf-8 -*-
from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError: 
        return float(s.strip())#strip()用于消除字符串中的空格

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7. 6 =', r)

main()