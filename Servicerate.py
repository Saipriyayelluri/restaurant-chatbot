#Rating function
def rating():
    print("\n-------------\nPlease rate our service here\nEnter your rating")
    print("1 to 5 (1 = Worst, 3 = Average, 5 = Excellent")
    rate = int(input())
    if rate == 1:
        print(
            "Sure! we will improve our services soon - Hope to have good time")
    elif rate == 2:
        print(
            "Thank you ! You will have the best service next time - Have a good day"
        )
    elif rate == 3:
        print(
            "Our services will be enhanced soon ! - Have a nice day"
        )
    elif rate == 4:
        print(
            "Thank you best services will be provided to you soon - Have an awesome day"
        )
    elif rate == 5:
        print(
            "THANK YOU FOR YOUR FEEDBACK HOPE YOU ENJOYED OUR SERVICES - ENJOY THE REST OF YOUR DAY"
        )