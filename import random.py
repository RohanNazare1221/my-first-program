import random

# List of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is not in what you have, but who you are.",
    "Every sunrise is permission to begin again.",
    "Let ambition be your snooze button.",
    "Begin before comfort wakes up",
    "Start small; momentum handles big."
]

# Pick a random quote
random_quote = random.choice(quotes)

print(" Random Quote of the Day:")
print(random_quote)