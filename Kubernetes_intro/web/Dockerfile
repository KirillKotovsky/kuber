# FROM  python:3.7-alpine
# RUN useradd -r -u 1001 -g appuser appuser
# USER appuser
# RUN python -m pip install Django
# RUN pip install djangorestframework
# WORKDIR /app
# COPY  . /app
# EXPOSE 8000

FROM python:3
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
RUN useradd -r -u 1001 -g sudo appuser
USER appuser
# ENTRYPOINT python ./manage.py runserver 0.0.0.0:8000
ENTRYPOINT ["python", "./manage.py", "runserver", "0.0.0.0:8000" ]
# CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
EXPOSE 8000