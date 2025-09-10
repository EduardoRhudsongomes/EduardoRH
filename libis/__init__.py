def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor digite um numero valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu nao digitar numero\033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' *42

def cabeçalho(txt):
    print(linha())
    print((txt.center(42)))
    print(linha())
def menu(lista):
    cabeçalho('      MENU PRINCIPAL        ' )
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m  - \033[34m {item}\033[m')
        cont +=1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc