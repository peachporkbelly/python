from flask import Flask, request #이 클래스의 인스턴트가 wsgi 어플리케이션이 된다
app = Flask(__name__) #단일모듈 사용시 __name__

@app.route('/') #route 데코레이터를 사용해 Flask에게 어떤 URL이 우리가 작성한 함수를 실행시키는지 알려줌
def hello_world():
    return 'hello world!'


#url 변수 부분 추가
@app.route('/user/<username>')
def show_user_profile(username):
    return f'this is {username}'

@app.route('/age/<int:age>')
def show_user_age(age):
    return f'you are {age} year old'

#get이 return되었다
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        return "post returned"
    else:
        return 'get returned'



if __name__ == '__main__': #실행한 서버가 현재 동작되는 유일한 서버라는걸 보여줌 
    app.run(port=50000)