class Bijekcio_sor:
    def __init__(self, **kwargs):
        self.destination_range_start = kwargs['destination_range_start']
        self.source_range_start = kwargs['source_range_start']
        self.range_length = kwargs['range_length']
    
    def __str__(self):
        return ' '.join((str(self.destination_range_start), str(self.source_range_start), str(self.range_length)))

    def tartalmazza(self, elem:int)->bool:
        return self.source_range_start <= elem and elem < self.source_range_start+self.range_length
    
    def __getitem__(self, a:int)->int:
        if self.tartalmazza(a):
            return a - self.source_range_start + self.destination_range_start
        return a
    
    def inverz(self):
        return Bijekcio_sor(
            source_range_start = self.destination_range_start,
            destination_range_start = self.source_range_start,
            range_length = self.range_length,
            )

class Bijekcio:
    def __init__(self, bijekcio_sorok:list[str]):
        self.bijekcio_sorok = sorted(bijekcio_sorok, key=lambda bs: bs.source_range_start)
        

    def beolvas(path:str) -> list[Bijekcio_sor]:
        result = []
        for sor in open(path, 'r'):
            t = sor.strip().split(' ')
            result.append(Bijekcio_sor(
                destination_range_start=int(t[0]),
                source_range_start=int(t[1]),
                range_length=int(t[2]),
                ))
        return result

    def __str__(self) -> str:
        return '\n'.join([str(bs) for bs in self.bijekcio_sorok])

    def keres(self, elem:int):
        e = 0
        v = len(self.bijekcio_sorok)-1
        while e <= v:
            k = (e+v) // 2
            if self.bijekcio_sorok[k].tartalmazza(elem):
                return k
            elif elem < self.bijekcio_sorok[k].source_range_start:
                v = k-1
            elif elem > self.bijekcio_sorok[k].source_range_start:
                e = k+1
        return e

    def __getitem__(self, a:int) -> int:
        h = self.keres(a)
        # print(f'megtaláltam {a}-t, itt a helye: {h}')
        if h == len(self.bijekcio_sorok):
            return a
        sor = self.bijekcio_sorok[h]
        if sor.tartalmazza(a):
            return a - sor.source_range_start + sor.destination_range_start
        return a
    
    def inverz(self):
        return Bijekcio([sor.inverz() for sor in self.bijekcio_sorok])
    



def kompozicio_alkalmazasa(bijekciolista:list[Bijekcio], elem:int) -> int:
    a = elem
    # print(f'{a} ', end='')
    for bijekcio in bijekciolista:
        # print('most ezen megy át:')
        # print(bijekcio)
        a = bijekcio[a]
        # print(f'-> {a}', end=' ')
    # print(f' => {a}')
    return a



def beolvas(dir:str) -> tuple[list[Bijekcio], list[int]]:
    h2l = Bijekcio(Bijekcio.beolvas(f'{dir}/7_humidity-to-location.txt'))
    t2h = Bijekcio(Bijekcio.beolvas(f'{dir}/6_temperature-to-humidity.txt'))
    l2t = Bijekcio(Bijekcio.beolvas(f'{dir}/5_light-to-temperature.txt'))
    w2l = Bijekcio(Bijekcio.beolvas(f'{dir}/4_water-to-light.txt'))
    f2w = Bijekcio(Bijekcio.beolvas(f'{dir}/3_fertilizer-to-water.txt'))
    s2f = Bijekcio(Bijekcio.beolvas(f'{dir}/2_soil-to-fertilizer.txt'))
    s2s = Bijekcio(Bijekcio.beolvas(f'{dir}/1_seed-to-soil.txt'))

    bijekciolista = [s2s, s2f, f2w, w2l, l2t, t2h, h2l]
    seeds = [int(elem) for elem in open(f'{dir}/0_seeds.txt').readline().split(' ')]
    return (bijekciolista, seeds)


def megold_1(dir:str):
    bijekciolista, seeds = beolvas(dir)

    min = kompozicio_alkalmazasa(bijekciolista, seeds[0])

    i = 1
    while i < len(seeds):
        alt = kompozicio_alkalmazasa(bijekciolista, seeds[i])
        if alt < min:
            min = alt
        i+=1
    return min

def megold_2(dir:str):
    bijekciolista, seeds = beolvas(dir)
    inverz_bijekciok = [bijekcio.inverz() for bijekcio in bijekciolista]
    inverz_bijekciok.reverse()
    # print(f'ez itt 0-ára ható inverz bijekció:')
    # print(inverz_bijekciok[1])
    # print(f'így hat 0-ra:')
    # print(f'0 -> {inverz_bijekciok[1][0]}')


    # for i, inverz_bijekcio in enumerate(inverz_bijekciok):
    #     print(i)
    #     print(inverz_bijekcio)
    print(f'ezek a seedek: '+', '.join([str(s) for s in seeds]))

    eddig = max([sor.destination_range_start+sor.range_length for sor in bijekciolista[-1].bijekcio_sorok])
    print(f'Eddig fogja nézni a teszteket: {eddig}')
    for i in range(0, eddig, 1):
        if i%100000==0:
            print(i)
        if tartalmazza_honnan_range_list(kompozicio_alkalmazasa(inverz_bijekciok, i), seeds):
            return i
    return eddig+1

def tartalmazza_honnan_range(e:int, honnan:int, range:int) -> bool:
    return honnan <= e and e <= honnan+range

def tartalmazza_honnan_range_list(e:int, seeds:list[int]) -> bool:
    for i in range(0, len(seeds), 2):
        if tartalmazza_honnan_range(e, seeds[i], seeds[i+1]):
            return True
    return False



# print(f"A legkisebb a példában: {megold_1('example')}")
# print(f"A legkisebb az inputban: {megold_1('input')}")
# print(f"A legkisebb a példában: {megold_2('example')}")
print(f"A legkisebb az inputban: {megold_2('input')}")
