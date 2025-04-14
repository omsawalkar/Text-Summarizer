# Importing necessary libraries from Sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Function to read the content of a text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to summarize the text using Sumy
def summarize_text_sumy(text, num_sentences=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)

# Main function to run the summarizer
def main():
    # Read the text data from a file
    text_data = read_text_file('sample_text.txt')
    
    # Print the original text
    print("Original Text:")
    print(text_data)
    
    # Summarize the text
    summary = summarize_text_sumy(text_data, num_sentences=2)
    
    # Print the summary
    print("\nSummary:")
    print(summary)

# Entry point of the script
if __name__ == "__main__":
    main()
