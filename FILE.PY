from Flask import Flask
app= Flask(__name__)
@app.route('/')

def home():

    return 'Hello Ethiopia'
if __name__=="__main__":
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug=True,use_reloader=True)


