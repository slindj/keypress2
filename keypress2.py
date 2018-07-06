import multiprocessing as mp
#import MySQLdb
import logging
import yaml
import time
import curses

def fobReader(q):
    time.sleep(10)
    q.put("FOO")


def keypress(p):

    with open("keypress2.yaml", "r") as yamlconfig:
        CONFIG = yaml.load(yamlconfig)

    logfile = CONFIG['logging']['filename']
    logformat = CONFIG['logging']['format']

    sqlhost = CONFIG['sql']['host']
    sqlport = CONFIG['sql']['port']
    sqluser = CONFIG['sql']['user']
    sqlpasswd = CONFIG['sql']['pw']
    sqldb = CONFIG['sql']['db']
    
    print("Starting KeyPress v2")
    
    print(q.get())

def setup(stdscr):
    stdscr.clear()
    ctx = mp.get_context('spawn')

    q = ctx.Queue()
    p = ctx.Process(target=fobReader, args=(q,))
    p.start()
    keypress(p)
    p.join()


if (__name__ == '__main__'):
    ctx = mp.get_context('spawn')


    pass

