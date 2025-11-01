class Car:
    def __init__(self, brand, model, year, price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.available = True  # pieejamība

    def rent(self):
        """Atzīmē automašīnu kā iznomātu."""
        if self.available:
            self.available = False
            return True
        return False

    def return_car(self):
        """Atzīmē automašīnu kā atgrieztu."""
        self.available = True

    def __str__(self):
        status = "Pieejama" if self.available else "Iznomāta"
        return f"{self.brand} {self.model} ({self.year}) - {status}, {self.price_per_day} €/dienā"


class RentalSystem:
    def __init__(self):
        self.cars = []  # saraksts ar automašīnām

    def add_car(self):
        """Pievieno jaunu automašīnu sistēmā."""
        brand = input("Ievadi marku: ")
        model = input("Ievadi modeli: ")
        try:
            year = int(input("Ievadi gadu: "))
            price = float(input("Ievadi cenu par dienu (€): "))
        except ValueError:
            print(" Nepareiza ievade!")
            return

        car = Car(brand, model, year, price)
        self.cars.append(car)
        print(" Automašīna pievienota!")

    def show_all_cars(self):
        """Parāda visas automašīnas."""
        if not self.cars:
            print(" Sistēmā nav automašīnu.")
            return
        print("\n🚘 Automašīnu saraksts:")
        for i, car in enumerate(self.cars, start=1):
            print(f"{i}. {car}")

    def rent_car(self):
        """Iznomā automašīnu pēc izvēles."""
        self.show_all_cars()
        try:
            idx = int(input("\nIevadi automašīnas numuru, kuru vēlies iznomāt: ")) - 1
            if 0 <= idx < len(self.cars):
                car = self.cars[idx]
                if car.rent():
                    print(f" Tu iznomāji: {car.brand} {car.model}")
                else:
                    print(" Šī automašīna jau ir iznomāta!")
            else:
                print(" Nepareizs numurs.")
        except ValueError:
            print(" Ievadi skaitli!")

    def return_car(self):
        """Atgriež automašīnu."""
        self.show_all_cars()
        try:
            idx = int(input("\nIevadi automašīnas numuru, kuru vēlies atgriezt: ")) - 1
            if 0 <= idx < len(self.cars):
                car = self.cars[idx]
                car.return_car()
                print(f" Automašīna {car.brand} {car.model} atgriezta.")
            else:
                print(" Nepareizs numurs.")
        except ValueError:
            print(" Ievadi skaitli!")

    def show_statistics(self):
        """Aprēķina statistiku — vidējo cenu un dārgāko auto."""
        if not self.cars:
            print(" Nav datu statistikai.")
            return
        avg_price = sum(car.price_per_day for car in self.cars) / len(self.cars)
        max_price_car = max(self.cars, key=lambda c: c.price_per_day)
        print("\n Statistika:")
        print(f" - Vidējā nomas cena: {avg_price:.2f} €")
        print(f" - Dārgākais auto: {max_price_car.brand} {max_price_car.model} ({max_price_car.price_per_day} €/dienā)")


def main():
    system = RentalSystem()

    while True:
        print("\n===  AUTOMAŠĪNU NOMAS SISTĒMA ===")
        print("1. Pievienot automašīnu")
        print("2. Parādīt visas automašīnas")
        print("3. Iznomāt automašīnu")
        print("4. Atgriezt automašīnu")
        print("5. Parādīt statistiku")
        print("0. Iziet")

        choice = input("Izvēlies darbību: ")

        if choice == "1":
            system.add_car()
        elif choice == "2":
            system.show_all_cars()
        elif choice == "3":
            system.rent_car()
        elif choice == "4":
            system.return_car()
        elif choice == "5":
            system.show_statistics()
        elif choice == "0":
            print(" Uzredzēšanos!")
            break
        else:
            print(" Nepareiza izvēle, mēģini vēlreiz.")


if __name__ == "__main__":
    main()
