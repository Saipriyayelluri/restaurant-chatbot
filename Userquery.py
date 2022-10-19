import re
import random
import time


def query():
    print("!!!!!!=======================================!!!!!!")
    # Greeting the user
    list1 = ["Hi ! I'm Sophia welcome to our lord of fried restaurant",
             "Hi ! I'm Angelina welcome to our restaurant LOF", "Hi! I'm Julee its refreshing to our restaurant",
             "Hi !  I'm Riya welcome to lord of  fried restaurant"]
    print(random.choice(list1))
    time.sleep(1)
    # creating a list to hold the compliments to the username
    list2 = ["Its a great name", "I loved your name", "It's such a good name", "wow its a nice name"]
    # asking the name of the user
    name = str(input("What is your name?\n ", ))
    while (name == " " or len(name) < 0 or not name.isalpha()):
        user_input = input('Please enter valid name (I think name must contain alphabets )')
        name = user_input
        pass
    print(random.choice(list2))  # Giving compliments mentioned in list2
    print("welcome to our lord of fried restaurant🤝" + name)
    # asking the users location
    location = str(input("what is your  location?\n ", )).lower()
    while (location == " " or len(location) < 3 or not location.isalpha()):
        location = input("Hoo!🤔it is not looking like a place (enter your valid location): ")
    list3 = ["Ohoo we have three branches around your location want to place an order 🙃! yes (or) no : ",
             "Yup we have 2 branches near by you🤔! yes (or) no: ",
             "we have only 1 branch that is few kilometers away to you. wanna order any food item🙄! yes (or) no : "]
    print(random.choice(list3))
    order = input()
    print(order)
    # restricting the email id of user using regular expressions
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # expression to check email
    mail = input("Enter your email: ")
    a = re.fullmatch(regex, mail)

    # Checking whether valid email input given or not
    def check(email, b):
        while (email == ' ' or len(email) == 0 or b == None):
            mail = input("Enter your email correctly: ")
            b = re.fullmatch(regex, mail)

    check(mail, a)
    user_input1 = ''
    while user_input1 != "no":
        if order == "yes":
            print("ok let me know the items that we have")
            # Asking question to the user
            in_order = ('what   are the items your that you want order select from the below list?')
            # CREATING THE LIST OF MENU ITEMS THAT ARE AVAILABLE
            items = {"1": "Burger", "2": "pizza", "3": "chicken rolls", "4": "pani puri", "5": "biryani",
                     "6": "shawarma",
                     "7": "grilled chicken", "8": "egg rolls", "9": "butter chicken", "10": "chicken wings",
                     "11": "spring rolls", "12": "paneer curry", "13": "fishfry", "14": "noodles", "15": "sandwhich",
                     "16": "chicken kabab", "17": "mutton curry", "18": "egg biryani", "19": "mashed potatoes",
                     "20": "roti and curry", "21": "mutton kabab", "22": "mushroom curry", "23": "french fries",
                     "24": "fish curry", "25": "cheese rolls."}

            time.sleep(2)
            print(items)
            print("Here is a list of items ")  # printing the items available in dictionary
            item = ''
            a = 'yes'
            while a == 'yes':
                item = input("select your menu item: ").lower()
                if item in items:
                    print("let me know your exact location dear")
                    print("give ur mobile number ... for contacting you")
                    number = ""
                    b = 'yes'
                    while b == 'yes':
                        number = input("Enter your mobile number: ")
                        # using the regular expressions and creating a number pattern
                        pattern = re.compile("(0/91)?[-\s]?[6-9][0-9]{9}")
                        if pattern.fullmatch(number):
                            print('OK our team will contact you within a  few minutes')
                            print("your order will be placed after contacting you customer !🤝")
                            a = 'no'
                            b = 'no'
                        else:
                            print("Oop's🙃!we couldn't reach out your number check that you enter a valid number ")
                            b = 'yes'

                else:
                    print(
                        " sorry😣😔 the item you have ordered is not available in our menu list ,could you please select the item from our menu list ")
                    break
        elif order not in "yes" and "no":
            print("sorry i can't understand what you have been typed please say 'yes' or 'no'")

        else:
            order == "no"
            print("its fine  thank you for visiting 🙂 Hope so you enjoyed our services")

        response = input("Do you want to try again yes(or) no: ").lower()
        user_input1 = response
    else:
        print("OK we will meet next time BYE!!")
