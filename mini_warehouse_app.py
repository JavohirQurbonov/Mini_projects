products = {
    'adrenaline': {'narxi': 200, 'soni': 20},
    'coca-cola': {'narxi': 10000, 'soni': 30},
    'morojniy': {'narxi': 20000, 'soni': 10},
    'non' : {'narxi':5000,'soni':200}
}

def add_product(product_name,product_price,product_quantity):

    name = product_name.strip().lower()
    price = int(product_price)
    quantity = int(product_quantity)
    if price > 0 and quantity > 0:
        if name not in products.keys():
            products[name] = {'narxi': price, 'soni': quantity}
            products_list()
            print("Mahsulot qo'shildi!!!")
        else:
            products[name]['soni'] += quantity
            products_list()
    else:
        print("Ma'lumot kiritishda xatolik.Qaytadan urinib ko'ring!!!")
        products_list()


def get_out_product(product_name,product_quantity):

    if product_name not in products.keys():
        print(f"Bizda {product_name}-mahsuloti mavjud emas!!!")
    elif product_quantity<products[product_name]['soni']:
        products[product_name]['soni'] -= product_quantity
        print(f"{product_name}-mahsulotidan {products[product_name]['soni']}-ta qoldi")
    else:
        print(f"Afsuski {product_name}-mahsulotidan {products[product_name]['soni']}-ta mavjud!!!")
        try:
            while True:
                question=input("Mahsulotni borini olasizmi?(y/n)")
                if question=='y':
                    products[product_name]['soni'] -= products[product_name]['soni']
                    if products[product_name]['soni'] == 0:
                        products.pop(product_name,None)
                    products_list()
                    break
        except ValueError:
            print("Tog'ri bo'limni tanlang!")


def products_list():
    print(f"{'Mahsulot nomi':<15} | {'Narxi':<12} | {'Miqdori':<12} | {'Umumiy summa':<14}")
    print("-" * 65)
    for k, v in products.items():
        print(f"{k.title():<15} | {v['narxi']:<12} | {v['soni']:<12} | {v['narxi'] * v['soni']:<14}")


def input_data():
    while True:
        back_to_menu=False
        try:
            command=int(input("1.Mahsulot qo'shish\n2.Mahsulot olib chiqish\n3.Mahsulotlar ro'yxati\n0.Chiqish\nBo'limni tanlang:"))
            if command not in [0,1,2,3]:
                print("\nTog'ri bo'limni tanlang!\n")
                continue
            if command==0:
                print("Dastur tugadi!!!")
                break
            if command==1:
                while True:
                    print("\n---MAHSULOT QO'SHISH BO'LIMI---\n")
                    product_name = input("Mahsulot nomini kiriting('exit'-chiqish):")
                    if product_name=='exit':
                        back_to_menu=True
                        break
                    try:
                        product_price=int(input("Mahsulot narxini kiriting('exit'-chiqish):"))
                        if product_price=='exit':
                            back_to_menu = True
                            break
                        product_quantity=int(input("Mahsulot miqdorini kiriting('exit'-chiqish):"))
                        if product_quantity=='exit':
                            back_to_menu = True
                            break
                        add_product(product_name, product_price, product_quantity)
                    except ValueError:
                        print("Ma'lumot kiritishda xatolik!")
                        ask=input("Yana mahsulot kiritasizmi?(y/n)")
                        if ask=='n':
                            break
                if back_to_menu:
                    continue

            if command == 2:
                while True:
                    print("\n---MAHSULOT OLIB CHIQISH BO'LIMI---\n")
                    product_name = input("Mahsulot nomini kiriting('exit'-chiqish):")
                    if product_name == 'exit':
                        back_to_menu = True
                        break
                    try:
                        product_quantity = int(input("Mahsulot miqdorini kiriting('exit'-chiqish):"))
                        if product_quantity == 'exit':
                            back_to_menu = True
                            break
                        get_out_product(product_name, product_quantity)
                    except ValueError:
                        print("Ma'lumot kiritishda xatolik!")
                        ask = input("Yana mahsulot olib chiqasizmi?(y/n)")
                        if ask == 'n':
                            break
                if back_to_menu:
                    continue

            if command == 3:
                while True:
                    print("\n---MAHSULOTLAR RO'YXATI BO'LIMI---\n")
                    products_list()
                    question=input("Menyuga qaytasizmi?(y/n)")
                    if question == 'y':
                        back_to_menu = True
                        break

                if back_to_menu:
                    continue

            return command
        except ValueError:
            print("Tog'ri bo'limni tanlang!")
            question=input("Menyuga qaytasizmi?(y/n)")
            if question=='n':
                break

input_data()