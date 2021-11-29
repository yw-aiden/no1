# coding:gbk
import os


def down(n):
    s = "shutdown -s -t " + str(n)
    os.system(s)


down(10)
