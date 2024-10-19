import os
import json
import websocket
from dotenv import load_dotenv

# Load environment variables from .env file (if any)
load_dotenv()

# Fetch the token from environment variables
auth_token = os.getenv('DERIV_AUTH_TOKEN')

if not auth_token:
    print("Authorization token not found. Please set the 'DERIV_AUTH_TOKEN' environment variable.")
    exit()

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("Connected to Deriv WebSocket API")

if __name__ == "__main__":
    websocket_url = "wss://ws.binaryws.com/websockets/v3?app_id=1089"  # WebSocket URL for Deriv

    # Create a WebSocket application
    ws = websocket.WebSocketApp(websocket_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # Run the WebSocket
    ws.run_forever()
