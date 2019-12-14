from flask import Flask,render_template,redirect,url_for,request,g,session,flash
import os
import text
from werkzeug import secure_filename
import PyPDF2 
app=Flask(__name__)
app.config['SECRET_KEY'] =os.urandom(24)

@app.route('/')
def index():
    return render_template("front.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file']
        read_pdf = PyPDF2.PdfFileReader(f)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)
        txt=page_content
        session['txt']=txt
        return render_template("upload.html",txt=session['txt'])

@app.route('/upsearch',methods=['POST','GET'])
def search1():
    if(request.method=="POST"):
        try:
            text.main1(1,session['txt'])
        except:
            flash('*Please upload the file and press Index')
            return redirect(url_for('upload'))

        src=request.form["src"] 
        if(len(src)==0):
            flash('*The search Bar is empty')
            return render_template("upload.html",txt=session['txt']) 
        src=src.lower()
        session['src']=src  
        l=[]
        l=text.search2(session['src'])
        return render_template("upload.html",txt=session['txt'],wrd=session['src'],l=l)    


@app.route('/send1',methods=['POST','GET'])
def send1():
    if(request.method=="POST"):
        txt=request.form['text']
        if(len(txt)==0):
            flash('*Please upload the file and press Index')
            return render_template("upload.html")

        for k in list(session):
            print(k)
            session.pop(k,None)    
        session['txt']=txt
        text.main1(1,txt)
        return render_template("upload.html",txt=session['txt'])



@app.route('/send',methods=['POST','GET'])
def send():
    if(request.method=="POST"):      
        txt=request.form['text']
        if(len(txt)==0):
            flash('*Please paste the file and press index')
            return render_template("front.html")

        for k in list(session):
            print(k)
            session.pop(k,None)   
        session["txt"]=txt
        text.main(1,txt)
        return render_template("front.html",txt=session['txt'])
            

@app.route('/search',methods=['POST','GET'])
def search():
    if(request.method=="POST"):
        src=request.form["src"]
        if(len(src)==0):
            flash('*The search Bar is empty')
            return render_template("front.html",txt=session['txt'])

        src=src.lower() 

        session['src']=src
        l=[]
        text.main(1,session['txt'])
        l=text.search1(src)
        return render_template("front.html",txt=session['txt'],wrd=session['src'],l=l)

@app.route('/clear')
def clear():
    session.pop("txt",None)
    session.pop("src",None)
    return render_template("front.html",txt="") 


@app.route('/clear1')
def clear1():
    session.clear()
    return render_template("upload.html")     




if __name__ == '__main__':
   app.run(debug=True)    