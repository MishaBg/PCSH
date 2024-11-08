from operator import itemgetter


class cath:
    def __init__(self, id, fio, sal, dep_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.dep_id = dep_id


class facul:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CathFacul:
    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id


faculs = [
    facul(1, 'РК'),
    facul(2, 'РТ'),
    facul(3, 'ИУ'),


    facul(11, 'СМ'),
    facul(22, 'Эн'),
    facul(33, 'МТ'),
]



caths = [
    cath(1, 'ИУ5', 25000, 3),
    cath(2, 'ИУ6', 35000, 3),
    cath(3, 'ИУ7', 45000, 3),
    cath(4, 'РК6', 35000, 1),
    cath(5, 'РТ5', 25000, 2),
]


CathFaculs = [
    CathFacul(1,1),
    CathFacul(2,2),
    CathFacul(3,3),
    CathFacul(3,4),
    CathFacul(3,5),


    CathFacul(11,1),
    CathFacul(22,2),
    CathFacul(33,3),
    CathFacul(33,4),
    CathFacul(33,5),
]


def main():
    """Основная функция"""

    one_to_many = [(e.fio, e.sal, d.name) 
        for d in faculs
        for e in caths 
        if e.dep_id==d.id]
    
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id) 
        for d in faculs
        for ed in CathFaculs
        if d.id==ed.dep_id]
    
    many_to_many = [(e.fio, e.sal, dep_name) 
        for dep_name, dep_id, emp_id in many_to_many_temp
        for e in caths if e.id==emp_id]
    
    #задание1
    res = sorted(one_to_many, key=itemgetter(0))
    print(res)

    #задание2
    one_to_many = sorted(one_to_many, key=itemgetter(2))
    temp = ''
    cur = 0
    res2 = [[name, 0]
            for fio, val, name in one_to_many]
    
    for i in range(0, len(res2)):
        if res2[i][0] != temp:
            temp = res2[i][0]
            cur = i
            res2[i][1] += 1
        else:
            res2[cur][1] += 1

    temp = ''
    res2 = list(filter(lambda y: y[1] != 0, res2))
    print(res2)

    #задание3
    res3 = [[fio, name]
            for fio, val, name in many_to_many
                if fio[0] == 'И']
    print(res3)


if __name__ == '__main__':
    main()
