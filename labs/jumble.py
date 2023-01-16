

file = open("outline.md")

from pathlib import Path

print(Path("outline.md").read_text().splitlines())

words = ["testing"]

# Pick a random word
