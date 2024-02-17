# Soluções em código

O presente projeto é a solução do desafio de código proposto pela PWC, cujo objetivo era desenvolver um software que recebe um endereço em uma única string e deve retornar nome e número da rua separados. 

O repositório contém um executável .exe, dentro da pasta *dist* com uma interface gráfica desenvolvida em *python*, que pode ser
executada em qualquer máquina, independendo  do sistema operacional e não sendo necessário a instalação
de um interpretador *python* na máquina.

## O repositório contém: 

> pasta build: contém arquivos temporários que são usados durante a execução do programa.

> pasta dist: é onde os programas compilados ficam armazenados.

> pasta images: contém as imagens utilizadas neste mesmo arquivo para representar o software.

> pasta src(source): contém o código original e o ambiente virtual, que contém todas as bibliotecas necessárias para rodar as soluções, além de um arquivo 'requirements.txt' por garantia e versatilidade

> pasta test_cases: contém o arquivo de casos de teste ('input_output.pdf')  para facilitar o teste da solução e servir como prévia do resultado esperado.

## Instalação e Requisitos

> O programa foi empacotado com a biblioteca *pyinstaller*, o que faz com que não sejam necessários arquivos ou extensões externas para executar o software.

> Após a instalação dos arquivos, basta buscar a pasta *dist* e executar o arquivo *main.exe* para visualizar as funcionalidades da aplicação.

## Imagens do projeto final

### Caso Simples
![Caso Simples](https://github.com/Nomadicsquash09/PWC_adress_formatter/blob/main/images/caso_simples.png?raw=True)

### Caso mais complexo
![Caso mais Complexo](https://github.com/Nomadicsquash09/PWC_adress_formatter/blob/main/images/caso_complexo.png?raw=True)

### Caso de endereço internacional
![Caso Internacional](https://github.com/Nomadicsquash09/PWC_adress_formatter/blob/main/images/caso_internacional.png?raw=True)