Script = ['INSERT INTO `g6_livros` (`id_livro`, `titulo`, `ano_publicacao`, `id_autor`, `id_editora`, `id_genero`) VALUES']

arq = open ('livros.csv', 'r', encoding='UTF-8')
s = arq.readline()
s = arq.readline().rstrip()
while s != '':
    s = s.split(';')
    Script.append(f"('{s[0]}', '{s[1]}', '{s[2]}', '{s[3]}', '{s[4]}', '{s[5]}'),")
    s = arq.readline().rstrip()
arq.close()

Script[-1] = Script[-1].replace('),', ');')

for linha in Script:
    print(linha)


arqScript = open('script2.txt', 'w', encoding='UTF-8')
for linha in Script:
    arqScript.write(f"{linha}\n")

arqScript.close()