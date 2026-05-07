import random
import string
import subprocess

try:
    letter = random.choice(string.ascii_letters)

    with open("text.txt", "a") as file:
        file.write(letter + "\n")

    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"Added letter {letter}"],
        check=True
    )
    subprocess.run(["git", "push"], check=True)

    print(f"Successfully pushed: {letter}")

except Exception as e:
    print("Error:", e)