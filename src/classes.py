class VendingMachine:
    def __init__(self, name: str, accepted_coins: [], beverages: {}, location: str, starting_coins: {}):
        self.name = name
        self.accepted_coins = accepted_coins
        self.beverages = beverages
        self.location = location
        self.current_coins = starting_coins

    def is_valid_payment(self, paid: dict) -> bool:
        return False if [coin for coin in paid.keys() if coin not in self.accepted_coins] else True

    def is_payment_enough(self, paid: dict, beverage: str):
        bvg_price = self.beverages.get(beverage).get("price", 0)
        if bvg_price == 0:
            raise ValueError("Error Contact Supplier...")
        payment = sum([coin * count for coin, count in paid.items()])
        equal_pay = True if payment == bvg_price else False
        if payment >= bvg_price:
            return payment, equal_pay
        else:
            return 0, equal_pay

    def calculate_required_change(self, payment):
        change = payment
        coins = {}
        for coin in sorted(self.accepted_coins, reverse=True):
            if change >= coin:
                coins[coin] = change // coin
                change = change % coin
        return coins

    def is_beverage_available(self, beverage: str) -> bool:
        return True if self.beverages.get(beverage).get("quantity") > 0 else False

    def buy_beverage(self, beverage, paid_coins):
        if beverage not in self.beverages:
            return "beverage not available..."
        if not self.is_beverage_available(beverage):
            return "beverage not available, Wait for your money..."
        if not self.is_valid_payment(paid_coins):
            return "invalid coins..."
        payment, equal_pay = self.is_payment_enough(paid_coins, beverage)
        if payment == 0:
            return "insufficient payment..."
        if not equal_pay:
            required_change = self.calculate_required_change(payment)
            if not self.process_money_change(required_change):
                return "insufficient change..."
        self.current_coins = {coin: self.current_coins.get(coin, 0) + count for coin, count in paid_coins.items()}
        self.beverages[beverage]["quantity"] -= 1
        return "Done, Enjoy your beverage..."

    def process_money_change(self, required_change):
        for coin, count in required_change.items():
            if self.current_coins[coin] < count:
                return False
            self.current_coins[coin] -= count
        return True

    def refilling_beverage(self, beverage, quantity):
        self.beverages[beverage]["quantity"] += quantity
        return "beverage refilled..."

    def refilling_change(self, coins):
        self.current_coins = {coin: self.current_coins.get(coin, 0) + count for coin, count in coins.items()}
        return "change refilled..."


class VendingMachines:
    def __init__(self, names: [], accepted_coins: [], beverages: {}, locations: []):
        self.names = names
        self.coins = accepted_coins
        self.beverages = beverages
        self.locations = locations
        self.vms = {}

    def update_location_for_vm(self, new_location, name):
        if name not in self.names:
            return "name is wrong..."
        self.vms[name].location = new_location
        return "location updated..."

    def add_vm(self, name, accepted_coins, beverages, location, starting_coins: {}):
        if name in self.names:
            print("name already exists...")
        vm = VendingMachine(name, accepted_coins, beverages, location, starting_coins)
        self.vms[name] = vm
        self.names.append(name)
        self.locations.append(location)
        return vm
