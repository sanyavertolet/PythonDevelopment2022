import cmd
import importlib
import pynames
import shlex

class NameGen(cmd.Cmd):
    language = pynames.LANGUAGE.NATIVE
    prompt = '(NameGen) '   

    def do_language(self, args):
        args = shlex.split(args)[0]
        if args == 'RU':
            self.language = pynames.LANGUAGE.RU
            print('Language is set to Russian.')
        elif args == 'EN':
            self.language = pynames.LANGUAGE.EN
            print('Language is set to English.')
        else:
            self.language = pynames.LANGUAGE.NATIVE
            print('Language is set to Native.')


    def do_generate(self, args):
        AbstractGenerators = ['FromTablesGenerator', 'FromListGenerator', 'FromCSVTablesGenerator']
        args = shlex.split(args)
        module = importlib.import_module(f'pynames.generators.{args[0].lower()}')
        if args[0] == 'elven' and len(args) > 1:
            generator = args[1] + 'NamesGenerator'
        elif args[0] == 'iron_kingdoms' and len(args) > 1:
            generator = args[1] + 'FullnameGenerator'
        else:
            generator = [gen for gen in dir(module) if gen.endswith('Generator') and gen not in AbstractGenerators][0]
        generator = getattr(module, generator)
        gender = pynames.GENDER.FEMALE if args[-1] == 'female' else pynames.GENDER.MALE
        try:
            name = generator().get_name_simple(gender=gender, language=self.language)
        except:
            name = generator().get_name_simple(gender=gender)
        print(name)


    def do_info(self, args):
        pass

NameGen().cmdloop()
