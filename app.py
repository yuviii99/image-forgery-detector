from flask import Flask, request, render_template, g, jsonify
import os
import cv2
from skimage.metrics import structural_similarity
import hashlib


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
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

# Task 6a: Calculate MD5 Hash


# Task 6b: Calculate MD5 Hash



# Task 5: Calculate Similarity of Images



if __name__ == '__main__':
    app.run(debug=True)