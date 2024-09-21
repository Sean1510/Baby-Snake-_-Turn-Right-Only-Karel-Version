import tkinter as tk
import math
import random
import time

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

# Karel's dimension in 400x400 canvas
KAREL_TO_LEFT_EDGE = 67
KAREL_TO_RIGHT_EDGE = 66
KAREL_TO_TOP_EDGE = 40
KAREL_TO_BOTTOM_EDGE = 41
KAREL_BODY_LINE_WIDTH = 6
KAREL_LEG_WIDTH = 25
KAREL_TOP_LINE_LENGTH = 164
KAREL_BOTTOM_LINE_LENGTH = 180
KAREL_LEFT_LINE_LENGTH = 239
KAREL_RIGHT_LINE_LENGTH = 223
KAREL_WIDOW_START_POINT_X = 162
KAREL_WIDOW_START_POINT_Y = 74
KAREL_WIDOW_WIDTH = 103
KAREL_WIDOW_HEIGHT = 146
KAREL_MOUTH_START_POINT_X = 214
KAREL_MOUTH_START_POINT_Y = 255
KAREL_MOUTH_WIDTH = 68
KAREL_BACK_LEG_START_POINT = 212
KAREL_BACK_LEG_LENGTH_HORIZONTAL = 51
KAREL_BACK_LEG_LENGTH_VERTICAL = 59
KAREL_FRONT_LEG_START_POINT = 213
KAREL_FRONT_LEG_LENGTH_HORIZONTAL = 69
KAREL_FRONT_LEG_LENGTH_VERTICAL = 44

KAREL_SIZE = 80
ORIGINAL_KAREL_SIZE = 400
# karel's parameters in KAREL_SIZE
X1_1 = (KAREL_TO_LEFT_EDGE + KAREL_BACK_LEG_LENGTH_HORIZONTAL) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y1_1 = KAREL_TO_TOP_EDGE * KAREL_SIZE / ORIGINAL_KAREL_SIZE
X1_2 = (KAREL_TO_LEFT_EDGE + KAREL_BACK_LEG_LENGTH_HORIZONTAL + KAREL_TOP_LINE_LENGTH) * \
       KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y1_2 = Y1_1
X1_3 = (ORIGINAL_KAREL_SIZE - KAREL_TO_RIGHT_EDGE) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y1_3 = (ORIGINAL_KAREL_SIZE - KAREL_RIGHT_LINE_LENGTH - KAREL_FRONT_LEG_LENGTH_VERTICAL - KAREL_TO_BOTTOM_EDGE) * \
       KAREL_SIZE / ORIGINAL_KAREL_SIZE
X1_4 = X1_3
Y1_4 = (ORIGINAL_KAREL_SIZE - KAREL_FRONT_LEG_LENGTH_VERTICAL - KAREL_TO_BOTTOM_EDGE) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
X1_5 = (KAREL_WIDOW_START_POINT_X + KAREL_WIDOW_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y1_5 = Y1_4
X1_6 = X1_5
Y1_6 = (KAREL_WIDOW_START_POINT_Y + KAREL_WIDOW_HEIGHT) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
X1_7 = X1_5
Y1_7 = KAREL_WIDOW_START_POINT_Y * KAREL_SIZE / ORIGINAL_KAREL_SIZE
X1_8 = KAREL_WIDOW_START_POINT_X * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y1_8 = Y1_7
X1_9 = X1_8
Y1_9 = Y1_6
X1_10 = X1_5
Y1_10 = Y1_6
X1_11 = X1_5
Y1_11 = Y1_4
X1_12 = (ORIGINAL_KAREL_SIZE - KAREL_TO_RIGHT_EDGE - KAREL_BOTTOM_LINE_LENGTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y1_12 = Y1_4
X1_13 = X1_1
Y1_13 = (KAREL_TO_TOP_EDGE + KAREL_LEFT_LINE_LENGTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE

X2_1 = X1_1
Y2_1 = Y1_1
X2_2 = X1_2
Y2_2 = (KAREL_TO_TOP_EDGE + KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE

X3_1 = (KAREL_TO_LEFT_EDGE + KAREL_BACK_LEG_LENGTH_HORIZONTAL + KAREL_TOP_LINE_LENGTH - math.sqrt(2) *
        KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y3_1 = Y1_1
X3_2 = X1_2
Y3_2 = Y1_1
X3_3 = X1_3
Y3_3 = Y1_3
X3_4 = X1_3
Y3_4 = (ORIGINAL_KAREL_SIZE - KAREL_RIGHT_LINE_LENGTH - KAREL_FRONT_LEG_LENGTH_VERTICAL - KAREL_TO_BOTTOM_EDGE +
        math.sqrt(2) * KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE

X4_1 = (ORIGINAL_KAREL_SIZE - KAREL_TO_RIGHT_EDGE - KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y4_1 = Y1_3
X4_2 = X1_3
Y4_2 = Y1_4

X5_1 = X1_12
Y5_1 = (ORIGINAL_KAREL_SIZE - KAREL_FRONT_LEG_LENGTH_VERTICAL - KAREL_TO_BOTTOM_EDGE - KAREL_BODY_LINE_WIDTH) * \
       KAREL_SIZE / ORIGINAL_KAREL_SIZE
X5_2 = X1_3
Y5_2 = Y1_4

X6_1 = X1_1
Y6_1 = (KAREL_TO_TOP_EDGE + KAREL_LEFT_LINE_LENGTH - math.sqrt(2) * KAREL_BODY_LINE_WIDTH) * \
       KAREL_SIZE / ORIGINAL_KAREL_SIZE
X6_2 = (ORIGINAL_KAREL_SIZE - KAREL_TO_RIGHT_EDGE - KAREL_BOTTOM_LINE_LENGTH + math.sqrt(2) * KAREL_BODY_LINE_WIDTH) * \
       KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y6_2 = Y1_4
X6_3 = X1_12
Y6_3 = Y1_4
X6_4 = X1_1
Y6_4 = Y1_13

X7_1 = X1_1
Y7_1 = Y1_1
X7_2 = (KAREL_TO_LEFT_EDGE + KAREL_BACK_LEG_LENGTH_HORIZONTAL + KAREL_BODY_LINE_WIDTH) * \
       KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y7_2 = Y1_13

X8_1 = X1_8
Y8_1 = Y1_7
X8_2 = X1_5
Y8_2 = (KAREL_WIDOW_START_POINT_Y + KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE

X9_1 = (KAREL_WIDOW_START_POINT_X + KAREL_WIDOW_WIDTH - KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y9_1 = Y1_7
X9_2 = X1_5
Y9_2 = Y1_6

X10_1 = X1_8
Y10_1 = (KAREL_WIDOW_START_POINT_Y + KAREL_WIDOW_HEIGHT - KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
X10_2 = X1_5
Y10_2 = Y1_6

X11_1 = X1_8
Y11_1 = Y1_7
X11_2 = (KAREL_WIDOW_START_POINT_X + KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y11_2 = Y1_6

X12_1 = KAREL_MOUTH_START_POINT_X * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y12_1 = KAREL_MOUTH_START_POINT_Y * KAREL_SIZE / ORIGINAL_KAREL_SIZE
X12_2 = (KAREL_MOUTH_START_POINT_X + KAREL_MOUTH_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y12_2 = (KAREL_MOUTH_START_POINT_Y + KAREL_BODY_LINE_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE

X13_1 = KAREL_TO_LEFT_EDGE * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y13_1 = KAREL_BACK_LEG_START_POINT * KAREL_SIZE / ORIGINAL_KAREL_SIZE
X13_2 = X1_1
Y13_2 = (KAREL_BACK_LEG_START_POINT + KAREL_LEG_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE

X14_1 = X13_1
Y14_1 = Y13_1
X14_2 = (KAREL_TO_LEFT_EDGE + KAREL_LEG_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y14_2 = (KAREL_BACK_LEG_START_POINT + KAREL_BACK_LEG_LENGTH_VERTICAL) * KAREL_SIZE / ORIGINAL_KAREL_SIZE

X15_1 = KAREL_FRONT_LEG_START_POINT * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y15_1 = Y1_4
X15_2 = (KAREL_FRONT_LEG_START_POINT + KAREL_LEG_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y15_2 = (ORIGINAL_KAREL_SIZE - KAREL_TO_BOTTOM_EDGE) * KAREL_SIZE / ORIGINAL_KAREL_SIZE

X16_1 = X15_1
Y16_1 = (ORIGINAL_KAREL_SIZE - KAREL_TO_BOTTOM_EDGE - KAREL_LEG_WIDTH) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
X16_2 = (KAREL_FRONT_LEG_START_POINT + KAREL_FRONT_LEG_LENGTH_HORIZONTAL) * KAREL_SIZE / ORIGINAL_KAREL_SIZE
Y16_2 = Y15_2

DELAY = 200 # parameter to control moving volecity
DELAY_TURN = 0.2 # parameter to control turning volecity


# this function returns the max of a list's value with even index.
def max_even_index(lst):
    return max(lst[::2])


# this function returns the max of a list's value with odd index.
def max_odd_index(lst):
    return max(lst[1::2])


class Karel:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        # draw text at the bottom left corner to show the score
        self.score_text = self.canvas.create_text(10, CANVAS_HEIGHT - 10, anchor='sw', text='0 beepers in the bag')
        self.score = 0
        # draw karel
        self.tuples = [(X1_1, Y1_1), (X1_2, Y1_2), (X1_3, Y1_3), (X1_4, Y1_4), (X1_5, Y1_5),
                       (X1_6, Y1_6), (X1_7, Y1_7), (X1_8, Y1_8), (X1_9, Y1_9), (X1_10, Y1_10),
                       (X1_11, Y1_11), (X1_12, Y1_12), (X1_13, Y1_13), (X2_1, Y2_1), (X2_2, Y2_2),
                       (X3_1, Y3_1), (X3_2, Y3_2), (X3_3, Y3_3), (X3_4, Y3_4), (X4_1, Y4_1),
                       (X4_2, Y4_2), (X5_1, Y5_1), (X5_2, Y5_2), (X6_1, Y6_1), (X6_2, Y6_2),
                       (X6_3, Y6_3), (X6_4, Y6_4), (X7_1, Y7_1), (X7_2, Y7_2), (X8_1, Y8_1),
                       (X8_2, Y8_2), (X9_1, Y9_1), (X9_2, Y9_2), (X10_1, Y10_1), (X10_2, Y10_2),
                       (X11_1, Y11_1), (X11_2, Y11_2), (X12_1, Y12_1), (X12_2, Y12_2), (X13_1, Y13_1),
                       (X13_2, Y13_2), (X14_1, Y14_1), (X14_2, Y14_2), (X15_1, Y15_1), (X15_2, Y15_2),
                       (X16_1, Y16_1), (X16_2, Y16_2)]
        self.draw_karel()
        # draw beeper
        self.beeper_x = random.randint(0, CANVAS_WIDTH // KAREL_SIZE - 1) * KAREL_SIZE
        self.beeper_y = random.randint(0, CANVAS_HEIGHT // KAREL_SIZE - 1) * KAREL_SIZE
        self.draw_beeper()
        # define two lists to store dx and dy, which are important parameters in canvas.move() function.
        self.dx = [0]
        self.dy = [0]
        # the initial moving direction when there's no arrow press.
        self.direction = 'Right'
        # binding the arrow keys on the keyboard to change the direction
        self.master.bind('<Left>', lambda e: self.change_direction('Left'))
        self.master.bind('<Right>', lambda e: self.change_direction('Right'))
        self.master.bind('<Up>', lambda e: self.change_direction('Up'))
        self.master.bind('<Down>', lambda e: self.change_direction('Down'))
        # the main part of this program
        self.motion()

    # draw karel using given tuples. The key point is all shapes' tags are the same.
    def draw_karel(self):
        # karel's body
        self.canvas.create_polygon(self.tuples[0], self.tuples[1], self.tuples[2], self.tuples[3],
                                   self.tuples[4], self.tuples[5], self.tuples[6], self.tuples[7],
                                   self.tuples[8], self.tuples[9], self.tuples[10], self.tuples[11],
                                   self.tuples[12], fill='magenta', tags='karel')

        # the top horizontal line of Karel
        self.canvas.create_rectangle(self.tuples[13], self.tuples[14], fill='black', tags='karel')

        # the top right slope line of Karel, the second point is the same with top line's second point
        self.canvas.create_polygon(self.tuples[15], self.tuples[16], self.tuples[17], self.tuples[18], tags='karel')

        # the right vertical line of Karel, the second point is the same with the top right slope line's third point
        self.canvas.create_rectangle(self.tuples[19], self.tuples[20], fill='black', tags='karel')

        # the bottom horizontal line of Karel
        self.canvas.create_rectangle(self.tuples[21], self.tuples[22], fill='black', tags='karel')

        # the bottom left slope line of Karel, the third point is the same with the bottom horizontal line's
        # fourth point
        self.canvas.create_polygon(self.tuples[23], self.tuples[24], self.tuples[25], self.tuples[26], tags='karel')

        # the left vertical line of Karel, the third point is the same with the bottom left slope line's fourth point
        self.canvas.create_rectangle(self.tuples[27], self.tuples[28], fill='black', tags='karel')

        # the top line of the screen/window
        self.canvas.create_rectangle(self.tuples[29], self.tuples[30], fill='black', tags='karel')

        # the right line of the screen/window
        self.canvas.create_rectangle(self.tuples[31], self.tuples[32], fill='black', tags='karel')

        # the bottom line of the screen/window
        self.canvas.create_rectangle(self.tuples[33], self.tuples[34], fill='black', tags='karel')

        # the left line of the screen/window
        self.canvas.create_rectangle(self.tuples[35], self.tuples[36], fill='black', tags='karel')

        # the mouth of Karel
        self.canvas.create_rectangle(self.tuples[37], self.tuples[38], fill='black', tags='karel')

        # the back horizontal leg of Karel
        self.canvas.create_rectangle(self.tuples[39], self.tuples[40], fill='black', tags='karel')

        # the back vertical leg of Karel
        self.canvas.create_rectangle(self.tuples[41], self.tuples[42], fill='black', tags='karel')

        # the front vertical leg of Karel
        self.canvas.create_rectangle(self.tuples[43], self.tuples[44], fill='black', tags='karel')

        # the front horizontal leg of Karel
        self.canvas.create_rectangle(self.tuples[45], self.tuples[46], fill='black', tags='karel')

    def draw_beeper(self):
        self.canvas.create_rectangle(self.beeper_x, self.beeper_y, self.beeper_x + KAREL_SIZE,
                                     self.beeper_y + KAREL_SIZE, tags='beeper', width=0)
        self.canvas.create_polygon(self.beeper_x + KAREL_SIZE / 2, self.beeper_y, self.beeper_x + KAREL_SIZE,
                                   self.beeper_y + KAREL_SIZE / 2, self.beeper_x + KAREL_SIZE / 2,
                                   self.beeper_y + KAREL_SIZE, self.beeper_x, self.beeper_y + KAREL_SIZE / 2,
                                   fill='deep sky blue', tags='beeper')

    def change_direction(self, direction):
        self.direction = direction

    def motion(self):
        # if facing direction is not the same with self.direction, turn right then get dx, dy and update to the list respectively.
        # if the same, get dx, dy and update to the list respectively
        if self.direction == 'Left':
            if self.facing_direction() != 'Left':
                self.turn_right()
            dx, dy = -KAREL_SIZE, 0
            self.dx.append(dx)
            self.dy.append(dy)
        elif self.direction == 'Right':
            if self.facing_direction() != 'Right':
                self.turn_right()
            dx, dy = KAREL_SIZE, 0
            self.dx.append(dx)
            self.dy.append(dy)
        elif self.direction == 'Up':
            if self.facing_direction() != 'Up':
                self.turn_right()
            dx, dy = 0, -KAREL_SIZE
            self.dx.append(dx)
            self.dy.append(dy)
        elif self.direction == 'Down':
            if self.facing_direction() != 'Down':
                self.turn_right()
            dx, dy = 0, KAREL_SIZE
            self.dx.append(dx)
            self.dy.append(dy)

        self.canvas.move('karel', dx, dy)
        # update the tuples after each move
        self.tuples_after_move()
        # check the boundaries. when karel runs out of canvas stop the game.
        shape_coordinates = self.canvas.coords('karel')
        if max_even_index(shape_coordinates) < 0 or max_odd_index(shape_coordinates) < 0 or max_even_index(
                shape_coordinates) > CANVAS_WIDTH or max_odd_index(shape_coordinates) > CANVAS_HEIGHT:
            self.canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2,
                                    text=f'Game Over! {self.score} beepers in the bag.', fill='magenta')
            return
        # check if there's beeper. if so pick the beeper.
        item_coordinates = self.canvas.coords('beeper')
        objs = self.canvas.find_overlapping(*item_coordinates)
        if len(objs) >= 18:
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f'{self.score} beepers in the bag')
            new_x, new_y = random.randint(0, CANVAS_WIDTH // KAREL_SIZE - 1) * KAREL_SIZE, \
                random.randint(0, CANVAS_HEIGHT // KAREL_SIZE - 1) * KAREL_SIZE
            self.canvas.moveto('beeper', new_x, new_y)
        self.master.after(DELAY, self.motion)

    def facing_direction(self):
        tuple_list = self.canvas.coords('karel')
        if self.tuples[2][0] == max_even_index(tuple_list) and self.tuples[3][1] == max_odd_index(tuple_list):
            return 'Right'
        elif self.tuples[0][0] == max_even_index(tuple_list) and self.tuples[2][1] == max_odd_index(tuple_list):
            return 'Down'
        elif self.tuples[0][0] == max_even_index(tuple_list) and self.tuples[0][1] == max_odd_index(tuple_list):
            return 'Left'
        elif self.tuples[3][0] == max_even_index(tuple_list) and self.tuples[0][1] == max_odd_index(tuple_list):
            return 'Up'

    # keep turning right until the facing direction is the same with self.direction.
    def turn_right(self):
        while self.direction != self.facing_direction():
            # get the new tuples
            self.tuples_after_turn()
            # delete the karel with previous facing direction
            self.canvas.delete('karel')
            # draw karel based on the new tuples
            self.draw_karel()
            # update canvas immediately, so we can see the process of turning.
            self.canvas.update()
            time.sleep(DELAY_TURN)

    def tuples_after_turn(self):
        for index, a_tuple in enumerate(self.tuples):
            x, y = a_tuple
            new_x = KAREL_SIZE - (y - sum(self.dy)) + sum(self.dx)
            new_y = x - sum(self.dx) + sum(self.dy)
            self.tuples[index] = (new_x, new_y)
        return self.tuples

    def tuples_after_move(self):
        for index, a_tuple in enumerate(self.tuples):
            x, y = a_tuple
            new_x = x + self.dx[-1]
            new_y = y + self.dy[-1]
            self.tuples[index] = (new_x, new_y)
        return self.tuples


root = tk.Tk()
game = Karel(root)
root.mainloop()
