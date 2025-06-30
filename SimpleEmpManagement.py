import json
import sqlite3

try:
    class Employees:

        def __init__(self, database = 'test.db'):
            self.con = sqlite3.connect(database)
            self.crs = self.con.cursor()
            self.crs.execute('''CREATE TABLE IF NOT EXISTS emp(
                                Staffnumber INTEGER PRIMARY KEY,
                                name VARCHAR(20),
                                joined DATE)''')

        def showt(self):
            self.crs.execute(f'select * from emp')
            for i in self.crs.fetchall():#fetchall returns a list of tuples
                print(i)

        def addemp(self,*vals):
            self.crs.execute(f'insert into emp (name,joined) values {vals};')

        def savend(self):
            self.con.commit()
            self.con.close()

        def svtojs(self):
            jstemp = []
            self.crs.execute(f'select * from emp')
            for i in self.crs.fetchall():
                jstemp.append({f'{i[0]}':f'{i[1]}','joined':f'{i[2]}'})
            temob = json.dumps(jstemp, indent=4)
            with open('example.json', 'w') as jsfile:
                jsfile.write(temob)


        def exec(self,sql: str):
            self.crs.execute(sql)

        def delemp(self,dname):
            self.crs.execute(f'DELETE FROM emp WHERE name="{dname}" ;')

    hand = Employees()

    while True:
        print('''select option:
                1.add employee
                2.see members
                3.delete employee
                4.Execute Sql
                5.Save to json
                6.Exit''')

        match(int(input('input:'))):
            case 1:
                while True:
                    hand.addemp(input('enter name:'), input('enter Date:'))
                    print('added')
                    inp = input('do you want to continue(Y or N)?')
                    if inp == 'N' or inp == 'n':
                        break
            case 2:
                hand.showt()
            case 3:
                hand.delemp(input('Enter name:'))
            case 4:
                hand.exec(input('Command:'))
            case 5:
                hand.svtojs()
            case 6:
                hand.savend()
                break
            case _:
                print('invalid value')

except Exception as e:
    print(f'An error has been occurred: {e}')