from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Portfolio Project</title>
        <style>
            body {
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }

            .container {
                max-width: 700px;
                margin: auto;
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            }

            h1 {
                color: #38bdf8;
                font-size: 42px;
            }

            h2 {
                color: #f8fafc;
            }

            p {
                font-size: 18px;
                line-height: 1.6;
            }

            .badge {
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                border-radius: 25px;
                background: #38bdf8;
                color: #0f172a;
                font-weight: bold;
            }

            footer {
                margin-top: 30px;
                color: #cbd5e1;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 DevOps Portfolio Project</h1>

            <h2>Dockerized Flask Application</h2>

            <p>
                This application was built using Flask and
                containerized with Docker as part of my DevOps learning journey.
            </p>

            <div>
                <span class="badge">Python</span>
                <span class="badge">Flask</span>
                <span class="badge">Docker</span>
                <span class="badge">Linux</span>
                <span class="badge">GitHub</span>
            </div>

            <footer>
                Built by Noor Sabahat | Aspiring DevOps Engineer
            </footer>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)