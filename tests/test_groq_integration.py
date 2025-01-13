"""
Test Suite for Groq Integration Module

This module provides comprehensive testing for the Groq LLM integration.
It tests the content processing and analysis capabilities by:
1. Testing basic API functionality
2. Verifying transcript analysis
3. Testing frame text analysis
4. Handling common API errors
"""

import os
import pytest
from src.groq_integration import process_content, analyze_transcript, analyze_extracted_text
from src.config import GROQ_API_KEY

# Sample test data
SAMPLE_CAPTIONS = [
    {"start": 0, "end": 2, "text": "Hello, today we'll learn about Python programming"},
    {"start": 2, "end": 4, "text": "We'll cover basic syntax and functions"},
    {"start": 4, "end": 6, "text": "Let's start with a simple example"}
]

SAMPLE_FRAME_TEXTS = [
    {"frame": "frame_001.png", "text": "def hello_world():"},
    {"frame": "frame_002.png", "text": "    print('Hello, World!')"},
    {"frame": "frame_003.png", "text": "# This is a comment"}
]

def test_process_content():
    """
    Test basic content processing with Groq API.
    """
    try:
        print("\nTesting basic content processing...")
        
        # Test with simple content
        test_content = "What is Python programming language?"
        response = process_content(test_content)
        
        # Verify response structure
        assert response is not None, "Response should not be None"
        assert hasattr(response, 'choices'), "Response should have choices"
        assert len(response.choices) > 0, "Response should have at least one choice"
        assert response.choices[0].message.content.strip(), "Response should have content"
        
        print("✓ Basic content processing successful")
        print(f"  Response length: {len(response.choices[0].message.content)} characters")
        
    except Exception as e:
        print(f"✗ Content processing test failed: {str(e)}")
        raise e

def test_analyze_transcript():
    """
    Test transcript analysis functionality.
    """
    try:
        print("\nTesting transcript analysis...")
        
        # Test with sample captions
        response = analyze_transcript(SAMPLE_CAPTIONS)
        
        # Verify response
        assert response is not None, "Response should not be None"
        assert hasattr(response, 'choices'), "Response should have choices"
        content = response.choices[0].message.content
        
        # Check if analysis contains expected sections
        assert "Main topics" in content, "Response should include main topics"
        assert "Key points" in content, "Response should include key points"
        assert "Summary" in content, "Response should include summary"
        
        print("✓ Transcript analysis successful")
        print("\nSample analysis sections:")
        print(f"  Content length: {len(content)} characters")
        
    except Exception as e:
        print(f"✗ Transcript analysis test failed: {str(e)}")
        raise e

def test_analyze_extracted_text():
    """
    Test frame text analysis functionality.
    """
    try:
        print("\nTesting frame text analysis...")
        
        # Test with sample frame texts
        response = analyze_extracted_text(SAMPLE_FRAME_TEXTS)
        
        # Verify response
        assert response is not None, "Response should not be None"
        assert hasattr(response, 'choices'), "Response should have choices"
        content = response.choices[0].message.content
        
        # Check if analysis contains expected sections
        assert any(keyword in content.lower() for keyword in ['code', 'snippet', 'function']), \
            "Response should identify code content"
        assert any(keyword in content.lower() for keyword in ['python', 'programming']), \
            "Response should identify programming language"
        
        print("✓ Frame text analysis successful")
        print(f"  Content length: {len(content)} characters")
        
    except Exception as e:
        print(f"✗ Frame text analysis test failed: {str(e)}")
        raise e

def test_error_handling():
    """
    Test error handling for common issues.
    """
    try:
        print("\nTesting error handling...")
        
        # Test with empty content
        with pytest.raises(ValueError) as exc_info:
            process_content("")
        assert "Text content cannot be empty" in str(exc_info.value)
        print("✓ Empty content error handled correctly")
        
        # Test with very long content
        long_content = "test " * 10000  # Very long content
        with pytest.raises(ValueError) as exc_info:
            process_content(long_content)
        assert "Text content is too long" in str(exc_info.value)  
        print("✓ Content length limit error handled correctly")
        
    except Exception as e:
        print(f"✗ Error handling test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    # Verify API key is available
    if not GROQ_API_KEY:
        print("✗ GROQ_API_KEY not found in environment variables")
        exit(1)
    
    print("Starting Groq integration tests...")
    
    # Run all tests
    test_process_content()
    test_analyze_transcript()
    test_analyze_extracted_text()
    test_error_handling()
    
    print("\nAll Groq integration tests completed successfully!") 