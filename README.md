# 🚀 Simple Flask Web Server with Docker

This is a simple Python Flask web server that listens on port 8087, retrieves the server's IP address from an external API, and fetches the hostname using the `socket` module. It's containerized using Docker and can be run using Docker commands or Docker Compose.

## Prerequisites

🐳 Docker should be installed on your machine.

## Usage

1. Clone or download this repository.

2. Navigate to the project directory.

3. Run using Docker Compose

    ```bash
    git clone https://github.com/Raz-Dahan/ipify-webserver.git
    cd ipify-webserver
    docker-compose up -d
    ```

4. Access the server
    - Open a web browser and go to `http://<your_server_ip>:8087/`


- Feel free to customize the solution and explore more about Flask, Docker, and web server development.
