#calculadora de probabilidad por aproximación a grandes números
import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self,**colors):
        self.contents = list()

        for k,v in colors.items():
            i=0
            while i <v :
                self.contents.append(k)                
                i+=1
            
    def __str__ (self):
        return  str(self.contents)           

        

    def draw(self,number_to_draw):
        i=0
        self.removed_balls = list()    
        if number_to_draw > len(self.contents):
            number_to_draw = len(self.contents)
        while i <  number_to_draw:

            r_index= random.randrange(len(self.contents))
            self.removed_balls.append(self.contents[r_index])
            self.contents.pop(r_index)            
            
            i+=1

        
        return self.removed_balls

#################################################################### 


def check_results(actual, expected):    
    # counter = 0
    # expected_copy = copy.deepcopy(expected)
    # actual_copy = copy.deepcopy(actual)
    # print('actual pre bucle',actual)
    # print('expected pre bucle', expected)

    # for item in actual_copy:
    #     item_temp =actual_copy[actual.index(item)]      

    #     print('actual',actual_copy)

    #     if item_temp in expected_copy:
    #         counter += 1
    #         expected_copy.pop(expected_copy.index(item_temp))
    #         actual_copy.pop(actual.index(item))
    #         print('expected post pop', expected_copy)
    #         print('actual post pop', actual_copy)

    #     else: continue
    #     if len(expected_copy) == 0 : break

    # if counter == len (expected_copy) : return True
    # else: return False


    actual_copy = copy.deepcopy(actual)
    expected_copy = copy.deepcopy(expected)
    flag = True
    for item in expected_copy:
        if item in actual_copy:
            actual_copy.pop(actual_copy.index(item))
        else: flag = False
    return flag

            




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
   
    M=0  

    for _ in range(num_experiments):      
        
        new_hat= copy.deepcopy(hat)     
        new_hat.draw(num_balls_drawn)

        expected_balls_list = list()
        
       

        for k,v in expected_balls.items():
            i=0
            while i <v :
                expected_balls_list.append(k)                
                i+=1   

      
        
        if check_results(new_hat.removed_balls,expected_balls_list)== True: M+=1
        
    
    probability =  M / num_experiments
   
    return probability

###############################################################################

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
actual = probability
expected = 0.272
print(actual)
print(expected)

# hat = Hat(black=6, red=4, green=3)

# probability = experiment(hat=hat, 
#                   expected_balls={"red":2,"green":1,'black':1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)
# print(probability)