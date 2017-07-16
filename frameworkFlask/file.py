from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "this is the default page"
@app.route('/apple')
def sample():
    return "<h1>This the sample</h1>"

@app.route('/mac/<name>',methods=['GET','POST'])
def mac_name(name):
    return render_template('app.html',name=name)

@app.route('/apple/count/<int:count>')
def count(count):
    count+=1
    return "<h1>This is my count: %d</h2>" % count


if __name__=='__main__':
    app.run(debug=True)