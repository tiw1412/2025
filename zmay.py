class field:
    def __init__(self, height, width, mainsymb, upgs, lrgs, gen = []):
        self.height = height
        self.width = width
        self.mainsymb = mainsymb
        self.upgs = upgs
        self.lrgs = lrgs
        self.gen = gen
    def pr_cl(self):
        astr = []
        for i in range(self.width):
            astr.append(self.mainsymb)
        for i in range(self.height):
            self.gen.append(astr)
        return self.gen


hght = 0
wght = 0
def prnfre(hght, wght):
    while True:
        print(chto[hght][wght], end=' ')
        wght += 1
        if wght == mainmap.width:
            wght = 0
            hght += 1
            print('')
        if hght == mainmap.height:
            break

mainmap = field(16, 16, '✡', '☪', '☪')
mainmap.pr_cl()
chto = mainmap.pr_cl()
print(chto)
print('--')
prnfre(hght, wght)
chto[0][1] = 'z'
prnfre(hght, wght)