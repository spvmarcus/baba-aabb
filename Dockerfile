FROM fedora

RUN dnf update -y && dnf install python3-pip -y

RUN pip install --upgrade pip

RUN pip install lark

RUN pip install Django==4.2.3

RUN pip install djangorestframework==3.14.0

# INSTALAR PACOTES NECESSÁRIOS PARA APLICAÇÃO
RUN pip install PyPDF2==3.0.1
RUN pip install reportlab==4.4.3


WORKDIR /

RUN django-admin startproject config

WORKDIR /config

RUN django-admin startapp core

ENTRYPOINT ["python3"]

#CMD ["bash"]

CMD ["manage.py", "runserver", "0.0.0.0:8080"]
    