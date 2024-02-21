from browser import document, window
from browser.widgets.dialog import InfoDialog
from bry.models import checkpass, verify
from bry.db_connection import get_database as db

def click(ev):
    email = document['email'].value
    password = document['password'].value


    if checkpass(email, password):
        if not verify(email, password, "users"):
            InfoDialog("Alert", f"Email ou senha incorretos.")

        if verify(email, password, "users"):
            InfoDialog("Alert", f"Login executado com sucesso, {email}!!")
            window.location.assign("/pages/home.html")

document['bt_'].bind("click", click)
