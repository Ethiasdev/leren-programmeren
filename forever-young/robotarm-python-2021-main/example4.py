from concurrent.futures.thread import BrokenThreadPool
from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')


# Jouw python instructies zet je vanaf hier:
for i in range(1,4):
    robotArm.grab()
    for b in range(1,3):
            robotArm.moveRight()
    robotArm.drop()
    if i == 3: break
    for k in range(1,3):
        robotArm.moveLeft()
    robotArm.grab() 

for h in range(1,4):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    if h == 3: break
    robotArm.moveRight()


    

    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()