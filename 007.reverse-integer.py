# coding=utf-8
import logging
logging.basicConfig(
    level=logging.WARN,
    format='Log:(%(asctime)-15s)--%(message)s',
)


def reverse(x):
    sign = -1 if x < 0 else 1
    logging.debug('sign = '+str(sign))
    x = abs(x)
    ans = 0
    while x:
        ans = ans * 10 + x % 10
        x //= 10
    return sign * ans if ans <= 0x7fffffff else 0

if __name__ == '__main__':
    print(reverse(321323))
