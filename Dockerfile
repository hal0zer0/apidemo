FROM python:3.8
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=settings

WORKDIR /code
COPY . /code/
COPY static /code/static
RUN pip install -r /code/requirements.txt
RUN ls -la /code/static

EXPOSE 8000
STOPSIGNAL SIGTERM
#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "apiassignment.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
