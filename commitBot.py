import random 
import string
import subprocess

letter = random.choice(string.ascii_letters)
with open("text.txt", "a") as file:
    file.write(letter + "\n")

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Added letter {letter}"])
subprocess.run(["git", "push"])

print(f"Pushed letter: {letter}")