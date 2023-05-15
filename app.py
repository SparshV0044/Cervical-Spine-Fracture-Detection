import os
import csv
from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    folder_name = ""
    if 'folder_name' in request.files:
        folder = request.files['folder_name']
        print('----------------folder----------------')
        print(type(folder))
        print(folder)
        folder_name = folder.filename
        print('-------------------------------------------')
        print(type(folder_name))
        print(folder_name)
        # string = "1.2.826.0.1.3680043.1476/1.dcm"
        match = re.match(r"(.*?)/", folder_name)
        extracted_string = match.group(1)
        print('-----------',extracted_string)


    csv_file = "C:\\Users\\spars\\Desktop\\Cervical Spine\\Cervical-Spine-Fracture-Detection\\submission.csv"  # Replace with the path to your CSV file
    images = "C:\\Users\\spars\\Desktop\\Cervical Spine\\Cervical-Spine-Fracture-Detection\\static\\images"
    rows = []
    with open(csv_file, 'r') as file:   
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        folder_index = header.index('patient_id')

        for row in csv_reader:
            if row[folder_index] == extracted_string:
                rows.append(row)
                image_file = extracted_string + '.png'  # Assumes the image file extension is .jpg
                image_path = os.path.join(images, image_file)
                print(image_path)
                if not os.path.exists(image_path):
                    image_file = None

    return render_template('results.html', rows=rows, image_file=image_file)




if __name__ == '__main__':
    app.run(debug=True)
