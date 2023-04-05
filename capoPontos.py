import random
import telebot

chaveAPI = 'sua_chave_API_telegram'
bot = telebot.TeleBot(chaveAPI)

olimpo = ['lm', 'xulapa', 'waze', 'soca']
fora = ['xv']
dentro = ['pesado', 'melody', 'bixo']

class limparBanheiro:
    def __init__(self, olimpo, fora, dentro):
        self.olimpo = olimpo
        self.fora = fora
        self.dentro = dentro
        self.bOlimpo = []
        self.bFora = []
        self.bDentro = []

    def qtdQuartos(self):
        self.maiorQuarto = self.olimpo
        self.banheiro = ''
        for self.moradores in zip(self.olimpo, self.fora, self.dentro):
            if len(self.maiorQuarto) < len(self.olimpo):
                self.maiorQuarto = self.olimpo
            elif len(self.maiorQuarto) < len(self.fora):
                self.maiorQuarto = self.fora
            elif len(self.maiorQuarto) < len(self.dentro):
                self.maiorQuarto = self.dentro

        self.qtdMaiorQuarto = len(self.maiorQuarto)
    
    def verificar(frase):
        return True
    
   
    def escolhido(self):
        self.contador = 0
        mensagem = f'Cronograma mensal (limpeza dos banheiros)'

        for self.iVezes in range(len(self.olimpo)):
            self.contador += 1            
            if len(self.olimpo) > 0:
                self.escolhidoOlimpo = random.choice(self.olimpo)
                self.olimpo.remove(self.escolhidoOlimpo)
            elif len(self.olimpo) == 0:
                self.olimpo = self.bOlimpo

            if len(self.fora) > 0:
                self.escolhidoFora = random.choice(self.fora)
                self.fora.remove(self.escolhidoFora)
                self.bFora.append(self.escolhidoFora)
            elif len(self.fora) == 0:
                    self.fora = self.bFora   
                    self.ultimoEscolhidoDentro = ''

            if len(self.dentro) > 0:
                self.escolhidoDentro = random.choice(self.dentro)
                self.dentro.remove(self.escolhidoDentro)
                self.bDentro.append(self.escolhidoDentro)
            elif len(self.dentro) == 0:
                self.dentro = self.bDentro

            mensagem += f'\n\nOs escolhidos da semana {self.contador} para limparem os banheiros são:\nOlimpo: {self.escolhidoOlimpo}\nFora: {self.escolhidoFora}\nDentro: {self.escolhidoDentro}\n'           
            
        print(mensagem)

    def livres(self):
        print(self.olimpo)
        print(self.dentro)
        print(self.fora)  

lista = limparBanheiro(olimpo, fora, dentro)
lista.escolhido()


comodos = ['sala', 'sala de estudos','cozinha']
moradores = ['lm', 'pix', 'xulapa', 'pesado', 'waze', 'soca', 'melody', 'bixo']

class limparCasa:
    def __init__(self, comodos, moradores):
        self.comodos = comodos        
        self.moradores = moradores
        self.dupla = []
        self.listaDuplas = []
        self.dia = ['segunda', 'quarta', 'sexta']
        self.dicionario = {}

        for self.caponeano in range(3):
            self.dupla = random.choices(self.moradores, k=2,)
            self.listaDuplas.append(self.dupla)
            if self.dupla[0] in self.moradores and self.dupla[1] in self.moradores:
                self.moradores.remove(self.dupla[0])
                self.moradores.remove(self.dupla[1])
            #print(self.listaDuplas)

    def limpeza(self):
        for self.qtd in range(len(self.dia)):
            self.dicionario[random.choice(self.listaDuplas)]=self.dia[self.qtd]
        print(self.dicionario)    

        
limparCasa(comodos, moradores)            



