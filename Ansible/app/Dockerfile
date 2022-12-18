FROM ubuntu
WORKDIR ./
COPY . ./
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install flask
EXPOSE 8082
