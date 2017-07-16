from flask import Flask,request,render_template,jsonify

app=Flask(__name__)
@app.route('/loginpage')
def login():
    return render_template('app_html.html')
    

@app.route('/get_data/',methods=['GET','POST'])
def get_data():
    print request.args.to_dict()
    outputdata=request.args.to_dict()
    if (outputdata['inputemail']=='ranjithakolluru@gmail.com' and outputdata['inputpassword']=='Anju'):
        result ="True"
    else:
        result='False'

    print result    
    return jsonify({'result':result})    


@app.route('/profile')
def profile():
    return render_template('profilePage.html')


if __name__=='__main__':
    app.run(debug=True)   