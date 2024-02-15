# importando a biblioteca de regular expressions
import re

from tkinter import *
from tkinter import ttk

# essa função será usada para separar a string de endereço em rua/avenida e número
def address_formatter(address_string):

    # aqui iniciamos um bloco try/except para tratar possíveis erros
    try:
        # essa será a lista que armarzenará as informações separadas
        address = []

        # esse dicionário será usado para armazenar as REs buscadas na string
        id_pattern = {
            # RE para av. ou rua
            'av_pattern': r'^\D+\d+(?=\D+\d+$)|[^\W\d][\D\s]+[^\s\W\d]',
            # RE para  o número (com ou sem letra)
            'number_pattern': r'(?=\D+\d+)\b[^\W]\D{,3}\b\d+$|^\d+\w?\b|\d+\s?\w?\b$',
        }

        # iterando através da lista de REs para separar as informações
        for pattern in id_pattern.values():     
            # faz a busca individualmente através das REs fornecidas
            add_element = re.findall(pattern, address_string)
            # adiciona os elementos encontrados na lista vazia
            address.extend(add_element) if len(add_element) else address.extend(['não informado'])
        

        # a função retorna as informações na mesma lista
        formatted_string.config(state='normal')
        formatted_string.delete(1.0, END)  # Limpar o texto anterior
        formatted_string.insert(END, f"Endereço formatado:\n\n")
        formatted_string.insert(END,  "Rua: ")
        formatted_string.insert(END, '\nNúmero: '.join(address))  # Exibir a lista formatada na caixa de texto
        formatted_string.config(state='disabled')
    
    # Tratamento para erros da biblioteca "re"
    except re.error as e:

        # caso haja algum erro com a RE, ele será informado ao usuário
        print('Erro ao processar expressão regular:', e)
        return
    
    except TclError as e:
        # Caso haja algum erro relacionado à interface gráfica, ele também é informado
        print('Erro na interface gráfica:', e)
    
    # Tratamento para outros erros inesperados
    except Exception as e:
        # caso haja outro tipo de erro, também é informado ao usuário
        print('Ops! Ocorreu um erro inesperado:', e)
        return
    
def close_window(window):
    window.destroy()

def clear_input(input, output):
    input.delete(1.0, END)
    output.config(state='normal')
    output.delete(1.0, END)
    output.config(state='disabled')

def button_hover_enter(btn):
    btn.config(bg=ui_font_color_hover)

def button_hover_leave(btn):
    btn.config(bg=ui_btn_color)

root = Tk()  # criando janela principal
root.title('PWC - formatador de endereços')
frm = ttk.Frame(root, padding=10)
root.geometry('650x650')
root.resizable(False, False)

ui_font = ('Verdana', 10)
ui_main_title_font_bold = ('Verdana', 14, 'bold')
ui_title_font_bold = ('Verdana', 12, 'bold')
ui_font_button = ('Verdana', 11)
ui_font_color = 'white'
ui_btn_color = '#363636'
ui_font_color_hover = '#303030'
ui_blocked_font_color = '#8c8b8b'

root.config(
    background='#262626',
)

guidance_text = Label(root, 
        text='FORMATADOR DE ENDEREÇOS', 
        font=ui_main_title_font_bold,
        fg=ui_font_color,
        background=root.cget('background'),
    )
guidance_text.grid(column=0, row=0, padx=30, pady=10, columnspan=3)

user_input_text = Label(root, 
        text='INPUT:', 
        font=ui_title_font_bold,
        fg=ui_font_color,
        background=root.cget('background'),
    )
user_input_text.grid(column=0, row=2, padx= 30, pady=30, sticky=(N))

user_input = Text(root,
        width=30, 
        height=18, 
        font=ui_font,
        bd=0,
        fg=ui_font_color,
        bg='#363636'
    )
user_input.grid(column=0, row=3, padx=30, pady=20)
user_input.config(
    padx=10, pady=10
)

output_text = Label(root,
        text='OUTPUT:', 
        font=ui_title_font_bold,
        fg=ui_font_color,
        background=root.cget('background'),
    )
output_text.grid(column=1, row=2, columnspan=2, padx=50, pady=30, sticky=(S))

formatted_string = Text(root, 
        state='disabled', 
        width=30, 
        height=18,
        font=ui_font,
        bd=0,
        fg=ui_font_color,
        bg='#363636'
    )
formatted_string.grid(column=1, row=3, columnspan=2, padx=30, pady= 20)
formatted_string.config(
    padx=10, pady=10
)

format_button = Button(root,  
        text="FORMATAR", 
        command=lambda: address_formatter(user_input.get(1.0, END)),
        height=1,
        width=62, 
        font=ui_font_button, 
        bg=ui_btn_color,
        bd=0,
        fg=ui_font_color,
    )
format_button.grid(column=0, row=4, padx=5,  pady=5, columnspan=3)
format_button.config(
    padx=7, pady=7
)
format_button.bind('<Enter>', lambda x: button_hover_enter(format_button))
format_button.bind('<Leave>', lambda x: button_hover_leave(format_button))

clr_button = Button(root, 
        text='LIMPAR', 
        command=lambda: clear_input(user_input ,formatted_string),
        height=1,
        width=62, 
        font=ui_font_button, 
        bg=ui_btn_color,
        bd=0,
        fg=ui_font_color,
    )
clr_button.grid(column=0, row=5, padx=5, pady=5, columnspan=3)
clr_button.config(
    padx=7, pady=7
)
clr_button.bind('<Enter>', lambda x: button_hover_enter(clr_button))
clr_button.bind('<Leave>', lambda x: button_hover_leave(clr_button))

ext_button = Button(root, 
        text='SAIR', 
        command=lambda: close_window(root),
        height=1,
        width=62, 
        font=ui_font_button, 
        bg=ui_btn_color,
        bd=0,
        fg=ui_font_color,
    )
ext_button.grid(column=0, row=6, padx=5, pady=5, columnspan=3)
ext_button.config(
    padx=7, pady=7
)
ext_button.bind('<Enter>', lambda x: button_hover_enter(ext_button))
ext_button.bind('<Leave>', lambda x: button_hover_leave(ext_button))

root.mainloop()