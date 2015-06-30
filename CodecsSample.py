# coding=utf-8
from __future__ import nested_scopes, generators, division, absolute_import, with_statement, print_function, \
    unicode_literals

"""
    Name:       CodecsSample
    Author:     Andy Liu
    Email :     andy.liu.ud@hotmail.com
    Created:    3/25/2015
    Copyright:  All rights reserved.
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
import os
import codecs


def writefile(fn, v_ls):
    with codecs.open(fn, 'wb', 'utf-8') as f:
        for i in v_ls:
            f.write(i + os.linesep)


def readfile(fn):
    with codecs.open(fn, 'r', 'utf-8') as f:
        for line in f:
            print(line.strip())


if __name__ == '__main__':
    fn = u'codecs.txt'
    ls = [u'1.python', u'2.how to pythonic', u'3.python cook', u'4.python编程']
    writefile(fn, ls)
    readfile(fn)
