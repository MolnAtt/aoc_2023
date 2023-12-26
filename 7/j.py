from re import sub
def beolvas(path:str) -> list[tuple[str, int]]:
    return [ (p[0], int(p[1])) for p in [ sor.split(' ') for sor in open(path, 'r')]]

def ennyiter_sorrend_alapjan(sorrend):
    return { figura:i for i,figura in enumerate(sorrend) }

def abcbevalt(abc:str, lap_ennyit_er:dict[str,int], s:str):
    return ''.join([abc[lap_ennyit_er[c]] for c in s])

def rendezes_1(figura_ennyit_er:dict[str,int], abc:str, lap_ennyit_er:dict[str,int], hb:tuple[str,int])->tuple[int, str]:
    return (figura_ennyit_er[figura(hb[0])], abcbevalt(abc, lap_ennyit_er, hb[0]))

def rendezes_2(figura_ennyit_er:dict[str,int], abc:str, lap_ennyit_er:dict[str,int], hb:tuple[str,int])->tuple[int, str]:
    return (figura_ennyit_er[optimize_2(figura_ennyit_er, abc, lap_ennyit_er,figura(hb[0]))], abcbevalt(abc, lap_ennyit_er, hb[0]))

def optimize_2(figura_ennyit_er:dict[str,int], abc:str, lap_ennyit_er:dict[str,int], hand:str) -> str:
    nemJk = { c for c in hand if c!='J'}
    if len(nemJk)==0:
        return 'AAAAA'
    return sorted([ sub('J', nemJ, hand) for nemJ in nemJk ], key=lambda hb : rendezes_1(figura_ennyit_er, abc, lap_ennyit_er, hb))[-1]

def lapstatisztika(s:str) -> dict[str, int]:
    d = {}
    for c in s:
        if c in d.keys():
            d[c]+=1
        else:
            d[c]=1 
    return d

def figura(s:str) -> str:
    ertekek = lapstatisztika(s).values()
    if 5 in ertekek:
        return 'five_of_a_kind'
    if 4 in ertekek:
        return 'four_of_a_kind'
    if 3 in ertekek:
        return 'full_house' if 2 in ertekek else 'three_of_a_kind'
    if 2 in ertekek:
        return 'two_pair' if len([x for x in ertekek if x == 2]) == 2 else 'one_pair'
    return 'high_card'

def solve(figura_ennyit_er, abc, lap_ennyit_er, rendezofv, hand_bid) -> int:
    return sum([(i+1)*e[1] for i, e in enumerate(sorted(hand_bid, key=lambda hb: rendezofv(figura_ennyit_er, abc, lap_ennyit_er, hb), reverse=True))])


abc = 'abcdefghijklmnopqrstuvwxyz'
lapsorrend_1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
lapsorrend_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
figurasorrend = ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card',]
figura_ennyit_er = ennyiter_sorrend_alapjan(figurasorrend)
lap_ennyit_er = ennyiter_sorrend_alapjan(lapsorrend_1)


# h = 'KKJJT'
# print('optimize', h, optimize_2(figura_ennyit_er, abc, lap_ennyit_er,h))
# hand_bid = beolvas('example.txt')
hand_bid = beolvas('example.txt')

# print(figura('32T3K'))
# print(figura('T55J5'))
# print(figura('KK677'))
# print(figura('KTJJT'))
# print(figura('234JA'))

print('----------- input: ---------------')
print(*hand_bid, sep='\n')
print('--------------- most sorban ---------------')
for i, e in enumerate(sorted(hand_bid, key=lambda hb: rendezes_1(figura_ennyit_er, abc, lap_ennyit_er, hb), reverse=True)):
    print(i+1, e, abcbevalt(abc, lap_ennyit_er, e[0]))

print(solve(figura_ennyit_er, abc, lap_ennyit_er, rendezes_2, hand_bid))


