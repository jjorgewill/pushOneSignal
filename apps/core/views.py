# -*- coding: utf-8 -*-
from apps.core.helpers import OneSignalHelper
import requests
import json


def sendNotification(request):
    signal = OneSignalHelper()
    signal.notify(message="holaa",title="test")
    print("joo")