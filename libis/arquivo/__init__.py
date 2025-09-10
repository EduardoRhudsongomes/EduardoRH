from libis import cabeçalho


def aquivoExiste(nome):
    '''arquivoExiste verifica se o arquivo onde vai ser salvo os dados, existe'''
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    '''criarArquivo cria o arquivo onde vai ser guardado os dados de cadastro'''
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criaçao do arquivo')
    else:
        print(f'Arquivo {nome}criado com sucesso')
    finally:
        a.close()

def lerArquivo(nome):
    '''lerArquivo lê os dados salvos no arquivo, inclusive os que forem adicionados'''
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1]= dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    '''cadastrar é usado para cadastrar novos usuarios e suas idades'''
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registo de {nome} adicionado')
            a.close()


def apagarusuario(arq, posição):
    usuario = int(input('qual posição do usuario?'))
    del usuario

