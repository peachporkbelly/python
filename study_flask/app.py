from flask import Flask, render_template, request

app = Flask(__name__)

#일반적인 라우트 방식
@app.route('/')
def home():
    return 'hello world'

@app.route('/echo/<thing>')
def echo(thing):
    return "say hello to my little friend: %s" %thing

#인수를 하나만 전달, html에 랜더링
@app.route('/echo2/<thing>')
def echo2(thing):
    return render_template('flask2.html',thing=thing)

#인수를 여러개 전달. 단순히 URL 자체를 확장한다.
@app.route('/echo3/<thing>/<place>')
def echo3(thing, place):
    return render_template('flask3.html', thing=thing, place=place)

#인수를 여러개 전달. get 매개변수로 인수를 제공한다
#http://127.0.0.1:3000/echo4?thing=sua&place=myhouse
@app.route('/echo4')
def echo4():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask4.html', thing=thing, place=place)

#인수를 여러개 전달. dictionary **연산자를 사용해 한 딕셔너리로부터 여러 인수를 템플릿에 전달할 수 있음
#http://127.0.0.1:3000/echo5/?thing=sua&place=school
@app.route('/echo5/')
def echo5():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask5.html', **kwargs) #입력 인수가 많으면 타이핑 줄일 수 있음

if __name__ == '__main__':
    app.run(port=3000)