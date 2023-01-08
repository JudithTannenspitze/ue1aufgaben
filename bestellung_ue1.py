

class order:
    bestellnummer = "b1"
    number_of_orders = 0
    def __init__(self,order_date,comment):
        self.order_date = order_date
        self.comment = comment
        self.__class__.number_of_orders+=1
        self.bestellnummer = "B" + str(self.number_of_orders)
        self.number_of_products = 0
        self.__product_list = []
   
    def hinzufuegen_liste(self,product):
        if (self.number_of_products>=5):
            return False
        self.__product_list.append(product)
        self.number_of_products+=1
        return True

    def calculate_wholeprice(self):
        whole_price = 0
        for order_item in self.__product_list:
            whole_price = whole_price + order_item.price
        return whole_price
     


class product (order):
    
     def __init__(self,name,description,price):
        self.name = name
        self.description = description
        self.price = price

    

    
    
        


bestellungOne = order(21/10/2022,"hallo")
print (bestellungOne.bestellnummer)
bestellungTwo = order(22/10/2022,"hihi")
print(bestellungTwo.bestellnummer)
product1 = product("Hose","Überlänge",15.00)
product2 = product("T-Shirt","bestickt",10.00)
product3 = product("Langarmpullover","für Winter",20.00)
product4 = product("Skiunterhose","für Ski fahren",5.00)
product5 = product("Socken","für warme Füße",5.00)
product6 = product("Fahrrad","mobil unterwegs",50.00)
bestellungTwo.hinzufuegen_liste(product1)
bestellungTwo.hinzufuegen_liste(product2)
bestellungTwo.hinzufuegen_liste(product3)
bestellungTwo.hinzufuegen_liste(product4)
print(bestellungTwo.hinzufuegen_liste(product5))
print(bestellungTwo.hinzufuegen_liste(product6))
print("gesamtpreis" + str(bestellungTwo.calculate_wholeprice()))
