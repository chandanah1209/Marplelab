from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system details
    full_name = "Chandana H"  # Replace with your actual name
    username = os.getenv("USER", "codespace")
    
    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get HTOP output (top command)
    top_output = subprocess.getoutput("top -b -n 1")

    # Generate response
    response = f"""
    <h1>HTOP Endpoint</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
