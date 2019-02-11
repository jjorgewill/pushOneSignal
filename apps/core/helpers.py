from onesignal import OneSignalError

from apps.core import properties
import onesignal as onesignal_sdk


class OneSignalHelper(object):
    """

    Manager One Signal

    """

    def __init__(self):
        """

        Inicializa las claves de Onesignal

        :return:
        """
        self.user_auth_key = properties.user_auth_key
        self.app_auth_key = properties.app_auth_key
        self.app_id = properties.app_id
        try:
            self.client = onesignal_sdk.Client(user_auth_key=self.user_auth_key,
                                        app={"app_auth_key": self.app_auth_key, "app_id": self.app_id})
        except OneSignalError as e:
            print(e)



    def notify(self, message, title=None, segment=None):
        """

        Realiza una notificacion por defecto a todos los usuarios

        :param message:
        :param segment:
        :return:
        """
        new_notification = onesignal_sdk.Notification(contents={"en": message})
        new_notification.set_parameter("headings", {"en": title})
        if title:
            new_notification.set_parameter("headings", {"en": title})
        # set target Segments
        new_notification.set_included_segments(["All"])
        new_notification.set_excluded_segments(["Inactive Users"])

        # send notification, it will return a response
        onesignal_response = self.client.send_notification(new_notification)
        print(onesignal_response.status_code)
        print(onesignal_response.json())