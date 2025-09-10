import time
from libis import *
from libis.arquivo import *
arq = 'cursoemvideo.txt'

if aquivoExiste(arq):
    print('aquivo encontrado com sucesso!')
else:
    print('aquivo nao escontrado')
    criarArquivo(arq)

while True:
    resposta = menu(['ver usuarios cadastrados','Cadastrar novo usuario','sair do sistema','Apagar usuario'])
    if resposta == 1:
        # opção de listar conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #opção para cadastrar novos usuarios
        cabeçalho('CADASTRAR NOVO USUARIO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #opção para sair do programa
        cabeçalho('opção 3')
    elif resposta ==4:
        #opção para apagar usuario
        a = open(arq, 'rt')
        for c in a:
            qual_usuario= int(input(f'qual dos usuarios'))
            print(f'temos {c}', end='')

        #qual_usuario = int(input(f'qual usuario '))
        #try:
        #    print(f' tem {max(a[qual_usuario])}')
        #except:
       #     print('não foi possivel')
        cabeçalho('opção 4')

    else:
        cabeçalho('\033[31mERRO! digite uma opção valida\033[m')

    time.sleep(2)