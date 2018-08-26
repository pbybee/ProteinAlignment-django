FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
COPY requirements.txt /web/
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install -r requirements.txt
COPY . /web/
#RUN python /web/manage.py collectstatic
RUN ["chmod", "+x", "/web/entrypoint.sh"]
ENTRYPOINT ["sh", "/web/entrypoint.sh"]
