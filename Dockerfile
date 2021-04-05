FROM python:3.7

RUN pip3 install --upgrade pip

# install poppler, tesseract
RUN apt-get update
RUN apt-get install -y poppler-utils
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y vim

# Copy OntologyKB for models and client
COPY . /tmp/hopeiq/
RUN cd /tmp/hopeiq/ && python setup.py install

