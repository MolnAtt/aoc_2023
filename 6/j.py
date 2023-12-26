from re import sub
from math import sqrt, floor, ceil
from functools import reduce

def beolvas_1(path:str)->tuple[list[int], list[int]]:
    return ([int(s) for s in sub(r' +', r' ', sub(r'^.*:', r'', sor)).strip().split(' ')] for sor in open(path, 'r') )

def beolvas_2(path:str)->tuple[list[int], list[int]]:
    return tuple(int(sub(r' +', r'', sub(r'^.*:', r'', sor)).strip()) for sor in open(path, 'r') )

def masodfoku_egyenlet_megoldokeplete(a:float, b:float, c:float) -> tuple[float, float]:
    return tuple((-b+sign*sqrt(b*b-4*a*c))/(2*a) for sign in (-1,1))

def tartalmazott_egeszek_szama(intervallum:tuple[float, float]) -> int:
    return ceil(intervallum[0])-floor(intervallum[1])-1

def solve_1(path):
    time, distance = beolvas_1(path)
    menetdarabok = [tartalmazott_egeszek_szama(masodfoku_egyenlet_megoldokeplete(-1, t, -(distance[i]))) for i,t in enumerate(time)]
    return reduce(lambda x,y: x*y, menetdarabok)

def solve_2(path):
    time, distance = beolvas_2(path)
    return tartalmazott_egeszek_szama(masodfoku_egyenlet_megoldokeplete(-1, time, -distance))

print(solve_1('example.txt'))
print(solve_1('input.txt'))

print(solve_2('example.txt'))
print(solve_2('input.txt'))
