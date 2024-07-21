FROM python:3.12.4

# copy the requirements.txt file into tmp directory
COPY requirements.txt /tmp/requirements.txt

# Upgrade pip and install requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip &&\
    python -m pip install --no-cache-dir --timeout 3000000 -r /tmp/requirements.txt

# Copy the entire project
COPY . /app

# Setup project workinh directory
WORKDIR /app

# Expose Port
EXPOSE 8000

# Run the appliaction
CMD [ "uvicorn", "api:app", "--host", "0.0.0.0" ,"--port", "8000"]