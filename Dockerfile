# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
# Fron-Userbot
# Fron

RUN git clone -b Fron-Userbot https://github.com/Kikuk23/Fron-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Kikuk23/Fron-Userbot/Fron-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
