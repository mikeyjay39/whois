#!/bin/bash

whois $1 | grep -e "Domain Name:" -m 1 -e Registrar: -m 1 -e "Name Server:" -m 4
