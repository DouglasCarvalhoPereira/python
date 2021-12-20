class TV:
    #Toda classe deve ser inciada com um função __init_, a partir dele todos os objetos recebe os atributos da classe.
    def __init__(self) -> None:
        super().__init__()
        self.cor = 'preto'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'netflix'
        self.volume = 10


#Objeto 1
tv_sala = TV()

#Objeto 2
tv_quarto = TV()

tv_sala.cor = 'Prata'
tv_sala.ligada = True
tv_sala.tamanho = 55
tv_sala.canal = 'Amazon Prime'
tv_sala.volume = '13'


#Alterando atributo das classes - Objeto 1
print(tv_sala.cor,
tv_sala.ligada,
tv_sala.tamanho,
tv_sala.canal,
tv_sala.volume)


