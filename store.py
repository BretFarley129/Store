class Product(object):
    def __init__(self, price, itemName, weight, brand, Cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = Cost
        self.status = "for sale"
        

    def display_info(self):
        print 'Price: {}\nItem Name: {}\nWeight: {}\nBrand: {}\nCost: {}\nStatus: {}'.format(str(self.price), str(self.itemName), str(self.weight), str(self.brand),str(self.cost), self.status)
        print ""
        return self

    def sell(self):
        self.status = "sold"
        return self
        
    def addTax(self):
        tax = .08*self.price
        total = self.price + tax
        return total

    def returnItem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "for sale"
            self.price *= .8
        return self

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def addProduct(self, item):
        self.products.append(item)
        return self
    
    def removeProduct(self, item):
        self.products.remove(item)
        return self
    
    def inventory(self):
        print "displaying inventory:"
        print "---------------------"
        for i in self.products:
            i.display_info()
        return self


turkey = Product(30, "turkey", "10 lbs", "Trader Joes", 20)
jacket = Product(49.99, "jacket", "2 lbs", "Gucci", 40)
waterBottle = Product(100.00, "bottle", "20 lbs", "Arrowhead", 2)
keys = Product(5, "some random keys", "0,1 lbs", "Why do you need to know?", 0)

stuff = [turkey, jacket,waterBottle]

cornerStore = Store(stuff, "The corner", "Sum Gui")
cornerStore.inventory()
cornerStore.addProduct(keys)
cornerStore.inventory()
cornerStore.removeProduct(jacket)
cornerStore.inventory()