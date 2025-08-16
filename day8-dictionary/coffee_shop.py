menu = {
    'milk_tea': 25,
    'black_tea': 15,
    'samosa': 20,
    'chaumin': 50,
    'momo': 120,
    'pasta': 60,
    'pakauda': 10
}

def show_menu():
    print("\nmilk_tea: 25\nblack_tea: 15\nsamosa: 20\nchaumin: 50\nmomo: 120\npasta: 60\npakauda: 10")
def your_order():
    print("\n=================Welcome to our Cafe ===================")
    print("Following are the today's dishes:")
    show_menu()
    total_price = 0
    order = input("What would you like to have? ").strip()
    if order in menu:
        total_price += menu[order]
        order  = input("Anything else? yes or no ").strip()
        if order =="yes":
            show_menu()
            order = input("What would you like to have? ").strip()
            total_price += menu[order]
            print(f"your total bill is Rs. {total_price}.")
        else:
            print(f"Your total bill  is Rs. {total_price}.")
    else:
        print("Sorry!, this is not available now.")
        response = input("Would would like to have anything else? yes or no ").strip()
        response = response.lower()
        if response == "yes":
            show_menu()
            order = input("What would you like to have? ")
            total_price += menu[order]
            print(f"Your total bill is Rs.{total_price}.")
        else:
            print(f"Your tootal bill  is {total_price}")

your_order()