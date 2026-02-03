class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")



class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")




def main():
    print("=== Car Information Entry ===\n")
    while True:
        try:
            year = input("Enter the year (e.g., 2023): ").strip()
            year = int(year)
            if year < 1886 or year > 2100:  
                print("Please enter a realistic year.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the year.")

    make = input("Enter the make (e.g., Toyota, Honda): ").strip()
    model = input("Enter the model (e.g., Corolla, Civic): ").strip()

    while True:
        doors = input("Enter number of doors (2 or 4): ").strip()
        if doors in ["2", "4"]:
            doors = int(doors)
            break
        print("Please enter either 2 or 4.")

    roof = input("Enter roof type (solid or sun roof): ").strip().lower()
    if "sun" in roof or "moon" in roof:
        roof = "sun roof"
    else:
        roof = "solid"

    my_car = Automobile(year, make, model, doors, roof)

    print("\n" + "="*40)
    print("     Your Car Information")
    print("="*40)
    
    my_car.display_info()
    
    print("="*40 + "\n")



if __name__ == "__main__":
    main()