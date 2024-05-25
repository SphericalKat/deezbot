# Python 3.11
FROM python@sha256:091e0f5da680e5c972c59cb7eca172141bb6350045b592c284e2fd3bf2916dd9 as build

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
FROM python@sha256:fc39d2e68b554c3f0a5cb8a776280c0b3d73b4c04b83dbade835e2a171ca27ef

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
