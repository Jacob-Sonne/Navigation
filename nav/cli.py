import sys
import argparse
from core import add_shortcut, remove_shortcut, list_shortcuts, resolve_path

command_list = [
    ("--add", "<path> <name>"),
    ("--")
]

parser = argparse.ArgumentParser(
    prog="Navigation",
    description="Shortcut manager"
)
parser.add_argument('--add', nargs=2, metavar=('PATH', 'NAME'), help='Add a new shortcut')
parser.add_argument('--remove', metavar='NAME', help='Remove an existing shortcut')
parser.add_argument('--list', action='store_true', help='Print all added shortcuts by name and path')
parser.add_argument('--resolve_path', metavar=('NAME'), help='Print the path of a specific shortcut')



def main():
    args = parser.parse_args()

    if args.add:
        path, name = args.add
        add_shortcut(path, name)
        print(f"Add shortcut with name={name}, path={path}")

    elif args.remove:
        name = args.remove
        remove_shortcut(name)
        print(f"Remove shortcut named {name}")

    elif args.list:
        list_shortcuts()
        print("List all shortcuts")

    elif args.resolve_path:
        name = args.resolve_path
        resolve_path(name)
        print(f"Resolve shortcut named {name}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()