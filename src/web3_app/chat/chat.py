from threading import Thread
import time
import flet as ft

from web3_app.web3_app import database_new_messages

class Message():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment="start"
        self.controls=[
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(message.user_name)),
                    color=ft.colors.WHITE,
                    bgcolor=self.get_avatar_color(message.user_name),
                ),
                ft.Column(
                    [
                        ft.Text(message.user_name, weight="bold"),
                        ft.Text(message.text,width=200, selectable=True),
                    ],
                    tight=True,
                    spacing=5,
                ),
            ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

thread_generated = False
sended_message = []
def main(page: ft.Page):
    global thread_generated
    global sended_message
    page.horizontal_alignment = "stretch"
    page.title = "Web3"




    def send_message_click(e):
        global sended_message
        new = False
        total_list = database_new_messages.get_all()
        for each_new_message in total_list:
            the_value = total_list[each_new_message]
            if the_value not in sended_message:
                sended_message.append(the_value)
                new = True
        if new:
            page.pubsub.send_all("Message")


    def threaderblock_situation_tracker():
        while True:
            send_message_click("e")
            time.sleep(5)

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    def on_message(the_message):
        global sended_message
        chat.controls = []
        for each_message in sended_message:
            message = Message(each_message[0], each_message[1], "chat_message")
            if message.message_type == "chat_message":
                m = ChatMessage(message)
            elif message.message_type == "login_message":
                m = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
            chat.controls.append(m)
            page.update()

    page.pubsub.subscribe(on_message)
    on_message("hi")
    if not thread_generated:
        print("Threader started")
        Thread(target=threaderblock_situation_tracker).start()
        thread_generated = True




    # Add everything to the page
    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
            
        ),
    )
