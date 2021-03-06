#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mehdi-H
# @Date:   2015-03-04 23:46:58
# @Last Modified by:   Mehdi-H
# @Last Modified time: 2015-03-06 00:25:58

import sublime, sublime_plugin
import webbrowser
import os

# /*==========  Dictionnaires des langages (en minuscule) et documentations  ==========*/

dic = {
    "css": "http://www.w3schools.com/cssref/css3_pr_%s.asp",
    "google": "https://www.google.fr/#q=%s",
    "html": "http://www.w3schools.com/jsref/dom_obj_%s.asp",
    "java": "https://search.oracle.com/search/search?q=%s",
    "javascript": "http://www.w3schools.com/jsref/met_%s.asp",
    "matlab": "http://fr.mathworks.com/help/search.html?qdoc=%s&submitsearch=Search",
    "php": "https://php.net/manual/fr/function.%s",
    "python": "https://docs.python.org/3/search.html?q=%s",
    "sass": "http://compass-style.org/search/?q=%s",
    "scss": "http://compass-style.org/search/?q=%s",
}

class OpenDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = ""
        for region in self.view.sel():
            selection += self.view.substr(region).lower()
            if len(selection) == 0:
                sublime.error_message("Vous devez mettre un mot en surbrillance pour le rechercher.")
            else:
                pack = self.view.settings().get('syntax')
                webbrowser.open(getOnlineLibrary(dic,getLanguage(pack)) % selection)

def getLanguage(str):
    return os.path.basename(str).split('.')[0].lower()

def getOnlineLibrary(d,l):
    if l not in d and (l!="plain text"):
        return d["google"] + ' ' + l
    elif l not in d:
        return d["google"]
    else:
        return d[l]
