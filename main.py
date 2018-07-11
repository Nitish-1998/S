from default import spy
import sys

##==============================================Add friends================================================================
def add_friend():
    new_friend = {'name' : ' ',
                  'sal'  : ' ',
                  'age'  : ' ',
                  'rating' : ' '
                  }
    new_friend['name'] = input('Enter your friend name : ')
    new_friend['sal'] = input('Enter your friend salutation: ')
    new_friend['age'] = int(input('Enter your friend age : '))
    new_friend['rating'] = float(input('Enter your rating : '))
    #new_name = input('Enter your friend name: ')
    #new_age = int(input('Enter your friend age: '))
    #new_rating = float(input('Enter your ratings: '))
#    present_status = True
    if len(new_friend['name']) > 0 and new_friend['name'].isalpha() and new_friend['age']>=13 and new_friend['age']<=60:
        friends.append(new_friend['name'])
        friends.append(new_friend['sal'])
        friends.append(new_friend['age'])
        friends.append(new_friend['rating'])
        friends.append(True)
        #print("%s succesfully added as your friend." %new_name)
    else:
        print("your entered details dosen't match with ur friend ")

    return len(friends)
#===============================================Start_chat function========================================================
def start_chat(spy):

    current_status_message = None
    t = None
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
            t = add_friend()
            #print("%s succesfully added as your friend" %friends[len(new_friend['name']) - 1]
            print("You have %d total friends now" %t)
        elif menu_choice == 0:
            show_menu = False
            sys.exit()
        else:
            print('Invalid choice\nplease try again..!!')

#===============================================Add_Status function=======================================================
def add_status(current_status_message):

    if current_status_message !=  None:

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
           updated_status_message = STATUS_MSG[status_sel - 1]

       else:
           print('You have entered an invalid choice')

    else:
           print('Invalid Choice')

    return updated_status_message

#===============================================Main program=========================================================
question= 'Do you want to continue with ur default user(y/n)? '
choice=input(question)
friends=[]
STATUS_MSG = ["busy","gym","can't talk"]                                        #Status message listS
if choice =='Y' or choice == 'y':
    start_chat(spy)

elif choice =='N' or choice =='n':

    print('Welcome to spychat \nYou must tell me your name first.')
    spy['name'] = input('Enter your name:')
    if len(spy['name'])>0 and spy['name'].isalpha():
        spy['salutation'] = input('Hello ' +spy['name'] + ' What should i call u (Mr/Miss?):')
        spy['name'] = spy['salutation'] + ' ' + spy['name']
        print('Welcome '+ spy['name'] +' I need some more details before you get started ' )
        spy['age'] = input('Enter ur Age: ')
        spy['age'] = int(spy['age'])
        if  spy['age']>13 and spy['age']<60:
            spy['rating'] = input('Enter ur Ratings: ')
            spy['rating'] = float(spy['rating'])
            if spy['rating']<5.0:
                print('Profile created succesfully \nName: ' +spy['name']  + ' \nAge: ' +str(spy['age'])  + ' \nRating: ' +str(spy['rating']) )
                print('Proud to have you onboard')
                start_chat(spy)

            else:
                print("Invalid ratings")
        else:
            print("Sorry!You Age are not able to create  account")
    else:
        print("Sorry!Please enter a valid name")

else:
    print('Sorry! Invalid choice')
