from transformers import pipeline

def generate_summary(text):
    # Load the pre-trained summarization model
    summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

    # Generate summary
    summary = summarization_pipeline(text, max_length=100, min_length=30, do_sample=False)

    # Extract the summarized text from the output
    summarized_text = summary[0]['summary_text']
    
    return summarized_text
