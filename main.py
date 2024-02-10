# essa função será usada para separar a string de endereço em rua/avenida e número
def address_formatter(user_input):
    try:
        # essa será a lista que armarzenará as informações separadas
        address = []
        # aqui estamos simplesmente separando o input recebido usando apenas com base em espaço
        street, num = user_input.split(' ')
        # agora vamos adicionar as informações separadas à nossa lista
        address.append(street)
        address.append(num)
        # a função retorna as informações na mesma lista 
        return address
    except ValueError:
        print('Ops! Parece que algo está errado no seu endereço.')
        print('Tente usar o padrão "Rua (ou Avenida) Número" separados por espaço.')
        return None
# com uso de um loop, permitimos que o usuário faça quantos inputs quiser
while True:
    # armazena o input do usuário em uma variável
    user_input = input(f'Informe o endereço (rua e número): ')
    # aqui tratamos um input vazio
    if not user_input.strip():
        print('Digite informações válidas!')
        continue
    # aqui chamamos a função  criada acima, passando o input como parâmetro e recebendo os itens em uma variável
    formatted_address = address_formatter(user_input)
    #  se a função anterior não retornar None, significa que tudo deu certo e podemos mostrar os dados formatados
    if formatted_address is None:
        continue
    # mostrando os dados separados para o usuário
    print(formatted_address)
