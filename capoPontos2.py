import random
import telegram.ext as tl
#print(dir(telegram.ext))

##import telebot

banheiros = {'Olimpo':['Lm', 'Soca', 'Waze', 'Xulapa'], 'Fora':['Xv'], 'Dentro':['Pesado', 'Melody', 'Bixo']}
dia = ['segunda', 'quarta', 'sexta']
caponeano = ['Lm', 'Soca', 'Waze', 'Xulapa', 'XV', 'Pesado', 'Melody', 'Bixo']

def mudar(update, context):
    addOuRemover = str(input('Você deseja [adicionar] ou [remover] mmorador: ')).lower().strip()
    quarto = str(input('Qual quarto?: ')).strip().capitalize()
    morador = str(input('Qual o nome do morador? ')).strip().capitalize()

    if addOuRemover == 'adicionar':
        banheiros[quarto].append(morador)
    elif addOuRemover == 'remover':    
        banheiros[quarto].remove(morador)
    else:
        print('Não entendi sua resposta') 
    

def escolhido():
    escolhido = {}
    print('limpeza dos banheiros da semana:\n')
    for elemen in banheiros.keys():
        escolhido[elemen] = random.choice(banheiros[elemen])
        print(f'{elemen}: {escolhido[elemen]}')    


def faxina():
    responsaveis = {}
    print('Limpeza dos comodos da semana\n')
    for elemen in dia:
        responsaveis[elemen] = random.choices(caponeano, k=2)
        print(f'{elemen}: {responsaveis[elemen][0]} e {responsaveis[elemen][1]}')    

def grama():
    cortador = random.choice(caponeano)
    print(f'Cortar grama: {cortador}')


def addDog():
    diaDogs = {'segunda': [],'terça': [],'quarta': [],'quinta': [],'sexta': [], 'sabado': [], 'domingo':[]}
    nome = str(input('Digite seu nome: '))
    diaEscolhido = str(input('Digite o dia para passear com as dog: '))

    if len(diaDogs[diaEscolhido]) < 2:
        diaDogs[diaEscolhido].append(nome)
    else:
        print(f'{diaEscolhido} já está cheio')
    print(diaDogs)        


listc = []
def listacompras():
    global listc
    ans = input("Você quer ver a lista de compras ou adicionar algo? (ver/adicionar)\n").lower().strip()
    if ans == "ver":
        print(listc)
    elif ans == "adicionar":
        item = input("O que será adicionado?")
        listc = listc.append(item)
    else:
        print("Para de ser burro e escreve a resposta no formato certo")
##def main():
##    token1 = "6109792618:AAESMhq22CTD6yq113VZvMC2OgJ7V1aMrAM"
##    updater = tl.Updater(token1)
##    dp = updater.dispatcher
##
##    dp.add_handler(tl.CommandHandler('mudar', mudar, pass_args=True))
##    dp.add_handler(tl.CommandHandler('escolhido', escolhido))
##    dp.add_handler(tl.CommandHandler('faxina', faxina))
##    dp.add_handler(tl.CommandHandler('grama', grama))
##    dp.add_handler(tl.CommandHandler('addDog', addDog))
##    dp.add_handler(tl.CommandHandler('listacompras', listacompras))
##
##    updater.start_polling()
##    updater.idle()
##
#if __name__ == '__main__':
#    main()

##mudar()
escolhido()
#faxina()
##grama()
##addDog()
#listacompras()
##sistemadepontos()
