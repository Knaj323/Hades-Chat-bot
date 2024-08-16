from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def query_database(question):
    conn = sqlite3.connect('wiki_data.db')
    c = conn.cursor()
    
    c.execute('''SELECT content FROM Articles WHERE content LIKE ?''', ('%' + question + '%',))
    content = c.fetchone()
    
    conn.close()
    
    return content[0] if content else "Sorry, I couldn't find an answer to your question."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    response = query_database(question)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)