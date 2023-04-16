import webview

def display_html_gui(htmlfile):
    webview.create_window('SHEELA', url=htmlfile, width=800, height=600)
    webview.start()
    htmlfile = 'gui.html'
    display_html_gui(htmlfile)

