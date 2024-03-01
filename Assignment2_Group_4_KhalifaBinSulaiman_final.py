"""GROUP 4 | ASSIGNMENT 2 | "CURRENCY CONVERTER" | GCIS.123 | SUBMITTED TO PROF. D.COVACEVIC."""

"""This program is designed to perform a conversion of UAE Dirhams into such currencies as Euros, British Pound Sterlings, United States Dollars
and Russian Rubles as well as performing backward conversions from these currencies into UAE Dirhams. The user is presented with the menu which allows him to
choose an option of which currencies he/she would like to convert. The code converts the amount entered by multiplying it to the rate of conversion."""

def conversion():                                                                               # here we showcase the menu options for the user
    print("These are the conversion options, please choose what would you like to convert.")
    print("1. Convert AED to Euro (EUR)")                                                       # AED - EUR
    print("2. Convert AED to British Pound Sterling (GBP)")                                     # AED - GBP
    print("3. Convert AED to United States Dollar (USD)")                                       # AED - USD
    print("4. Convert AED to Russian Ruble (RUB)")                                              # AED - RUB - we added this conversion to be different from our classmates :)
    print("5. Convert Euro (EUR) to AED")                                                       # EUR - AED
    print("6. Convert British Pound Sterling (GBP) to AED")                                     # GBP - AED
    print("7. Convert United States Dollar (USD) to AED")                                       # USD - AED
    print("8. Convert Russian Ruble (RUB) to AED")                                              # RUB - AED - we added this conversion to be different from our classmates :)
    print("9. Exit")

"""The functions below perform the conversion according to the exchange rates using WHILE, IF, ELSE, ELIF statements."""

def aed_to_euro(money):
    return money * 0.25

def aed_to_british_pound(money):
    return money * 0.22

def aed_to_dollar(money):
    return money * 0.27

def aed_to_ruble(money):
    return money * 24.96

def euro_to_aed(amount):
    return amount * 3.97

def british_pound_to_aed(amount):
    return amount * 4.64

def dollar_to_aed(amount):
    return amount * 3.67

def ruble_to_aed(amount):
    return amount * 0.04

def main():                                                                                     # here we use our MAIN function with the implemented WHILE loop.
    while True:                                                                                 # here we use a WHILE function.
        conversion()
        choice = int(input())
        if choice == 9:
            print("Understandable, have a nice day!")
            break                                                                               # in case if the user doesn't want to perform a conversion, we give an option to exit and the program stops using IF and BREAK.
        else:
            quantity = float(input("Enter the quantity of desired currency: "))
            if choice == 1:                                                                     # here we use IF, ELIF statements to distinguish between our options chosen by the user.
                print(quantity, "AED is equal to", aed_to_euro(quantity), "EUR")
            elif choice == 2:
                print(quantity, "AED is equal to", aed_to_british_pound(quantity), "GBP")
            elif choice == 3:
                print(quantity, "AED is equal to", aed_to_dollar(quantity), "USD")
            elif choice == 4:
                print(quantity, "AED is equal to", aed_to_ruble(quantity), "RUB")
            elif choice == 5:
                print(quantity, "EUR is equal to", euro_to_aed(quantity), "AED")
            elif choice == 6:
                print(quantity, "GBP is equal to", british_pound_to_aed(quantity), "AED")
            elif choice == 7:
                print(quantity, "USD is equal to", dollar_to_aed(quantity), "AED")
            elif choice == 8:
                print(quantity, "RUB is equal to", ruble_to_aed(quantity), "AED")

if __name__ == "__main__":
    main()

"""Note for professor: For some reason, throughout our development the code started showing ValueError: invalid literal for int() with base 10:
Although, it is working properly, just press PLAY button second time."""

