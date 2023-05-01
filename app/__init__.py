from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import model
import time
app = Flask(__name__)
f=None


@app.route('/result', methods=['GET', 'POST'])
def uploader_file():
    filename = None
    if request.method == 'POST':
        f = request.files['file1']
        f.save("./app/img/"+secure_filename(f.filename))
        filename = "./app/img/"+secure_filename(f.filename)
    value = model.analysis(filename)
    val1 = value[0]
    val2 = {'normal':value[1][0], 'cataract':value[1][1],'glaucoma':value[1][2],'other retina disease':value[1][3]}
    return render_template('submit.html', v1 = val1, v2 =val2)

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/About')
def About():
    return render_template('About.html')

#index page
@app.route('/', methods = ['POST', 'GET'])
def upload_file():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    