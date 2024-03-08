import flet as ft

def main(pagina):
    texto = ft.Text("IsaZap") 

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else: 
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entered the chat", size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        campo_mensagem.value = ""
        pagina.update()
    
    campo_mensagem = ft.TextField(label="Type your message: ", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Send", on_click=enviar_mensagem)
    # linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()

    titulo_popup = ft.Text("Welcome to the IsaZap :D")
    nome_usuario = ft.TextField(label="Please enter you name: ")
    botao_entrar = ft.ElevatedButton("Enter Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(open=False,
                            modal=True, 
                            title=titulo_popup, 
                            content=nome_usuario,
                            actions=[ft.ElevatedButton("Start", on_click=entrar_chat)]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Start Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)
