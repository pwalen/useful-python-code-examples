from time import sleep

text = "Let's randomly select an integer within the given range"

# print the text string above one letter at a time, all on the same line
for letter in text:
    print(letter, end='', flush=True)
    sleep(0.1)