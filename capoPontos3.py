import random
import telegram.ext as tl

banheiros = {'Olimpo': ['Lm', 'Soca', 'Waze', 'Xulapa'], 'Fora': ['Xv'], 'Dentro': ['Pesado', 'Melody', 'Bixo']}
dia = ['segunda', 'quarta', 'sexta']
caponeano = ['Lm', 'Soca', 'Waze', 'Xulapa', 'XV', 'Pesado', 'Melody', 'Bixo']
comodos = ['sala', 'sala de estudos', 'cozinha', 'cozinha de fora', 'varanda']
listc = []

def mudar(update, context):
    args = context.args
    #update.message.reply_text(args)
    if len(args) < 3:
        update.message.reply_text('Você precisa fornecer 3 argumentos: adicionar/remover, quarto e morador')
        return

    add_ou_remover = args[0].lower().strip()
    quarto = args[1].strip().capitalize()
    morador = args[2].strip().capitalize()

    if add_ou_remover == 'adicionar':
        banheiros[quarto].append(morador)
        update.message.reply_text(f'{morador} adicionado ao quarto {quarto}')
    elif add_ou_remover == 'remover':
        if morador in banheiros[quarto]:
            banheiros[quarto].remove(morador)
            update.message.reply_text(f'{morador} removido do quarto {quarto}')
        else:
            update.message.reply_text(f'{morador} não está no quarto {quarto}')
    else:
        update.message.reply_text('Não entendi sua resposta')
    

def banheiro(update, context):
    escolhido = {}
    message = 'limpeza dos banheiros da semana:\n'
    for elemen in banheiros.keys():
        escolhido[elemen] = random.sample(banheiros[elemen], k = 1)
        message += f'{elemen}: {escolhido[elemen][0]}\n'
    update.message.reply_text(message)

def faxina(update, context):
    responsaveis = {}
    message = 'Limpeza dos cômodos da semana\n'
    for elemen in comodos:
        responsaveis[elemen] = random.sample(caponeano, k=2)
        message += f'{elemen}: {responsaveis[elemen][0]}\n'
    update.message.reply_text(message)

def grama(update, context):
    cortador = random.choice(caponeano)
    update.message.reply_text(f'Cortar grama: {cortador}')

def main():
    token1 = "6109792618:AAESMhq22CTD6yq113VZvMC2OgJ7V1aMrAM"
    updater = tl.Updater(token1)
    dp = updater.dispatcher

    dp.add_handler(tl.CommandHandler('mudar', mudar, pass_args=True))
    dp.add_handler(tl.CommandHandler('banheiro', banheiro))
    dp.add_handler(tl.CommandHandler('faxina', faxina))
    dp.add_handler(tl.CommandHandler('grama', grama))
    ##dp.add_handler(tl.CommandHandler('addDog', addDog))
    ##dp.add_handler(tl.CommandHandler('listacompras', listacompras))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
