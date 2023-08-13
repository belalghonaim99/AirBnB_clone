#!/usr/bin/python3
"""Console module for the AirBnB clone project."""

import cmd
import re

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that defines the command interpreter.
    """

    prompt = "(hbnb) "
    classes = [BaseModel, User, State, City, Amenity, Place, Review]
    class_dict = {c.__name__: c for c in classes}

    def default(self, line):
        """
        Check for <class>.<command>(<args>) syntax.
        <args> can be empty, <id> only, <id> <name> <value>, or <id> <dict>.
        """
        alt_syntax_cmds = {'all', 'count', 'show', 'destroy', 'update'}
        if re.fullmatch(r"^\w{4,9}\.\w{3,7}\(.*\)$", line) is None:
            return
        for cmd in alt_syntax_cmds:
            if cmd in line:
                # params tuple with ('<class>', '<cmd>', '(<args>)')
                params = list(line.partition(cmd))
                params[0] = params[0].strip('.')
                # '(<args>)' becomes list of strings
                params[2] = params[2].strip('()')
                if '{' in params[2] and '}' in params[2]:
                    params[2] = params[2].split(', ', 1)
                else:
                    params[2] = params[2].split(', ')
                params[2] = [arg.strip('"') for arg in params[2]]
                if params[1] == 'all':
                    self.do_all(params[0])
                elif params[1] == 'count':
                    if params[0] not in HBNBCommand().class_dict.keys():
                        print("** class doesn't exist **")
                    else:
                        print(len([v for v in storage.all().values()
                                   if v.__class__.__name__ == params[0]]))
                elif params[1] == 'show':
                    self.do_show(params[0] + ' ' + ' '.join(params[2]))
                elif params[1] == 'destroy':
                    self.do_destroy(params[0] + ' ' + ' '.join(params[2]))
                elif params[1] == 'update':
                    if '{' in params[2] and '}' in params[2]:
                        dict_arg = eval(params[2][1])
                        if isinstance(dict_arg, dict):
                            for key, value in dict_arg.items():
                                # <class> <id> <attr name> <attr value>
                                update_line = ' '.join((params[0], params[2][0], key, str(value)))
                                self.do_update(update_line)
                    else:
                        update_line = params[0] + ' ' + ' '.join(params[2])
                        self.do_update(update_line)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty lines are ignored"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        else:
            new_instance = self.class_dict[args[0]]()
            storage.save()
            print(new_instance.id)

    # Rest of the methods (do_show, do_destroy, do_all, do_update) remain unchanged

if __name__ == "__main__":
    HBNBCommand().cmdloop()
