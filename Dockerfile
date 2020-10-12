FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

# Execute test script
# RUN python3 ./main.py file_manager -a "create" -f "file_output.txt" -l "log_file.txt"
# RUN python3 ./main.py file_manager -a "send" -d "My initial string." -f "file_output.txt" -l "log_file.txt"
# RUN python3 ./main.py file_manager -a "send" -d "Another string." -f "file_output.txt" -l "log_file.txt"
# RUN python3 ./main.py file_manager -a "replace" -rd "Another string." -d "An even better string." -f "file_output.txt" -l "log_file.txt"

# RUN python3 ./main.py network_manager -a "connect" --host "localhost" --port 4000 -l "log_file.txt"
# RUN python3 ./main.py network_manager -a "send" --host "localhost" --port 4000 -d "My AWESOME string." -l "log_file.txt"
# RUN python3 ./main.py network_manager -a "close" --host "localhost" --port 4000

ENTRYPOINT []