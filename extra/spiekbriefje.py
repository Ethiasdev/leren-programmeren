def copper2silver(amount:int) -> float:
    zilver = amount / 10
    return float(zilver)
    

def silver2gold(amount:int) -> float:
    goud = amount / 5
    return float(goud)

def copper2gold(amount:int) -> float:
    silver = amount / 10
    goud = silver / 5
    return float(goud)

def platinum2gold(amount:int) -> float:
    platinum = amount * 25
    return platinum

def getItemsValueInGold(items:list) -> float:
    lijst = []
    for item in items:
        if item['price']['type'] == 'copper':
            copper = item['amount'] * item['price']['amount']
            lijst.append(copper2gold(copper))
        elif item['price']['type'] == 'silver':
            silver = item['amount'] * item['price']['amount']
            lijst.append(silver2gold(silver))
        elif item['price']['type'] == 'platinum':
            platinum = item['amount'] * item['price']['amount']
            lijst.append(platinum2gold(platinum))
        else:
            goud = item['amount'] * item['price']['amount']
            lijst.append(goud)
    return sum(lijst)


def getInterestingInvestors(investors:list) -> list:
    return [item for item in investors if item['profitReturn'] < 10]

def getAdventuringInvestors(investors:list) -> list:
    return [item for item in investors if item['adventuring'] and item['profitReturn'] < 10 ]

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totalCost = 0
    totalCost += getItemsValueInGold(gear)


    return totalCost

testInverstorsList1 = [{
    'profitReturn' : 5,
    'adventuring' : True
}]

testGearList1 = [{
    'amount' : 3,
    'price' : {
        'amount' : 1,
        'type' : 'gold'
    }
}]

print(getTotalInvestorsCosts(testInverstorsList1, testGearList1))


