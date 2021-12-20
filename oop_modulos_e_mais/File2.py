class TV:
    #Toda classe deve ser inciada com um função __init_, a partir dele todos os objetos recebe os atributos da classe.
    def __init__(self) -> None:
        super().__init__()
        self.cor = 'preto'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal 
        

#Objeto 1
tv_sala = TV()

#Objeto 2
tv_quarto = TV()

print(tv_quarto.canal)
tv_quarto.mudar_canal('Amazon Prime')
print(tv_quarto.canal)

