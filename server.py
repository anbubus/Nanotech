from browser import document
from browser.widgets.dialog import InfoDialog
from models import checkpass, verify
from db_connection import get_database as db

def click(ev):
    email = document['email'].value
    password = document['password'].value


    if checkpass(email, password):
        if not verify(email, password, "users"):
            InfoDialog("Alert", f"Email ou senha incorretos.")

        if verify(email, password, "users"):
            InfoDialog("Alert", f"Login executado com sucesso, {email}!!")

document['bt_'].bind("click", click)

