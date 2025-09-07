from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for Hello World
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Project 4</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 500px;
        }
        h1 {
            color: #333;
            margin-bottom: 1rem;
            font-size: 2.5em;
        }
        p {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 1rem;
        }
        .status {
            background: #4CAF50;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            display: inline-block;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello World!</h1>
        <p>Welcome to Test Project 4</p>
        <p>This is a simple web service running in Docker</p>
        <div class="status">✅ Service is running successfully</div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello_world():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health_check():
    return {'status': 'healthy', 'message': 'Test Project 4 is running'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
