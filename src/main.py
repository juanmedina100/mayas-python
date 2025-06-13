import flet as ft


def main(page: ft.Page):
    # page.window_width = 250
    page.bgcolor = ft.colors.BLUE
    page.title = "Maya Flet App"
    counter = ft.Text("0", size=50, data=0)
    caja = ft.Container(
        content=ft.Column(),
        padding=10,
        alignment=ft.alignment.center,
    )
    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()



    def decimal_a_maya(e):
        valor =int(linea1.value)
        if valor == 0:
            return ["𝍩"]  # símbolo de cero

        niveles = []
        while valor > 0:
            resto = valor % 20
            valor //= 20
            if resto == 0:
                niveles.append("𝍩")
            else:
                barras = "━━━━━━━━ " * (resto // 5)
                puntos = "● " * (resto % 5)
                niveles.append(puntos + "\n" + barras)
            respuesta.value = ""
            caja.content.controls.clear()  # Limpiar la caja antes de agregar nuevos controles
            # Recorrer niveles en orden inverso y acumularlos en respuesta.value
            for level in reversed(niveles):  # Invertir el orden
                # respuesta.value += str(level).strip() + "\n"
                caja.content.controls.append(ft.Container(content=ft.Text(str(level).strip(),text_align=ft.TextAlign.CENTER,size=20),bgcolor=ft.Colors.BLACK26, width=140))
            caja.update()

            # respuesta.update()  # Actualizar la interfaz
        

    linea1 = ft.TextField()
    btn = ft.ElevatedButton(
        "Calcular Maya",on_click=decimal_a_maya, bgcolor=ft.colors.GREEN_300
    )
    respuesta = ft.Text()
    respuesta.value = "𝍩"  # símbolo de cero

    col = ft.Column(
        [linea1,btn, respuesta,caja],
    )
    # col.controls.append(ft.Text("Ingrese un número decimal:"))
    page.add(col)

    # page.floating_action_button = ft.FloatingActionButton(
    #     icon=ft.Icons.ADD, on_click=increment_click
    # )
    # page.add(
    #     ft.SafeArea(
    #         ft.Container(
    #             counter,
    #             alignment=ft.alignment.center,
    #         ),
    #         expand=True,
    #     )
    # )


ft.app(main)
