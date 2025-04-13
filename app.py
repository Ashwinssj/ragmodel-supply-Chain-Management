from flask import Flask, render_template, request
from agents.product_profiling import profile_product
from agents.sourcing import sourcing_advice
from agents.knowledge_base import fetch_web_insight
from agents.llm_agent import query_ollama

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        product = request.form['product']
        question = request.form['question']
        
        profile = profile_product(product)
        sourcing = sourcing_advice(profile)
        web_info = fetch_web_insight(f"{question} about {product}")
        
        final_prompt = f"""
You are a supply chain expert. Given the product: {product}
Product profile: {profile}
User question: {question}
Sourcing advice: {sourcing}
Web-based insight: {web_info}

Give a clear, professional, and useful answer.
"""
        response = query_ollama(final_prompt)
        
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
