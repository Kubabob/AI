import random
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name: str, distance_from_club: int = 100) -> None:
        self.name = name
        self.distance = 0
        self.time_since_started = 0
        self.distance_from_home = distance_from_club
        self.distance_from_club = distance_from_club
        self.path_history = {}


    def step(self) -> None:
        probability_of_step = random.randint(1, 10)


        if 1 <= probability_of_step <= 5:
            self.distance += 1
            self.distance_from_home -= 1
            self.path_history[self.time_since_started] = self.distance
        elif 6 <= probability_of_step <= 8:
            self.path_history[self.time_since_started] = self.distance
        else:
            self.distance -= 1
            self.distance_from_home += 1
            self.path_history[self.time_since_started] = self.distance

        self.time_since_started += 1

    def next_party(self) -> None:
        self.distance = 0
        self.time_since_started = 0
        self.distance_from_home = self.distance_from_club
        self.path_history = {}


def simulation(object: Student, size_of_simulation: int) -> float:
    simulation_chart = {}

    for simulation_index in range(1, size_of_simulation+1):
        while object.distance_from_home > 0:
            object.step()
        else:
            simulation_chart[simulation_index] = object.time_since_started
            object.next_party()
    else:
        plt.plot(simulation_chart.keys(), simulation_chart.values())
        plt.show()

    return sum(simulation_chart.values())/size_of_simulation

if __name__ == '__main__':
    
    Kuba = Student(name='Kuba')

    print(f'Mean number of steps: {simulation(Kuba, 10)}')

    


    

    
    