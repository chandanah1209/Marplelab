from flask import Flask
import subprocess
import os
import datetime

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Chandana H"
    username = os.getlogin()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <pre>
    Name: {name}
    User: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """
    return response

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)
