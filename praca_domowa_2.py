import random
import matplotlib.pyplot as plt
import time

class Student:
    def __init__(self, name: str, is_taking_break: bool) -> None:
        self.name = name
        self.xpos = 0
        self.ypos = 0
        self.steps = 0
        self.path_history = {}
        self.is_taking_break = is_taking_break
        self.forwards = 0
        self.pause = 0
        self.backwards = 0
        self.ratio = []

    
    def step_OX(self) -> None:
        probability_of_step = random.randint(1, 10)
        self.steps += 1

        if 1 <= probability_of_step <= 5:
            self.xpos += 1
            self.path_history[self.steps] = (self.xpos, self.ypos)
            self.forwards += 1
        elif 9 <= probability_of_step <= 10:
            self.xpos -= 1
            self.path_history[self.steps] = (self.xpos, self.ypos)
            self.backwards += 1

        else:
            if self.is_taking_break:
                self.path_history[self.steps] = (self.xpos, self.ypos)
                self.pause += 1
            else: 
                self.steps -= 1
                pass
            

    def step_OY(self) -> None:
        probability_of_step = random.randint(1, 10)
        self.steps += 1

        if 1 <= probability_of_step <= 5:
            self.ypos += 1
            self.path_history[self.steps] = (self.xpos, self.ypos)
            self.forwards += 1
        elif 9 <= probability_of_step <= 10:
            self.ypos -= 1
            self.path_history[self.steps] = (self.xpos, self.ypos)
            self.backwards += 1
        else:
            if self.is_taking_break:
                self.path_history[self.steps] = (self.xpos, self.ypos)
                self.pause += 1
            else: 
                self.steps -= 1
                pass

    def decide_direction(self) -> None:
        if random.randint(0, 1) == 0:
            self.step_OX()
        else:
            self.step_OY()

    def next_party(self) -> None:
        self.xpos = 0
        self.ypos = 0
        self.steps = 0
        self.path_history = {}
        self.choice_history = {}
        self.forwards = 0
        self.pause = 0
        self.backwards = 0
        #self.steps
        

class Simulation:
    def __init__(self, object: Student, size_of_simulation: int, position_of_home: tuple, is_comparison: bool=False) -> None:
        self.object = object
        self.size_of_simulation = size_of_simulation
        self.position_of_home = position_of_home
        self.is_comparison = is_comparison
        

    def chart(self):
        simulation_chart = {}

        for simulation_index in range(1, self.size_of_simulation+1):
            while (self.object.xpos, self.object.ypos) != self.position_of_home:
                self.object.decide_direction()
                #print(f'Position: {(object.xpos, object.ypos)}')
                if self.object.xpos > 1.1*self.position_of_home[0] or self.object.ypos > 1.1*self.position_of_home[1]:
                    self.object.next_party()
                    #print(f'Obiekt {self.object.name} nie dotarł do domu')
                    pass
            else:
                simulation_chart[simulation_index] = self.object.steps
                self.object.ratio.append((self.object.forwards, self.object.pause, self.object.backwards))
                self.object.next_party()
        else:
            if self.is_comparison:
                return (sum(simulation_chart.values())/self.size_of_simulation), simulation_chart#, self.object.ratio
            else:
                #plt.plot(simulation_chart.keys(), simulation_chart.values())
                plt.hist(simulation_chart.values())
                plt.show()
                return (sum(simulation_chart.values())/self.size_of_simulation)
            
    

        
class Comparison:
    def __init__(self, object1: Student, object2: Student, size_of_simulation: int, position_of_home: tuple) -> None:
        self.object1 = object1
        self.object2 = object2
        self.size_of_simulation = size_of_simulation
        self.position_of_home = position_of_home
        pass

    def comparison_mean_steps(self):
        simulation1 = Simulation(self.object1, self.size_of_simulation, self.position_of_home, True)
        plt.subplot(2, 1, 1)
        chart1: dict = simulation1.chart()[1]
        plt.plot(chart1.keys(), chart1.values())

        simulation2 = Simulation(self.object2, self.size_of_simulation, self.position_of_home, True)
        plt.subplot(2, 1, 2)
        chart2: dict = simulation2.chart()[1]
        plt.plot(chart2.keys(), chart2.values())

        for i in range(self.size_of_simulation):
            print(f'{i+1}. Ratio1: {self.object1.ratio[i]};     F/P: {round(self.object1.ratio[i][0]/self.object1.ratio[i][1], 2)};     P/B: {round(self.object1.ratio[i][1]/self.object1.ratio[i][2], 2)};     F/B: {round(self.object1.ratio[i][0]/self.object1.ratio[i][2], 2)}    Ratio2: {self.object2.ratio[i]};      F/B: {round(self.object2.ratio[i][0]/self.object2.ratio[i][2], 2)}')
            
        print(f'Mean steps1: {simulation1.chart()[0]}   Mean steps2: {simulation2.chart()[0]}')

        plt.show()



if __name__ == '__main__':
    Kuba = Student(name='Kuba', is_taking_break=True)
    Jan = Student(name='Jan', is_taking_break=False)

    comparison = Comparison(Kuba, Jan, 20, (100, 100))
    comparison.comparison_mean_steps()

    '''
    Notki:
    Wzrost F/P i F/B przy jednoczesnym spadku P/B daje korzystne wyniki
####### zla hipoteza
    1. przypadek przerw:
        ~2 F/P przy ~1.5 P/B i ~3.5 F/B oznacza prog 250 krokow 
        R = (F/P + F/B) / P/B
        250:
        -0.03 +0.05 -0.4 R=-8.6
        -0.15 +0.2 -0.3 R=-2.25
        +0.1 -0.1 -0.6 R=4
        300:
        -0.6 +0.8 -0.3 R=-1.125
        -0.25 +0.2 -0.5 R=-3.75
        -0.15 -0.1 -0.9 R=-10.5
        350:
        -0.7 +0.35 -0.9 R=-0.56
        -0.45 +0.05 -1.1 R=-31
        -0.4 +0 -1.1 R=-150
        400:
        -0.35 -0.3 -1.5 R=6
        0 -0.45 -1.4 R=3
        -0.5 -0.09 -1.35 R=20
########
    1. przypadek brania przerw:
        im wiecej F/B tym nizsza liczba krokow, wiecej F/P bedzie dawalo nizsza liczbe krokow niz P/B przy tym samym F/B
        ~3 F/B ~2 F/P okolo 250 krokow 
        ~3 F/B ~2 P/B okolo 300 krokow

        roznica F/B i F/P mniejsza o ~0.5 da ~100 wiecej krokow


    2. przypadek nie brania przerw:
        im wieksze ratio F/B tym mniej krokow, prog okolo 2.9/3.0 to prog ponizej 300 krokow, im blizej 4.0 tym blizej 250 krokow, ~2.5 350 krokow
    2.1. hipoteza:
        roznica F/B o 0.5-1 oznacza skok o 50 krokow
    '''


