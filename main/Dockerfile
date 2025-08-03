FROM python

RUN mkdir /app

COPY . /app

RUN python -m pip install -r /app/requirements.txt

ADD . /app

EXPOSE 5000

WORKDIR /app

# ENTRYPOINT ["uvicorn","-w","4","-b","0.0.0.0:5000","app:app","--timeout 120"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# ENTRYPOINT ["python","main.py"]