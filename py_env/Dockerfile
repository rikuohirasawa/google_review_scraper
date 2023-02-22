FROM --platform=linux/amd64 python:3.11
WORKDIR /app
COPY . .
EXPOSE 8001
RUN apt-get -y update
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN pip3 install -r requirements.txt
COPY server.py .
CMD [ "python", "./server.py" ]