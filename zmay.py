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
            print(str(astr))
        self.gen.append(astr)
        return(self.gen)

mainmap = field(16, 16, '✡', '☪', '☪')
mainmap.pr_cl()
print(mainmap.pr_cl())