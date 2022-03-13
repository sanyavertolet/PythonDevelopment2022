import ast
import difflib
import importlib
import inspect
import sys
import textwrap

def get_functions(prefix, members):
    functions = [(prefix + '.' + member_name, get_abstract_source(member_obj)) for member_name, member_obj in members if inspect.isfunction(member_obj)]
    classes = [(member_name, member_obj) for member_name, member_obj in members if inspect.isclass(member_obj) and not member_name.startswith('__')]
    methods = [(method_name, method_obj) for class_name, class_obj in classes for method_name, method_obj in get_functions(prefix + '.' + class_name, inspect.getmembers(class_obj))]
    return functions + methods

def get_abstract_source(member_obj):
    tree = ast.parse(textwrap.dedent(inspect.getsource(member_obj)))
    for node in ast.walk(tree):
        for attr in ['name', 'id', 'arg', 'arrt']:
            if hasattr(node, attr):
                setattr(node, attr, '_')
    return ast.unparse(tree)


def get_abstract_functions(module_name):
    return get_functions(module_name, inspect.getmembers(importlib.import_module(module_name)))


if len(sys.argv) != 1:
    functions = sum([get_abstract_functions(sys.argv[i]) for i in range(1, len(sys.argv))], [])
    l = []
    for fname1, fsource1 in functions:
        for fname2, fsource2 in functions:
            if fname1 != fname2:
                ratio = difflib.SequenceMatcher(None, fsource1, fsource2).ratio()
                if ratio > 0.95:
                    l.append(' '.join(sorted([fname1, fname2])))
    print('\n'.join(sorted(list(set(l)))))
else:
    print('Usage: python3 file1 [file2...]')

