class PhoneBook:
    def __init__(self, id):
        self.id = id
        self.slownik = {}

    def __str__(self):
        return f"{self.slownik}"

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return (self.slownik == other.slownik and self.id == other.id)

    def __gt__(self, other):
        assert isinstance(other, self.__class__)
        if len(self.slownik.keys()) > len(other.slownik.keys()):
            return True
        else:
            return False

    def add_record(self, user, number):
        cyfry = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        assert len(user) != 0, "Nazwa uzytkownika jest pusta"
        assert number != "", "Numer jest pusty"

        for i in range(len(number)):        #tu do sprawdzenia mozna bylo wykorzystac isDecimal albo isNumeric
            assert cyfry.count(number[i]) != 0, "W numerze wystepuja inne znaki niz cyfry!"

        self.slownik[user] = number


    def show_records(self):
        for x, y in self.slownik.items():
            print(f"{x}: {y}")

if __name__ == '__main__':
    ksiazka = PhoneBook(1)
    try:
        ksiazka.add_record("", "123")
    except AssertionError as err:
        print(err)

    try:
        ksiazka.add_record("Adam", "")
    except AssertionError as err:
        print(err)
    try:
        ksiazka.add_record("Adam", "123asd123")
    except AssertionError as err:
        print(err)

    try:
        ksiazka.add_record("Adam", "123567123")
        ksiazka.add_record("Ewa", "123")
    except AssertionError as err:
        print(err)

    ksiazka.show_records()
    print(ksiazka)

    ksiazka1 = PhoneBook(1)
    ksiazka1v1 = PhoneBook(1)

    try:
        if (ksiazka1 == ksiazka1v1):
            print("Slowniki sa rowne")
        else:
            print("Slowniki NIE SA rowne")
    except AssertionError as err:
        print(err)

    ksiazka1.add_record("Jan", "123")
    ksiazka1.add_record("Wojciech", "321")
    ksiazka1v1.add_record("Marianna", "678")

    print(ksiazka1)
    print(ksiazka1v1)

    try:
        if (ksiazka1 > ksiazka1v1):
            print("Slownik po lewej stronie jest wiekszy od tego po prawej")
        else:
            print("Slownik po prawej stronie jest wiekszy od tego po lewej")
    except AssertionError as err:
        print(err)
