from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for f in range(5):
    
    for i in range(f): robotArm.moveRight()
    robotArm.grab()
    for k in range(9 -f -f): robotArm.moveRight()
    robotArm.drop()
    for z in range(9 + f): robotArm.moveLeft()
    
robotArm.wait()