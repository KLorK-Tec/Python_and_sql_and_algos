
from rich.table import Table
from rich.console import Console


table = Table(title="Jadval tozie")
table.add_column('xi')
table.add_column('fi')
table.add_column('Fi')
table.add_column('xifi')
table.add_column('xi^2fi')
inp = input('1-num,num,... \n2-num,fi,... \nMode:')
if inp == '1':
    rs = input('Values:').split(',')
elif inp == '2':#For ease of use
    rsk = input('Values and fi:').split(',')
    m = ''
    for i in range(0,len(rsk),+2):
        m += (f'{rsk[i]},' * int(rsk[i+1]))
    rs = m.split(',')
    rs.pop()
else:
    print('Invalid Input')

def normvalues():
    try:
        rsxi = []
        rsfi = []
        rs.sort()
        k = 1
        for i in range(1,len(rs)):#Builds fi using check each algorithm
            if rs[i] == rs[i - 1]:
                k += 1
                if i == len(rs) - 1:
                    rsfi.append(k)
                    k = 0
            else:
                rsfi.append(k)
                if i == len(rs) - 1:
                    rsfi.append(1)
                    continue
                k = 1
        for i in range(len(rs)):#Builds xi
            if rs[i] == rs[i - 1]:
                continue
            else:
                rsxi.append(int(rs[i]))
        l = 0
        rsFI = []
        for i in rsfi: #Builds Fi
            l += i
            rsFI.append(l)

        rxifi = []
        for i in range(len(rsxi)):#Builds xifi
            rxifi.append(rsxi[i] * rsfi[i])

        rxi2fi = []
        for i in range(len(rsxi)):#Builds xi2fi
            rxi2fi.append(rsxi[i] * rxifi[i])

        for i in range(len(rsxi)):
            table.add_row(f'{rsxi[i]}', f'{rsfi[i]}', f'{rsFI[i]}', f'{rxifi[i]}', f'{rxi2fi[i]}')
        nfi = sum(rsfi)
        sigxifi = sum(rxifi)
        sigxi2fi = sum(rxi2fi)
        variance = (sigxi2fi-(sigxifi * sigxifi)/nfi)/(nfi-1)
        print(f'x-mean = {sigxifi/rsFI[len(rsxi)-1]}')
        print(f'S^2x = {variance}')
        print(f'S = {variance // 2}')
    except Exception as e:
        print(f'an Error has occurred: {e}')

def valueproxy():
    rs = input('Values:').split(',')

normvalues()
console = Console()
console.print(table)
