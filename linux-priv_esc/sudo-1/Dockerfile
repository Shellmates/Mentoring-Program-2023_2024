FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y openssh-server sudo

RUN useradd -m -s /bin/bash ctf && \
    useradd --no-create-home ctf-cracked && \
    echo 'ctf:ctf' | chpasswd

WORKDIR /home/ctf

RUN chown -R root:root . && chmod 555 . 

COPY --chmod=400 --chown=ctf-cracked challenge/flag.txt .
COPY challenge/perms /etc/sudoers.d/

RUN ln -s /dev/null .bash_history
RUN chmod -r /tmp /var/tmp

EXPOSE 22


ENTRYPOINT service ssh start && tail -f /dev/null
