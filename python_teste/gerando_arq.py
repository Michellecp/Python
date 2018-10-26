print('Video Aula')
print('Gerando arquivo Texto')

arquivo=open('text.txt','w')
print('O nome do arquivo é ', arquivo.name)

arquivo.write("Lista de Pessoas da Familia Pacheco\n\n")
arquivo.write("João\n")
arquivo.write("Ines\n")
arquivo.write("Jefferson\n")
arquivo.write("Alexandra\n")
arquivo.write("#Isso não deve ser impresso\n")
arquivo.write("Michelle\n")
arquivo.flush()

print('O modo ao qual o seu arquivo foi aberto é', arquivo.mode)

print('O arquivo esta fechando?',arquivo.closed)

arquivo=open("test.txt","r")
print('O modo ao qual o arquivo o seu arquivo foi aberto é:',arquivo.mode)

for linha in arquivo.readlines():
    print(linha)

arquivo.close()
print('O arquivo esta fechado?', arquivo.closed)