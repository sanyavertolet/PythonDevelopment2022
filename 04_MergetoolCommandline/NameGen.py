import cmd
import pynames
import shlex

class NameGen(cmd.Cmd):
    language = pynames.LANGUAGE.NATIVE
    

    def do_language(self, args):
        if args == 'RU':
            self.language = pynames.LANGUAGE.RU
        elif args == 'EN':
            self.language = pynames.LANGUAGE.EN
        else:
            self.language = pynames.LANGUAGE.NATIVE


    def do_generate(self, args):
        pass


    def do_info(self, args):
        pass


