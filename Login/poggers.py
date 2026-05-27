import customtkinter

#import PIL

def click():
    user_digitado = user.get()
    senha_digitada = senha.get()
    print(user_digitado)
    print(senha_digitada)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text='LOGIN', width=40, height=28, fg_color='transparent')
texto.pack(padx= 10, pady=10)



user = customtkinter.CTkEntry(janela, placeholder_text="Seu Usuário")
user.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

butao = customtkinter.CTkButton(janela, text= "Confirmar", command=click, fg_color="green")
butao.pack()

janela.mainloop()