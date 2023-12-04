szamjelek = '0123456789'

def szimbolum(c):
    return c not in szamjelek and c !='.'

def beolvas(path:str) -> list[str]:
    return [sor.strip() for sor in open(path, 'r')]

def elso_nemszam(sor:str, i:int) -> int:
    for j in range(i, len(sor), 1):
        if sor[j] not in szamjelek:
            return j
    return len(sor)

def itteni_szamstring(sor:str, j:int) -> str:
    if sor[j] not in szamjelek:
        return None
    return sor[j:elso_nemszam(sor,j)]

def sor_szamai(sor:str) -> list[int, int]:
    '''
    pl. '467..114..' ---> [(0, '467'), (5, '114')]
    '''
    result = []
    j = 0
    while j<len(sor):
        szamstring = itteni_szamstring(sor, j)
        if szamstring == None:
            j+=1
        else:
            result.append((j, szamstring))
            j += len(szamstring)
    return result

def lekerdezhetok(i:int,j:int, m:list[str]) -> bool:
    return 0<=i and i<len(m) and 0<=j and j<len(m[0])

def is_part_number(m:list[str], szam:tuple[int,int,str])-> bool:
    i,j,s = szam
    #előtte:
    if 0<j and szimbolum(m[i][j-1]):
        return True
    #utána:
    if j+len(s)<len(m[0]) and szimbolum(m[i][j+len(s)]):
        return True
    #alatta és felette:
    for k in (i-1,i+1):
        for l in range(j-1, j+len(s)+1, 1):
            if lekerdezhetok(k,l,m) and szimbolum(m[k][l]):
                return True
    return False

def part_numbers(m:list[str], szamok:list[tuple[int,int,str]])-> bool:
    return [szam for szam in szamok if is_part_number(m, szam)]

def matrix_szamai(m:list[str]) -> list[tuple[int,int,str]]:
    return [(i,j,szam) for i,sor in enumerate(m) for j,szam in sor_szamai(sor)]

def megold_1(m:list[str]) -> int:
    return sum(int(szam) for _,_,szam in part_numbers(m, matrix_szamai(m)))

def szam_kozbulso_szamjele_alapjan(m:list[str], i:int, j:int) -> tuple[int,int,str]:
    l = j
    while(0<=l and m[i][l] in szamjelek):
        l-=1
    return (l+1,itteni_szamstring(m[i], l+1))

def ha_van_itt_valami_beleteszi(m:list[str], i:int, j:int, tomb:set[tuple[int,int,str]]) -> None:
    szam = szam_kozbulso_szamjele_alapjan(m, i, j)
    if szam != None:
        e, s = szam
        tomb.add((i,e,s))

def kornyezo_szampar(m:list[str], i:int, j:int) -> tuple[tuple[int,int,str],tuple[int,int,str]]:
    result = set()
    for k in (i-1, i, i+1):
        for l in (j-1, j, j+1):
            if lekerdezhetok(k,l,m) and m[k][l] in szamjelek:
                ha_van_itt_valami_beleteszi(m, k, l, result)
    if len(result) != 2:
        return None
    l = list(result)
    return l[0], l[1]
    
def gear_ratio(m:list[str], i:int, j:int) -> int:
    if m[i][j] !='*':
        return 0
    szampar = kornyezo_szampar(m, i, j)
    if szampar == None:
        return 0
    return int(szampar[0][2])*int(int(szampar[1][2]))

def megold_2(m:list[str]):
    return sum(gear_ratio(m, i, j) for i,sor in enumerate(m) for j,c in enumerate(sor))

print('első feladat megoldása: ', megold_1(beolvas('input.txt')))
print('második feladat megoldása: ', megold_2(beolvas('input.txt')))
