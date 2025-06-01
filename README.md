# Cultural Compass

Cultural Compass is a web application that helps travelers understand cultural differences between cities. Using the power of ChatGPT, it provides dynamic, accurate information about cultural norms, tipping customs, greetings, and unique local foods to help users navigate new cultural environments.

## Features

- Compare cultural norms between any cities worldwide
- Dynamic cultural information powered by ChatGPT
- Learn about tipping customs and social etiquette
- Discover local greetings and social customs
- Find unique local foods to try
- City name autocomplete suggestions
- Modern, responsive design
- Easy-to-use interface

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd cultural-compass
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
```bash
# On Unix/macOS:
export OPENAI_API_KEY='your-api-key-here'

# On Windows:
set OPENAI_API_KEY=your-api-key-here
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to:
```
http://localhost:5000
```

## How It Works

Cultural Compass uses the ChatGPT API to generate accurate, up-to-date cultural information for any city in the world. When you enter two cities to compare, the application:

1. Makes API calls to ChatGPT to get cultural information for both cities
2. Caches the results to minimize API calls
3. Presents the information in an easy-to-read comparison format

## Current Supported Cities

- New York City
- Tokyo

More cities will be added in future updates!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 