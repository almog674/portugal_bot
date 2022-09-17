from constants import PHONE_NUMBER, USER_TO_NOTIFY, MINUTES_BETWEEN_MONITORING
from monitor.agandamentos_monitor import AgandamentosMonitor
from notifier.whatsapp_notifier import WhatsappNotifier
from web_bot.web_scapper import AgamdamentosBot


def main():
    groups = {USER_TO_NOTIFY: [PHONE_NUMBER], "roee": ["+97222222"]}
    my_notifier = WhatsappNotifier(groups)

    bot = AgamdamentosBot()
    monitor = AgandamentosMonitor(bot, my_notifier, MINUTES_BETWEEN_MONITORING)
    monitor.monitor()


if __name__ == '__main__':
    main()
