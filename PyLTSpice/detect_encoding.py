# coding=utf-8
#!/usr/bin/env python

# -------------------------------------------------------------------------------
# Name:        international_support.py
# Purpose:     Pragmatic way to detect encoding.
#
# Author:      Nuno Brum (nuno.brum@gmail.com) with special thanks to Fugio Yokohama (yokohama.fujio@gmail.com)
#
# Created:     14-05-2022
# Licence:     refer to the LICENSE file
# -------------------------------------------------------------------------------
"""
International Support functions
Not using other known unicode detection libraries because we don't need something so complicated. LTSpice only supports
for the time being a reduced set of encodings.
"""


def detect_encoding(file_path, expected_str: str = '') -> str:
    """
    Simple strategy to detect file encoding.  If an expected_str is given the function will scan through the possible
    encodings and return a match.
    If an expected string is not given, it will use the second character is null, high chances are that this file has an
    'utf_16_le' encoding, otherwise it is assuming that it is 'utf-8'.
    :param file_path: path to the filename
    :type file_path: str
    :param expected_str: text which the file should start with
    :type expected_str: str
    :return: detected encoding
    :rtype: str
    """
    if expected_str:  # if expected string is not empty
        f = open(file_path, 'rb')  # Open the file as a binary file
        tmp = f.read(2 * len(expected_str))  # Read the beginning of the contents of the file
        f.close()
        for encoding in ('utf-8', 'utf_16_le'):  # Add other possible encodings
            if tmp.decode(encoding).startswith(expected_str):
                return encoding
        raise UnicodeError("Unable to detect log file encoding")
    else:
        f = open(file_path, 'rb')  # Open the file as a binary file
        tmp = f.read(2)  # Read the beginning of the contents of the file
        f.close()
        return 'utf-8' if tmp[1] != 0 else 'utf_16_le'