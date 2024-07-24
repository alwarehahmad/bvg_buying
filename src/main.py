from classes import *


def main():
    locations = ["KL", "PJ", "Penang"]
    accepted_coins = [10, 20, 50, 100, 200]
    beverages = {
        "Pepsi": {
            "price": 11,
            "quantity": 1
        },
        "Coke": {
            "price": 40,
            "quantity": 10
        },
        "7Up": {
            "price": 150,
            "quantity": 10
        },
        "Sprite": {
            "price": 255,
            "quantity": 10
        }
    }

    vending_machines = VendingMachines(accepted_coins=accepted_coins, beverages=beverages, locations=locations,
                                       names=[])
    vm = vending_machines.add_vm(name="KL", accepted_coins=accepted_coins, beverages=beverages, location="KL",
                                 starting_coins={10: 5, 20: 2, 50: 5, 100: 2, 200: 2})
    print(vm.buy_beverage("Pepsi", {10: 2}))


if __name__ == "__main__":
    main()
