#/usr/bin/env python

import sys, os

from .itunes.translation import iTunesTranslator

# Ability to provide preference in environment for default command
try:
    default_command = os.environ['CLITUNES_DEFAULT_COMMAND']
except KeyError:
    default_command = 'playpause'

if len(sys.argv) > 1:
    command_name = ' '.join(sys.argv[1:]).lower()
else:
    command_name = default_command

translator = iTunesTranslator()

command = translator.parse(command_name)
sys.exit(translator.execute(command))

