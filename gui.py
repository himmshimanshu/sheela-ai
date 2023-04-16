import webview

def Gui():
    webview.create_window('Sheela', 'http://127.0.0.1:5500/gui.html')
    webview.start()

Gui()