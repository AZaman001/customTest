# check Dockerhub grab the base image you want
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy all/required files from the current directory contents into the container at /app
COPY flaskApp.py flaskApp.py

# Install any needed packages specified in requirements.txt
RUN pip3 install Flask && pip3 install requests

# ENTRYPOINT because if I run container with additional commands this will still not be ignored
ENTRYPOINT ["python3", "flaskApp.py"]
