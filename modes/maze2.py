"""
Should navigate the maze, using a hyped up hug the wall tactic (probs needs some fixing though)
"""
from time import sleep

from robot import ROBOT
from settings import DEBUG, MAZE_CLOSE_THRESH, MAZE_PICKINESS, MAZE_SIDE_THRESH, MAZE_ROBOT_TURN_TIME


class Maze2:
    def __init__(self):
        self.state = "forwards"
        self.side_dist = 0
        self.count = 0
        self.turn = 0
        self.follow_side = 2


    @staticmethod
    def dprint(txt):
        if DEBUG:
            print(txt)

    def update(self):
        #The original maze2
        """
        self.count += 1

        distances = ROBOT.get_distance()
        if self.count > 1000:
            self.dprint(distances)
            self.count = 0
        if self.state == "forwards":
            Checks if robot has space on either side, i.e a turn, and if so, takes it
            making sure that it is a wide turn so as not to hit a wall

            if distances[0] > MAZE_SIDE_THRESH or distances[0] == 0:
                self.dprint("Left turn sighted Wall on the left is {} away!".format(distances[0]))
                self.state = "turning"
                self.side_dist = distances[0]
                sleep(0.3)
                ROBOT.set_tank(-1, 1)
            elif distances[2] > MAZE_SIDE_THRESH or distances[2] == 0:
                self.dprint("Right turn sighted Wall on the right is {} away!".format(distances[2]))
                self.state = "turning"
                self.side_dist = distances[2]
                sleep(0.3)
                ROBOT.set_tank(1, -1)


            elif 0 < distances[0] < MAZE_CLOSE_THRESH:
                ROBOT.bear_right()
                self.dprint("Bearing right")
            elif 0 < distances[2] < MAZE_CLOSE_THRESH:
                self.dprint("Bearing left")
                ROBOT.bear_left()

            else:
                ROBOT.forwards(speed=0.5)
                self.dprint("Forwards!")

        elif self.state == "turning":
            #self.dprint("Turning! Waiting for {}, getting {}".format(self.side_dist, distances[1]))
            if distances[1] >= MAZE_PICKINESS:
                self.dprint("Turning stopped!")
                ROBOT.forwards(speed=0.5)
                self.state = "forwards"
                sleep(0.5)
        """
<<<<<<< HEAD
=======
        #The second maze2
        """
>>>>>>> a1df43d25124a601623724b8b00058a0b9032020
        distances = ROBOT.get_distance()

        
        if distances[self.follow_side] > 10 or distances[self.follow_side] == 0:
            print("Bear RIGHT {}".format(distances[self.follow_side]))
            if self.follow_side == 0:
                ROBOT.bear_left(change=100)
            else:
                ROBOT.bear_right(change=100)
        elif distances[self.follow_side] <= 5:
            print("Bear LEFT {}".format(distances[self.follow_side]))
            if self.follow_side == 0:
                ROBOT.bear_right(change=100)
            else:
                ROBOT.bear_left(change=100)
        else:
            print("{} From right wall, going forwards".format(distances[self.follow_side]))
            ROBOT.forwards(speed=0.5)
        """
        #the third maze2

<<<<<<< HEAD

        if distances[2] > 80:
            self.follow_side = 0
            print("Following left side now!")

        

            
=======
        distances = ROBOT.get_distance()
        if distances[0] <=15 and distances[1] <=15:
            ROBOT.right(duration=0.75)
        elif distances[0] > 30:
            ROBOT.bear_right()
        elif distances[0] <= 10:
            ROBOT.bear_left()
        else:
            ROBOT.forwards(speed=0.5)
>>>>>>> a1df43d25124a601623724b8b00058a0b9032020


