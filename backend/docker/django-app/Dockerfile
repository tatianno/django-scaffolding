FROM python:3.11.4

RUN apt-get update \
	&& apt-get install -y \
		python3-dev \
		vim

WORKDIR /usr/src/webapps
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN django-admin startproject app .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]