from commands.list_command import ListCommand, ListCommandSwitches
from commands.add_command import AddCommand, AddCommandSwitches
from commands.delete_command import DeleteCommand, DeleteCommandSwitches

class CommandProcessor:
    def __init__(self):
        self.commands = {
            "l": ListCommand(),
            "a": AddCommand(),
            "d": DeleteCommand()
        }

    def main(self):
        GREEN = '\033[92m'
        RESET = '\033[0m'
        while True:
            command_line_input = input(f"{GREEN}Enter command: {RESET}")
            command, switches = self.parse_command(command_line_input)
            command_obj = self.commands[command]

            if not command_obj:
                print(f"Command {command} is not available.")
                continue

            self.execute_command(command_obj, switches)
            command_obj.reset()

    def parse_command(self, command_line_input):
        switches = {}

        tokens = [
            token for token in command_line_input.split(" ") if token]
        command = tokens[0]

        switch_indices = [i for i, token in enumerate(
            tokens[1:]) if token.startswith("-")]

        for i, index in enumerate(switch_indices):
            switch = tokens[index + 1]
            if i < len(switch_indices) - 1:
                argument = tokens[index + 2: switch_indices[i + 1] + 1]
            else:
                argument = tokens[index + 2:]

            arg_str = " ".join(argument)
            switches[switch] = arg_str.replace('"', '')

        return command, switches

    def execute_command(self, command_obj, switches):
        # if isinstance(command_obj, ListCommand):
        #     filtering_switches = [
        #         s for s in switches if s in ListCommandSwitches.get_filtering_switches()]
        #     if len(filtering_switches) > 1:
        #         print("Error: Only one filtering switch is allowed.")
        #         return

        for switch in sorted(switches, key=lambda s: command_obj.get_precedence(s)):
            method = self.get_method(command_obj, switch)
            if method:
                param = switches[switch]
                method(param) if param else method()

        if "-v" not in switches and isinstance(command_obj, ListCommand):
            command_obj.list()

    def get_method(self, command_obj, switch):
        switch_enum = type(command_obj).__name__ + "Switches"
        try:
            enum_class = globals()[switch_enum]

            method_name = None
            for name, member in enum_class.__members__.items():
                if member.value == switch:
                    method_name = name
                    break

            if not method_name:
                print(f"Switch '{switch}' not found in {switch_enum}")
                return None

            method = getattr(command_obj, method_name.lower(), None)
            return method
        except KeyError as e:
            print(f"KeyError: {e}")
            return None
        except AttributeError as e:
            print(f"AttributeError: {e}")
            return None


cp = CommandProcessor()