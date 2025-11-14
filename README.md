# SuperSeller - HTML to Python Integration Guide

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Server
```bash
python app.py
```

### 3. Open in Browser
- Open your browser and go to: `http://localhost:5000`
- Click the "Start Chat" button
- The Python script (`background_task.py`) will run in the background

## How It Works

1. **index.html**: Contains the button that sends a request to the server
2. **app.py**: Flask server that receives the request and runs the Python script in a background thread
3. **background_task.py**: The actual Python script that runs in the background

## Customization

- Edit `background_task.py` to run your custom Python code
- The script runs in a separate thread, so the webpage won't freeze
- Response times are instant (script runs in background)
- Check console/terminal output to see script progress

## Notes

- Make sure Python and pip are installed
- The server runs on `http://localhost:5000` by default
- You can modify the port in `app.py` if needed
- For production, use a WSGI server like Gunicorn instead of Flask's development server
