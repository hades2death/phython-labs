class Vzuttya:
    stock_count = 0
    collection = ""

    def __init__(self):
        self.__producer = "Unknow"
        self.__price = 0
        self.__size = 0.0
        self.__color = "Unknow"
        self.__sale = 0


    def __init__(self, producer, price, size, color, sale):
        self.__producer = producer
        self.__price = price
        self.__size = size
        self.__color = color
        self.__sale = sale



    def get_producer(self):
        return self.__producer

    def set_producer(self, producer):
        self.__producer = producer

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_sale(self):
        return self.__sale

    def set_sale(self, sale):
        self.__sale = sale


    def __str__(self):
        return f"Виробник: {self.__producer}, Ціна: {self.__price}, Розмір: {self.__size}, Колір: {self.__color}, Продажі: {self.__sale}"

    def __repr__(self):
        return f"Взуття('{self.__producer}', {self.__price}, {self.__size}, '{self.__color}', {self.__sale})"

    def __del__(self):
        print(f"{self.__repr__()} видаляється.")


def main():

    shoe1 = Vzuttya("Nike", 100, 42, "Black", 15)
    shoe2 = Vzuttya("Adidas", 120, 40, "White", 20)
    shoe3 = Vzuttya("Puma", 80, 38, "Blue", 30)


    print(shoe1)
    print(shoe2)
    print(shoe3)


    shoes = [shoe1, shoe2, shoe3]

    top_selling = [0]

    for shoe in shoes:

     if shoe.get_sale() > top_selling

        top_selling = shoes

    print("\nНайбільш продана пара:")
    print(top_selling)


if __name__ == "__main__":
    main()
