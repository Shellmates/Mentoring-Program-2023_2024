FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y openssh-server sudo

RUN useradd -m -s /bin/bash ctf && \
    useradd --no-create-home -s /bin/bash ctf-cracked && \
    echo 'ctf:ctf' | chpasswd

RUN chmod -r /tmp /var/tmp 

WORKDIR /home/ctf

RUN chown -R root:root . && \
    chmod o+rx .
COPY --chown=root:ctf-cracked --chmod=440 challenge/flag.txt .
COPY --chown=root:ctf-cracked --chmod=555 challenge/my_ls .
COPY challenge/perms /etc/sudoers

EXPOSE 22

ENTRYPOINT service ssh start && tail -f /dev/null
