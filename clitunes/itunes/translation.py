from __future__ import print_function

import sys

import subprocess, shlex
from ..translation import Translator

class iTunesTranslator(Translator):
    # Mapping of custom commands
    commands = {
        'next': 'to next track',
        'skip': 'to next track',

        'previous': 'to previous track',
        'prev': 'to previous track',

        'ff': 'to fast forward',
        'rw': 'to rewind'
    }

    base_command = "osascript -e 'tell application \"iTunes\" {0}'"

    unknown_command_error = 'The variable {0} is not defined.'
    unknown_error = "An unexpected iTunes error occured. Details are as follows:\n{0}"

    def parse(self, command):
        if command in self.commands:
            command = self.commands[command]
        else:
            command = 'to {0}'.format(command)

        return self.base_command.format(command)

    def execute(self, command):
        process = subprocess.Popen(shlex.split(command),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

        return_code = process.wait()

        if return_code != 0:
            error = process.stderr.read()
            unknown_command = unknown_command_error.format(command_name)

            if unknown_command in error:
                print('{0} is an unsupported command.'.format(command_name), file=sys.stderr)
            else:
                print(unknown_error.format(error), file=sys.stderr)

        return return_code

