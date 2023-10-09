# Trabalho - Bruno Fernandes Peixoto e Gabriel Moreira Borges

class Aluno:
    def __init__(self):
        self.Nome = []
        self.Matricula = []
        self.ListaDeProcura = []

    def Inserir_Usuario(self, Nome_a, Matricula_a):
        self.Nome.append(Nome_a)
        self.Matricula.append(Matricula_a)

    def ExibirUsuario(self, mensagem):
        print(mensagem)
        qtde = len(self.Nome)
        for i in range(qtde):
            print(f"{i + 1}) Nome: {self.Nome[i]}; Matricula: {self.Matricula[i]}")

    def PesquisarAlunoNome(self, NomeAluno):
        alunoencontrado = []
        qtde = len(self.Nome)
        for i in range(qtde):
            if self.Nome[i].find(NomeAluno) != -1:
                alunoencontrado.append(i)
        qtde = len(alunoencontrado)
        if qtde == 0:
            print("Aluno não encontrado")
        else:
            for i in range(qtde):
                print(f"Nome: {self.Nome[alunoencontrado[i]]}; Matricula: {self.Matricula[alunoencontrado[i]]}")

    def ExcluirProduto(self):

        with open('alunos.txt', 'r+') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(';')
                qtde = len(dados)

                if qtde == 0:
                    print("Não há produtos cadastrados!")
                else:
                    #ProdutoAExcluir = int(input("Digite o ID do produto que deseja excluir: "))
                    linha.pop(dados[0])
                    linha.pop(dados[1])
                    linha.pop(dados[2])

    def ExcluirProduto(self):
            Id = input("\nID: ")
            confirma = input("Confirma a exclusão de "+Id+"? \ns/n: ")
            confirma.lower()

        if confirma == 's':
            with open("alunos.txt", 'r') as arquivo:
                indexProduto = arquivo.readlines()
                posicao =




    def LimparLista(self, Nome_a, Matricula_a):
        self.Nome.clear()
        self.Matricula.clear()

    def salvar_produto(self, Produto_a, Id_a, Valor_a):
        with open('alunos.txt', 'a') as arquivo:
            arquivo.write(f'{Produto_a}; {Id_a}; {Valor_a}\n')
        arquivo.close()

    def consultar_aluno(self, matricula):
        with open('alunos.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(';')
                if dados[0] == matricula:
                    return f'Matrícula: {dados[0]}\nNome: {dados[1]}\nEndereço: {dados[2]}'
                return 'Aluno não encontrado'

    def teste(self, mensagem):

        with open('alunos.txt', 'r') as arquivo:
            print("Lista de Produtos: ")
            for linha in arquivo:
                dados = linha.strip().split(';')
                qtde = len(dados)
                print(f'{qtde}) Produto: {dados[0]}, ID: {dados[1]}, Preço: R${dados[2]}')
        arquivo.close()

Alu = Aluno()
while True:
    menu = """
        MENU INICIAL

    1 - Inserir Novo Produto
    2 - Exibir Produto(s)
    3 - Excluir Produto(s)
    4 - Excluir Todos os Produto(s)
    5 - Pesquisar Produto(s)
    6 - Sair
"""

    print(menu)
    OpcaoSelecionada = int(input("Digite a opção: "))
    if OpcaoSelecionada == 6:
        break
    elif OpcaoSelecionada == 1:
        Produto_a = input("Digite o nome do Produto: ")
        Id_a = input("Digite o ID do Produto: ")
        Valor_a = input("Digite o preço do Produto: ")
        Alu.salvar_produto(Produto_a, Id_a, Valor_a)
    elif OpcaoSelecionada == 2:
        Alu.teste("\nAlunos Cadastrados: ")
    elif OpcaoSelecionada == 3:
        #ProdutoExcluido = input("Selecione o Aluno que Deseja excluir: ")
        Alu.ExcluirProduto()
    elif OpcaoSelecionada == 4:
        Alu.LimparLista(Nome_a, Matricula_a)
    elif OpcaoSelecionada == 5:
        NomeAluno = input("Digite o nome do Aluno que deseja pesquisar: ")
        Alu.consultar_aluno(Matricula_a)