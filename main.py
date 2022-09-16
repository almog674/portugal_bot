import pywhatkit

PHONE_NUMBER = "+972542141100"
NOTHING_MESSAGE = "Just a test of the bot"
FOUND_MESSAGE = "THe bot found something!"


def main():
    pywhatkit.sendwhatmsg_instantly(PHONE_NUMBER, NOTHING_MESSAGE)


if __name__ == "__main__":
    main()
