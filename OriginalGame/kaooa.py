import turtle
import math as m

dictionary = {
    "0":{"nn":[4,3],"snn":[7,1]},
    "1":{"nn":[8,3,6,5],"snn":[0,2]},
    "2":{"nn":[7,8],"snn":[1,4]},
    "3":{"nn":[1,4,0,5],"snn":[9,6]},
    "4":{"nn":[9,3,0,7],"snn":[2,5]},
    "5":{"nn":[1,3],"snn":[4,8]},
    "6":{"nn":[8,1],"snn":[7,3]},
    "7":{"nn":[2,9,8,4],"snn":[6,0]},
    "8":{"nn":[2,7,1,6],"snn":[9,5]},
    "9":{"nn":[7,4],"snn":[8,3]}
}
class IntersectionUtils:
    @staticmethod
    def intersection_point(line1, line2):
        (x1, y1), (x2, y2) = line1
        (x3, y3), (x4, y4) = line2
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return None
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        return px, py

class Gameboard:
    def __init__(self):
        self.screen = turtle.getscreen()
        self.screen.bgcolor("#e1f0da")
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.occupied_array = [0] * 10
        self.intersected_list = []
        self.initialize_game()

    def initialize_game(self):
        self.set_up_board()
        self.draw_star()
        self.draw_circle()

    def set_up_board(self):
        self.turtle.penup()
        self.turtle.goto(-50, 340)
        self.turtle.pendown()
        self.turtle.write("The Kaooa Game", font=("Arial", 20, "bold"))
        self.turtle.penup()
        self.turtle.goto(-180, 100)
        self.turtle.pendown()
        self.turtle.speed(0)

    def draw_star(self):
        self.turtle.width(3)
        self.turtle.pencolor("#123728")
        list1_points = []
        self.turtle.fd(450)
        for i in range(5):
            if i % 2 == 0:
                list1_points.append(self.turtle.position())
                self.turtle.left(36)
                self.turtle.bk(450)
            else:
                list1_points.append(self.turtle.position())
                self.turtle.left(36)
                self.turtle.fd(450)
        self.list1_list = [(list1_points[i - 1], list1_points[i]) for i in range(1, len(list1_points))]
        self.list1_list.append((list1_points[-1], list1_points[0]))
        self.calculate_intersections(self.list1_list)

    def calculate_intersections(self, lines):
        for j in range(len(lines)):
            for k in range(j):
                    intersection = IntersectionUtils.intersection_point(lines[j], lines[k])
                    if intersection:
                        self.intersected_list.append(intersection)

    def fill_circle(self, color, intersection,num):
        # print(color)
        # print(intersection)
        # print(num)
        self.turtle.penup()
        self.turtle.goto(intersection)
        self.turtle.setheading(270) 
        self.turtle.forward(30)  
        self.turtle.setheading(0)  
        self.turtle.pendown()
        self.turtle.fillcolor(color)
        self.turtle.write(num,align="center",font=("Arial",12,"normal"))
        self.turtle.begin_fill()
        self.turtle.circle(30) 
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.goto(intersection[0], intersection[1] - 10)
        self.turtle.setheading(0)
        self.turtle.pendown()
        self.turtle.write(num, align="center", font=("Arial", 12, "normal"))
    def draw_circle(self):
        for i in range(len(self.intersected_list)):
            self.fill_circle("#99bc85", self.intersected_list[i],i)
        self.turtle.speed(0)
        self.turtle.hideturtle()

class Player:
    def __init__(self, name, color, occupied_array, intersected_list):
        self.name = name
        self.color = color
        self.positions = []
        self.index=[]
        self.occupied_array = occupied_array
        self.intersected_list = intersected_list
    def make_move(self, index):
        print(len(self.positions),self.name)
        if len(self.positions)==1 and self.name=="vulture": 
            # print(1)
            self.occupied_array[index]=1
            print("sab")
            return True
        elif self.occupied_array[index] == 0:
            self.occupied_array[index] = 1 if self.name == "vulture" else 2
            self.positions.append(self.intersected_list[index])
            self.index.append(index)
            return True
        return False
    def draw_move(self, i,color=False):
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(self.intersected_list[i])
        turtle.pendown()
        if color:
            turtle.dot(60,color)
        else:
            turtle.dot(60,self.color)
        turtle.penup()
        turtle.goto(self.intersected_list[i])
        turtle.setheading(270)  
        turtle.forward(10)  
        turtle.setheading(0)  
        turtle.pendown()
        turtle.write(i, align="center", font=("Arial", 12, "normal"))

class KaooaGame:
    def __init__(self):
        self.board = Gameboard()
        self.vulture = Player("vulture", "#59b4c3", self.board.occupied_array, self.board.intersected_list)
        self.crow = Player("crow", "#E78895", self.board.occupied_array, self.board.intersected_list)
        self.current_player = self.vulture
        self.kill_count=0
        turtle.onscreenclick(self.on_screen_click)
    def start_game(self):
        turtle.mainloop()
    def on_screen_click(self, x, y):
        if self.in_circle(x, y):
            if self.win_crow():
                turtle.clearscreen()
                turtle.write(f"{self.current_player.name.capitalize()} Wins", align="center",font=("Arial", 36, "italic"))
                turtle.hideturtle()
            else:
                self.switch_turns()
    def in_index(self,value):
        for i in range(len(self.board.intersected_list)):
            if (self.board.intersected_list[i]==value):
                return i
        return -1
    def in_circle(self, x, y):
        for i, point in enumerate(self.board.intersected_list):
            if m.sqrt((x - point[0]) ** 2 + (y - point[1]) ** 2) < 30.0:
                # print(self.current_player.name)
                # print(self.current_player.positions)
                # print(self.current_player.make_move(i))
                if self.current_player.name=="vulture"  and self.current_player.make_move(i) and len(self.current_player.positions)==1:
                    # print('sabe')
                    fni=dictionary[str(self.current_player.index[-1])]["nn"]
                    sni=dictionary[str(self.current_player.index[-1])]["snn"]
                    self.board.occupied_array[self.current_player.index[-1]]=0
                    self.current_player.draw_move(self.current_player.index[-1],"#99bc85")
                    self.current_player.index.pop(-1)
                    self.current_player.index.append(i)
                    self.current_player.positions.pop(-1)
                    self.current_player.positions.append(self.board.intersected_list[i])
                    if i in sni:
                        for j in range(len(fni)):
                            if self.board.occupied_array[fni[j]]==2:
                                self.board.occupied_array[fni[j]]=0
                                self.current_player.draw_move(fni[j],"#99bc85")
                                ind=self.in_index(self.board.intersected_list[fni[j]])
                                print(ind)
                                value=self.board.intersected_list[ind]
                                self.crow.positions.remove(value)
                                self.crow.index.remove(ind)
                                self.current_player.draw_move(i)
                                self.kill_count+=1
                                return True
                    else:
                        # print("sa")
                        self.current_player.draw_move(i)
                        return True
                elif self.current_player.make_move(i):
                    self.current_player.draw_move(i)
                    return True
        return False
    def win_crow(self):
        if len(self.vulture.positions) > 0 and len(self.crow.positions) > 0:
            index1 = self.board.intersected_list.index(self.vulture.positions[-1])
            choice1, choice2 = dictionary[f"{index1}"]["nn"], dictionary[f"{index1}"]["snn"]
            if all(self.board.occupied_array[ele - 1] == 2 for ele in choice1) and \
               all(self.board.occupied_array[ele - 1] == 2 for ele in choice2):
                return True
        if self.kill_count==4:
            return True
        return False

    def switch_turns(self):
        self.current_player = self.crow if self.current_player == self.vulture else self.vulture

game = KaooaGame()
game.start_game()
