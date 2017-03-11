#! /usr/bin/python3


# Whois script created by Michael Jeszenka for Hostica.com
# need to install python-whois module
# sudo pip3 install python-whois
# https://bitbucket.org/richardpenman/pywhois


import whois


print('Enter domain for Whois lookup: ')
domain = input()
w = whois.whois(domain)
print(w.text)
