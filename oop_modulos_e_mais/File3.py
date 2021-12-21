class TV:
    #Toda classe deve ser inciada com um função __init_, a partir dele todos os objetos recebe os atributos da classe.
    #Passando parametros para a função __init__ eu estou deifinindo como cada OBJETO será iniciado.
    def __init__(self, tamanho) -> None:
        super().__init__()
        self.cor = 'preto'
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal 
        

#Objeto 1
tv_sala = TV(tamanho=10)

#Objeto 2
tv_quarto = TV(tamanho=10)

print(tv_sala.tamanho)

