#!/usr/bin/python3

import sys
sys.path.append("..")

import DNS

if __name__ == '__main__':

  domain = input('Enter domain name: ')
  record = input('Enter DNS record: ')

  DNSinfo = DNS.DnsRequest(domain, qtype=record)
  a = DNSinfo.req()
  
  a.show()
