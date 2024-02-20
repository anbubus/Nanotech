from browser import document
from browser.widgets.dialog import InfoDialog
from db_connection import get_database as db

def checkpass(n,p):
    if not p:
        InfoDialog("Alert", f"Senha Vazia")
    if not n:
        InfoDialog("Alert", f"Email Vazio")

    return True

#ela ta recebendo n de email, p de senha e d da tabela users 
def verify(n,p,d):
    db = db
    users = db[d]
    for user in users:
        email = user['email']
        password = user['password']
        if n == email and p == password:

            return True
