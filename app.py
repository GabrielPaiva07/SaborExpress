import os

restaurantes = [{'nome': 'Bistro da Lú', 'categoria':'japonesa', 'ativo':False}, 
                {'nome': 'Pizza Suprema', 'categoria':'italiana', 'ativo':True},
                {'nome': 'Cantina da Maria', 'categoria':'mineira', 'ativo':False}
]


def exibir_nome_do_programa():
      '''
      Está função é responsável por exibir o nome do programa

      Print:
      Nome do programa(Sabor Express)
      '''
      print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
      '''
      Esta função é responsável para exibir as opções do programa

      Opções:
      - 1. Cadastrar o Restaurante
      - 2. Listar os retaurantes
      - 3. Alterar os estado(Ativo/Desativado) dos restaurantes
      - 4. Sair da aplicação
      '''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alterar estado do restaurante')
      print('4. Sair')

def voltar_menu():
      input('Pressione Enter para continuar...')
      main()

def opcao_invalida():
      '''
      Está função é responsável pela resposta ao executa um comando errado

      printa (Opção invalida) e retorna ao menu
      
      '''
      print('Opção Invalida!\n')
      voltar_menu()

def exibir_subtitulo(texto):
      '''Esta função é reservada para exibir um subtitulo sempre que chamada
      
      Ela limpa o terminal e logo apos:
      
      Printa:
      O Texto pelo requerimento e faz uma linha de asteriscos ao redor
      '''
      os.system('cls')
      linha = '*' * len(texto)
      print(linha)
      print(texto)
      print(linha)
      print()


def cadastar_novo_restaurantes():
      '''
      Essa função é responsável por cadastrar um novo restaurante
      
      
      Inputs:
      - Nome Do Restaurante
      - Categoria

      Outputs:
      -Adiciona um novo restaurante a lista de restaurantes

      '''
      exibir_subtitulo('Cadastrar novo Restaurante')
      nome_do_restaurante = input('Digite o nome do restaurante:')
      categoria = input(f'Digite a categoria do restaurante do {nome_do_restaurante} (ex: japonesa, italiana, mineira): ')
      dados_do_restaurante =  {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
      print(f'O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
      restaurantes.append(dados_do_restaurante)
      voltar_menu()

def listar_restaurantes():
      '''Esta função é responsável por listar os restaurantes
      
      Lista o restaurante,categoria e o seu status

      Ultiliza um sistema loop for para listar o restaurante dentro do dicionário restaurantes
      retornando seu nome,categoria e se está atiavdo ou não. 
      e logo após, retorna ao menu através da função (voltar_menu)
      '''
      exibir_subtitulo('Listando restaurantes')
      print ('Nome do restaurante'.ljust(22), '| Categoria'.ljust(22), '| Status')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_menu()

def ativar_restaurante():
      '''Esta função é responsável por ativar ou desativar o restaurante
      
      - Inputs:
      - Nome do restaurante

      - Outputs:
      - Retorna o restaurante ativo, caso queria ativar ou desativado, caso queira desativar o restaurante

      '''
      exibir_subtitulo('Alterar estado do Restaurante')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
      restaurante_encontrado = False      
      for restaurante in restaurantes:
            if nome_do_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O Restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O Restaurante {nome_do_restaurante} foi desativado com sucesso'
                  print(mensagem)
      if not restaurante_encontrado:
            print(f'O Restaurante {nome_do_restaurante} não foi encontrado')


      voltar_menu()

      

def  finalizar_app():
      '''
      Está função é responsável para finalizar a aplicação
      Puxa o exibir subtitulo, limpando a área e printando (Finalizando Aplicação) com asteriscos ao redor
      '''
      exibir_subtitulo("Finalizando aplicação")
      
def escolher_opcao():
      '''
      Esta função é responsavel por puxar as funções de acordo com a escolha do usúario.

      Input:
      - Escolha uma opção:

      Outputs:
      - Cadastrar Restaurante
      - Listar Restaurantes
      - Ativar Restaurantes
      - Sair da aplicação
      '''

      try:

            opcao_escolhida = int(input('Escolha uma opção: '))
                  
            if opcao_escolhida == 1:
                  cadastar_novo_restaurantes()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  ativar_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
      '''Está é a função principal da aplicação, responsável pela inicialização dela.
      
      Limpa o terminal e puxa as seguintes funções:
      Para exibir o nome do programa
      Para Exibir as opções
      e para escolhe-las.
      '''
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()


if __name__ == '__main__':
      main()

