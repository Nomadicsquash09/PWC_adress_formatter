# importando a biblioteca de regular expressions
import re

# essa função será usada para separar a string de endereço em rua/avenida e número
def address_formatter(address_string):

    # aqui iniciamos um bloco try/except para tratar possíveis erros
    try:

        # essa será a lista que armarzenará as informações separadas
        address = []

        # esse dicionário será usado para armazenar as REs buscadas na string
        id_pattern = {
            'av_pattern': r'^([\w\s]+?)(?:,| )\s*(\d+[a-zA-Z]*)$',      # RE para av. ou rua
            'number_pattern': r'^(\d+[a-zA-Z]*),?\s*([\w\s]+)$',   # RE para  o número (com ou sem letra)
        }

        # iterando através da lista de REs para separar as informações
        for pattern in id_pattern.values():
            # faz a busca individualmente através das REs fornecidas
            add_element = re.findall(pattern, address_string)
            # adiciona os elementos encontrados na lista vazia
            address.append(add_element)

        # a função retorna as informações na mesma lista
        return address
    

    except re.error as e:

        # caso haja algum erro com a RE, ele será informado ao usuário
        print('Erro ao processar expressão regular:', e)
        return
    except Exception as e:
        # caso haja outro tipo de erro, também é informado ao usuário
        print('Ops! Ocorreu um erro inesperado:', e)
        return
    
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