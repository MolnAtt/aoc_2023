from re import match, search

# BEOLVASÁS

def kockaszam(search) -> int:
    return 0 if search == None else int(search.group(1))

def rgbparszol(s:str) -> (int,int,int):
    return (kockaszam(search(r'(\d+) red', s)), kockaszam(search(r'(\d+) green', s)), kockaszam(search(r'(\d+) blue', s)))

def parszol(sor:str) -> list[(int,int,int)]:
    return [rgbparszol(rgb) for rgb in search(r'Game (\d.*):(.*)', sor).group(2).split(';')]

def beolvas(path:str) -> list[list[(int,int,int)]]:
    return [parszol(sor) for sor in open(path, 'r')]

# MEGOLDAS

def lehetseges_huzassorozat(huzassorozat:list[(int,int,int)], rgb:(int,int,int)) -> bool: 
    for huzas in huzassorozat:
        if lehetetlen_huzas(huzas, rgb):
            return False
    return True

def lehetetlen_huzas(huzas:(int,int,int), rgb:(int,int,int)) -> bool:
    h,u,z = huzas
    r,g,b = rgb
    return r<h or g<u or b<z

def megold_1(path:str)->int:
    osszeg = 0
    for i, huzassorozat in enumerate(beolvas(path)):
        if lehetseges_huzassorozat(huzassorozat, (12, 13, 14)):
            osszeg += (i+1)
    return osszeg

def minrgb(huzassorozat:list[(int,int,int)]) -> (int,int,int):
    minr = 0
    ming = 0
    minb = 0
    for r,g,b in huzassorozat:
        minr = max(minr,r)
        ming = max(ming,g)
        minb = max(minb,b)
    return (minr, ming, minb)

def megold_2(path:str) -> int:
    osszeg = 0
    for huzassorozat in beolvas(path):
        r,g,b = minrgb(huzassorozat)
        # print((r,g,b), r*g*b)
        osszeg += r*g*b
    return osszeg

# FŐPROGRAM

print('első feladat:')
print('    a példában:', megold_1('example.txt'))
print('    az inputban:', megold_1('input.txt'))

print('második feladat:')
print('    a példában:', megold_2('example.txt'))
print('    az inputban:', megold_2('input.txt'))

