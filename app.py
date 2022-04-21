from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)
@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['POST'])
def detect():
    if not request.method == "POST":
        return 
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    print(video)
    # subprocess.run("ls")
    subprocess.run(['python', 'detect.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))])

    return os.path.join(uploads_dir, secure_filename(video.filename))
    obj = secure_filename(video.filename)
    

@app.route('/return-files', methods=['post'])
def return_file():
    obj = request.args.get('obj')
    loc = os.path.join("runs/detect", obj)
    print(loc)
    with open("result.txt","r") as f:
        content=f.read()
        f.close()
    return render_template("index.html",content=content)
    # try:
    #     # return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
    #     # return send_from_directory(loc, obj)
    # except Exception as e:
    #     return str(e)



@app.route("/detected",methods=['post'])
def webo():
    subprocess.run(['python','detect1.py'])
    with open("result1.txt","r") as f1:
        content1=f1.read()
        a=len(content1)
        temp=content1[0]
        aa=[temp]
        for ii in range(1,a):
            if content1[ii] != temp:
                aa.append(content1[ii])
                temp=content1[ii]
        
        
        f1.close()
    return render_template("index.html",content=''.join(aa)) 




if __name__=="__main__":
    app.run(debug=True)


# @app.route('/display/<filename>')
# def display_video(filename):
# 	#print('display_video filename: ' + filename)
# 	return redirect(url_for('static/video_1.mp4', code=200))
 