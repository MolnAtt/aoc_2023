from re import search, Match

def nyertes_es_tied(s:Match[str]) -> tuple[set[int], set[int]]:
    return ({ int(szamstr) for szamstr in s.group(2).strip().split(' ') }, { int(szamstr) for szamstr in s.group(3).strip().split(' ') })

def beolvas(path:str) -> list[tuple[set[int], set[int]]]:
    return [nyertes_es_tied(search(r'Card *(\d*): (.*) \| (.*)', sor.replace('  ', ' '))) for sor in open(path, 'r')]

def nyeremeny_1(db:int) -> int:
    return 0 if db==0 else 2**(db-1)

def megold_1(halmazparok:list[tuple[set[int], set[int]]]) -> int:
    return sum(nyeremeny_1(len(nyertes.intersection(tied))) for nyertes,tied in halmazparok)

def megold_2(halmazparok:list[tuple[set[int], set[int]]]) -> int:
    m = [1]*len(halmazparok)
    for i,e in enumerate(len(nyertes.intersection(tied)) for nyertes,tied in halmazparok):
        for j in range(i+1, i+e+1, 1):
            m[j]+=m[i]
    return sum(m)

print(megold_1(beolvas('example.txt')))
print(megold_1(beolvas('input.txt')))

print(megold_2(beolvas('example.txt')))
print(megold_2(beolvas('input.txt')))


