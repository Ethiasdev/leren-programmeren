def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    naam = []
    for i in list:
        if (i[key]) == value:
            naam.append(i['name'])
        return naam

def getShareWithFriends(friends:list) -> int:
    return (getFromListByKeyIs(friends, 'shareWith', True))

friends = [{
    'name' : 'Jorick',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 9,
        'silver' : 9,
        'copper' : 43
    }
},{
    'name' : 'Grommel',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 1,
        'gold' : 2,
        'silver' : 2,
        'copper' : 8
    }
},{
    'name' : 'Tristan',
    'shareWith' : False,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 2,
        'silver' : 17,
        'copper' : 11
    }
},{
    'name' : 'Massimo',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 5,
        'silver' : 9,
        'copper' : 3
    }
},{
    'name' : 'Durbane',
    'shareWith' : True,
    'adventuring' : False,
    'cash' : {
        'platinum' : 1,
        'gold' : 5,
        'silver' : 12,
        'copper' : 11
    }
},{
    'name' : 'Otho',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 1,
        'silver' : 2,
        'copper' : 7
    }
}]

print(getShareWithFriends(friends))

