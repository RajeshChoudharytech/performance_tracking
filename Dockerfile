# official Python runtime as a parent image
FROM python:3.9

# environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Copy the Python scripts into the container
COPY scripts/slow_iteration.py scripts/revenue.py /code/


# Run the slow_iteration.py script as part of container startup
CMD ["python", "slow_iteration.py", "revenue.py"]
