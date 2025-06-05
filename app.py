from flask import Flask, render_template
import json
from datetime import datetime

app = Flask(__name__)

def read_projects():
    try:
        with open('projects.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

@app.route('/')
def index():
    projects = read_projects()
    return render_template('index.html', 
                         projects=projects,
                         total_projects=len(projects),
                         last_updated=datetime.now().strftime('%Y-%m-%d'))

if __name__ == '__main__':
    app.run(debug=True) 