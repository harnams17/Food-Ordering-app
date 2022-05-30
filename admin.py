admin_keys = {"harnam": "harnam@123"}

inven = {1: {'ItemName': 'Tandoori Chicken', 'FoodID': 1, 'Quantity': '100ml,250ml,4pieces', 'Price': 240, 'Stock': 14, 'Discount': '20%'},
        2: {'ItemName': 'Vegan Burger', 'FoodID': 2, 'Quantity': '1 Piece', 'Price': 320, 'Stock': 14, 'Discount': '40%'},
        3: {'ItemName': 'Truffle Cake', 'FoodID': 3, 'Quantity': '500gm', 'Price': 900, 'Stock': 14, 'Discount': '30%'}}
#nested dict

def add_new_item():
    itemname = input("Enter the Item name: ")
    foodid = int(input("Enter the item id: "))
    quantity = input("Enter the Quantity Value of item: ")
    price = int(input("Enter the price of the item: "))
    stock = int(input("Enter the stock value of item: "))
    dis_count = input("Enter the discount value: ")
    
    inven[itemid] = {
        "ItemName": itemname,
        "FoodID": foodid,
        "Quantity": quantity,
        "Price": price,
        "Stock": stock,
        "Discount": dis_count
    }
    print("The Item"+itemname+ "is successfully added")
    return inven


def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the price of item"))
    d = int(input("Enter the stock of the item"))
    e = input("Enter the quantity of the item")
    f = input("Enter the discount value: ")
    inven[item]["ItemName"] = a
    inven[item]["Price"] = b
    inven[item]["Stock"] = d
    inven[item]["Quantity"] = e
    inven[item]["Discount"] = f
    print("*****Edited item successfully*****")
    return inven

def show_inven():
    print("*****The list item should as follows:*****")
    for i in inven:
        print(inven[i]["FoodID"],'.',end=" ")
        print(inven[i]["ItemName"],end=" ")
        print('(',inven[i]["Quantity"],')',end=" ")
        print("INR", inven[i]["Price"],)
        print("Discount", inven[i]["Discount"])
        
        
       

def remove_item():
    d = int(input("Enter the Item id which you want to exit"))
    inven.pop(d)
    print("Remove item successfully ")
    return inven
