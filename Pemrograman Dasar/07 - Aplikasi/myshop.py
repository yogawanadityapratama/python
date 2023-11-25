class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

product_list = []

def createProduct():
    id = input("id: ")
    name = input("name: ")
    price = input("price: ")

    product = Product(id, name, price)
    product_list.append(product)
    
def readProduct():
    for i in product_list:
        print(i.id, i.name, i.price)

def updateProduct():
    id = input("Choice id to Update: ")

    product = None

    for i in product_list:
        if i.id == id:
            product = i
            break

    if product is None:
        print("Product not find.")
        return

    new_name = input("Update product name: ")
    new_price = input("Update product price: ")

    product.name = new_name
    product.price = new_price

    print("Product succesfull updated.")

def deleteProduct():
    id = input("Choice id to delete: ")
    for i in product_list:
        if i.id == id:
            product_list.remove(i)  

while True:
    print("Menu")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")

    user_input = input("Choice: ")

    match user_input:
        case "1":
            createProduct()
        case "2":
            readProduct()
        case "3":
            updateProduct()
        case "4":
            deleteProduct()