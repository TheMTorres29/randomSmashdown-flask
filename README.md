# Random Smashdown Flask

A simple Flask web application for randomizing fighters from Super Smash Bros Ultimate, built for fun and learning.

## Features
- Random fighter selection
- Simple web interface
- Easily deployable to AWS EC2

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/randomSmashdown-flask.git
   cd randomSmashdown-flask
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```

### Running Locally
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

### Deployment (AWS EC2 Example)
1. Launch an EC2 instance and SSH into it.
2. Install Python, pip, and git.
3. Clone this repository and install dependencies.
4. Run with Gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```
5. (Optional) Set up Nginx as a reverse proxy for production.

## Links
`https://ec2-3-95-67-134.compute-1.amazonaws.com/`

## File Structure
```
app.py
deploy.sh
fighters.py
static/
    style.css
    favicon.ico
templates/
    index.html
```

## License
MIT
