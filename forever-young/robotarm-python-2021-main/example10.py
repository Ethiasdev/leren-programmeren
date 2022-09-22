from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for x in range(5):
    
    for i in range(x): robotArm.moveRight()
    robotArm.grab()
    for k in range(9 -x -x): robotArm.moveRight()
    robotArm.drop()
    for k in range(9 + x): robotArm.moveLeft()
    
robotArm.wait()