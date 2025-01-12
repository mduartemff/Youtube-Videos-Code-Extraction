import pytesseract
import cv2
import os

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, img_thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return img_thresh

def process_frames(frames_dir):
    extracted_data = []
    for frame_file in sorted(os.listdir(frames_dir)):
        if frame_file.endswith(".png"):
            frame_path = os.path.join(frames_dir, frame_file)
            preprocessed_img = preprocess_image(frame_path)
            text = pytesseract.image_to_string(preprocessed_img, lang='eng', config='--psm 6')
            if text.strip():
                extracted_data.append({'frame': frame_file, 'text': text})
    return extracted_data
