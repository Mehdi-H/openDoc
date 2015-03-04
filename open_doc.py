import sublime, sublime_plugin
import webbrowser

class OpenDocCommand(sublime_plugin.TextCommand):
	def run(self, edit, url):
		selection = ""
		for region in self.view.sel():
			selection += self.view.substr(region)
		if len(selection) == 0:
			sublime.error_message("Vous devez mettre un mot en surbrillance pour le rechercher.")
		else:
			webbrowser.open(url % selection)