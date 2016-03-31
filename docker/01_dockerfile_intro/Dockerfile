FROM ubuntu

ADD mirror/sources.list /etc/apt/sources.list
RUN apt-get update -y && apt-get install apache2 -y
EXPOSE 80

CMD service apache2 start && tail -f /var/log/apache2/access.log
