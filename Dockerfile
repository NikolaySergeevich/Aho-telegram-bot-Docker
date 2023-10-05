FROM python:3.11.1

WORKDIR /home
ENV API_TOKEN="your token"
#RUN apt-get update && apt-get install -y apt-transport-https
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install --force-reinstall -v "aiogram==2.23.1"
RUN mkdir log
COPY *.py ./

ENTRYPOINT ["python", "main.py"]

