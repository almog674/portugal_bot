from notifier.whatsapp_notifier import WhatsappNotifier

PHONE_NUMBER = "+972542141100"
NOTHING_MESSAGE = "Just a test of the bot"
FOUND_MESSAGE = "THe bot found something!"


def main():
    groups = {"almog": [PHONE_NUMBER], "roee": ["+97222222"]}
    my_notifier = WhatsappNotifier(groups)
    print(my_notifier.get_all_groups())
    my_notifier.notify(NOTHING_MESSAGE, ["almog"])


if __name__ == "__main__":
    main()
