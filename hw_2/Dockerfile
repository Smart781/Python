FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python-is-python3 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install latex-generator-for-tables-and-images 

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-lang-cyrillic \
    && rm -rf /var/lib/apt/lists/*

CMD ["sh", "-c", "python image_check.py && pdflatex table_image.tex"]