import os
from flask import Blueprint, render_template , request , send_file
from downloadFunc import downloadFunc

myapp = Blueprint('myapp',__name__,static_folder='static',template_folder='templates')

@myapp.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST': 
        try:
            getVideoLink = request.form.get('url')
            video = downloadFunc(getVideoLink)
            return send_file(video,as_attachment=True)
            os.remove(video)
        except:
            return 'Bir hata meydana geldi.'
    return render_template('index.html')
