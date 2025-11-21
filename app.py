from flask import Flask, jsonify, render_template, request, redirect
from flask_cors import CORS
import subprocess
import threading
import os
import time
from background_task import main
app = Flask(__name__)
CORS(app)

def run_background_script():
    """Function to run your Python script in background"""
    try:
        # Replace 'your_script.py' with your actual Python script name
        result = subprocess.run(['python', 'background_task.py'], 
                              capture_output=True, 
                              text=True,
                              timeout=300)  # 5 minute timeout
        print("Script output:", result.stdout)
        if result.stderr:
            print("Script errors:", result.stderr)
    except Exception as e:
        print(f"Error running script: {e}")

@app.route('/run-script', methods=['POST'])
def run_script():
    """Handle button click and run Python script in background"""
    # Run script in a separate thread so it doesn't block the response
    thread = threading.Thread(target=run_background_script)
    thread.daemon = True
    thread.start()
    thread.join()  # Wait for background task to complete
    return redirect('/StartChat.html')
    


@app.route('/')
def index():
    """Serve the HTML file"""
    return render_template('index.html')

@app.route('/Name_For_Chat', methods=['GET'])
def get_name_for_chat():
    data=request.get_json()
    name=data['name'].strip()
    with open("UserNameForWeb.txt", "r") as Mainfile:
        list_of_names = Mainfile.readlines()
        Mainfile = [name.strip() for name in list_of_names]
    def check_name():
        if name in list_of_names:
            return jsonify({'exists': True})
        else:
            return jsonify({'exists': False})
    return check_name()

@app.route('/MyUserName_For_Chat', methods=['POST'])
def render_MY_name():
    YourUserName=main()
    return YourUserName
if __name__ == '__main__':
    app.run(debug=True, port=5000)
