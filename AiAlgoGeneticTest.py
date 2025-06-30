import random


class Knap:
    def __init__(self,weig,val):
        self.weight = weig
        self.value = val


k1,k2,k3 = (Knap(23,400),
            Knap(33,300),
            Knap(23,500))


knapitems = [k1,k2,k3]


def gen_init_pop(popsize,invisize):
    pop = []
    for invi in range(popsize):
        cuinv = []
        for gene in range(invisize):
            randgene = random.randint(0,1)
            cuinv.append(randgene)
        pop.append(cuinv)
    return pop

def cal_invid_fitness(indiv,knapitems,knapmax):
    totalwei = 0
    totalval = 0
    for genein in range(0,len(indiv)):
        curbit = indiv[genein]
        if curbit == 1:
            totalwei += knapitems[genein].weight
            totalval += knapitems[genein].value
    if totalwei > knapmax:
        return 0
    return totalval


def scoreofpop():
    scores = []
    for invid in popu:
        invidval = cal_invid_fitness(invid,knapitems,66)
        scores.append(invidval)
    return scores


popu = gen_init_pop(4,3)
print(popu)
print(scoreofpop())



