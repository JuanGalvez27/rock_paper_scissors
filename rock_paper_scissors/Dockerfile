FROM python:3.12-slim
RUN useradd -m rock_paper_scissors
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY django_apps django_apps
COPY core core
COPY manage.py requirements.txt /app/
RUN pip install -r requirements.txt
RUN chown -R rock_paper_scissors:rock_paper_scissors /app
USER rock_paper_scissors
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]