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


    @staticmethod
    def dprint(txt):
        if DEBUG:
            print(txt)

    def update(self):
        self.count += 1

        distances = ROBOT.get_distance()
        if self.count > 100:
            self.dprint(distances)
            self.count = 0
        if self.state == "forwards":
            """Checks if robot has space on either side, i.e a turn, and if so, takes it
            making sure that it is a wide turn so as not to hit a wall"""

            if distances[0] > MAZE_SIDE_THRESH or distances[0] == 0:
                self.dprint("Left turn sighted Wall on the left is {} away!".format(distances[0]))
                self.state = "turning"
                self.turn += 1
                if self.turn == 10 or distances[0] == 0:
                    sleep(0.8)
                    ROBOT.left(duration=MAZE_ROBOT_TURN_TIME)
                    ROBOT.forwards(speed=0.5)
                    sleep(1)
                    self.state = "forwards"
                else:
                    self.side_dist = distances[0]
                    sleep(0.3)
                    ROBOT.set_tank(-1, 1)
                    
                    
                
            #elif distances[2] > MAZE_SIDE_THRESH:
            #    self.state = "turning"
            #    self.turn += 1
            #    self.side_dist = distances[2]
            #    self.dprint("Right turn sighted! Wall on the right is {} away".format(distances[2]))
            #    sleep(0.7)
            #    ROBOT.right(duration=MAZE_ROBOT_TURN_TIME)
            #    ROBOT.forwards(speed=0.5)
            #    sleep(0.5)
            #    self.state = "forwards"


            elif 0 < distances[0] < MAZE_CLOSE_THRESH:
                ROBOT.bear_right()
                self.dprint("Bearing right")
            #elif 0 < distances[2] < MAZE_CLOSE_THRESH:
            #    self.dprint("Bearing left")
            #    ROBOT.bear_left()

            else:
                ROBOT.forwards(speed=0.5)
                self.dprint("Forwards!")

        elif self.state == "turning":
            self.dprint("Turning! Waiting for {}, getting {}".format(self.side_dist, distances[1]))
            if self.side_dist - MAZE_PICKINESS < distances[1]+15 < self.side_dist + MAZE_PICKINESS:
                self.dprint("Previous turn sighted was {}, now seeing {}".format(self.side_dist, distances[1]))
                self.dprint("Turning stopped!")
                ROBOT.forwards(speed=0.5)
                self.state = "forwards"
                sleep(0.5)



