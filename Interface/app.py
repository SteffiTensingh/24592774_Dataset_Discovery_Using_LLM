from flask import Flask, request, jsonify
from transformers import pipeline
import pandas as pd

app = Flask(__name__)

# Initialize the model (using a smaller model for simplicity)
model_name = 'distilbert-base-uncased'
nlp = pipeline('question-answering', model=model_name)

# Sample metadata (should be replaced with actual metadata)
metadata = pd.read_csv('C:\\24592774_Dataset_Discovery_Using_LLM\\MetaData_Creation\\MetaData_Notebooks\\Enriched_MetaData_DataSet.csv')

@app.route('/submit_query', methods=['POST'])
def submit_query():
    data = request.json
    query = data['query']

    # Perform the query processing (simplified example)
    results = []
    for item in metadata:
        if query.lower() in item['description'].lower() or query.lower() in item['tags'].lower():
            results.append(item)

    # Limit results to a reasonable number (e.g., top 5)
    results = results[:5]

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the model (using a smaller model for simplicity)
model_name = 'distilbert-base-uncased'
nlp = pipeline('question-answering', model=model_name)

# Sample metadata (should be replaced with actual metadata)
metadata = pd.read_csv('C:\\24592774_Dataset_Discovery_Using_LLM\\MetaData_Creation\\MetaData_Notebooks\\Enriched_MetaData_DataSet.csv')


@app.route('/submit_query', methods=['POST'])
def submit_query():
    data = request.json
    query = data['query']

    # Perform the query processing (simplified example)
    results = []
    for item in metadata:
        if query.lower() in item['description'].lower() or query.lower() in item['tags'].lower():
            results.append(item)

    # Limit results to a reasonable number (e.g., top 5)
    results = results[:5]

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
