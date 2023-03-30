import random
import matplotlib.pyplot as plt
import time

class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.xpos = 0
        self.ypos = 0
        self.time_since_started = 0
        self.path_history = {}

    
    def step_OX(self) -> None:
        probability_of_step = random.randint(1, 10)
        self.time_since_started += 1

        if 1 <= probability_of_step <= 5:
            self.xpos += 1
            self.path_history[self.time_since_started] = (self.xpos, self.ypos)
        elif 6 <= probability_of_step <= 8:
            self.path_history[self.time_since_started] = (self.xpos, self.ypos)
        else:
            self.xpos -= 1
            self.path_history[self.time_since_started] = (self.xpos, self.ypos)

    def step_OY(self) -> None:
        probability_of_step = random.randint(1, 10)
        self.time_since_started += 1

        if 1 <= probability_of_step <= 5:
            self.ypos += 1
            self.path_history[self.time_since_started] = (self.xpos, self.ypos)
        elif 6 <= probability_of_step <= 8:
            self.path_history[self.time_since_started] = (self.xpos, self.ypos)
        else:
            self.ypos -= 1
            self.path_history[self.time_since_started] = (self.xpos, self.ypos)

    def decide_direction(self) -> None:
        if random.randint(0, 1) == 0:
            self.step_OX()
        else:
            self.step_OY()

    def next_party(self) -> None:
        self.xpos = 0
        self.ypos = 0
        self.time_since_started = 0
        self.path_history = {}


def simulation(object: Student, size_of_simulation: int, position_of_home: tuple) -> float:
    simulation_chart = {}

    for simulation_index in range(1, size_of_simulation+1):
        while (object.xpos, object.ypos) != position_of_home:
            object.decide_direction()
            #print(f'Position: {(object.xpos, object.ypos)}')
            if object.xpos > 1.2*position_of_home[0] or object.ypos > 1.2*position_of_home[1]:
                object.next_party()
                print(f'Obiekt {object.name} nie dotarł do domu')
                pass
        else:
            simulation_chart[simulation_index] = object.time_since_started
            object.next_party()
    else:
        plt.plot(simulation_chart.keys(), simulation_chart.values())
        plt.show()

    return sum(simulation_chart.values())/size_of_simulation


if __name__ == '__main__':
    Kuba = Student(name='Kuba')

    print(f'Mean number of steps: {simulation(object=Kuba, size_of_simulation=20, position_of_home=(20, 20))}')


