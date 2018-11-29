import random

from flask import Flask, render_template, request, render_template_string, redirect

app = Flask(__name__)

short_urls={}
short=''
random_lst=list('0123456789abcdefghijklmnABCDEFGHIJopqrstuvwxyzKLMNOPQRSTUVWXYZ')

@app.route('/')
def index():
    global short
    return render_template('index.html')

@app.route('/short/',methods=['POST'])
def long_to_short():
    global short,short_urls
    long=request.form.get('long')
    print(long)
    if long=='':
        return render_template('index.html',short='请输入长网址',v='/')
    else:
        for k,v in short_urls.items():
            if v==long:
                return render_template('index.html', short="localhost:5000/"+k,v=v)
        else:
            while True:
                short = ''
                for alpha in range(6):
                    short+=random.choice(random_lst)
                if short not in short_urls:
                    short_urls[short]=long
                    break
                else:
                    continue
            print(short_urls)
            return render_template('index.html',short="localhost:5000/"+short,v=long)

@app.route('/<short>')
def go_to_short(short):
    global short_urls
    if short in short_urls:
        return redirect(short_urls[short])
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
