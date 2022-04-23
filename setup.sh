#!/bin/bash


if [ ! -d ./venv ]; then
    python3.7 -m venv venv
fi

. ./venv/bin/activate

pip3 install --upgrade pip

pip install -r requirements.txt

echo "Input your AtCoder account username and password."
read -p "Username: " USERNAME
read -sp "Password: " PASSWD
oj login -u ${USERNAME} -p ${PASSWD} "https://atcoder.jp/"