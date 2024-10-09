FROM n8nio/n8n

# Install Python 3
WORKDIR /app
USER root
RUN apk add --no-cache python3 py3-pip

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment
RUN . venv/bin/activate

COPY requirements.txt requirements.txt

RUN venv/bin/pip install -r requirements.txt

# Copy notion.py file
COPY notion.py /app/notion.py

# Set working directory

# Run notion.py script
CMD ["python3", "notion.py"]