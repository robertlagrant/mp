# Offical Python 3.6 image
FROM python:3.6-slim

# Working directory is app
WORKDIR /app

# Copy current directory contents to /app container
ADD . /app

# Install via requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
