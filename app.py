from flask import Flask, render_template, request
from text_summarizer import summarize_text_sumy  # Correct import statement

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    if request.method == 'POST':
        text_data = request.form['text']
        num_sentences = int(request.form['num_sentences'])
        summary = summarize_text_sumy(text_data, num_sentences)
    
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
