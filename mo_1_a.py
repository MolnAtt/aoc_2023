szamjelek = "0123456789"

def elso_szam(s:str) -> int:
    for c in s:
        if c in szamjelek:
            return c
    raise Exception('nincs is benne szam')

def utolso_szam(s:str) -> int:
    for i in range(len(s)-1, -1, -1):
        if s[i] in szamjelek:
            return s[i]
    raise Exception('nincs is benne szam')

def ketjegyuvel_osszeg(coll):
    osszeg = 0
    for sor in coll:
        osszeg += int(elso_szam(sor) + utolso_szam(sor))
    return osszeg


def megold(path:str) -> int:
    return ketjegyuvel_osszeg(open(path, 'r'))


print('példa:')
print(megold('examples/e1.txt'))
print('inputfájl:')
print(megold('inputs/1.txt'))
