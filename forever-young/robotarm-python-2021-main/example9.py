from RobotArm import RobotArm 
robotArm = RobotArm('exercise 9')
for x in range(11):
    robotArm.grab()
    for i in range(1,6): robotArm.moveRight()
    robotArm.drop()
    for i in range(1,6): robotArm.moveLeft()
    if robotArm.grab() == False:
        robotArm.moveRight()
robotArm.wait()