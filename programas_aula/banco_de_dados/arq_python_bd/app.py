Script = ['INSERT INTO `g6_genero` (`id_genero`, `descricao`) VALUES']

arq = open('generos.csv', 'r', encoding='utf-8')
s= arq.readline()
s = arq.readline().rstrip()

while s != '':
    s = s.split(';')
    Script.append(f"('{s[0]}','{s[1]}'),")
    s = arq.readline().rstrip()
arq.close()

Script[-1] = Script[-1].replace('),',');')

for linha in Script:
    print(linha)

arqScript = open('script.txt', 'w', encoding = 'utf-8')
for linha in Script:
    arqScript.write(f"{linha}\n")
arqScript.close()