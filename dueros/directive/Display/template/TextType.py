#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""

class TextType(object):
    PLAIN_TEXT = 'PLAIN_TEXT'
    RICH_TEXT = 'RICH_TEXT'

    @staticmethod
    def inEnum(position):
        return position == TextType.PLAIN_TEXT or position == TextType.RICH_TEXT

if __name__ == '__main__':

    print(TextType.PLAIN_TEXT)
    print(TextType.inEnum('aaa'))
