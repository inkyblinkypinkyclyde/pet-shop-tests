# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, pets_out):
    pet_shop["admin"]["pets_sold"] += pets_out


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    breed_list = list()
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return breed_list


def find_pet_by_name(pet_shop, pet_name):
    for index, pet in enumerate(pet_shop["pets"]):
        if pet["name"] == pet_name:
            return pet_shop["pets"][index]


def remove_pet_by_name(pet_shop, pet_name):
    for index, pet in enumerate(pet_shop["pets"]):
        if pet["name"] == pet_name:
            pet_shop["pets"].pop(index)


def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash):
    customer["cash"] = customer["cash"] - cash


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, added_pet):
    customer["pets"].append(added_pet)


def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(pet_shop, pet, customer):
    if pet in pet_shop["pets"]:
        if customer["cash"] >= pet["price"]:
            add_or_remove_cash(pet_shop, pet["price"])
            customer["pets"].append(pet)
            remove_pet_by_name(pet_shop, pet)
            customer["cash"] -= pet["price"]
            remove_pet_by_name(pet_shop, pet)
            increase_pets_sold(pet_shop, 1)
