# Exemplo de estrutura de armazenamento usando Dicionário de Dicionários   

# Lista inicial
Dados = {
    78: {'qtde':122, 'descr':'maçã', 'pcunit':3.99, 'unid':'kg'},
    53: {'qtde':41, 'descr':'tomate', 'pcunit':7.45, 'unid':'kg'},
    64: {'qtde':86, 'descr':'melancia', 'pcunit':9.98, 'unid':'pc'},
    23: {'qtde':246, 'descr':'laranja', 'pcunit':4.15, 'unid':'kg'},
    84: {'qtde':36, 'descr':'banana', 'pcunit':2.45, 'unid':'kg'},
    217: {'qtde':23, 'descr':'maionese', 'pcunit':14.67, 'unid':'pc'}
    }
for codigo, dados in Dados.items():
    print(f'{codigo} -> {dados}')

# Ampliação da relação de produtos
print('\nDados do novo produto')
cod    = int(input('código >> '))
while cod > 0:
    if cod in Dados:
        print(f'Este código já está em uso. Digite outro')
    else:
        produto = {}
        produto['qtde']   = int(input('quantidade >> '))
        produto['descr']  = input('descrição >> ')
        produto['pcunit'] = float(input('pc.unitário >> '))
        produto['unid']   = input('unidade >> ')
        Dados[cod] = produto

    cod    = int(input('\ncódigo >> ')) # código do proximo produto

for codigo, dados in Dados.items():
    print(f'{codigo} -> {dados}')







