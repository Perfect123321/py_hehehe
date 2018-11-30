# _*_ coding:utf-8 _*_
__auther__ = "bobby"
__date__ = "2018/10/27 1:19"

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ModifyPwdForm(forms.Form):
        #email = forms.EmailField(required=True)
        password1 = forms.CharField(required=True, min_length=5)
        password2 = forms.CharField(required=True, min_length=5)


