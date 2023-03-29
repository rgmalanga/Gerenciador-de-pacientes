# Importando as Bibliotecas Necessárias
import tkinter as tk
import tkinter.messagebox as messagebox
import json

# Carregando o arquivo utilizado como Banco de Dados
with open('dados.json', 'r') as arquivo_json:
    BD = json.load(arquivo_json)

# Implementação das funções necessárias

def registrar_paciente(Nome, Sobrenome, Data_de_Nascimento, CPF, Sexo, endereco=None, Status='Ativo'):
    if not all([Nome, Sobrenome, Data_de_Nascimento, CPF, Sexo, Status]):
        print("Todos os argumentos obrigatórios devem ser preenchidos.")
        messagebox.showwarning("Aviso", "Todos os argumentos obrigatórios devem ser preenchidos.")
        return
    for paciente in BD:
        if 'CPF' in paciente and paciente['CPF'] == CPF:
            print(f"CPF {CPF} já está cadastrado no sistema.")
            messagebox.showwarning("Aviso", f"CPF {CPF} já está cadastrado no sistema.")
            return
    paciente = {'Nome': Nome, 'Sobrenome': Sobrenome, 'Data de nascimento': Data_de_Nascimento, 'CPF': CPF, 'Sexo': Sexo,
     'Endereco': endereco, 'Status':Status}
    BD.append(paciente)
    print(f"Paciente {Nome, Sobrenome} cadastrado.")
    messagebox.showwarning("Aviso", f"Paciente {Nome, Sobrenome} cadastrado.")

def visualizar_pacientes():
    print(BD)   

def pesquisa_paciente_pelo_nome(Nome):
        pacientes = []
        for i, paciente in enumerate(BD):
            if paciente['Nome'] == Nome:
                pacientes.append(paciente)
        if pacientes:
            return pacientes
        else:
            print(f"Paciente com nome {Nome} não encontrado.")
            messagebox.showwarning("Aviso", f"Paciente com nome {Nome} não encontrado.")
            return None

def pesquisa_paciente_pelo_cpf(CPF):
    for i, paciente in enumerate(BD):
        if paciente['CPF'] == CPF:
            return paciente
    return None

def atualizar_paciente(paciente_cpf, nome=None, Sobrenome = None, data_nascimento=None, cpf=None, sexo=None, endereco=None, status=None):
    paciente = paciente_cpf
    if nome:
        paciente['Nome'] = nome
    if Sobrenome:
        paciente['Sobrenome'] = Sobrenome
    if data_nascimento:
        paciente['Data de Nascimento'] = data_nascimento
    if cpf:
        paciente['CPF'] = cpf
    if sexo:
        paciente['Sexo'] = sexo
    if endereco:
        paciente['Endereco'] = endereco
    if status:
        paciente['Status'] = status
    print(f"Dados de {paciente['Nome'], paciente['Sobrenome']} atualizados com sucesso.")
    tk.messagebox.showwarning("Aviso", f"Dados de {paciente['Nome'], paciente['Sobrenome']} atualizados com sucesso.")

# Implementação da GUI

class GerenciadorDepacientes:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de pacientes")

        self.label_name = tk.Label(master, text="Nome")
        self.label_name.grid(row=0, column=0)
        self.Entry_name = tk.Entry(master)
        self.Entry_name.grid(row=0, column=1)

        self.label_Sobrenome = tk.Label(master, text="Sobrenome")
        self.label_Sobrenome.grid(row=1, column=0)
        self.Entry_Sobrenome = tk.Entry(master)
        self.Entry_Sobrenome.grid(row=1, column=1)

        self.label_data_nascimento = tk.Label(master, text="Data de Nascimento (dd/mm/aaaa)")
        self.label_data_nascimento.grid(row=2, column=0)
        self.Entry_data_nascimento = tk.Entry(master)
        self.Entry_data_nascimento.grid(row=2, column=1)

        self.label_CPF = tk.Label(master, text="CPF (Apenas números)")
        self.label_CPF.grid(row=3, column=0)
        self.Entry_CPF = tk.Entry(master)
        self.Entry_CPF.grid(row=3, column=1)

        self.label_Sexo = tk.Label(master, text="Sexo (Masculino/Feminino)")
        self.label_Sexo.grid(row=4, column=0)
        self.Entry_Sexo = tk.Entry(master)
        self.Entry_Sexo.grid(row=4, column=1)

        self.label_endereco = tk.Label(master, text="Endereço (Opcional)")
        self.label_endereco.grid(row=5, column=0)
        self.Entry_endereco = tk.Entry(master)
        self.Entry_endereco.grid(row=5, column=1)

        self.label_status = tk.Label(master, text="Status (Ativo/Inativo)")
        self.label_status.grid(row=6, column=0)
        self.Entry_status = tk.Entry(master)
        self.Entry_status.grid(row=6, column=1)

        self.register_button = tk.Button(master, text="Cadastrar", command=self.cadastrar)
        self.register_button.grid(row=7, column=0)

        self.search_button = tk.Button(master, text="Consultar pelo nome", command=self.busca)
        self.search_button.grid(row=7, column=1)

        self.update_button = tk.Button(master, text="Editar informações do paciente", command=self.atualizar)
        self.update_button.grid(row=7, column=2)

        self.view_button = tk.Button(master, text ='Visualizar Pacientes cadastrados', command = self.visualizar)
        self.view_button.grid(row=7, column = 3)

        self.clear_button = tk.Button(master, text ='Limpar campos', command = self.limpar)
        self.clear_button.grid(row=1, column = 3)

    def cadastrar(self):
        name = self.Entry_name.get()
        Sobrenome = self.Entry_Sobrenome.get()
        data_nascimento = self.Entry_data_nascimento.get()
        CPF = self.Entry_CPF.get()
        Sexo = self.Entry_Sexo.get()
        endereco = self.Entry_endereco.get()
        status = self.Entry_status.get()
        registrar_paciente(name, Sobrenome, data_nascimento, CPF, Sexo, endereco, status)
        self.Entry_name.delete(0, tk.END)
        self.Entry_Sobrenome.delete(0, tk.END)
        self.Entry_data_nascimento.delete(0, tk.END)
        self.Entry_CPF.delete(0, tk.END)
        self.Entry_Sexo.delete(0, tk.END)
        self.Entry_endereco.delete(0, tk.END)
        self.Entry_status.delete(0, tk.END)

    def busca(self):
        nome = self.Entry_name.get()
        pacientes = pesquisa_paciente_pelo_nome(nome)
        if pacientes:
            janela_pesquisa = tk.Toplevel()
            janela_pesquisa.title("Pesquisa por Nome")
            for i in range(len(pacientes)):
                label_dados = tk.Label(janela_pesquisa, text=str(pacientes[i]))
                label_dados.grid(row=i, column=0)
        else:
            return None

    def atualizar(self):
        name = self.Entry_name.get()
        Sobrenome = self.Entry_Sobrenome.get()
        data_nascimento = self.Entry_data_nascimento.get()
        CPF = self.Entry_CPF.get()
        Sexo = self.Entry_Sexo.get()
        endereco = self.Entry_endereco.get()
        status = self.Entry_status.get()
        paciente = pesquisa_paciente_pelo_cpf(CPF)
        atualizar_paciente(paciente, name, Sobrenome, data_nascimento, CPF, Sexo, endereco, status)

    def visualizar(self):
        janela_nova = tk.Toplevel()
        janela_nova.title("Pacientes Cadastrados")

        for i in range(len(BD)):
            print(BD[i])
            label_dados = tk.Label(janela_nova, text = BD[i])
            label_dados.grid(row = i, column = 0)

    def limpar(self):
        self.Entry_name.delete(0, tk.END)
        self.Entry_Sobrenome.delete(0, tk.END)
        self.Entry_data_nascimento.delete(0, tk.END)
        self.Entry_CPF.delete(0, tk.END)
        self.Entry_Sexo.delete(0, tk.END)
        self.Entry_endereco.delete(0, tk.END)
        self.Entry_status.delete(0, tk.END)

root = tk.Tk()
app = GerenciadorDepacientes(root)
root.mainloop()

# Salvar os novos dados no Banco de dados

with open('dados.json', 'w') as arquivo_json:
    json.dump(BD, arquivo_json)