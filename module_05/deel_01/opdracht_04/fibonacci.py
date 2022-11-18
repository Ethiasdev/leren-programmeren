def fibonacci(beginGetal):
    aantalRondes = 0
    tweedeGetal = 1
    print(beginGetal)
    while aantalRondes < 15:
        beginGetal = beginGetal + tweedeGetal
        print(beginGetal)
        tweedeGetal = beginGetal + tweedeGetal
        print(tweedeGetal)
        aantalRondes += 1  



fibonacci(beginGetal=0)
