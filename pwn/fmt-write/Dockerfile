FROM ubuntu:22.10

RUN apt-get update && apt-get install socat gcc-multilib -y

COPY challenge /challenge

RUN chmod +x /challenge/start.sh /challenge/chall

WORKDIR /challenge

ENTRYPOINT ["/challenge/start.sh"]