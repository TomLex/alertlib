#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

from pyslack import SlackClient

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


########################################  EMAIL  ########################################
def send_to_email(mandrill_login, email_from='alertlib@skypicker.com', email_to=[], subject='', message='', list_of_files=[]):
    # email_to must be list
    smtp = smtplib.SMTP("smtp.mandrillapp.com",587)
    smtp.starttls()
    smtp.login(*mandrill_login)

    mpart = MIMEMultipart()
    mpart.set_charset("utf-8")
    mpart["From"] = email_from
    mpart["Subject"] = subject

    mpart.attach(MIMEText(message, 'plain'))

    for f in list_of_files:
        fpart = MIMEBase('application', "octet-stream")
        fpart.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(fpart)
        fpart.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        mpart.attach(fpart)
                
    for to in email_to:
        mpart["To"] = to
        smtp.sendmail(mpart["From"], to, mpart.as_string())

    smtp.close()



########################################  SLACK  ########################################

class ChatClient():
    def __init__(self, token, user, send_to):
        self.client = SlackClient(token)
        self.user = user
        self.send_to = send_to       

    def _send_msg(self, msg):
        self.client.chat_post_message(self.send_to, msg, username=self.user)

    def allow_airline(self, airline, iata):
        self._send_msg("Airline '%s (%s)' allowed in search" % (airline, iata))

    def disable_airline(self, airline, iata, reason):
        self._send_msg("Airline '%s (%s)' disabled in search because: %s" % (airline, iata, reason))

    def start_scraping(self, airline, iata):
        self._send_msg("Scraping of airline '%s (%s)' started" % (airline, iata))

    def stop_scraping(self, airline, iata, reason):
        self._send_msg("Scraping of airline '%s (%s)' stopped because: %s" % (airline, iata, reason))

    def start_automat(self, airline, iata):
        self._send_msg("Automat for airline '%s (%s)' started" % (airline, iata))

    def stop_automat(self, airline, iata, reason):
        self._send_msg("Automat for airline '%s (%s)' stopped because: %s" % (airline, iata, reason))

    def saving_deactivated(self, iata):
        self._send_msg("Saving results to DB deactivated for airline '%s' " % (iata))

    def saving_activated(self, iata):
        self._send_msg("Saving results to DB activated for airline '%s' " % (iata))

def create_chat_notificator(token, user='alertlib', send_to='#general', s_msg=None, e_msg=None, return_instance=False):
    def wrap(func):
        @wraps(func)
        def wrapped_f(*args, **kwargs):
            c = ChatClient(token, user, send_to)
            res = func(c, *args, **kwargs) if return_instance else func(*args, **kwargs)
            if not s_msg or not e_msg:
                if res:
                    if s_msg:
                        c._send_msg(s_msg)
                else:
                    if e_msg:
                        c._send_msg(e_msg)
            return res
        return wrapped_f
    return wrap

def send_to_slack(token, send_from, send_to, message):
    ChatClient(token, send_from, send_to)._send_msg(message)

