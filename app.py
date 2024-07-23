from flask import Flask, request, render_template, g, jsonify
import os
import cv2
from skimage.metrics import structural_similarity
import hashlib


app = Flask(__name__)
# Task 3a: Implement Image Upload Functionality
# Configure the upload folder



@app.route('/')
def index():
    return render_template('index.html')

# Task 4b: Handle Upload Request to Backend

def upload():
    # Task 3b: Implement Image Upload Functionality



    # Task 7: Determine Forgery and Display Results

    return

# Task 6a: Calculate MD5 Hash


# Task 6b: Calculate MD5 Hash



# Task 5: Calculate Similarity of Images



if __name__ == '__main__':
    app.run(debug=True)