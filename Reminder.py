import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "Time to SLEEP",
        message = "Slepp is necessary to recollect what you have learned",
        app_icon = "F:\Holidays\Food\sleep.ico",
        timeout = 5
    )
