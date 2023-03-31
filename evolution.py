from praca_domowa_2 import Student
import os
import sys
import matplotlib.pyplot as plt
import time


def logic_gate(a, b):
    if a and not b:
        return False
    elif not a and b:
        return False
    elif not a and not b:
        return False
    elif a and b:
        return True

class Path_finder:
    def __init__(self, reach_position: tuple, test_object: Student) -> None:
        self.reach_position = reach_position
        self.test_object = test_object
        self.deaths = 0
        self.wins = 0
        self.perfect_try = {}
        self.personal_best = sum(reach_position)*2
        self.max_best = sum(reach_position)
        self.best_tries = 0
        self.is_done = False
        pass

    def algoritm(self) -> None:
        start_time = time.time()
        # self.personal_best > self.max_best:
        while logic_gate((self.best_tries < 2), (self.personal_best > self.max_best)):
            while (self.test_object.xpos, self.test_object.ypos) != self.reach_position:
                self.test_object.decide_direction()
                if self.personal_best == self.max_best:
                    
                    pass
                if self.test_object.xpos > 1.1*self.reach_position[0] or self.test_object.ypos > 1.1*self.reach_position[1]:
                    self.test_object.next_party()
                    self.deaths += 1
                    self.show_actual_parameters()
                
            else:
                self.wins += 1
                if self.test_object.steps == self.personal_best:
                    #self.personal_best = self.test_object.steps
                    self.best_tries += 1
                    self.perfect_try = self.test_object.path_history
                    self.test_object.next_party()
                    self.deaths += 1
                    self.show_actual_parameters()
                elif self.test_object.steps < self.personal_best:
                    self.personal_best = self.test_object.steps
                    self.perfect_try = self.test_object.path_history
                    self.best_tries = 1
                    self.test_object.next_party()
                    self.deaths += 1
                    self.show_actual_parameters()
                else:
                    #self.best_tries = 0
                    self.test_object.next_party()
                    self.deaths += 1
                    self.show_actual_parameters()
                

        else:
            #self.perfect_try = self.test_object.path_history
            #self.is_done = True
            self.show_actual_parameters()
            end_time = time.time()
            sys.stdout.write(f'Nauczony!\n')
            sys.stdout.write(f'Zajęło to: {round((end_time-start_time)/60, 2)} minut i {round((end_time-start_time)%60, 2)} sekund\n')
            with open(file='perfect_try.txt', mode='w') as perfect_try:
                perfect_try.write(str(self.perfect_try))

            coords = [coord for coord in self.perfect_try.values()]
            #print(coords)
            x_coords = [x_coord[0] for x_coord in coords[:]]
            y_coords = [y_coord[1] for y_coord in coords[:]]
            #print(x_coords)
            #print(y_coords)
            plt.scatter(x_coords, y_coords)
            plt.show()
            #self.show_actual_parameters()
            
            
                

    def show_actual_parameters(self):
        clear = lambda: os.system('cls')
        clear()
        sys.stdout.write(f'Personal best: {self.personal_best}\n')
        sys.stdout.write(f'Deaths: {self.deaths}\n')
        sys.stdout.write(f'Wins: {self.wins}\n')
        sys.stdout.write(f'Best tries: {self.best_tries}\n')
        sys.stdout.flush()
        
        

def main():
    Kuba = Student('Kuba', False)
    evolution = Path_finder(reach_position=(10, 10), test_object=Kuba)
    
    evolution.algoritm()

if __name__ == '__main__':
    main()


