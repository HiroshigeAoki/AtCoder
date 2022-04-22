#!/bin/bash

username=$1
passwd=$2

pip install -r requirements.txt

oj login -u ${username} -p ${passwd} "https://atcoder.jp/"