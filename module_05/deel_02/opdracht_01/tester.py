from functions import print_colorvars
from functions import getEarnigs

testMainCharacter2 = {
    'name' : 'TestChar2',
    'cash' : {
        'platinum' : 1,
        'gold' : 4,
        'silver' : 4,
        'copper' : 10
    }
}
result2 = [{'name': 'TestChar2', 'start': 30.0, 'end': 200.0}]

if print(getEarnigs(170, testMainCharacter2, [], [])) != result2:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')

