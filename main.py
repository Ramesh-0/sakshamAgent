from voice import listen
from commands import process_command

print("Voice Dev Bot Started")

while True:

    command = listen()

    if command:
        process_command(command)