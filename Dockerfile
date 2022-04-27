# Use Python 3.x Latest
FROM python:3

# (DEFAULT PORT) for the terminal
EXPOSE 50765/udp

# Set working directory on container
WORKDIR /usr/src/app

# Copy the terminal files to the container
COPY terminal .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Start the terminal process
CMD ["python", "terminal.py"]