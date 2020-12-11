FROM python:3.6


WORKDIR /skeleton
COPY requirements.txt /skeleton
RUN pip install -r /skeleton/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 
COPY . /skeleton
CMD ["gunicorn", "-c", "guni.py", "wsgi:app"]
EXPOSE 5005
# CMD ["python", "run.py"]
