from default import Spy
from default import s
from default import friends
import sys
from steganography.steganography import Steganography
import csv
##################### Load friend ##########################################################################################
def load_friends():
    with open('db.csv','rb') as frnd_data:
        reader = csv.reader(frnd_data)
        for row in reader:
            new_friend = Spy(row[0] , row[1] , row[2] , row[3])
            friends.append(new_friend)
################################################ Select_a_friend ##########################################################
def Select_a_friend():
    item_num = 0
    for frnd in friend:
        print('%d. %s'%(item_num +1,frnd.name))
        item_num = item_num +1
    friend_choice = int(input('Enter a friend of your choice:  '))
    frnd_pos = friend_choice - 1
    return frnd_pos
############################################## Send Message ##############################################################
def send_message():
    friend_choice = Select_a_friend()
    original_img = raw_input("Enter the name of your image: ")
    output_path = "output.jpg"
    text  = raw_input("Enter your secreat message: ")
    Steganography.encode(original_img , output_path , text)
    print("Your message has been send successfully")
############################################# Read message ####################################################################
def read_message():
    sender = Select_a_friend()
    output_path = raw_input('What is the name of your file: ')
    secret_text = Steganography.decode(output_path)
    print(friends[sender].name + " : " + secret_text)

##==============================================Show friends ==============================================================
def show():
    for ele in friends:
        print(ele.name)
##==============================================Add friends================================================================
def add_friend():
    new_friend = Spy("", "" , 0, 0.0)
    new_friend.name  = raw_input('Enter your friend name : ')
    new_friend.salutation = raw_input('Enter your friend salutation: ')
    new_friend.age  = int(input('Enter your friend age : '))
    new_friend.rating = float(input('Enter your rating : '))

    #new_name = input('Enter your friend name: ')
    #new_age = int(input('Enter your friend age: '))
    #new_rating = float(input('Enter your ratings: '))
#    present_status = True
    if len(new_friend.name) > 0 and new_friend.name.isalpha() and new_friend.age>=13 and new_friend.age<=60:
        friends.append(new_friend)
        with open('db.csv','a') as frnd_data:
            writer = csv.writer(frnd_data)
            writer.writerow([new_friend.name , new_friend.salutation , new_friend.age , new_friend.rating])
        #print("%s succesfully added as your friend." %new_name)
    else:
        print("your entered details dosen't match with ur friend ")

    return len(friends)
#===============================================Start_chat function========================================================
def start_chat(s):

    #current_status_message = None
    t = None
    show_menu = True
    a = None

    while show_menu == True:

        menu ="""===============Menu=================
                 1.Status update.
                 2.Add friend.
                 3.Show friends.
                 4.Send message.
                 5.Read message
                 0.exit.
                 Enter your choice: """
        menu_choice=int(input(menu))
        if menu_choice==1:
            print('You select to update status')
            s.current_status_message = add_status(s.current_status_message)
            print('You have set %s as your status'%s.current_status_message)
        elif menu_choice==2:
            print('You select to add friend')
            t = add_friend()
            print("%s succesfully added as your friend" %friends[len(friends)-1].name)
            print("You have %d total friends now" %t)
        elif menu_choice == 3:
            print('You have selected to Show friends')
            a = show()
        elif menu_choice == 4:
            send_message()
        elif menu_choice == 5:
            read_message()
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
    default = raw_input('Do you want to select from older/default status  (y/n)?')  #asking user choice
    if default.upper() == 'N':
       new_status_message = raw_input('What on your mind?')                         #reading new status

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
choice=raw_input(question)
STATUS_MSG = ["busy","gym","can't talk"]                                        #Status message listS
if choice =='Y' or choice == 'y':
    start_chat(s)

elif choice =='N' or choice =='n':

    print('Welcome to spychat \nYou must tell me your name first.')
    s.name = raw_input('Enter your name:')
    if len(s.name)>0 and s.name.isalpha():
        s.name = raw_input('Hello ' +s.name + ' What should i call u (Mr/Miss?):')
        s.name = s.salutation + ' ' + s.name
        print('Welcome '+ s.name +' I need some more details before you get started ' )
        s.age = input('Enter ur Age: ')
        s.age = int(s.age)
        if s.age>13 and s.age<60:
            s.rating = input('Enter ur Ratings: ')
            s.rating = float(s.rating)
            if s.rating<5.0:
                print('Profile created succesfully \nName: ' +s.name  + ' \nAge: ' +str(s.age)  + ' \nRating: ' +str(s.rating) )
                print('Proud to have you onboard')
                start_chat(s)

            else:
                print("Invalid ratings")
        else:
            print("Sorry!You Age are not able to create  account")
    else:
        print("Sorry!Please enter a valid name")

else:
    print('Sorry! Invalid choice')
