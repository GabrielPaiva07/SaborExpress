from modelos.restaurante import Restaurante


restaurante_bruttus = Restaurante('Bruttus', 'Gourmet')
restaurante_bruttus.receber_avaliacao('João', 5)
restaurante_bruttus.receber_avaliacao('Laís', 4)
restaurante_bruttus.receber_avaliacao('Kaique', 3)
restaurante_pizzaplanet = Restaurante("Pizza Planet", 'Pizza')
restaurante_pizzaplanet.receber_avaliacao('João', 1)
restaurante_pizzaplanet.receber_avaliacao('Laís', 2)
restaurante_pizzaplanet.receber_avaliacao('Kaique', 5)
restaurante_vintage = Restaurante('Vintage', 'Mineira')
restaurante_vintage.receber_avaliacao('João', 5)
restaurante_vintage.receber_avaliacao('Laís', 5)
restaurante_vintage.receber_avaliacao('Kaique', 4)
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()