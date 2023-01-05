#!/bin/sh
socat -dd -T60 TCP-LISTEN:1337,reuseaddr,fork,su=nobody EXEC:/challenge/chall,stderr