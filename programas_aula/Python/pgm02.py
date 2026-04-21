# Exemplo de estrutura de armazenamento usando Dicionário de Listas   

# Lista inicial
Dados = {
    78: [122, 'maçã', 3.99, 'kg'],
    53: [41, 'tomate', 7.45, 'kg'],
    64: [86, 'melancia', 9.98, 'pc'],
    23: [246, 'laranja', 4.15, 'kg'],
    84: [36, 'banana', 2.45, 'kg'],
    217: [23, 'maionese', 14.67, 'pc']
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
        qtde   = int(input('quantidade >> '))
        descr  = input('descrição >> ')
        pcunit = float(input('pc.unitário >> '))
        unid   = input('unidade >> ')
        Dados[cod] = [qtde, descr, pcunit, unid]

    cod    = int(input('\ncódigo >> ')) # código do proximo produto

for codigo, dados in Dados.items():
    print(f'{codigo} -> {dados}')







