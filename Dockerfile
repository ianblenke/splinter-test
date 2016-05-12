FROM python:2.7

RUN pip install splinter nose bs4 && \
  # Install PhantomJS.
  apt-get update && \
  apt-get install -qqy curl vim jq && \
  curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
  apt-get install -qqy nodejs build-essential && \
  npm install -g phantomjs

COPY files /test
WORKDIR /test/

#CMD ["nosetests"]
CMD ["sh"]
