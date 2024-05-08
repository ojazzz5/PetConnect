from flask import Flask
import serial

app = Flask(__name__)

# Initialize serial connection
ser = serial.Serial('COM5', 9600)  # Adjust port and baud rate as needed

@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/connection_status')
def connection_status():
    try:
        # Send a command to Arduino and wait for response
        ser.write(b'ping\n')  # Send 'ping' command to Arduino
        response = ser.readline().decode().strip()  # Read response from Arduino
        if response == 'pong':
            return 'Arduino connected!'
        else:
            return 'Arduino not connected!'
    except Exception as e:
        return f'Error: {e}'

@app.route('/test_connection')
def test_connection():
    try:
        # Send a test command to Arduino and wait for response
        ser.write(b'test\n')  # Send 'test' command to Arduino
        response = ser.readline().decode().strip()  # Read response from Arduino
        if response == 'success':
            return 'Connection test successful!'
        else:
            return 'Connection test failed!'
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(debug=True)
