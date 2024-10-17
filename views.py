from django.shortcuts import render
from django.http import HttpResponse
import fitz  
from transformers import pipeline  
import json


qa_pipeline = pipeline("question-answering")

def home(request):
    if request.method == 'POST':
        # Get the uploaded PDF
        pdf = request.FILES['pdf']
        
        # Capture the question input from the form
        question = request.POST.get('question')
        
        # Initialize a variable to store the extracted text from the PDF
        pdf_text = ""
        
        # Open the PDF and extract text from each page
        with fitz.open(stream=pdf.read(), filetype="pdf") as doc:
            for page in doc:
                pdf_text += page.get_text()
        
        # Use question-answering model to find the answer
        answer = qa_pipeline(question=question, context=pdf_text[:2000])
        
        # Return the answer to the user
        return HttpResponse(f"Answer: {answer['answer']}")
    
    # Render the HTML form for uploading the PDF and entering the question
    return render(request, 'core/home.html')

def learning_path(request, topic):
    # Use the correct path to the JSON file based on your project structure
    with open('core/learning_paths.json') as f:
        paths = json.load(f)
    
    if topic in paths:
        return HttpResponse(f"Learning Path for {topic}: {paths[topic]}")
    else:
        return HttpResponse("No learning path available for this topic.")
