# pull base image
FROM python:3.10-slim
# sets the working Directory
WORKDIR /app
# set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependancies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy the rest of the application into the container at /app
COPY . /app/
# collect static files 
RUN python manage.py collectstatic --noinput
# Make port 8000 available
EXPOSE 8000
# run django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
