import tkinter as tk
from tkinter import messagebox

class BancoApp:
    def __init__(self, root):
        self.saldo = 0
        self.usuario = None
        self.historico = []
        self.modo_escuro = False
        
        root.title("Sistema Bancário")
        root.geometry("400x600")
        self.root = root
        
        self.configurar_cores()
        
        self.frame_header = tk.Frame(root, bg=self.bg_color, padx=20, pady=10)
        self.frame_header.pack(fill="x", side="top")
        
        self.btn_toggle = tk.Button(self.frame_header, text="Modo Escuro", command=self.toggle_modo, 
                                    font=("Arial", 12), bg="#4682b4", fg="white", relief="solid", bd=1, width=15)
        self.btn_toggle.pack(side="right")

        self.frame_registro = tk.Frame(root, bg=self.bg_color)
        self.frame_registro.pack(pady=50)
        
        tk.Label(self.frame_registro, text="Digite seu nome:", font=("Arial", 12), bg=self.bg_color, fg=self.fg_color).pack()
        self.entry_nome = tk.Entry(self.frame_registro, font=("Arial", 12))
        self.entry_nome.pack(pady=5)
        
        tk.Button(self.frame_registro, text="Registrar", command=self.registrar_usuario, 
                  font=("Arial", 12), bg="#4682b4", fg="white", relief="solid", bd=1).pack(pady=5)
        
        self.frame_principal = tk.Frame(root, bg=self.bg_color)
        self.label_titulo = tk.Label(self.frame_principal, text="", font=("Arial", 16, "bold"), bg=self.bg_color, fg=self.fg_color)
        self.label_saldo = tk.Label(self.frame_principal, text=f"Saldo: R$ {self.saldo:.2f}", font=("Arial", 14), bg=self.bg_color, fg=self.fg_color)
        
        self.entry_valor = tk.Entry(self.frame_principal, font=("Arial", 12))
        self.entry_valor.insert(0, "Digite o valor")
        self.entry_valor.bind("<FocusIn>", self.apagar_texto)
        self.entry_valor.pack(pady=5)
        
        self.btn_depositar = tk.Button(self.frame_principal, text="Depositar", command=self.depositar, font=("Arial", 12), bg="#4682b4", fg="white", relief="solid", bd=1)
        self.btn_sacar = tk.Button(self.frame_principal, text="Sacar", command=self.sacar, font=("Arial", 12), bg="#4682b4", fg="white", relief="solid", bd=1)
        self.btn_consultar = tk.Button(self.frame_principal, text="Consultar Saldo", command=self.consultar_saldo, font=("Arial", 12), bg="#4682b4", fg="white", relief="solid", bd=1)
        self.btn_historico = tk.Button(self.frame_principal, text="Ver Histórico", command=self.mostrar_historico, font=("Arial", 12), bg="#4682b4", fg="white", relief="solid", bd=1)
        
        self.label_alunos = tk.Label(root, text="Alunos: Victor Hugo, Luis Miguel e Miguel Eustáquio", 
                                     font=("Arial", 8), bg=self.bg_color, fg=self.fg_color, anchor="w")
        self.label_alunos.place(x=10, y=550)
    
    def configurar_cores(self):
        if self.modo_escuro:
            self.bg_color = "#2e2e2e"
            self.fg_color = "#ffffff"
        else:
            self.bg_color = "#f0f8ff"
            self.fg_color = "#000000"
    
    def toggle_modo(self):
        self.modo_escuro = not self.modo_escuro
        self.configurar_cores()
        self.atualizar_cores()
    
    def atualizar_cores(self):
        self.root.configure(bg=self.bg_color)
        self.frame_registro.configure(bg=self.bg_color)
        self.frame_principal.configure(bg=self.bg_color)
        self.frame_header.configure(bg=self.bg_color)
        
        self.label_titulo.config(bg=self.bg_color, fg=self.fg_color)
        self.label_saldo.config(bg=self.bg_color, fg=self.fg_color)
        self.label_alunos.config(bg=self.bg_color, fg=self.fg_color)
        
        for widget in [self.entry_nome, self.entry_valor]:
            widget.configure(bg=self.bg_color, fg=self.fg_color)
        
        for btn in [self.btn_depositar, self.btn_sacar, self.btn_consultar, self.btn_historico, self.btn_toggle]:
            btn.configure(bg="#4682b4", fg="white")

    def registrar_usuario(self):
        nome = self.entry_nome.get().strip()
        if not nome:
            messagebox.showerror("Erro", "Por favor, insira um nome válido.")
            return
        
        self.usuario = nome
        self.frame_registro.pack_forget()
        self.label_titulo.config(text=f"Bem-vindo, {self.usuario}!")
        self.label_titulo.pack(pady=10)
        self.label_saldo.pack(pady=10)
        self.entry_valor.pack(pady=5)
        self.btn_depositar.pack(pady=5)
        self.btn_sacar.pack(pady=5)
        self.btn_consultar.pack(pady=5)
        self.btn_historico.pack(pady=5)
        self.frame_principal.pack()
    
    def depositar(self):
        try:
            valor = float(self.entry_valor.get())
            if valor <= 0:
                raise ValueError("O valor deve ser maior que zero.")
            self.saldo += valor
            self.historico.append(f"Depósito: R$ {valor:.2f}")
            self.atualizar_saldo()
            messagebox.showinfo("Depósito", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")
    
    def sacar(self):
        try:
            valor = float(self.entry_valor.get())
            if valor <= 0:
                raise ValueError("O valor deve ser maior que zero.")
            if valor > self.saldo:
                raise ValueError("Saldo insuficiente.")
            self.saldo -= valor
            self.historico.append(f"Saque: R$ {valor:.2f}")
            self.atualizar_saldo()
            messagebox.showinfo("Saque", f"Saque de R$ {valor:.2f} realizado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")
    
    def consultar_saldo(self):
        messagebox.showinfo("Saldo Atual", f"Seu saldo é de R$ {self.saldo:.2f}")
    
    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo: R$ {self.saldo:.2f}")
    
    def mostrar_historico(self):
        if not self.historico:
            messagebox.showinfo("Histórico", "Nenhuma transação realizada até o momento.")
            return
        
        historico_texto = "\n".join(self.historico)
        messagebox.showinfo("Histórico de Transações", historico_texto)
    
    def apagar_texto(self, event):
        if self.entry_valor.get() == "Digite o valor":
            self.entry_valor.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
