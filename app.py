from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <body style="background:black;
                 color:white;
                 display:flex;
                 justify-content:center;
                 align-items:center;
                 height:100vh;
                 margin:0;
                 font-size:50px;">
        Hsen Awada 3amak
    </body>
    """

if __name__ == "__main__":
    app.run(debug=True)