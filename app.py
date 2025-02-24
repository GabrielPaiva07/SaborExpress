import os

restaurantes = [{'nome': 'Bistro da Lú', 'categoria':'japonesa', 'ativo':False}, 
                {'nome': 'Pizza Suprema', 'categoria':'italiana', 'ativo':True},
                {'nome': 'Cantina da Maria', 'categoria':'mineira', 'ativo':False}
]


def exibir_nome_do_programa():
      print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alterar estado do restaurante')
      print('5. Sair')

def voltar_menu():
      input('Pressione Enter para continuar...')
      main()

def opcao_invalida():
      print('Opção Invalida!\n')
      voltar_menu()

def exibir_subtitulo(texto):
      os.system('cls')
      linha = '*' * len(texto)
      print(linha)
      print(texto)
      print(linha)
      print()


def cadastar_novo_restaurantes():
      exibir_subtitulo('Cadastrar novo Restaurante')
      nome_do_restaurante = input('Digite o nome do restaurante:')
      categoria = input(f'Digite a categoria do restaurante do {nome_do_restaurante} (ex: japonesa, italiana, mineira): ')
      dados_do_restaurante =  {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
      print(f'O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
      restaurantes.append(dados_do_restaurante)
      voltar_menu()

def listar_restaurantes():
      exibir_subtitulo('Listando restaurantes')
      print ('Nome do restaurante'.ljust(22), '| Categoria'.ljust(22), '| Status')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_menu()

def ativar_restaurante():
      exibir_subtitulo('Ativar Restaurante')
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
      exibir_subtitulo("Finalizando aplicação")
      
def escolher_opcao():
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
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()


if __name__ == '__main__':
      main()

