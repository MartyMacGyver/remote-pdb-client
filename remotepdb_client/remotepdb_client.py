#!/usr/bin/env python3

"""
    Copyright (c) 2017 Martin F. Falatic

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

"""

import telnetlib
import time
import argparse
import signal
import sys
from colorama import Fore, Back, Style
try:
    from remotepdb_client.__config__ import PACKAGE_DATA
except ModuleNotFoundError:
    from __config__ import PACKAGE_DATA


TITLE = "{} v{}".format(PACKAGE_DATA['name'], PACKAGE_DATA['version'])


def signal_handler(signal, frame):
        print()
        print()
        print(Fore.RESET + "Exiting...")
        sys.exit(0)


def setup(params):
    signal.signal(signal.SIGINT, signal_handler)

    default_host = 'localhost'
    default_port = 4544
    default_delay = 0.5  # seconds between retries
    minimum_delay = 0.1
    default_theme = 'none'
    default_prompt = '(Pdb) '  # trailing spaces are important

    parser = argparse.ArgumentParser(description='Intelligent Client for RemotePDB')
    parser.add_argument('--host', type=str, required=False,
                        help='hostname to connect to')
    parser.add_argument('--port', type=int, required=False,
                        help='port to connect to')
    parser.add_argument('--delay', type=float, required=False,
                        help='connection retry delay')
    parser.add_argument('--theme', type=str, required=False,
                        help='output theme (dark, light, none)')
    parser.add_argument('--prompt', type=str, required=False,
                        help='debug prompt to wait for (including trailing spaces)')
    args = parser.parse_args()

    params['host'] = args.host if args.host else default_host
    params['port'] = args.port if args.port else default_port
    params['delay'] = args.delay if (args.delay and args.delay >= minimum_delay) else default_delay
    params['prompt'] = args.prompt if args.prompt else default_prompt

    theme = {
        'none': {
            'color_default': '',
            'color_prompt': '',
            'color_cmd': '',
            'color_output': '',
            'color_wait': '',
            'color_alert': '',
        },
        'light': {
            'color_default': Style.RESET_ALL,
            'color_prompt': Style.DIM + Fore.GREEN,
            'color_cmd': Style.NORMAL + Fore.BLUE,
            'color_output': Style.NORMAL + Fore.BLACK,
            'color_wait': Style.NORMAL + Fore.CYAN,
            'color_alert': Style.NORMAL + Fore.RED,
        },
        'dark': {
            'color_default': Style.RESET_ALL,
            'color_prompt': Style.BRIGHT + Fore.GREEN,
            'color_cmd': Style.NORMAL + Fore.YELLOW,
            'color_output': Style.NORMAL + Fore.WHITE,
            'color_wait': Style.NORMAL + Fore.CYAN,
            'color_alert': Style.NORMAL + Fore.RED,
        },
    }
    params['theme'] = args.theme.lower() if args.theme else default_theme
    params.update(theme[params['theme']])

    return params


def connector(params):
    remote = telnetlib.Telnet(params['host'], params['port'])
    textout = ''
    read_remote = True
    while textout not in ['c', 'q']:
        if read_remote:
            textin = remote.read_until(params['prompt'].encode('ascii'))
            text_main = textin.decode('ascii').rsplit(params['prompt'], 1)
            print()
            print(params['color_output'] + text_main[0] + params['color_prompt'] + params['prompt'].strip() + params['color_cmd'] + ' ', end='')
        textout = input().strip()
        if textout in ['cl', 'clear']:
            print(params['color_alert'] + "{} is not allowed here (blocks on stdin on the server)".format(textout))
            print()
            print(params['color_prompt'] + params['prompt'].strip() + params['color_cmd'] + ' ', end='', flush=True)
            read_remote = False
        else:
            # TODO history MFF uparrows cmd2?
            remote.write(textout.encode('ascii') + b'\n')
            read_remote = True
        if textout in ['e', 'exit', 'q', 'quit']:
            print()
            print(Fore.RESET + "Exiting...")
            sys.exit(0)


def main(params={}):
    setup(params=params)
    print()
    print("{} debugging via {}:{}".format(TITLE, params['host'], params['port']))
    waiting = False
    while 1:
        try:
            connector(params=params)
            waiting = False
        except (ConnectionRefusedError, EOFError):
            if not waiting:
                print()
                print(params['color_wait'] + "Waiting for breakpoint/trace...")
                waiting = True
            time.sleep(params['delay'])


if __name__ == '__main__':
    main()
