#!/usr/bin/env python

import requests

def mainn():
    print (("""\
     _    ___  _____ _____   ___   _   _  _   _  ___________ 
/  __ \  |_  |/  ___/  __ \ / _ \ | \ | || \ | ||  ___| ___ \
| /  \/    | |\ `--.| /  \// /_\ \|  \| ||  \| || |__ | |_/ /
| |        | | `--. \ |    |  _  || . ` || . ` ||  __||    / 
| \__/\/\__/ //\__/ / \__/\| | | || |\  || |\  || |___| |\ \ 
 \____/\____/ \____/ \____/\_| |_/\_| \_/\_| \_/\____/\_| \_|
          ______                                             
         |______|                                              by Hamza_Mandil""").encode('utf-8'))

def hamza():
    file1 = open("wordlist.txt", "r")
    readfile = file1.readline()
    for site in file1:
        url = site
        try:
                test = requests.get(url)
                content = test.headers
                if not 'X-Frame-Options' in content:
                        print "\033[1;37;40m" + url + "\033[1;32;40m  vulnerable !!!!! \n"
                else:
                        print "\033[1;37;40m" + url + "\033[1;31;40m  NOT vulnerable \n"
        except:
                print "\033[1;37;40m" + url + "NOT WORK"
mainn()
hamza()
