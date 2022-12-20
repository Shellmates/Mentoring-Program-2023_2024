FROM ubuntu:22.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install openssh-server sudo cowsay && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash ctf && \
    useradd --no-create-home ctf-cracked && \
    echo 'ctf:ctf' | chpasswd 

COPY challenge/flag.txt /flag.txt

RUN chown root:ctf-cracked /flag.txt && chmod 440 /flag.txt
RUN ln -s /dev/null /home/ctf/.bash_history 

COPY challenge/perms /etc/sudoers.d/

RUN chmod -r /tmp /var/tmp
ENTRYPOINT service ssh start && tail -f /dev/null
