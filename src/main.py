# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       eligo                                                        #
# 	Created:      9/5/2024, 8:04:51 AM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

controller = Controller()

leftOne = Motor(Ports.PORT1)
leftTwo = Motor(Ports.PORT2)
rightOne = Motor(Ports.PORT3)
rightTwo = Motor(Ports.PORT4)

speed = 100

def driveTask():
    while True:
        driveStraight = controller.axis3.position()
        driveTurn = controller.axis1.position()
        if driveTurn == 0:
            leftOne.spin(FORWARD, driveStraight, PERCENT)
            leftTwo.spin(FORWARD, driveStraight, PERCENT)
            rightOne.spin(FORWARD, driveStraight, PERCENT)
            rightTwo.spin(FORWARD, driveStraight, PERCENT)
        elif driveTurn < 0:
            driveTurn = abs(driveTurn)
            leftOne.spin(FORWARD, driveTurn, PERCENT)
            leftTwo.spin(FORWARD, driveTurn, PERCENT)
            rightOne.spin(FORWARD, driveTurn * 0.6, PERCENT)
            rightTwo.spin(FORWARD, driveTurn * 0.6, PERCENT)
        elif driveTurn > 0:
            leftOne.spin(FORWARD, driveTurn * 0.6, PERCENT)
            leftTwo.spin(FORWARD, driveTurn * 0.6, PERCENT)
            rightOne.spin(FORWARD, driveTurn, PERCENT)
            rightTwo.spin(FORWARD, driveTurn, PERCENT)
            


drive = Thread(driveTask)