import os

# Set your api tokens and proxy through environmental variables
# (add lines to your .bashrc and restart terminal):
# export WORDLE_REFEREE_BOT_TOKEN='XXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

token = os.getenv('WORDLE_REFEREE_BOT_TOKEN')
assert token is not None, 'Problem in reading WORDLE_REFEREE_BOT_TOKEN variable. Read tokens.py for information'
