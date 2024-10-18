# Python 3.11
FROM python@sha256:0a301600e451618e1c0a94c28b5d83f875f6f3c07820a71d6dd2565a000f7408 as build

# Install OS dependencies
RUN apt-get update && apt-get install -y build-essential curl

# Set venv
ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

# Install uv
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

# Create a virtual environment and install dependencies
COPY ./requirements.txt .
RUN /root/.cargo/bin/uv venv /opt/venv && \
    /root/.cargo/bin/uv pip install --no-cache -r requirements.txt

# Python 3.11-slim-bookworm app image
FROM python@sha256:0a301600e451618e1c0a94c28b5d83f875f6f3c07820a71d6dd2565a000f7408

# Copy the virtual environment from the previous image
COPY --from=build /opt/venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the code
COPY . .

# Run the application
CMD ["python", "main.py"]
