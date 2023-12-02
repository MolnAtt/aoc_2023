szamok = {
    '1':'1', 
    '2':'2', 
    '3':'3', 
    '4':'4', 
    '5':'5', 
    '6':'6', 
    '7':'7', 
    '8':'8', 
    '9':'9', 
    'one':'1', 
    'two':'2', 
    'three':'3', 
    'four':'4', 
    'five':'5', 
    'six':'6', 
    'seven':'7', 
    'eight':'8', 
    'nine':'9',
    }


def elso_szam_elso_feladathoz(s:str) -> int:
    for c in s:
        if c in szamok.keys():
            return c
    raise Exception('nincs is benne szam')


def utolso_szam_elso_feladathoz(s:str) -> int:
    for i in range(len(s)-1, -1, -1):
        if s[i] in szamok.keys():
            return s[i]
    raise Exception('nincs is benne szam')


def szam(s:str, i:int): 
    '''
    megnézi, hogy az s string i indexén kezdődik-e valamilyen szám bármilyen értelemben, ha igen, visszaadja azt, ha nem, None.
    '''
    for j in [1,3,4,5]:
        if i+j <= len(s) and s[i:i+j] in szamok.keys():
            return szamok[s[i:i+j]]
    return None


def ketjegyuvel_osszeg(coll, balrol, jobbrol):
    osszeg = 0
    for sor in coll:
        osszeg += int(balrol(sor) + jobbrol(sor))
    return osszeg


def megold(path:str, balrol, jobbrol) -> int:
    return ketjegyuvel_osszeg(open(path, 'r'), balrol, jobbrol)


def elso_szam_masodik_feladathoz(s:str) -> int:
    for i, _ in enumerate(s):
        sz = szam(s,i)
        if sz != None:
            return sz        
    raise Exception('nincs is benne szam')

def utolso_szam_masodik_feladathoz(s:str) -> int:
    for i in range(len(s)-1, -1, -1):
        sz = szam(s,i)
        if sz != None:
            return sz        
    raise Exception('nincs is benne szam')


print('példa az első részhez:')
print(megold('example_a.txt', elso_szam_elso_feladathoz, utolso_szam_elso_feladathoz))
print('inputfájlon:')
print(megold('input.txt', elso_szam_elso_feladathoz, utolso_szam_elso_feladathoz))

print('példa a második részhez:')
print(megold('example_b.txt', elso_szam_masodik_feladathoz, utolso_szam_masodik_feladathoz))

print('inputfájlon:')
print(megold('input.txt', elso_szam_masodik_feladathoz, utolso_szam_masodik_feladathoz))
