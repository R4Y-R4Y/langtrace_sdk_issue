# Use the latest version of the rasa/rasa base image
FROM python:3.12.3

# Set the working directory inside the container
WORKDIR '/app'

COPY requirements.txt /app/requirements.txt
# Install the required Python packages from requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Switch to root user to install dependencies
# USER root

# COPY wait-for-it.sh /wait-for-it.sh
# Ensure the wait script is executable
# RUN chmod +x /wait-for-it.sh


# Set the command to run when the container starts
EXPOSE 8000

# CMD ["sh", "/wait-for-it.sh", "postgres", "sh", "-c", "python manage.py migrate && python db_init.py && gunicorn --workers=3 --bind=0.0.0.0:8000 chatbot.wsgi:application"]
#CMD ["sh", "-c", "gunicorn --workers=3 --bind=0.0.0.0:8000 chatbot.wsgi:application"]
# CMD ["sh", "-c", "sleep 10000"]

