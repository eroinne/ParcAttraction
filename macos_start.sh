#! /bin/sh

cd python && pip3 install -r requirements.txt
cd ..
cd parc && chmod +x copy.sh && ./copy.sh < /dev/null
cd ..
cd python && python3 init.py
python3 -m flask --debug run

