import sublime, sublime_plugin
import webbrowser, pprint, re

settings = sublime.load_settings(__name__ + '.sublime-settings')

# location: he
class PrevuCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.find(settings.get('code') + '(.*)$', 0, sublime.IGNORECASE)
        if regions:
            region = re.sub(settings.get('code'), '', self.view.substr(regions), re.IGNORECASE)
            url = settings.get('url') + '/' + region.strip()
            sublime.status_message('Opening: ' + url)
            webbrowser.open_new(url)
        else:
            sublime.status_message('No preview location found.')