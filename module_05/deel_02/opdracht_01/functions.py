import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY

##################### M04.D02.O2 #####################

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

def getPersonCashInGold(personCash:dict) -> float:
    platinum = personCash['platinum'] * 25
    goud = personCash['gold']
    silver = personCash['silver'] / 5
    copper = personCash['copper'] / 10 / 5
    totaal = platinum + goud + silver + copper
    return totaal

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    copperPersoon = people * JOURNEY_IN_DAYS * COST_FOOD_HUMAN_COPPER_PER_DAY
    copperPaard = horses * JOURNEY_IN_DAYS * COST_FOOD_HORSE_COPPER_PER_DAY
    copperPersoonPaard = copperPersoon + copperPaard
    goud =  copper2gold(copperPersoonPaard)
    return round(goud, 2)
##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    naam = []
    for i in list:
        if i[key] == value:
            naam.append(i)
    return naam

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    new_list = []
    for dict in getAdventuringPeople(friends):
        if dict in getShareWithFriends(friends):
            new_list.append(dict)
    return new_list

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS + tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
  item_text = []
  for item in items:
    item_text.append("{amount}{unit} {name}".format(amount=item["amount"], name=item["name"], unit=item["unit"]))

  return ", ".join(item_text)

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

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()