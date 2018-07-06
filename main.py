from default import spy_name, spy_age, spy_rating
import sys

#===============================================Start_chat function========================================================
def start_chat(spy_name,spy_age,spy_rating):

    current_status_message = None
    show_menu = True

    while show_menu == True:

        menu ="""===============Menu=================
                 1.Status update.
                 2.Add friend.
                 0.exit.
                 Enter your choice: """
        menu_choice=int(input(menu))
        if menu_choice==1:
            print('You select to update status')
            current_status_message = add_status(current_status_message)
            print('You have set %s as your status'%current_status_message)
        elif menu_choice==2:
            print('You select to add friend')
        elif menu_choice == 0:
            show_menu = False
            sys.exit()
        else:
            print('Invalid choice\nplease try again..!!')

#===============================================Add_Status function=======================================================
def add_status(current_status_message):

    if current_status_message!= None:

        print('Your status is \n %s'%current_status_message)
    else:
        print('You don\'t have any current status')
    default = input('Do you want to select from older/default status  (y/n)?')  #asking user choice
    if default.upper() == 'N':
       new_status_message = input('What on your mind?')                         #reading new status

       if len(new_status_message) > 0:                                          #validation
          updated_status_message = new_status_message
          STATUS_MSG.append(updated_status_message)                             #Append Status
       else:
          print('You have not entered anything \n please try again')

    elif default.upper() == 'Y':
       item_pos = 1
       for msg in STATUS_MSG:
           print(str(item_pos) + '. ' +  msg)
           item_pos = item_pos + 1

       status_sel = int(input('Enter the status of your choice: '))

       if status_sel <= len(STATUS_MSG):
           updated_status_message = STATUS_MSG[item_pos - 1]

       else:
          print('You have entered an invalid choice')

    else:
          print('Invalid Choice')

    return updated_status_message

#===============================================Main program=========================================================
question= 'Do you want to continue with ur default user(y/n)? '
choice=input(question)
STATUS_MSG = ["busy","gym","can't talk"]                                        #Status message listS
if choice =='Y' or choice == 'y':
    start_chat(spy_name,spy_age,spy_rating)

elif choice =='N' or choice =='n':

    print('Welcome to spychat \nYou must tell me your name first.')
    spy_name = input('Enter your name:')
    if len(spy_name)>0 and spy_name.isalpha():
        spy_salutation = input('Hello ' +spy_name + ' What should i call u (Mr/Miss?):')
        spy_name = spy_salutation + ' ' + spy_name
        print('Welcome '+ spy_name +' I need some more details before you get started ' )
        spy_age = input('Enter ur Age: ')
        spy_age = int(spy_age)
        if  spy_age>13 and spy_age<60:
            spy_rating = input('Enter ur Ratings: ')
            spy_rating = float(spy_rating)
            if spy_rating<5.0:
                print('Profile created succesfully \nName: ' +spy_name  + ' \nAge: ' +str(spy_age)  + ' \nRating: ' +str(spy_rating) )
                print('Proud to have you onboard')
                start_chat(spy_name,spy_age,spy_rating)

            else:
                print("Invalid ratings")
        else:
            print("Sorry!You Age are not able to create  account")
    else:
        print("Sorry!Please enter a valid name")

else:
    print('Sorry! Invalid choice')
