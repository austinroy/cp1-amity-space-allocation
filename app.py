#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    Amity>>> add_person <first_name> <last_name> <title> [--accomodate=wantsaccomodation]
    Amity>>> create_room <room_type> <room_name>...
    Amity>>> print_room <room_name>
    Amity>>> reallocate_person <person_identifier> <new_room_name>
    Amity>>> load_people
    Amity>>> print_allocations [-o=filename]
    Amity>>> print_unallocated [-o=filename]
    Amity>>> save_state [--db=sqlite_database]
    Amity>>> load_state [--db=sqlite_database]
    Amity>>> (-i | --interactive)
    Amity>>> (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from amity import Amity
from pyfiglet import figlet_format
from termcolor import cprint


amity = Amity()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd, Amity):
    header = "A m i t y !"
    print cprint(figlet_format(header, font='cosmic'),
                 'green', attrs=['bold', 'blink'])
    intro = """Welcome to Amity Room allocation program! \
        '\n (type help for a list of commands.)

        List of commands
        =================================================
        create_room <Living|Office> <room_name>...
        add_person <first_name> <last_name> <Staff|Fellow> [--accomodate=wantsaccomodation]
        print_room <room_name>
        reallocate_person <person_identifier> <new_room_name>
        load_people
        print_allocations [--o=filename]
        print_unallocated [--o=filename]
        save_state [--db=sqlite_database]
        load_state [--db=sqlite_database]
        quit

        """
    prompt = 'Amity >>> '
    file = None

    @docopt_cmd
    def do_add_person(self, arg):
        """
        Usage: add_person <first_name> <last_name> <title> [--accomodate=wantsaccomodation]
        """
        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        person_title = arg["<title>"]
        if arg["--accomodate"]:
            wants_accomodation = arg["--accomodate"]
        else:
            wants_accomodation = "N"
        print(amity.add_person(first_name, last_name, person_title,
                               wants_accomodation))

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg["<room_type>"]
        for room_name in arg["<room_name>"]:
            print(amity.create_room(room_name, room_type))

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_id> <new_room_name>"""
        person_id = arg["<person_id>"]
        new_room_name = arg["<new_room_name>"]
        print(amity.reallocate_person(person_id, new_room_name))

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <filename>"""
        amity.load_people(arg)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        print(amity.print_room(arg["<room_name>"]))

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=filename]"""
        amity.print_allocations(arg)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--o=filename]"""
        amity.print_unallocated(arg)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=sqlite_database]"""
        amity.save_state(arg)

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state [--db=sqlite_database]"""
        amity.load_state(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
