FROM   python:latest
LABEL  name="Bean-jun"
LABEL  email="1342104001@qq.com"
ENV    home /root
WORKDIR ${home}

COPY   blogsystem ${home}
COPY   requirements.txt ${home}

RUN    python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN    cd blogsystem
RUN    python manage.py makemigrations
RUN    python manage.py migrate

CMD    python manage.py runserver 0.0.0.0:8000