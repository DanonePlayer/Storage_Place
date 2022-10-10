from tkinter import SUNKEN, PhotoImage, ttk, messagebox, RAISED, RIDGE
import tkinter as tk
from tkinter import *
import string
import datetime





class Tela():
    def __init__(self, master):
        self.janela  = master
        self.janela.title("Trabalho Fulero com Luiz")
        self.janela.geometry("1000x520")
        self.janela.resizable(width=0, height=0)
        self.janela.configure(bg="#DEB887")


        self.frm = tk.Frame(self.janela, height=90, bg="#DEB887")
        self.frm.grid(column=0, row=0, padx=20, ipadx=60, sticky=tk.N)

        self.lbl_nome = tk.Label(self.frm, text="Nome", bg="#DEB887")
        self.lbl_nome.grid(column=0, row=0)

        self.entry_nome = tk.Entry(self.frm)
        self.entry_nome.grid(column=0, row=1)

        self.lbl_preço = tk.Label(self.frm, text="Preço", bg="#DEB887")
        self.lbl_preço.grid(column=0, row=2)

        self.entry_preço = tk.Entry(self.frm)
        self.entry_preço.grid(column=0, row=3)


        self.lbl_estoque = tk.Label(self.frm, text="Quantidade", bg="#DEB887")
        self.lbl_estoque.grid(column=0, row=4)

        self.entry_estoque = tk.Entry(self.frm)
        self.entry_estoque.grid(column=0, row=5)

        self.entry_estoque.insert(0, 1)

        self.lbl_codigo = tk.Label(self.frm,text='Codigo', bg="#DEB887")
        self.lbl_codigo.grid(column=0, row=6)

        self.entry_codigo = tk.Entry(self.frm)
        self.entry_codigo.grid(column=0, row=7)

        self.btn_confirmar = tk.Button(self.frm, text="Confirmar", overrelief=SUNKEN, command=self.inserir)
        self.btn_confirmar.grid(column=0, row=8, pady=5)

        self.btn_retirada = tk.Button(self.frm, text="Retirar um Produto", overrelief=SUNKEN, command=self.retirada)
        self.btn_retirada.grid(column=0, row=9, pady=5)

        self.photo_delete = tk.PhotoImage(file="lixeira-de-reciclagem.png")

        self.btn_deletar = tk.Button(self.janela, image=self.photo_delete, command=self.remover)
        self.btn_deletar.grid(column=0, row=0, sticky=tk.NE, pady=157)

        self.photo_add_estoque = tk.PhotoImage(file="adicionar_estoque.png")

        self.bnt_add_estoque = tk.Button(self.janela, image=self.photo_add_estoque, command=self.adicionar_estoque)
        self.bnt_add_estoque.grid(column=0, row=0, sticky=tk.NE, pady=114)

        self.frm_esq = tk.Frame(self.janela, bg="#DEB887")
        self.frm_esq.grid(column=1, row=0)
        
        self.imgicon = tk.PhotoImage(file="a.png", height=222)
        self.janela.iconphoto(False, self.imgicon)


        self.lbl_prod = tk.Label(self.frm_esq, text="Produtos de Estoque", font="Broadway", bg="#7FFFD4", height=6, width=54)
        self.lbl_prod.grid(column=0, row=0)

        self.lblcima = tk.Label(self.frm_esq, bg="#FFD700", width=85, height=2)
        self.lblcima.grid(column=0, row=1)

        self.entry_pesquisa = tk.Entry(self.frm_esq)
        self.entry_pesquisa.grid(column=0, row=1, sticky=tk.E, padx=22)    

        self.photo = PhotoImage(file= "barra-de-pesquisa.png")
        self.photovoltar = PhotoImage(file= "costas.png")

        self.btn_voltar = tk.Button(self.frm_esq, image=self.photovoltar, command=self.consutar)
        self.btn_voltar.grid(column=0, row=1, sticky=tk.E, padx=175)

        self.btn_pesquisar = tk.Button(self.frm_esq, image=self.photo ,command=self.pesquisar)
        self.btn_pesquisar.grid(column=0, row=1, sticky=tk.E, padx=150)  

        produtos = ["Código", "Nome", "Preço", "Estoque"]

        self.tvw = ttk.Treeview(self.frm_esq, columns=produtos, show="headings", height=16)
        self.tvw.grid(column=0, row=2)

        for col in range(len(produtos)):
            self.tvw.heading(produtos[col], text=f"{produtos[col]}")
        
        self.tvw.column(produtos[0], minwidth=0, width=132)
        self.tvw.column(produtos[1], minwidth=0, width=205)
        self.tvw.column(produtos[2], minwidth=0, width=132)
        self.tvw.column(produtos[3], minwidth=0, width=132)


        self.scrtvw1 = ttk.Scrollbar(self.frm_esq, command=self.tvw.yview)
        self.scrtvw1.grid(column=0, row=2, ipady=146, sticky=tk.E)
        self.tvw.configure(yscroll=self.scrtvw1.set)
        

        self.frametvw2 = tk.Frame(self.janela)
        self.frametvw2.grid(column=0, row=0, sticky=tk.S)

        historico = ["Código", "Data", "Estoque"]

        self.tvw2 = ttk.Treeview(self.frametvw2, columns=historico, show="headings")
        self.tvw2.grid()

        for his in range(len(historico)):
            self.tvw2.heading(historico[his], text=f"{historico[his]}")
        
        self.tvw2.column(historico[0], minwidth=0, width=85)
        self.tvw2.column(historico[1], minwidth=0, width=85)
        self.tvw2.column(historico[2], minwidth=0, width=85)

        self.scrtvw2 = ttk.Scrollbar(self.frametvw2, command=self.tvw2.yview)
        self.scrtvw2.grid(column=0, row=0, ipady=86, sticky=tk.E)
        self.tvw2.configure(yscroll=self.scrtvw2.set)
        self.acrescenta_id = 0

        self.consutar()

    def inserir(self):
        key_status = 0
        key = 0
        self.codigo_insere = self.entry_codigo.get()
        nome = self.entry_nome.get()
        preço = self.entry_preço.get()
        quantidade = self.entry_estoque.get()

        dados = [self.codigo_insere, nome, preço, quantidade]

        for dads in dados:
            if dads == "":
                key = 1
        if key == 1:
            messagebox.showinfo("AVISO!", f"Preencha os campos {dads}")

        if key == 0:
            sql_consutar_nome = "SELECT nomes,código FROM produtos;"
            for i in db_consultar(sql_consutar_nome):
                for objetos in i:
                    if nome == objetos:
                        info = messagebox.askquestion("AVISO!",f"Produto: {nome}, Existente, deseja adicionar mais {nome}, ao estoque ?")
                        if info == 'yes':
                                print("a")

                                self.btn_confirmar["state"] = tk.DISABLED
                                self.entry_nome["state"] = tk.DISABLED
                                self.entry_preço["state"] = tk.DISABLED
                                self.entry_codigo["state"] = tk.DISABLED
                                self.btn_retirada["state"] = tk.DISABLED

                                self.frm_baixo = tk.Frame(self.janela, bg="#DEB887")
                                self.frm_baixo.grid(column=0, row=0, sticky=tk.N, padx=26, ipadx=60, pady=196)

                                self.photo_adiciona_produto = tk.PhotoImage(file="adicionar-produto.png")
                                self.btn_adiciona = tk.Button(self.frm_baixo, image=self.photo_adiciona_produto, overrelief=SUNKEN, command=self.retira_voltar, width=50)
                                self.btn_adiciona.pack(side=tk.LEFT)

                                self.photo_retira_volta = tk.PhotoImage(file="seta-esquerda.png")
                                self.btn_retira_volta = tk.Button(self.frm_baixo, image=self.photo_retira_volta, overrelief=SUNKEN, command=self.retira_voltar, width=50)
                                self.btn_retira_volta.pack(side=tk.LEFT)


                                key = 1
                        else:
                            key = 1
                    elif self.codigo_insere == str(objetos):
                        messagebox.showinfo("AVISO!",f"Produto de código:{self.codigo_insere}, Ja existente")
                        key = 1

        if key == 0:
            if self.acrescenta_id > 0:
                sql_inserir = f'INSERT INTO produtos VALUES("{self.codigo_insere}","{nome}","{preço}","{quantidade}", NULL);'

            sql_inserir = f'INSERT INTO produtos VALUES("{self.codigo_insere}","{nome}","{preço}","{quantidade}", NULL);'
            db_inserir(sql_inserir)
            messagebox.showinfo("AVISO!",f"Produto: {nome} , Inserido com Sucesso")
            self.entry_nome.delete(0,'end')
            self.entry_preço.delete(0,'end')
            self.entry_estoque.delete(0,'end')
            self.entry_codigo.delete(0, "end")

            self.insere_historico()

            self.consutar()

    def insere_historico(self):
        data = datetime.datetime.now()
        seleciona_id = f"SELECT ID FROM produtos WHERE código = {self.codigo_insere}"
        print(db_consultar(seleciona_id))
        tupla = db_consultar(seleciona_id)
        for ids in tupla[0]:
            sql_inserir_historico = f'INSERT INTO Historico VALUES("{ids}", "{data}", NULL)'
            db_inserir(sql_inserir_historico)

            # sql_pegar = f"SELECT estoque,código FROM produtos p, Historico h WHERE p.ID = {ids}"
            # for apaga in self.tvw2.get_children():
            #     self.tvw2.delete(apaga)
            # for insere_h in db_consultar(sql_pegar):
            #     self.tvw2.insert("", tk.END, values=(insere_h[1], data, insere_h[0]))





    def adicionar_estoque(self):
        self.selecionado_estoque_novo = self.tvw.selection()
        if len(self.selecionado_estoque_novo) != 1:
            messagebox.showerror("Alerta!", "Selecione um cliente para continuar")
        else:
            self.bloqueiar_botoes()        

            self.frm_baixo_estoque = tk.Frame(self.janela, bg="#DEB887")
            self.frm_baixo_estoque.grid(column=0, row=0, sticky=tk.N, padx=26, ipadx=60, pady=196)

            self.photo_insere_estoque = tk.PhotoImage(file="adicionar-produto.png")
            self.btn_insere_estoque = tk.Button(self.frm_baixo_estoque, image=self.photo_insere_estoque, overrelief=SUNKEN, command=self.confirma_adiciona_estoque, width=50)
            self.btn_insere_estoque.pack(side=tk.LEFT)

            self.photo_insere_volta = tk.PhotoImage(file="seta-esquerda.png")
            self.btn_insere_volta = tk.Button(self.frm_baixo_estoque, image=self.photo_insere_volta, overrelief=SUNKEN, command=self.insere_deposito_voltar, width=50)
            self.btn_insere_volta.pack(side=tk.LEFT)

    def confirma_adiciona_estoque(self):
            estoque_novo = self.entry_estoque.get()
            estoque_antigo = self.tvw.item(self.selecionado_estoque_novo, 'values')[3]
            novo_estoque = int(estoque_antigo) + int(estoque_novo)
            codigo = self.tvw.item(self.selecionado_estoque_novo, 'values')[0]
            sql_update_add_estoque = f'UPDATE produtos SET estoque = {novo_estoque} WHERE código = {codigo}'
            db_atualizar(sql_update_add_estoque)
            self.consutar()
            self.frm_baixo_estoque.destroy()
            self.desbloqueia_botoes()

    def remover(self):
        selecionado = self.tvw.selection()
        selecionado2 = self.tvw2.selection()
        if selecionado:
            if len(selecionado) != 1:
                messagebox.showerror("Alerta!", "Selecione um cliente para continuar")
            else:
                codigo = self.tvw.item(selecionado, 'values')[0]
                info = messagebox.askquestion("Alerta", 'Deseja realmente remover?')
                if info == 'yes':
                    query = f' DELETE FROM produtos WHERE código = {codigo}'
                    db_deletar(query)
                    self.consutar()
                    messagebox.showinfo("AVISO!", f"Cliente: {codigo} removido com sucesso!")
                    self.acrescenta_id + 1
                else:
                    messagebox.showerror("ALERTA!", 'Operação cancelada!')
        elif selecionado2:
            print("fazer")

        self.consutar()

    def pesquisar(self):
        l = 0
        letras_minusculas = list(string.ascii_lowercase)
        letras_maiusculas = list(string.ascii_uppercase)

        pesquisa = self.entry_pesquisa.get()

        for letra in letras_minusculas:
            if letra in pesquisa:
                l = 1
        for letra in letras_maiusculas:
            if letra in pesquisa:
                l = 1

        if l == 1:
            sql_pesquisar = f'SELECT * FROM produtos WHERE nomes LIKE "%{pesquisa}%"'
            for i in self.tvw.get_children():
                self.tvw.delete(i)
            for i in db_consultar(sql_pesquisar):
                self.tvw.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))

        elif l == 0:
            pesquisa = int(pesquisa)
            sql_pesquisar = f'SELECT * FROM produtos WHERE código= {pesquisa}'

            for i in self.tvw.get_children():
                self.tvw.delete(i)
            for i in db_consultar(sql_pesquisar):
                self.tvw.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))


    def retirada(self):
        select = self.tvw.selection()
        if select == ():
            messagebox.showerror("Aviso!", "Escolha um item")
        elif len(select) > 1:
            messagebox.showerror("Aviso!", "Escolha apenas um item")
        else:
            self.frm_baixo = tk.Frame(self.janela, bg="#DEB887")
            self.frm_baixo.grid(column=0, row=0, sticky=tk.N, padx=26, ipadx=60, pady=196)

            self.photo_retira = tk.PhotoImage(file="preparar.png")
            self.btn_confirma_retirada = tk.Button(self.frm_baixo, image=self.photo_retira, overrelief=SUNKEN, command=self.confirma_retirada, width=50)
            self.btn_confirma_retirada.pack(side=tk.LEFT)

            self.photo_retira_volta = tk.PhotoImage(file="seta-esquerda.png")
            self.btn_retira_volta = tk.Button(self.frm_baixo, image=self.photo_retira_volta, overrelief=SUNKEN, command=self.retira_voltar, width=50)
            self.btn_retira_volta.pack(side=tk.LEFT)
            
            self.entry_codigo.delete(0, "end")
            self.entry_estoque.delete(0, "end")
            self.entry_nome.delete(0, "end")
            self.entry_preço.delete(0, "end")

            codigo = self.tvw.item(select, "values")[0]
            
            self.quantidade_estoque = self.tvw.item(select, "values")[3]
            preço_estoque = self.tvw.item(select, "values")[2]
            self.nome_estoq = self.tvw.item(select, "values")[1]



            self.entry_nome.insert(0, self.nome_estoq)
            self.entry_preço.insert(0, preço_estoque)
            self.entry_codigo.insert(0, codigo)
            self.entry_estoque.insert(0, self.quantidade_estoque)

            self.bloqueiar_botoes()

    def insere_deposito_voltar(self):
        self.desbloqueia_botoes()
        self.frm_baixo_estoque.destroy()
        

    def retira_voltar(self):
        self.desbloqueia_botoes()
        self.frm_baixo.destroy()
        

    def confirma_retirada(self):
        nome = self.nome_estoq
        novo_estoque = self.entry_estoque.get()
        quantidade_estoque = int(self.quantidade_estoque)
        novo_estoque = int(novo_estoque)
        if quantidade_estoque >= novo_estoque:
            estoque_atualizado = quantidade_estoque - novo_estoque
            sql_update_estoque = f'UPDATE produtos SET estoque = {estoque_atualizado} WHERE nomes = "{nome}"'
            db_atualizar(sql_update_estoque)
            self.consutar()
            self.retira_voltar()
        else:
            messagebox.showerror("Aviso", "Você tem menos produtos")

        


    def consutar(self):
        sql_consutar_produtos = "SELECT * FROM produtos;"
        for i in self.tvw.get_children():
            self.tvw.delete(i)
        for i in db_consultar(sql_consutar_produtos):
            self.tvw.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))

        sql_consultar_historico = "SELECT código,Data,estoque FROM produtos NATURAL JOIN Historico;"
        for apagaH in self.tvw2.get_children():
            self.tvw2.delete(apagaH)
        for insele_h in db_consultar(sql_consultar_historico):
            self.tvw2.insert("", tk.END, values=(insele_h[0], insele_h[1], insele_h[2]))

    def bloqueiar_botoes(self):
            self.btn_confirmar["state"] = tk.DISABLED
            self.entry_nome["state"] = tk.DISABLED
            self.entry_preço["state"] = tk.DISABLED
            self.entry_codigo["state"] = tk.DISABLED
            self.btn_retirada["state"] = tk.DISABLED
    
    def desbloqueia_botoes(self):
        self.btn_confirmar["state"] = tk.NORMAL
        self.entry_nome["state"] = tk.NORMAL
        self.entry_preço["state"] = tk.NORMAL
        self.entry_codigo["state"] = tk.NORMAL
        self.btn_retirada["state"] = tk.NORMAL
        self.entry_nome.delete(0, "end")
        self.entry_preço.delete(0, "end")
        self.entry_codigo.delete(0, "end")
        self.entry_estoque.delete(0, "end")
    



#criar um arquivo separado só pra isso
import sqlite3
from sqlite3 import Error


def conexao():
    caminho = "/home/carlos.amorim/Downloads/Nova_Pasta/at_tkinter.db"
    try:
        con = None
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)

sql_insert = 'INSERT INTO produtos VALUES(2, "Teste2", 1, 1.9);'

sql_tabela = """
             CREATE TABLE produtos(
             código INT(10) PRIMARY KEY NOT NULL,
             nomes VARCHAR(100) NOT NULL,
             preço INT(20),
             estoque INT(20))
             """

sql_update = 'UPDATE cliente SET nome = "Elias Charizard" WHERE id = 8'
sql_delete = 'DELETE FROM produtos WHERE estoque = "";'
sql_consutar = "SELECT * FROM produtos;"
# print(conexao())

def db_consultar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    except Error as er:
        print(er)

def db_inserir(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Registros inseridos")
    except Error as er:
        print(er)

def db_tabela(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Tabela inserida")
    except Error as er:
        print(er)

def db_atualizar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        print("Atualiza funcionando")
    except Error as er:
        print(er)

def db_deletar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        print("Deletado com Sucesso!")
    except Error as er:
        print(er)

# db_tabela(sql_tabela)
# db_deletar(sql_delete)
# atualizar(sql_update)
# db_inserir(sql_insert)
# for i in db_consultar(sql_consutar):
#     print(i)


janela = tk.Tk()
Tela(janela)
janela.mainloop()