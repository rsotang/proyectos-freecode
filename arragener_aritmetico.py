def arithmetic_arranger(problems,mode=False):

    #the function takes a list of numeric strings as argument
    #we have to take each element of the list, parse it, and create different
    #case for each element

    #first, error checking for too many problesms 
    if len(problems) > 5: return 'Error: Too many problems.'  

    #second, the actual work done by the function

    line1=str()
    line2=str()
    total_line=str()
    solution_line=str()   

    for problem in problems:       

        element = problem.split() #separate the operation based on whitespace      
       
       #error checking for operator
        if not element[1] == '+': 
            if not element[1] == '-':
                return 'Error: Operator must be \'+\' or \'-\'.'      
       

        op1=element[0]
        op2=element[2]
        result_line=''

        if mode == True:

            if element[1] == '+':
                solution = int(op1) + int(op2)

            else: solution = int(op1) - int(op2)
            solution = str(solution)
        

        #error checking for digits and length of numbers 

        if len(op1)>4 or len(op2)>4 : return 'Error: Numbers cannot be more than four digits.'

        if op1.isnumeric() is not True or op2.isnumeric() is not True: return 'Error: Numbers must only contain digits.'       

        #print(element,op1,op2) #debugging

        if len(op1)> len(op2):             
            op1 = '  ' + op1             

            while len(op2)< len(op1)-1:
                op2 = ' ' + op2

            op2 = element[1] + op2                          

            for i in range(len(op2)):
                result_line= result_line + '-' 

            if mode == True:
                while len(solution) < len(result_line):
                    solution = ' ' + solution                        


        elif len(op2)> len(op1): 

            op2= ' '+ op2
            op2 = element[1] + op2 

            while len(op1)< len(op2):
                op1 = ' ' + op1

            for i in range(len(op1)):
                result_line= result_line + '-'
            
            if mode == True:
                while len(solution) < len(result_line):
                    solution = ' ' + solution

        else : 
            op2= ' '+ op2
            op2 = element[1] + op2 

            while len(op1)<len(op2):
                op1 = ' ' + op1

            for i in range(len(op1)):
                result_line= result_line +'-'

            if mode == True:
                while len(solution) < len(result_line):
                    solution= ' ' + solution

        line1 = line1 + op1 + '    '
        line2 = line2 + op2 + '    '
        total_line= total_line + result_line + '    '

        if mode==True:
            solution_line = solution_line+ solution+ '    '
        
        if mode == True:
            arranged_problems = line1.rstrip() +'\n' + line2.rstrip() +'\n' + total_line.rstrip() +'\n' + solution_line.rstrip()  
        else:  arranged_problems = line1.rstrip() +'\n' + line2.rstrip() +'\n' + total_line.rstrip()

    return arranged_problems

actual = arithmetic_arranger(['3 + 855','3801 - 2','45 + 43','123 + 49'] )
print(actual)
expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"

if actual == expected: print ('correcto')
else : print ('caca')
