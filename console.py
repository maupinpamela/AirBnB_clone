#!/usr/bin/python3
import cmd
import sys
import models
import shlex
from models.base_model import BaseModel
"""Command Prompt"""


class HBNBCommand(cmd.Cmd):
    """Class for the command prompt"""
    def emptyline(self):
        pass

    def do_EOF(self, args):
        """Control D will exit program"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves and prints id"""
        if len(args) == 0:
            print("** class name missing ** ")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            newinstance = BaseModel()
            newinstance.save()
            print(newinstance.id)

    def do_show(self, args):
        """ Prints the string of an instance based on class name and id"""

        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            new_dict = models.storage.all()
            if key in new_dict:
                print(new_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""

        args = shlex.split(args)
        if len(args) == 0:
            print("** class missing name **")
        elif args[0] != "BaseModel":
            print("**class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            new_dict = models.storage.all()
            if key in new_dict:
                del new_dict[key]
            else:
                print("** no instance found **")


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
