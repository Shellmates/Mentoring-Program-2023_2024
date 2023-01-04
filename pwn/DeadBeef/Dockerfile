FROM i386/ubuntu:latest

RUN apt-get update && apt-get upgrade -y
# Setup challenge environment
RUN apt-get install -y socat gcc-multilib gdb

WORKDIR /challenge
COPY challenge .
COPY src/chall.c .

RUN gcc -no-pie chall.c -o chall
RUN chmod +x entrypoint.sh chall

USER nobody 

ENTRYPOINT ["./entrypoint.sh"]