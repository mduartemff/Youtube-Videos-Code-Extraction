"""
OCR Processing Module

This module handles the extraction of text from video frames using OCR (Optical Character Recognition).
It uses OpenCV for image preprocessing and Tesseract for text extraction.
The module provides functions for both individual image preprocessing and batch frame processing.
"""

import pytesseract
import cv2
import os

def preprocess_image(image_path):
    """
    Preprocess an image for better OCR accuracy.
    
    Args:
        image_path (str): Path to the input image file
        
    Returns:
        numpy.ndarray: Preprocessed image array optimized for OCR
        
    Raises:
        FileNotFoundError: If the image file doesn't exist
        cv2.error: If the image cannot be processed
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")
        
    # Apply Otsu's thresholding for better text separation
    _, img_thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return img_thresh

def process_frames(frames_dir):
    """
    Process all frames in a directory and extract text using OCR.
    
    Args:
        frames_dir (str): Directory containing the frame images (PNG format)
        
    Returns:
        list: List of dictionaries containing frame information:
            - frame (str): Frame filename
            - text (str): Extracted text from the frame
            
    Raises:
        FileNotFoundError: If the frames directory doesn't exist
        Exception: If OCR processing fails
    """
    if not os.path.exists(frames_dir):
        raise FileNotFoundError(f"Frames directory not found: {frames_dir}")
        
    extracted_data = []
    
    # Process each PNG frame in sorted order
    for frame_file in sorted(os.listdir(frames_dir)):
        if frame_file.endswith(".png"):
            frame_path = os.path.join(frames_dir, frame_file)
            try:
                # Preprocess the image and extract text
                preprocessed_img = preprocess_image(frame_path)
                text = pytesseract.image_to_string(preprocessed_img, lang='eng', config='--psm 6')
                
                # Only add frames that contain text
                if text.strip():
                    extracted_data.append({
                        'frame': frame_file,
                        'text': text.strip()
                    })
            except Exception as e:
                print(f"Error processing frame {frame_file}: {str(e)}")
                continue
                
    return extracted_data 