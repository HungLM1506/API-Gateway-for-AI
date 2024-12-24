# API-Gateway-for-AI


This guide will help you configure Nginx to act as an API Gateway, routing requests to different services such as Streamlit (UI) and FastAPI (API). We will use an Nginx configuration file to accomplish this.

## 1. Setup Instructions

### 1.1. Prerequisites

- Python 3.8 or higher.
- GPU support (optional, but recommended).
- Libraries listed in `requirements.txt`.

### 1.2. Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HungLM1506/API-Gateway-for-AI.git
   cd API-Gateway-for-AI
   ```

2. Set up a Python environment (recommended):

   ```bash
   python -m venv api_gateway
   source api_gateway/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```




## 2. Steps to Follow

### 2.1. Create the Nginx Configuration File

First, you need to create a new Nginx configuration file to route the requests to the correct services.

1. Open a terminal and create a new configuration file in the `/etc/nginx/sites-available/` directory:

   ```bash
   sudo nano /etc/nginx/sites-available/my_app.conf
   ```

2. Paste the following content into the file:
```
server {
    listen 80;
    server_name yourdomain.com;  # Replace "yourdomain.com" with your domain name

    # Route to Streamlit (UI)
    location /streamlit/ {
        rewrite ^/streamlit(/.*)$ $1 break;  # Remove "/streamlit" from the URL when forwarding
        proxy_pass http://localhost:8501/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Route to FastAPI (API)
    location /api/ {
        rewrite ^/api(/.*)$ $1 break;  # Remove "/api" from the URL when forwarding
        proxy_pass http://localhost:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Ensure that Nginx forwards requests to the services correctly
    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
    }

    # Define error handling and custom pages (if needed)
    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
    }
}
```

### 2.2. Create a Symlink to the `sites-enable` Directory
To make Nginx use the new configuration file, you need to create a symlink from the `sites-available` directory to the `sites-enabled` directory:

``` bash
sudo ln -s /etc/nginx/sites-available/my_app.conf /etc/nginx/sites-enabled/
```
If there is already a linked file, run the following code before creating the symlink:
``` bash
sudo rm /etc/nginx/sites-enabled/my_app.conf
```

### 2.3. Check the Nginx Configuration
Before restarting Nginx, check your configuration to ensure there are no syntax errors:

``` bash
sudo nginx -t
```

### 2.4. Restart Nginx
Once you have verified the configuration, restart Nginx to apply the changes:
``` bash
sudo systemctl restart nginx
```

### 2.5. Verify Operation

- Access http://localhost/streamlit/ to use the Streamlit UI.
- Access http://localhost/api/ to use the FastAPI API.

### 2.6. Check Logs (If Issues Occur)
If there are issues with the configuration or the services are not working correctly, you can check the Nginx error log to troubleshoot:

``` bash
sudo tail -f /var/log/nginx/error.log
```

### 2.7. Nginx Directory Structure
- `/etc/nginx/nginx.conf`: The main Nginx configuration file.
- `/etc/nginx/sites-available/`: The directory containing configuration files for individual applications.
- `/etc/nginx/sites-enabled/`: The directory containing symlinks to the configuration files that are enabled.

### 2.8. Adding a New Service
If you have a new service and want to add it to Nginx, you will need to create a new `.conf` configuration file for that service. Each service typically has its own configuration file for easier management and configuration in Nginx.