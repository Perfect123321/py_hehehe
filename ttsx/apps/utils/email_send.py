# _*_ coding:utf-8 _*_
__auther__ = "bobby"
__date__ = "2018/11/9 21:59"
from random import Random
from django.core.mail import send_mail

from users.models import Emallver
from ttsx.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str


def send_register_email(email, send_type="register"):
    email_recoed = Emallver()
    coad = random_str(16)
    email_recoed.code = coad
    email_recoed.emall = email
    email_recoed.send_type = send_type
    email_recoed.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕学在线网注册链接"
        email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(coad)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email] )
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "慕学在线网密码重置链接"
        email_body = "请点击下面的链接充值你的密码:http://127.0.0.1:8000/reset/{0}".format(coad)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass





