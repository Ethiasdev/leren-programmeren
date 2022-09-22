from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
for l in range (20):
    robotArm.grab()
    color = robotArm.scan()

    if color == "red":
        for i in range(9): robotArm.moveRight()
        robotArm.drop()
        for h in range(9): robotArm.moveLeft()
    else:
        robotArm.drop()
        for k in range(1): robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()