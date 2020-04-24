FROM alpine:edge
RUN apk add py3-setuptools
COPY requirements.txt /usr/src/app/
RUN apk add --update py-pip
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/
COPY templates/index_post.html /usr/src/app/templates/
EXPOSE 5000
CMD ["python3", "/usr/src/app/app.py", "/var/run/docker.sock"]
