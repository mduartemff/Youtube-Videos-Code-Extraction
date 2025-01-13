"""
Test Suite for OCR Processing Module

This module provides comprehensive testing for the OCR processing functionality.
It tests both image preprocessing and text extraction capabilities by:
1. Creating test images with known text content
2. Verifying preprocessing operations
3. Validating OCR text extraction accuracy
4. Cleaning up test artifacts
"""

import os
import cv2
import numpy as np
from ocr_processing import process_frames, preprocess_image

def create_test_image(text, output_path):
    """
    Create a test image with specified text for OCR testing.
    
    Args:
        text (str): Text to write on the image
        output_path (str): Path where the test image will be saved
        
    Returns:
        str: Path to the created test image
        
    Raises:
        cv2.error: If image creation or writing fails
    """
    # Create a white image
    img = np.ones((100, 400), dtype=np.uint8) * 255
    
    # Add text to image with good contrast for OCR
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text, (10, 50), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Save the image
    cv2.imwrite(output_path, img)
    return output_path

def setup_test_frames():
    """
    Create a directory with test frames containing known text.
    
    Returns:
        tuple: Contains:
            - frames_dir (str): Path to the test frames directory
            - created_files (list): List of paths to created test images
            - test_data (list): List of (text, filename) tuples for verification
            
    Raises:
        OSError: If directory creation fails
    """
    frames_dir = "test_frames"
    os.makedirs(frames_dir, exist_ok=True)
    
    # Create test images with known text
    test_data = [
        ("Hello World", "frame_001.png"),
        ("Testing OCR", "frame_002.png"),
        ("Python Code", "frame_003.png")
    ]
    
    created_files = []
    for text, filename in test_data:
        filepath = os.path.join(frames_dir, filename)
        create_test_image(text, filepath)
        created_files.append(filepath)
    
    return frames_dir, created_files, test_data

def cleanup_test_files(frames_dir, created_files):
    """
    Clean up test files and directories after testing.
    
    Args:
        frames_dir (str): Directory containing test frames
        created_files (list): List of file paths to clean up
    """
    print("\nCleaning up test artifacts...")
    
    # Clean up test image files
    for file in created_files:
        try:
            os.remove(file)
            print(f"  Cleaned up: {file}")
        except Exception as e:
            print(f"  Warning: Could not remove {file}: {str(e)}")
    
    # Clean up test directory
    try:
        os.rmdir(frames_dir)
        print(f"  Cleaned up: {frames_dir}/")
    except Exception as e:
        print(f"  Warning: Could not remove {frames_dir}: {str(e)}")

def test_ocr_processing():
    """
    Test OCR processing functionality.
    
    This test function:
    1. Creates test images with known text content
    2. Tests image preprocessing operations
    3. Verifies OCR text extraction accuracy
    4. Ensures proper cleanup of test files
    
    The test creates a controlled environment with known text content
    to verify both the preprocessing steps and final OCR results.
    """
    try:
        print("Starting OCR processing test...")
        
        # Setup test environment
        frames_dir, created_files, test_data = setup_test_frames()
        
        # Test preprocessing
        print("\nTesting image preprocessing...")
        test_image_path = created_files[0]
        preprocessed = preprocess_image(test_image_path)
        if preprocessed is not None and isinstance(preprocessed, np.ndarray):
            print(f"✓ Image preprocessing successful")
            print(f"  Image shape: {preprocessed.shape}")
            print(f"  Data type: {preprocessed.dtype}")
        else:
            print("✗ Image preprocessing failed")
        
        # Test frame processing
        print("\nTesting frame processing...")
        results = process_frames(frames_dir)
        
        if results:
            print(f"✓ Frame processing successful: {len(results)} frames processed")
            
            # Check results
            print("\nChecking extracted text:")
            for i, (expected_text, filename) in enumerate(test_data):
                found = False
                for result in results:
                    if result['frame'] == filename:
                        found = True
                        extracted_text = result['text'].strip()
                        if expected_text.lower() in extracted_text.lower():
                            print(f"✓ Frame {filename}: Text matched")
                            print(f"  Expected: {expected_text}")
                            print(f"  Found: {extracted_text}")
                        else:
                            print(f"✗ Frame {filename}: Text mismatch")
                            print(f"  Expected: {expected_text}")
                            print(f"  Found: {extracted_text}")
                if not found:
                    print(f"✗ Frame {filename}: Not processed")
        else:
            print("✗ Frame processing failed")
            
    except Exception as e:
        print(f"\n✗ Test failed with error: {str(e)}")
        raise e
    finally:
        # Clean up test artifacts
        cleanup_test_files(frames_dir, created_files)

if __name__ == "__main__":
    test_ocr_processing() 