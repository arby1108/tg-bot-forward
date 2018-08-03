import logging
import os
import re
import sys
from configparser import ConfigParser

from telethon import TelegramClient, events
from telethon.tl.functions import channels

logging.basicConfig(format="%(message)s", level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if len(sys.argv) == 1:
    config_file = "config.ini"
elif len(sys.argv) == 2:
    config_file = sys.argv[1]
else:
    sys.exit("Error: command line arguments are not valid.")

config = ConfigParser()
config.read(config_file)

api_id = config.getint("telethon", "api_id")
api_hash = config.get("telethon", "api_hash")
session_name = config.get("telethon", "session_name", fallback="default")

client = TelegramClient(session_name, api_id, api_hash)

forwarder_channels = [client.get_input_entity(c.strip())
                      for c in config.get("forwarder", "channels",
                                          fallback="").split(",")]
recipient = client.get_input_entity(config.get("forwarder", "recipient",
                                               fallback="me").strip())

@client.on(events.NewMessage)
async def forwarder(event):
   
    if event.photo:
        print(event.stringify())
        await client.send_message("t.me/sexitbookdownload", event.message)
    elif event.video:
        await client.send_message("t.me/sexitbookdownload", event.message)
    elif event.video_note:
        await client.send_message("t.me/sexitbookdownload", event.message)
    elif event.gif:
        await client.send_message("t.me/sexitbookdownload", event.message)

    elif event.raw_text:
        print(event.stringify())
 
 

client.start()

print('(Press Ctrl+C to stop this)')
client.run_until_disconnected()
