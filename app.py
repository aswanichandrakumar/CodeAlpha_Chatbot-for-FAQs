import json
import spacy
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Load FAQ data from JSON
with open('faq_data.json', 'r') as f:
    faqs = json.load(f)

def find_best_match(query):
    user_doc = nlp(query.lower())
    best_answer = None
    highest_similarity = 0

    for faq in faqs:
        question = faq['question']
        answer = faq['answer']
        question_doc = nlp(question.lower())
        similarity = user_doc.similarity(question_doc)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_answer = answer

    return best_answer if highest_similarity > 0.5 else "Sorry, I couldn't find an answer for that."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = find_best_match(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_query = data.get("message", "")
    response = get_best_match(user_query)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
