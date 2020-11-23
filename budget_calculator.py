import decimal

class Category:

    name=''
    ledger = list()
    def __init__ (self, name_in):
        self.name=name_in.capitalize()
        self.ledger=list()
        

    def get_balance(self):
        balance = list()
        if len(self.ledger) <1: return 0

        for item in self.ledger:
            balance.append(item['amount'])
        
        return sum(balance)

    def check_funds(self,amount):
        if amount <= self.get_balance(): return True
        else: return False        

    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount,'description':description})
        
    
    def withdraw(self,amount,description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({'amount':- amount,'description':description})
            return True
        else: return False   

    def transfer(self,amount,receiver):        
        self.withdraw(amount,'Transfer to '+ receiver.name)
       
        receiver.deposit(amount,'Transfer from '+self.name)
        return True

    def get_withdrawls(self):
        withdrawls = 0
        for item in self.ledger:
            if item['amount'] < 0:
                withdrawls += item['amount']
        return withdrawls

    def __str__(self):     
        item_string = str()
        title_string=self.name.center(30).replace(' ','*')

        for item in self.ledger: 
            #item_string = item_string + item['description'][:23].center(23).lstrip()+str(item['amount'])[:7].center(7).rstrip()+'\n'
            description_string = item['description'][:23]
            while len(description_string)<23: description_string= description_string + ' '
            #amount_string = str(item['amount'])[:7]
            number_format = item['amount']
            amount_string= str(f'{number_format:7.2f}')   
            item_string +=description_string + amount_string + '\n'

        end_string = 'Total: '+ str(self.get_balance())

        
        
        return title_string +'\n'+ item_string+end_string
        
    
                  

########################################################

def round_int(number):
    mult=10
    return int(number*mult)/ mult

def get_total_withdrawls(categories):

    total = 0 
    withdrawls = list()
    

    for category in categories:
        total += category.get_withdrawls()
        withdrawls.append(category.get_withdrawls())
        
    # for withdrawl in withdrawls:
    #     percentages.append(round_int(withdrawls[withdrawl]/total)
    rounded = list(map(lambda x: round_int(x/total), withdrawls))
    return rounded

    
    
    

def create_spend_chart(categories):
    title = 'Percentage spent by category\n'
    grid=title +''
    percentages = get_total_withdrawls(categories)

    for i in range(100,0,-10):
        grid_unit = ' '
        for percentage in percentages :
            if percentage *100 >=i:
                grid_unit+='o  '
            else: grid_unit += '   '
        grid +=  str(i).rjust(3)+'|'+grid_unit+'\n'
    
    result_line = '-' + len(categories)*'---'
    category_name=list()
    name_grid = ''
    for category in categories:
        category_name.append(category.name)

    biggest = max(category_name,key=len)

    for i in range (len(biggest)):
        name_str = '     '

        for name in category_name:
            if i >= len(name):
                name_str+= '   '
            else: name_str += name[i] + '  '
            
        name_str += '\n'
        name_grid += name_str
    name_grid = name_grid[:len(name_grid)-1]

    grid += result_line.rjust(len(result_line)+4) + '\n' + name_grid
    return grid 
 
    


########################################################


# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")

# clothing = Category("Clothing")

# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)


# auto =Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)


#print(food)
#print(clothing)
food = Category('food')
entertainment=Category('entertainement')
business = Category('business')




food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

print(actual)
print(expected)
if actual==expected: print('bien')
else:print('mal')

print('len actual',len(actual),'len expected', len(expected))

for letter in range(len(actual)-1) :
    if actual[letter] == expected[letter]:
        continue
    else: print (expected[letter])