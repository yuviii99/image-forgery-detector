from flask import Flask, request, render_template, g, jsonify
import os
import cv2
from skimage.metrics import structural_similarity
import hashlib


app = Flask(__name__)
UPLOAD_FOLDER = '/usercode/ImageForgeApp/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file1' in request.files and 'file2' in request.files:
        g.file1 = request.files['file1']
        g.file2 = request.files['file2']

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
    
        g.file1.save(os.path.join(app.config['UPLOAD_FOLDER'], g.file1.filename))
        g.file2.save(os.path.join(app.config['UPLOAD_FOLDER'], g.file2.filename))
    else:
        return jsonify({'error': 'Upload two images for similarity calculation'}), 400


    # Task 7: Determine Forgery and Display Results

    return

def calculate_hash(file_path):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        while file_chunk := file.read(8192):
            md5.update(file_chunk)
    return md5.hexdigest()

def caluclate_md5():
    file_path1 = os.path.join(UPLOAD_FOLDER, g.file1.filename)
    file_path2 = os.path.join(UPLOAD_FOLDER, g.file2.filename)
    hash1 = calculate_hash(file_path1)
    hash2 = calculate_hash(file_path2)
    return hash1==hash2

SSIM_THRESHOLD = 0.9

def calculate_similarity():
    # Load and compare image similarity
    image_path1 = os.path.join(UPLOAD_FOLDER, g.file1.filename)
    image_path2 = os.path.join(UPLOAD_FOLDER, g.file2.filename)
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # Resize the image to have both of the same size
    image1_resized = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

    # Calculate the similarity
    ssim_score = ssim(image1_resized, image2)

    if ssim_score > SSIM_THRESHOLD:
        return True
    return False

if __name__ == '__main__':
    app.run(debug=True)