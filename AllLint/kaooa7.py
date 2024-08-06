"""kaooa implementation"""
import turtle
import math as m

dictionary = {
    "1": {
        "nn": [4, 5],
        "snn": [2, 8]
    },
    "2": {
        "nn": [7, 4, 9, 6],
        "snn": [1, 3],
    },
    "3": {
        "nn": [9, 8],
        "snn": [2, 5]
    },
    "4": {
        "nn": [2, 1, 6, 5],
        "snn": [10, 7],
    },
    "5": {
        "nn": [4, 8, 10, 1],
        "snn": [3, 6],
    },
    "6": {
        "nn": [2, 4],
        "snn": [9, 5],
    },
    "7": {
        "nn": [2, 9],
        "snn": [8, 4],
    },
    "8": {
        "nn": [9, 5, 3, 10],
        "snn": [7, 1],
    },
    "9": {
        "nn": [7, 8, 2, 3],
        "snn": [6, 10]
    },
    "10": {
        "nn": [8, 5],
        "snn": [9, 4]
    }
}


def option_choices(vulture1):
    """optionchoices"""
    index = intersected_list.index(vulture1[-1])
    return dictionary[f"{index+1}"]["nn"], dictionary[f"{index+1}"]["snn"]


def intersection_point(point1, point2):
    """intersecting point"""
    x_1, y_1 = point1[0]
    x_2, y_2 = point1[1]
    x_3, y_3 = point2[0]
    x_4, y_4 = point2[1]
    m_line1 = (y_2 - y_1) / (x_2 - x_1)
    b_line1 = y_1 - m_line1 * x_1
    m_line2 = (y_4 - y_3) / (x_4 - x_3)
    b_line2 = y_3 - m_line2 * x_3
    x_intersection = (b_line2 - b_line1) / (m_line1 - m_line2)
    y_intersection = m_line1 * x_intersection + b_line1
    return x_intersection, y_intersection


def fill_circle(color, list1, extra=False):
    """circle filling"""
    if not extra:
        length = len(list1)
        tur.fillcolor(color)
        tur.begin_fill()
        tur.circle(30)
        tur.end_fill()
        tur.penup()
        tur.goto(list1[-1])
        tur.pendown()
        tur.write(length, align="center", font=("Arial", 12, "normal"))
    if extra:
        # print(list1[0])
        tur.penup()
        tur.goto(intersected_list[list1[0]-1])
        tur.right(90)
        tur.fd(30)
        tur.left(90)
        tur.pendown()
        tur.fillcolor(color)
        tur.begin_fill()
        tur.circle(30)
        tur.end_fill()
        tur.penup()
        tur.goto(intersected_list[list1[0]-1])
        tur.pendown()
        # tur.write(first_index+1, align="center", font=("Arial", 12, "normal"))
        tur.write(list1[0], align="center", font=("Arial", 12, "normal"))


def draw_circle(tur1, list1, vulture1, crow1, click_count1,
                occupied_array1, index1, kill_count, selected1,
                change1=False, change2=False, change3=False, change4=False):
    """draw_circle"""
    # length=len(list1)
    tur1.penup()
    tur1.goto(list1[-1])
    tur1.right(90)
    tur1.fd(30)
    tur1.left(90)
    tur1.pendown()
    if change1:
        print("sfd")
        if len(vulture) == 2:
            print("2")
            first_index = intersected_list.index(vulture[0])
            fill_circle("#59b4c3", list1)
            tur1.penup()
            tur1.goto(vulture[0])
            tur1.right(90)
            tur1.fd(30)
            tur1.left(90)
            tur1.pendown()
            tur1.fillcolor("#99bc85")
            tur1.begin_fill()
            tur1.circle(30)
            tur1.end_fill()
            tur1.penup()
            tur1.goto(vulture[0])
            tur1.pendown()
            tur1.write(first_index+1, align="center",
                      font=("Arial", 12, "normal"))
            vulture1.pop(0)
            occupied_array1[first_index] = 0
            # option_choices(tur,vulture,crow)
        elif len(vulture) == 1:
            print("1")
            fill_circle("#59b4c3", list1)
            option_choices(vulture1)
    elif change2:
        print("sfdd")
        if click_count[0] >= 0:
            # print("rishabh")
            fill_circle("#E78895", list1)
    elif change3:
        print("sfddd")
        first_index = intersected_list.index(vulture1[0])
        fill_circle("#59b4c3", list1)
        tur1.penup()
        tur1.goto(vulture[0])
        tur1.right(90)
        tur1.fd(30)
        tur1.left(90)
        tur1.pendown()
        tur1.fillcolor("#99bc85")
        tur1.begin_fill()
        tur1.circle(30)
        tur1.end_fill()
        tur1.penup()
        tur1.goto(vulture[0])
        tur1.pendown()
        tur1.write(first_index+1, align="center", font=("Arial", 12, "normal"))
        vulture.pop(0)
        occupied_array1[first_index] = 0
        # index=find_desired_index(vulture,crow)
        # print(index1-1)
        tur1.penup()
        tur1.goto(intersected_list[index1-1])
        tur1.right(90)
        tur1.fd(30)
        tur1.left(90)
        tur1.pendown()
        tur1.fillcolor("#99bc85")
        tur1.begin_fill()
        tur1.circle(30)
        tur1.end_fill()
        tur1.penup()
        tur1.goto(intersected_list[index1-1])
        tur1.pendown()
        tur1.write(index1, align="center", font=("Arial", 12, "normal"))
    elif change4:
        # print("sohan")
        print("sfdddd")
        a_a = []
        a_a.append(selected[0])
        print(a_a)
        b_b = []
        b_b.append(selected[1])
        print(b_b)
        fill_circle("#99bc85", a_a, True)
        fill_circle("#E78895", b_b, True)
    else:
        fill_circle("#99bc85", list1)
    tur1.speed(0)
    tur1.hideturtle()


def all_empty(occupied_array, choice, choice1, vulture):
    # print("imp")
    # print(choice)e
    """"empty choice"""
    print(choice)
    for ele in choice:
        flag = 1
        if occupied_array[ele-1] == 2:
            for ele1 in dictionary[f"{ele}"]["nn"]:
                print(ele1)
                if ele1 in choice1:
                    if occupied_array[ele1-1] == 2:
                        print("sohangupta")
                        flag = 1
                        # return True
                    if occupied_array[ele1-1] == 0:
                        print("sohanmaupa")
                        flag = 0
                        return False
                        # return False
    if flag == 1:
        for ele in choice:
            if occupied_array[ele-1] == 0:
                print("sohan gupta")
        return True
    return False


def in_circle(x, y, tur, flag, vulture, crow, click_count,
              occupied_array, crows_filled, crows_count,
              selected, index4):
    """in_circle"""
    for i in range(len(intersected_list)):
        # print(crows_filled[0],flag[0])
        if ((m.sqrt((x-intersected_list[i][0])**2+(y-intersected_list[i][1])**2)) < 30.0
                and flag[0] == 1 and occupied_array[i] == 0):
            # print(i)
            # print("aaaaa")
            if len(vulture) == 1:
                print("aaaaaa")
                choice, choice1 = option_choices(vulture)  # print("skdnmf")
                neighbour_choice = dictionary[f"{i+1}"]["nn"]
                index3 = intersected_list.index(vulture[-1])
                another_choice = dictionary[f"{index3+1}"]["nn"]
                for ele in neighbour_choice:
                    for ele1 in another_choice:
                        if ele == ele1:
                            to_search = ele
                print(choice1)
                print(i+1)
                if i+1 in choice1:
                    # print("sohan")
                    neighbour_choice = dictionary[f"{i+1}"]["nn"]
                    index3 = intersected_list.index(vulture[-1])
                    another_choice = dictionary[f"{index3+1}"]["nn"]
                    for ele in neighbour_choice:
                        for ele1 in another_choice:
                            if ele == ele1:
                                to_search = ele
                    if occupied_array[to_search-1] == 2:
                        # imp_flag=1
                        # print("sohnq1")
                        vulture.append(intersected_list[i])
                        draw_circle(tur, intersected_list[:(i+1)], vulture,
                                    crow, click_count, occupied_array, to_search, kill_count,
                                    selected, False, False, True)
                        flag[0] = 0
                        occupied_array[i] = 1
                        occupied_array[to_search-1] = 0
                        click_count[0] += 1
                        kill_count[0] += 1
                        crows_count[0] -= 1
                        if kill_count[0] >= 4:
                            tur.clear()
                            tur.write("Vulture Wins", font=(
                                "Arial", 36, "italic"))
                        return True
                elif i+1 in choice and occupied_array[i] == 0 and all_empty(occupied_array,
                                                                            choice, choice1,
                                                                            vulture):
                    print("sjdfknfed")
                    vulture.append(intersected_list[i])
                    draw_circle(tur, intersected_list[:(i+1)], vulture,
                                crow, click_count, occupied_array, 0,
                                kill_count, selected, True, False)
                    flag[0] = 0
                    occupied_array[i] = 1
                    occupied_array[to_search-1] = 0
                    click_count[0] += 1
                    return True
            else:
                # print("govind")
                vulture.append(intersected_list[i])
                draw_circle(tur, intersected_list[:(i+1)], vulture,
                            crow, click_count, occupied_array, 0, kill_count,
                            selected, True, False)
                flag[0] = 0
                occupied_array[i] = 1
                click_count[0] += 1
                return True
        if ((m.sqrt((x-intersected_list[i][0])**2+(y-intersected_list[i][1])**2)) < 30.0 and
                flag[0] == 0 and occupied_array[i] == 0 and len(crow) <= crows_count[0]):
            crow.append(intersected_list[i])
            draw_circle(tur, intersected_list[:(i+1)], vulture, crow,
                        click_count, occupied_array, 0, kill_count, selected, False, True)
            flag[0] = 1
            click_count[0] += 1
            occupied_array[i] = 2
            if crows_count[0] == len(crow):
                crows_filled[0] = 1
            return True
        if (m.sqrt((x-intersected_list[i][0])**2+(y-intersected_list[i][1])**2) < 30.0 and
                flag[0] == 0 and crows_filled[0] == 1):
            # flag1=0
            if (occupied_array[i] == 2) and len(selected) == 0:
                selected.append(i+1)
                index4.append(crow.index(intersected_list[i]))
            if len(selected) == 1 and occupied_array[i] == 0:
                selected.append(i+1)
            if len(selected) == 2:
                print("draw")
                choice = dictionary[f"{selected[0]}"]["nn"]
                if selected in choice:
                    draw_circle(tur, intersected_list[:(i+1)], vulture, crow,
                                click_count, occupied_array, 0, kill_count,
                                selected, False, False, False, True)
                # flag1=0
                    print(index4)
                    crow[index4[0]] = intersected_list[selected[1]-1]
                    selected = []
                    index4 = []
                    flag[0] = 1
                else:
                    selected = []
                    index4 = []
                    print("Not current moment")


def win_crow(vulture1, crow1):
    if (len(vulture1) > 0 and len(crow1) > 0):
        index1 = intersected_list.index(vulture1[-1])
        choice1, choice2 = dictionary[f"{index1+1}"]["nn"], dictionary[f"{index1+1}"]["snn"]
        flag = 0
        for ele in choice1:
            if occupied_array[ele-1] != 2:
                flag = 1
        for ele1 in choice2:
            if occupied_array[ele1-1] != 2:
                flag = 1
        if flag == 0:
            return True
        else:
            return False
    else:
        return False


def on_screen_click(x_x, y_y):
    """on_screen_click"""
    if in_circle(x_x, y_y, tur, flag, vulture, crow, click_count,
                 occupied_array, crows_filled, crows_count, selected, index4):
        # print("circle clicked")
        # print(flag)
        pass
    if win_crow(vulture, crow):
        tur.clear()
        tur.write("Crow Wins", font=("Arial", 36, "italic"))





class StarCase:
    """defining star class"""

    def __init__(self):
        self.screen = turtle.getscreen()
# screen.tracer(0)
        self.screen.bgcolor("#e1f0da")
        self.tur2=turtle.Turtle();
        self.tur2.penup()
        self.tur2.goto(-50, +340)
        self.tur2.pendown()
        self.tur2.write("The Kaooa Game", font=("Arial", 20, "bold"))
        self.tur2.hideturtle()
        self.tur = turtle.Turtle()
        self.tur.penup()
        self.tur.goto(-180, 100)
        self.list1_points = []
        self.list1_points.append((-180, 100))
        # draw_circle(list1_points)
        self.tur.pendown()
        self.tur.speed(0)

    def draw_star(self):
        self.tur.width(3)
        self.tur.pencolor("#123728")
        self.tur.fd(450)
        self.list1_points.append(self.tur.position())
        self.tur.left(36)
        self.tur.bk(450)
        self.list1_points.append(self.tur.position())
        self.tur.left(36)
        self.tur.fd(450)
        self.list1_points.append(self.tur.position())
        self.tur.left(36)
        self.tur.bk(450)
        self.list1_points.append(self.tur.position())
        self.tur.left(36)
        self.tur.fd(450)
        return self.tur, self.list1_points


flag = [0]
selected = []
click_count = [0]
kill_count = [0]
crows_filled = [0]
crows_count = [7]
index4 = []
occupied_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
obj = StarCase()
tur, list1_points = obj.draw_star()
list1_list = []
for i in range(1, len(list1_points)):
    list1_list.append([list1_points[i-1], list1_points[i]])
list1_list.append((list1_points[-1], list1_points[0]))
intersected_list = []
for j in range(5):
    for k in range(j):
        intersected_list.append(
            (intersection_point(list1_list[j], list1_list[k])))


# print(intersected_list)
vulture = []
crow = []
for i in range(1, len(intersected_list)+1):
    tur.speed(0)
    draw_circle(tur, intersected_list[:i], vulture,
                crow, click_count, occupied_array, 0, kill_count, selected)

turtle.onscreenclick(on_screen_click)
turtle.mainloop()
# turtle.done()
