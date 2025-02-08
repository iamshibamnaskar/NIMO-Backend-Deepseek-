# FastAPI Chat Streaming with Ollama

This project is a FastAPI-based backend that streams AI-generated responses using the Ollama `deepseek-r1:1.5b` model. The responses are streamed in real-time to provide a more interactive chat experience.

## Features
- Uses FastAPI for handling API requests
- Supports CORS for frontend integration
- Streams responses from the Ollama chat model
- Runs on `http://localhost:8000`

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)
- Ollama (for AI model inference)

## Installation & Setup

### 1. Install Ollama
To run this project, you need to install Ollama on your system. Follow the official installation instructions:

```sh
curl -fsSL https://ollama.com/install.sh | sh
```

After installation, verify that Ollama is installed correctly by running:

```sh
ollama --version
```

### 2. Install the Required AI Model
This project uses the `deepseek-r1:1.5b` model. Download and install it by running:

```sh
ollama pull deepseek-r1:1.5b
```

### 3. Clone the Repository
Clone the project from your repository:

```sh
git clone <your-repo-url>
cd <your-project-directory>
```

### 4. Install Dependencies
Install the required Python dependencies using:

```sh
pip install fastapi uvicorn ollama
```

## Running the Server
Once everything is set up, start the FastAPI server with:

```sh
python main.py
```

Or using Uvicorn directly:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will be available at: [http://localhost:8000](http://localhost:8000)

## API Endpoints

### `POST /query`
This endpoint accepts a JSON payload with a `message` and streams the AI response in real time.

#### Example Request:
```json
{
  "message": "Hello, how are you?"
}
```

#### Example Response:
A streamed text response from the `deepseek-r1:1.5b` model.

## Frontend Integration
To integrate with a frontend running on `http://localhost:5173`, ensure your frontend makes a POST request to `http://localhost:8000/query` and listens to the streamed response.

## License
This project is licensed under the MIT License.

---

Now you're all set to build and experiment with AI-powered chat applications! 🚀

