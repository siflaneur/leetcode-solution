# coding=utf-8
# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='Log:(%(asctime)-15s)--%(message)s',
# )


def palindrome_number(x: int) ->bool:
    copy = x
    tmp = 0
    while x:
        tmp = tmp * 10 + x % 10
        x //= 10
    return copy == tmp

