# SpeakEasy

A powerful, lightweight machine-learning Python chat engine.

## What makes SpeakEasy better than other machine-learning solutions?

SpeakEasy is *specifically* designed to help first-timers implement impressive machine-learning chat as quickly and easily as possible, while providing a powerful open-source framework for more experienced users to build upon.

### It's simple.

At under 120 lines of well-commented code, SpeakEasy is blazing-fast and easy to understand... but only if you want to. Most importantly, the way it works *makes sense*.

### It's powerful.

Unlike other chat engines, SpeakEasy doesn't come hardcoded with assumptions about language constructs or I/O syntax. No punctuation? No spaces? No alphanumeric characters? No *printable* characters? No problem! SpeakEasy has been tested to fully support any Unicode input or output, making it perfect for chatting in English, Chinese, Arabic, Morse, binary, or any other language you can dream up.

It is also designed to be robust... and *impressive*. While it's suprisingly simple to use SpeakEasy to power a chatterbot which is being trained in real-time, it can also be set up to serve replies without learning or repeating anything the user says. This is perfect for customer-service solutions that suggest the most logical answer to a user's request, implementations that seek to avoid offensive phrases, or scripted games where the replies must remain in-character. It's also easy to improve the accuracy of these replies without necessarily learning any new phrases.

And, anything it does learn is saved for future conversations, even if the program itself ends. Multiple bots can read and update the same data file simultaneously, and everything saved is human-readable and easily edited. Plus, the file is *small*.

### It's easy!

With just 2 foolproof functions, SpeakEasy is perfect for anyone who needs an intelligent machine-learning solution, but doesn't want to set it up or waste time figuring out complicated implementatons. It's also great for those looking to dip their toes in machine learning for the first time.

`learn(prompt, response, score=True)`: Learn `response` as a reply to `prompt`.

`reply(prompt)`: Return a response to `prompt`.

There are no dependancies to install, no objects to create, and no setup to worry about - just import and call. SpeakEasy handles all persistent file creation and management for you.

```python
"""A infinite, machine-learning chatterbot."""

from speakeasy import * # Import reply and learn from speakeasy.py.

user = input() # Get user's input.

while user: # Keep looping if user input isn't empty.

    bot = reply(user) # Get a reply to the input string.
    print(bot) # Show reply to user.
    user = input() # Get the user's response.
    learn(bot, user) # Learn user's response and save for future use.
```
