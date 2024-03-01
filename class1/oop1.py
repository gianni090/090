class Vehicle:
    def __init__(self, number, owner_name, passport_data, issue_date, expiration_date, region):
        self.number = number
        self.owner_name = owner_name
        self.passport_data = passport_data
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        self.region = region

class VehicleRegistry:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_owners_by_issue_date(self, date):
        owners = []
        for vehicle in self.vehicles:
            if vehicle.issue_date == date:
                owners.append(vehicle.owner_name)
        return owners

    def get_numbers_by_region(self, region):
        numbers = []
        for vehicle in self.vehicles:
            if vehicle.region == region:
                numbers.append(vehicle.number)
        return numbers

def main():
    registry = VehicleRegistry()

    registry.add_vehicle(Vehicle("н090ву", "Иванов Иван Иванович", "1234 567890", "2024-01-01", "2025-01-01", "Москва"))
    registry.add_vehicle(Vehicle("м777мм", "Петров Петр Петрович", "5678 901234", "2024-01-01", "2025-01-01", "Ростов"))

    owners_by_issue_date = registry.get_owners_by_issue_date("2024-01-01")
    print("Список владельцев с заданной датой выдачи номера:")
    for owner in owners_by_issue_date:
        print(owner)

    numbers_by_region = registry.get_numbers_by_region("Ростов")
    print("Список номеров средств с заданным регионом приписки:")
    for number in numbers_by_region:
        print(number)

if __name__ == "__main__":
    main()