from flask import Flask, render_template, request, jsonify
import openai
import os
import json
from functools import lru_cache

app = Flask(__name__)

# Your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY') # Use environment variable

def get_city_info(city_name):
    """Get cultural information for a city using ChatGPT API."""
    prompt = f"""Provide cultural information for {city_name} in the following JSON format:
    {{
        "name": "{city_name}",
        "tipping": "brief description of tipping customs",
        "greeting": "brief description of common greetings",
        "unique_foods": ["list", "of", "must-try", "local", "foods"],
        "cultural_norms": [
            "list of important cultural norms",
            "and social customs",
            "that visitors should know"
        ],
        "cool_facts": ["list", "of", "interesting", "or", "unique", "facts", "or", "attractions"]
    }}
    Keep descriptions concise and factual. Focus on practical information for visitors. The cool_facts should be interesting tidbits or unique attractions not necessarily related to daily cultural interactions like tipping or greetings."""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a cultural expert providing accurate, practical information about cities around the world."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        # Extract and parse the JSON response
        content = response.choices[0].message.content
        # Find JSON content between curly braces
        json_str = content[content.find('{'):content.rfind('}')+1]
        return json.loads(json_str)
    except Exception as e:
        print(f"Error getting city info: {str(e)}")
        return None

@lru_cache(maxsize=100)
def get_cached_city_info(city_name):
    """Cache city information to avoid repeated API calls."""
    return get_city_info(city_name)

@app.route('/')
def home():
    return render_template('index.html', title='Cultural Compass')

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        origin_city = request.form.get('origin_city', '').strip()
        destination_city = request.form.get('destination_city', '').strip()
        
        if not origin_city or not destination_city:
            return render_template('compare.html', 
                                 error="Please enter both cities",
                                 title='Compare Cities')
        
        # Get city information from ChatGPT
        origin_data = get_cached_city_info(origin_city)
        destination_data = get_cached_city_info(destination_city)
        
        if not origin_data or not destination_data:
            return render_template('compare.html', 
                                 error="Unable to retrieve information for one or both cities. Please try again.",
                                 title='Compare Cities')
        
        # Pass destination data including cool_facts
        return render_template('results.html',
                             origin=origin_data,
                             destination=destination_data,
                             title='Cultural Comparison')
    
    return render_template('compare.html', title='Compare Cities')

@app.route('/api/cities/suggest', methods=['GET'])
def suggest_cities():
    """Get city suggestions based on partial input."""
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])
    
    # Common cities for suggestions
    common_cities = [
        "New York", "London", "Paris", "Tokyo", "Sydney",
        "Berlin", "Rome", "Barcelona", "Amsterdam", "Singapore",
        "Dubai", "Hong Kong", "Bangkok", "Seoul", "Istanbul"
    ]
    
    suggestions = [city for city in common_cities if query in city.lower()]
    return jsonify(suggestions[:5])  # Return top 5 suggestions

if __name__ == '__main__':
    if not os.getenv('OPENAI_API_KEY'):
        print("Warning: OPENAI_API_KEY environment variable not set!")
    
    # Get port from environment variable, default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    app.run(debug=True, host='0.0.0.0', port=port) 
