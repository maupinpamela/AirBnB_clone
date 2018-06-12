#!/usr/bin/python3
import cmd
import sys
import models
from models import storage
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


"""Command Prompt"""


class HBNBCommand(cmd.Cmd):
    """Class for the command prompt"""

    class_names = ["BaseModel", "State", "City",
                   "Review", "Amenity", "Place", "User"]

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
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        else:
            check = 0
            for i in range(len(HBNBCommand.class_names)):
                if args[0] == HBNBCommand.class_names[i]:
                    new_instance = eval(HBNBCommand.class_names[i] + "(" + ")")
                    new_instance.save()
                    print(new_instance.id)
                    check = 1
            if check == 0:
                print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string of an instance based on class name and id"""

        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        check = 0
        for i in range(len(HBNBCommand.class_names)):
            if args[0] != HBNBCommand.class_names[i]:
                check = 1
        if check == 0:
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
        check = 0
        for i in range(len(HBNBCommand.class_names)):
            if args[0] != HBNBCommand.class_names[i]:
                check = 1
        if check == 0:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            new_dict = models.storage.all()
            if key in new_dict:
                del new_dict[key]
            else:
                print("** no instance found **")

    def do_update(self, args):
        """
        Updates an instance based on exact class name and id
        """
        args = shlex.split(args)
        if len(args) == 4:
            class_id = "{}.{}".format(args[0], args[1])
            setattr(storage.all()[class_id], args[2], args[3])
            storage.all()[class_id].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_all(self, args):
        """
        do_all - prints string representation of all instances
        """
        temp_dict = models.storage.all()
        if args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        if args == "all":
            for obj in temp_dict:
                print([temp_dict[obj]])
        else:
            for obj in temp_dict:
                print([temp_dict[obj]])

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
