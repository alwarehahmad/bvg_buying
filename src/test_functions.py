from src.classes import VendingMachines


def test_success_purchase():
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

    assert "Done, Enjoy your beverage..." == vm.buy_beverage("Pepsi", {10: 2})

    vm.refilling_change({10: 5, 20: 2, 50: 5, 100: 2, 200: 5})
    assert vm.current_coins == {10: 12, 20: 2, 50: 5, 100: 2, 200: 5}


def test_no_change_purchase():
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
    vm = vending_machines.add_vm(name="ahmad", accepted_coins=accepted_coins, beverages=beverages, location="KL",
                                 starting_coins={10: 0, 20: 0, 50: 0, 100: 0, 200: 0})
    assert "insufficient change..." == vm.buy_beverage("Pepsi", {10: 2})

    stat = vending_machines.update_location_for_vm("KL", "Jeff")
    assert "name is wrong..." == stat


def main():
    print(test_success_purchase())
    print(test_no_change_purchase())


if __name__ == "__main__":
    main()
