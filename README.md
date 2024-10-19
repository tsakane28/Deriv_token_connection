# Deriv WebSocket API Client

A Python client for interacting with Deriv's WebSocket API.

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

```bash
git clone <repository_url>
cd <repository_directory>
pip install websocket-client python-dotenv
```

## Quick Start

1. Create `.env` file:
```plaintext
DERIV_AUTH_TOKEN=your_auth_token_here
```

2. Run the client:
```bash
python main.py
```

## Features

- Real-time WebSocket connection to Deriv API
- Secure token management using environment variables
- Event-based message handling
- Error handling and connection management

## WebSocket Events

| Event | Description |
|-------|-------------|
| on_open | Triggered when connection established |
| on_message | Handles incoming WebSocket messages |
| on_error | Manages connection errors |
| on_close | Handles connection closure |

## Environment Variables

Required variables in `.env`:
- `DERIV_AUTH_TOKEN`: Your Deriv API authorization token

## Error Handling

The client includes comprehensive error handling for:
- Connection failures
- Authentication errors
- Invalid messages
- Network interruptions

## License

MIT License. See [LICENSE](LICENSE) file.

## Contributing

1. Fork the repository
2. Create feature branch
3. Submit pull request

For detailed API documentation, visit [Deriv API docs](https://api.deriv.com).
