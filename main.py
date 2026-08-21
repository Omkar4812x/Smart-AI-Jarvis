from voice_manager import take_command
from automation import execute

print("Genius: System Online. I am ready.")

while True:
    command = take_command()

    if not command:
        continue

    response = execute(command)

    if response:
        print(response)

    if "exit" in command or "quit" in command:
        print("System shutting down.")
        break
