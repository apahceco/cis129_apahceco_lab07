




from decimal import Decimal


def main():
    #

    QUIT = 0
    while QUIT == 0:
        A = 0
        A_TOTAL_SEAT = 300
        A_PRICE = 20
        a_total_income = 0
        a_counter = 0 
        a_ticket_left = A_TOTAL_SEAT - a_counter

        B = 0
        B_TOTAL_SEAT = 500
        B_PRICE = 15
        b_total_income = 0
        b_counter = 0
    
        b_ticket_left = B_TOTAL_SEAT - b_counter

        C = 0
        C_TOTAL_SEAT = 200
        C_PRICE = 10
        c_total_income = 0
        c_counter = 0
        c_ticket_left = C_TOTAL_SEAT - c_counter

        get_dash()
        print('Welcome, to Who Named it Theater!!\n')
        print('You can run this program in 2 way.\nFirst way is to gather total number of ticket sold in each section to calculate total income.\n Second way is to enter ticket as they are sold.')

    
        QUIT = program('Enter (-99) To quit this program.\nEnter (1) To get total amount of ticket for each section and calculate total income.\nEnter (2) To enter tickets as you go.\n')
        get_dash()
        while QUIT == 1 or QUIT == 'no':
            get_dash()
            print('\n')
            
            a_counter, a_total_income = total_section_a(a_counter,a_total_income,A_PRICE,A_TOTAL_SEAT)
            get_dash()
            print('\n')
            
            b_counter, b_total_income = total_section_b(b_counter,b_total_income,B_PRICE,B_TOTAL_SEAT)
            get_dash()
            print('\n')
            
            c_counter, c_total_income = total_section_c(c_counter,c_total_income,C_PRICE,C_TOTAL_SEAT)
            get_dash()
            print('\n')
            
            QUIT = yes_no('Do you want to end this program? (yes/no): ')
            if QUIT == 'no':
                get_dash()
                print('\n')
                results(a_counter,b_counter,c_counter,a_total_income,b_total_income,c_total_income)
                    


           
            
        while QUIT == 2 or QUIT == 'no':
            
            get_dash()
            print('Enter (-99) To quit this program.')
            
            print(f'Ticket for section A are ${A_PRICE} per seat.\nThere are currently {a_ticket_left} seats left in section A.\n')
            
            print(f'Ticket for section B are ${B_PRICE} per seat.\nThere are currently {b_ticket_left} seats left in section B.\n')

            print(f'Ticket for section C are ${C_PRICE} per seat.\nThere are currently {c_ticket_left} seats left in section C.\n')
            
            user_input = get_section('Please, enter the letter of which sections that you would like to seat in. (A, B, or C): ')

            if user_input.lower() == 'a':
                
                a_counter,a_ticket_left, a_total_income = section_a(a_counter,a_ticket_left,a_total_income,A_PRICE,A_TOTAL_SEAT)
                
            elif user_input.lower() == 'b':

                b_counter,b_ticket_left,b_total_income = section_b(b_counter,b_ticket_left,b_total_income,B_PRICE,B_TOTAL_SEAT)

            elif user_input.lower() == 'c':

                c_counter,c_ticket_left,c_total_income = section_c(c_counter,c_ticket_left,c_total_income,C_PRICE,C_TOTAL_SEAT)
                
            else:
                QUIT = yes_no('Do you want to end this program? (yes/no): ')
                if QUIT == 'no':
                    get_dash()
                    print('\n')
                    results(a_counter,b_counter,c_counter,a_total_income,b_total_income,c_total_income)
                    a_counter = 0
                    a_total_income = 0
                    a_ticket_left = A_TOTAL_SEAT - a_counter
                    b_counter = 0
                    b_total_income = 0
                    b_ticket_left = B_TOTAL_SEAT - b_counter
                    c_counter = 0
                    c_total_income = 0
                    c_ticket_left = C_TOTAL_SEAT - c_counter
                               
                
        get_dash()
        results(a_counter,b_counter,c_counter,a_total_income,b_total_income,c_total_income)
        get_dash()
    
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------

def total_section_a(a_counter,a_total_income,A_PRICE,A_TOTAL_SEAT):
    #
    while True:
        try:
            print('Enter (-99) for zero and no entry.')
            a_counter = get_positive_integer('How many ticket were sold in section A?: ')
            
            if a_counter == -99 :
                a_counter = 'No Entry'
                a_total_income = 0.00
                print(f'Total income for section A is ${a_total_income:0.2f}')
                return a_counter, a_total_income
            elif a_counter <= A_TOTAL_SEAT :
                a_total_income = Decimal(a_counter * A_PRICE)
                print(f'Total income for section A is ${a_total_income:0.2f}')
                return a_counter, a_total_income
               
            else:
                a_counter = A_TOTAL_SEAT - a_counter
                over_stack = a_counter * -1
                print('Incorrect data entered. Section A only has',A_TOTAL_SEAT,'seats avaliable. Your are over by',over_stack ,'seats.')
        except ValueError:
            print(a_counter)
            print('Incorrect Data entered, please re-attempt')



                   
def section_a(a_counter,a_ticket_left,a_total_income,A_PRICE,A_TOTAL_SEAT):
    
    get_dash()
    print('There are',a_ticket_left, 'seats left.\n')
    print(f'Ticket for section A are ${A_PRICE:0.2f} per seat.\n')
        
        
    while a_counter <= A_TOTAL_SEAT:

        if a_ticket_left == 0:
            print('Sorry, there are no more ticket avaibale in this section.')
            return a_counter, a_ticket_left, a_total_income 

        a_ticket = get_positive_integer('How many ticket would you like to purshase?')

        if a_ticket == -99:
            return a_counter, a_ticket_left, a_total_income 
     
        a_counter += a_ticket
        
        a_ticket_left = A_TOTAL_SEAT - a_counter

        print(a_ticket_left)
        print(a_counter)
        
        over_stack = a_ticket_left * -1
        while a_counter > A_TOTAL_SEAT:

            a_counter -= a_ticket
            a_ticket_left = A_TOTAL_SEAT + a_counter

            print('Sorry, your over by',over_stack ,' seat.')
            print('If you would like to choose another section (enter -99).\nIf not, please try again. The number of seat remaining are',a_ticket_left)
            a_ticket = get_positive_integer('How many ticket would you like to purshase?')
            
            a_counter += a_ticket
            a_ticket_left = A_TOTAL_SEAT - a_counter

            print(a_ticket_left)
            print(a_counter)
            print(a_ticket)
            
        total_price = Decimal(a_ticket * A_PRICE)
        print(f'You\'er total is ${total_price:0.2f}')            
        a_total_income += total_price
        
        
        return a_counter, a_ticket_left, a_total_income



#----------------------------------------------------------------------------------------------------------------------------------------------------------
def total_section_b(b_counter,b_total_income,B_PRICE,B_TOTAL_SEAT):
    #This will calculate 
    while True:
        try:
            b_counter = get_positive_integer('How many ticket were sold in section B?: ')
            if b_counter == -99:
                b_counter = 'No Entry'
                b_total_income = 0.00
                print(f'Total income for section B is ${b_total_income:0.2f}')
                return b_counter, b_total_income
            elif b_counter <= B_TOTAL_SEAT :
                b_total_income = Decimal(b_counter * B_PRICE)
                print(f'Total income for section B is ${b_total_income:0.2f}')
                return b_counter, b_total_income
                
            else:
                b_counter = B_TOTAL_SEAT - b_counter
                over_stack = b_counter * -1
                print('Incorrect data entered. Section B only has',B_TOTAL_SEAT,'seats avaliable. Your over by',over_stack ,'seats.')
        except ValueError:
            print('Incorrect Data entered, please re-attempt')

        

def section_b(b_counter,b_ticket_left,b_total_income,B_PRICE,B_TOTAL_SEAT):

    get_dash()
    print('There are',b_ticket_left, 'seats left.\n')
    print(f'Ticket for section B are ${B_PRICE:0.2f} per seat.\n')
        
        
    while b_counter <= B_TOTAL_SEAT:

        if b_ticket_left == 0:
            print('Sorry, there are no more ticket avaibale in this section.')
            return b_counter, b_ticket_left, b_total_income

        b_ticket = get_positive_integer('How many ticket would you like to purshase?')

        if b_ticket == -99:
            return b_counter, b_ticket_left, b_total_income
        
        total_price = Decimal(b_ticket * B_PRICE)

        print(f'You\'er total is ${total_price:0.2f}')
            
        b_counter += b_ticket
        
        b_ticket_left = B_TOTAL_SEAT - b_counter
        
        print(b_ticket_left)
        print(b_counter)

        over_stack = b_ticket_left * -1
        while b_counter > B_TOTAL_SEAT:

            b_counter -= b_ticket
            b_ticket_left = B_TOTAL_SEAT + b_counter

            print('Sorry, your over by',over_stack ,' seat.')
            print('If you would like to choose another section (enter -99).\nIf not, please try again. The number of seat remaining are',b_ticket_left)
            b_ticket = get_positive_integer('How many ticket would you like to purshase?')
            
            b_counter += b_ticket
            b_ticket_left = B_TOTAL_SEAT - b_counter

            print(b_ticket_left)
            print(b_counter)

        total_price = Decimal(b_ticket * B_PRICE)
        print(f'You\'er total is ${total_price:0.2f}')            
        b_total_income += total_price
            
                
                
        return b_counter, b_ticket_left, b_total_income

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def total_section_c(c_counter,c_ticket_left,c_total_income,C_PRICE,C_TOTAL_SEAT):
    #
    while True:
        try:
            c_counter = get_positive_integer('How many ticket were sold in section C?: ')
            if c_counter == -99:
                c_counter = 'No Entry'
                c_total_income = 0.00
                print(f'Total income for section C is ${c_total_income:0.2f}')
                return c_counter, c_total_income, c_total_income
            
            elif c_counter <= C_TOTAL_SEAT:
                c_total_income = Decimal(c_counter * C_PRICE)
                print(f'Total income for section C is ${c_total_income:0.2f}')
                return c_counter, c_total_income, c_total_income
            else:
                c_counter = C_TOTAL_SEAT - c_counter
                over_stack = c_counter * -1
                print('Incorrect data entered. Section C only has',C_TOTAL_SEAT,'seats avaliable. Your over by',over_stack ,'seats.')
        except ValueError:
            print('Incorrect Data entered, please re-attempt')



def section_c(c_counter,c_ticket_left,c_total_income,C_PRICE,C_TOTAL_SEAT):

    get_dash()
    print('There are',c_ticket_left, 'seats left.\n')
    print('Ticket for section C are',C_PRICE,'per seat.\n')
        
        
    while c_counter <= C_TOTAL_SEAT:

        if c_ticket_left == 0:
            print('Sorry, there are no more ticket avaibale in this section.')
            return c_counter, c_ticket_left,c_total_income

        c_ticket = get_positive_integer('How many ticket would you like to purshase?')

        if c_ticket == -99:
            return c_counter, c_ticket_left,c_total_income
        
        total_price = Decimal(c_ticket * C_PRICE)

        print(f'You\'er total is ${total_price:0.2f}')
            
        c_counter += c_ticket
        
        c_ticket_left = C_TOTAL_SEAT - c_counter
        
        print(c_ticket_left)
        print(c_counter)

        over_stack = c_ticket_left * -1
        while c_counter > C_TOTAL_SEAT:

            c_counter -= c_ticket
            c_ticket_left = C_TOTAL_SEAT + c_counter

            print('Sorry, your over by',over_stack ,' seat.')
            print('If you would like to choose another section (enter -99).\nIf not, please try again. The number of seat remaining are',c_ticket_left)
            c_ticket = get_positive_integer('How many ticket would you like to purshase?')
            
            c_counter += c_ticket
            c_ticket_left = C_TOTAL_SEAT - c_counter

            print(c_ticket_left)
            print(c_counter)
        total_price = Decimal(c_ticket * C_PRICE)
        print(f'You\'er total is ${total_price:0.2f}')            
        c_total_income += total_price
                
                
        return c_counter, c_ticket_left, c_total_income

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def get_integer(message):
    #Getting a interger 
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print('Incorrect Data entered, please re-attempt')



def get_section(message):
    #validating user input to getting section vaule 
    while True:
        user_input = input(message)
        if user_input.lower() == 'a':
            return user_input
        elif user_input.lower() == 'b':
            return user_input
        elif user_input.lower() == 'c':
            return user_input
        elif user_input == '-99':
            return user_input
        else:
            print('Error, invailed enetry')   
    return user_input



def get_positive_integer(message):
    # Getting positive interger with the exseption of -99 to quit
    while True:
        try:
            user_input = int(input(message))
            if user_input == -99 or user_input > 1:
                return user_input
            elif user_input > 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
            
            
def program(message):
    # validating user input to getting program value to run each section  
    while True:
        try:
            user_input = int(input(message))
            if user_input == 1 or user_input == 2 or user_input == -99:
                return user_input
            else:
                print('Error, invailded entery.')
        except ValueError:
            print("Please enter a valid entry (1, 2, or -99).")

def main_program(message):
       # validating user input to getting program value to run each section  
    while True:
        try:
            user_input = int(input(message))
            if user_input == 0 or user_input == 1:
                return user_input
            elif user_input == -99:
                return user_input
            else:
                print('Error, invailded entery.')
        except ValueError:
            print("Please enter a valid entry (1, 2, or -99).")


def yes_no(message):
    # This validate user input for yes or no to run program again
    while True:
        try:
            user_input = input(message)
            if user_input.lower() == 'no' or user_input.lower() == 'yes':
                return user_input
        except ValueError:
            print('Error, please enter (yes or no)!')
            
def results(a_counter,b_counter,c_counter,a_total_income,b_total_income,c_total_income):
    # Display results
    print(f'The total amount of ticket sold for section A were {a_counter}.\nWith a total income of ${a_total_income:0.2f}')
    print(f'The total amount of ticket sold for section B were {b_counter}.\nWith a total income of ${b_total_income:0.2f}')
    print(f'The total amount of ticket sold for section C were {c_counter}.\nWith a total income of ${c_total_income:0.2f}')
    total_ticket = a_counter + b_counter + c_counter
    total_income = a_total_income + b_total_income + c_total_income
    print(f'The total amount of ticket sold {total_ticket} and total income is ${total_income:0.2f}')
    return 

def get_dash():
    #print dashes for separation 
    for row in range(2):
        get_dash = print('-' * 60)
    return 



main()

QUIT = main_program('\nAre you sure you want to quit.\n\nEnter (0) To run program again.\nEnter (-99) To quit this program.\n')
if QUIT == 0:
    main()
else:
    print('Thank you, have a great day!\n See you next time!')







    
