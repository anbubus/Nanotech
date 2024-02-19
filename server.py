from browser import document
from browser.widgets.dialog import InfoDialog
from models import checkpass

def click(ev):

    name = document['name'].value
    password = document['pass'].value


    if checkpass(name, password):
        InfoDialog("Alert", f"Login executado com sucesso, {name}!!!")
document['bt_'].bind("click", click)