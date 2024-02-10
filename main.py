
def address_formatter(user_input):
    address = []
    street, num = user_input.split(' ')
    address.append(street)
    address.append(num)
    return address


while True:
    user_input = input(f"Informe o endereço (rua e número): ")

    print(address_formatter(user_input))
