import PySimpleGUI as sg


def algoritmo_de_luhn(numero_cartao):
    # Remover espaços em branco e converter pra inteiro
    digitos = [int(digito) for digito in numero_cartao.replace(' ', '')]

    # Passo 1: Dobrar os dígitos a partir do penúltimo (índice - 2) da direita pra esquerda
    for i in range(len(digitos) - 2,  - 1, - 2):
        digitos[i] *= 2
        if digitos[i] > 9:
            digitos[i] -= 9

    # Passo 2: calcular a soma total
    total_soma = sum(digitos)

    # Passo 3: verificar se a soma termina em  0
    return total_soma % 10 == 0


def interface_usuario():
    layout = [
        [sg.Text('Digite o número do cartão de crédito: ')],
        [sg.Input(key='numero_cartao')],
        [sg.Button('Verificar'), sg.Button('Sair')],
        [sg.Text('', key='resultado')],
    ]

    window = sg.Window('Verificador de Cartão de Crédito', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break

        numero_cartao = values['numero_cartao'].replace(' ', '')
        if algoritmo_de_luhn(numero_cartao):
            resultado = 'Seu cartão é válido!'
        else:
            resultado = 'Seu cartão é inválido!'

        window['resultado'].update(resultado)

    window.close()


if __name__ == '__main__':
    interface_usuario()
