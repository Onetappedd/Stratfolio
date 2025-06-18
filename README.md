# MyPortfolio

MyPortfolio is a small demonstration service that returns a simple asset allocation based on a risk profile and investment amount. The backend is written with FastAPI and can optionally fetch live prices from the Marketstack API.

## Setup
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. (Optional) To use live Marketstack prices, export your API key:
   ```bash
   export MARKETSTACK_API_KEY=<your_key>
   ```

## Running the server
Start the application using uvicorn:
```bash
uvicorn main:app --reload
```
The API exposes a `/generate` endpoint that accepts JSON with `risk_level`, `amount`, and `use_api`.

## Testing
The project uses `pytest`. Run tests with:
```bash
pytest -q
```
