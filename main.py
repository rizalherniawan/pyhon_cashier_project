class Transaction():
    def __init__(self,item,item_price,total_item):
        self.item = item
        self.item_price = item_price
        self.total_item = total_item
    
    def update_item(self, item):
        self.item = item
    
    def update_item_price(self, item_price):
        self.item_price = item_price

    def update_total_item(self, total_item):
        self.total_item = total_item

    def count_total_price(self):
        return self.total_item * self.item_price


carts = []

def add_item(item, item_price, total_item):
    transact = Transaction(item, item_price, total_item)
    carts.append(transact)

def update_item_name(targetItem, name):
    for x in carts:
        if (x.item == targetItem):
            x.update_item(name)
            break

def update_item_price(targetItem, price):
    for x in carts:
        if (x.item == targetItem):
            x.update_item_price(price)
            break

def update_item_qty(targetItem, qty):
    for x in carts:
        if (x.item == targetItem):
            x.update_total_item(qty)
            break

def reset_transaction():
    carts.clear()


def delete_item(targetItem):
    targetIndex = 0
    for x in range(len(carts)):
        if (carts[x].item == targetItem):
            targetIndex = x
            break
    carts.pop(targetIndex)


def total_transaction():
    total_sum = 0
    for x in carts:
        total_sum += x.count_total_price()
    if (total_sum > 200000):
        total_sum - (total_sum * 0.05)
    elif (total_sum > 300000):
        total_sum - (total_sum * 0.08)
    elif (total_sum > 500000):
        total_sum - (total_sum * 0.1)
    return total_sum


data_amount = int(input("masukan jumlah data yang akan dimasukan: "))
x = 0
while x < data_amount:
    name = input("masukan nama item: ")
    quantity = int(input("masukan jumlah item: "))
    price = int(input("masukan harga item: "))
    add_item(name, price, quantity) 
    x += 1
print("\n")
print("pilih metode yang akan dipilih dengan mengetikan angka:\n1. Update nama item\n2. Update jumlah item\n3. update harga item\n4. Delete item\n5. Reset transaksi\n6. Hitung total transaksi")
option = int(input("masukan angka: "))
while option > 0 and option < 7:
    if(option == 1):
        targetName = input("masukan nama pencarian: ")
        newName = input("masukan nama baru: ")
        update_item_name(targetName, newName)
        option = int(input("masukan angka selanjutnya: "))
    elif(option == 2):
        targetName = input("masukan nama pencarian: ")
        amount = int(input("masukan jumlah: "))
        update_item_qty(targetName, amount)
    elif(option == 6):
        print("total transaksi anda adalah sebesar: ", total_transaction())
        break

