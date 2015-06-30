# coding=utf-8
from __future__ import unicode_literals

"""
    Name:       KitchenSink
    Author:     Andy Liu
    Email :     andy.liu.ud@hotmail.com
    Created:    3/24/2015
    Copyright:  Copyright ©Intel Corporation. All rights reserved.
    Licence:    This program is free software: you can redistribute it
    and/or modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation, either version 3 of
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import logging
from logging.handlers import RotatingFileHandler
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from optparse import OptionParser
from ConfigFile import ConfigFileParser
from CollectData import CollectData
from GenerateReport import Report


class SendMail:
    def __init__(self):
        self._email_info = self._load_email_info()

    @staticmethod
    def _load_email_info():
        _config = ConfigFileParser()
        return _config.load_email_info()

    def send_mail(self, _content):
        logging.debug('Into function send_mail')
        _smtp = smtplib.SMTP(self._email_info['host'])
        _msg = MIMEText(_content, _subtype=self._email_info['subtype'], _charset=self._email_info['encoding'])
        _msg['Subject'] = Header(self._email_info['subject'] % CollectData.get_current_time(),
                                 self._email_info['encoding'])
        _msg['from'] = self._email_info['from']
        _msg['to'] = self._email_info['to']
        logging.info('Send email from %s to %s' % (self._email_info['from'], self._email_info['to']))
        _smtp.sendmail(self._email_info['from'], self._email_info['to'].split(';'), _msg.as_string())
        _smtp.quit()


def parse_command_line():
    """
    parse command line
    """
    usage = "usage: %prog -d/--debug\n"
    parser = OptionParser(usage=usage)
    parser.add_option("-d", "--debug", action="store_true", dest="debug", default=False,
                      help="Show debug info")
    (options, args) = parser.parse_args()
    return args, options


def init_logger(_debug=True):
    LOG_PATH_FILE = "kw_protex.log"
    LOG_MODE = 'a'
    LOG_MAX_SIZE = 1 * 1024 * 1024  # 1M
    LOG_MAX_FILES = 1  # 1 Files: kw_protex.log
    LOG_DEBUG_FORMAT = "%(asctime)s %(levelname)-10s[%(filename)s:%(lineno)d(%(funcName)s)] %(message)s"
    LOG_INFO_FORMAT = "%(asctime)s %(levelname)-10s%(message)s"

    _debug_formatter = logging.Formatter(LOG_DEBUG_FORMAT)
    _info_formatter = logging.Formatter(LOG_INFO_FORMAT)
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)
    rfh = RotatingFileHandler(LOG_PATH_FILE, LOG_MODE, LOG_MAX_SIZE, LOG_MAX_FILES)
    rfh.setLevel(logging.DEBUG)
    rfh.setFormatter(_debug_formatter)
    ch = logging.StreamHandler()
    if _debug:
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(_debug_formatter)
    else:
        ch.setLevel(logging.INFO)
        ch.setFormatter(_info_formatter)
    _logger.addHandler(rfh)
    _logger.addHandler(ch)
    return _logger


if '__main__' == __name__:
    args, opts = parse_command_line()

    logger = init_logger(opts.debug)
    logger.info('================== Start ==================')
    logger.info('================== Start ==================')
    logger.info('================== Start ==================')
    collection = CollectData()
    data = collection.collect_data()
    report = Report()
    content = report.render(data)
    if opts.debug:
        with open('Content.html', 'w') as f:
            f.write(content)
    sender = SendMail()
    sender.send_mail(content)
    logger.info('=================== End ===================')
    logger.info('=================== End ===================')
    logger.info('=================== End ===================')
