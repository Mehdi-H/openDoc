import sublime, sublime_plugin
import webbrowser
import os

dic = {
    "python": "https://docs.python.org/3/search.html?q=%s",
    "php": "https://php.net/manual/fr/function.%s",
    "html": "http://www.w3schools.com/jsref/dom_obj_%s.asp",
    "css": "http://www.w3schools.com/cssref/css3_pr_%s.asp",
    "scss": "http://compass-style.org/search/?q=%s",
}

class OpenDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = ""
        for region in self.view.sel():
            selection += self.view.substr(region)
            if len(selection) == 0:
                sublime.error_message("Vous devez mettre un mot en surbrillance pour le rechercher.")
            else:
                pack = self.view.settings().get('syntax')
                webbrowser.open(getOnlineLibrary(dic,getLanguage(pack)) % selection)

def getLanguage(str):
    return os.path.basename(str).split('.')[0].lower()

def getOnlineLibrary(d,l):
    return d[l]
