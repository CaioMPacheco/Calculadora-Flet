import flet as ft

def main(page: ft.Page):

    page.window.height = 350
    page.window.width = 300
    def button_clicked(e):
        nonlocal expression
        if e.control.text == "=":
            try:
                expression = str(eval(expression))  # Avalia a expressão
            except:
                expression = "Error"
        elif e.control.text == "C":
            expression = ""  # Limpa a expressão
        else:
            expression += e.control.text
        result.value = expression
        page.update()

    expression = ""
    
    # Resultado da calculadora
    result = ft.Text(value=expression, size=45, text_align=ft.TextAlign.RIGHT)
    
    # Layout da calculadora
    page.add(
        ft.Column([
            ft.Container(
                content=result,
                padding=10
            ),
            ft.Row([
                ft.ElevatedButton(text="7", on_click=button_clicked),
                ft.ElevatedButton(text="8", on_click=button_clicked),
                ft.ElevatedButton(text="9", on_click=button_clicked),
                ft.ElevatedButton(text="/", on_click=button_clicked),
            ]),
            ft.Row([
                ft.ElevatedButton(text="4", on_click=button_clicked),
                ft.ElevatedButton(text="5", on_click=button_clicked),
                ft.ElevatedButton(text="6", on_click=button_clicked),
                ft.ElevatedButton(text="*", on_click=button_clicked),
            ]),
            ft.Row([
                ft.ElevatedButton(text="1", on_click=button_clicked),
                ft.ElevatedButton(text="2", on_click=button_clicked),
                ft.ElevatedButton(text="3", on_click=button_clicked),
                ft.ElevatedButton(text="-", on_click=button_clicked),
            ]),
            ft.Row([
                ft.ElevatedButton(text="C", on_click=button_clicked),
                ft.ElevatedButton(text="0", on_click=button_clicked),
                ft.ElevatedButton(text="=", on_click=button_clicked),
                ft.ElevatedButton(text="+", on_click=button_clicked),
            ])
        ])
    )

ft.app(target=main)
