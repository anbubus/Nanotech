from browser import document
from browser.widgets.dialog import InfoDialog

def checkpass(n,p):
    if not p:
        InfoDialog("Alert", f"Senha Vazia")
    if not n:
        InfoDialog("Alert", f"Nome Vazio")

    return True