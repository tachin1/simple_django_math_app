FROM centos:7

RUN yum -y install epel-release && yum -y update && yum -y install python2-pip && yum -y install vim-enhanced && yum -y install mod_wsgi && pip install --upgrade pip==9.0.3 setuptools==24.2 && pip install pymongo && pip install django && pip install django-rest-framework

COPY math/ /var/www/
copy math_api.conf  /etc/httpd/conf.d/
EXPOSE 81
ENTRYPOINT ["apachectl"]
CMD ["-DFOREGROUND"]
