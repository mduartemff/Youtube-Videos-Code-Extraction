"""
Groq Integration Module

This module handles the integration with Groq's LLM API for processing
extracted video content. It provides functionality for text analysis
and content understanding using Groq's language models.
"""

import os
from groq import Groq
from src.config import GROQ_API_KEY

def process_content(text_content, model="llama-3.1-8b-instant"):
    """
    Process text content using Groq's language model.
    
    Args:
        text_content (str): The text content to process
        model (str): The Groq model to use (default: llama-3.1-8b-instant)
        
    Returns:
        dict: The processed response from Groq
        
    Raises:
        ValueError: If text_content is empty or too long
        Exception: If API call fails or processing error occurs
    """
    if not text_content.strip():
        raise ValueError("Text content cannot be empty")
    
    if len(text_content) > 10000:  # Adjust limit as needed
        raise ValueError("Text content is too long")
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that analyzes video content."
                },
                {
                    "role": "user",
                    "content": text_content
                }
            ],
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False
        )
        return completion
    except Exception as e:
        raise Exception(f"Failed to process content with Groq: {str(e)}")

def analyze_transcript(captions):
    """
    Analyze video transcript using Groq.
    
    Args:
        captions (list): List of caption dictionaries with text content
        
    Returns:
        dict: Analysis results from Groq
        
    Raises:
        Exception: If analysis fails
    """
    # Combine caption text
    full_text = "\n".join([c['text'] for c in captions])
    
    # Create analysis prompt
    prompt = f"""Analyze the following video transcript and provide:
1. Main topics discussed
2. Key points or insights
3. Summary of content

Transcript:
{full_text}"""
    
    return process_content(prompt)

def analyze_extracted_text(frame_texts):
    """
    Analyze text extracted from video frames using Groq.
    
    Args:
        frame_texts (list): List of dictionaries containing frame text data
        
    Returns:
        dict: Analysis results from Groq
        
    Raises:
        Exception: If analysis fails
    """
    # Combine frame text
    text_content = "\n".join([
        f"Frame {f['frame']}: {f['text']}"
        for f in frame_texts
    ])
    
    # Create analysis prompt
    prompt = f"""Analyze the following text extracted from video frames and provide:
1. Identify any code snippets or technical content
2. List tools, technologies, or concepts mentioned
3. Extract any important commands or syntax

Extracted Text:
{text_content}"""
    
    return process_content(prompt) 