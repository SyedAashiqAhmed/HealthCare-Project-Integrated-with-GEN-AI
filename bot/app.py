from flask import Flask, request, render_template
from langchain_together import Together
import os

app = Flask(__name__)

# ✅ Make sure this model is publicly accessible
model_name = "mistralai/Mistral-7B-Instruct-v0.1"

# 🔑 Set your Together API key
together_api_key = "a939da6ba566cb8878fdea04fec513936ed33837415ddf22c184129f8540526b"

llm = Together(
    model=model_name,
    temperature=0.7,
    max_tokens=512,
    together_api_key=together_api_key
)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        symptoms = request.form.get("symptoms")
        prompt = f"You are a helpful medical assistant. A patient has the following symptoms: {symptoms}. Suggest possible causes and remedies."
        response = llm.invoke(prompt)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
