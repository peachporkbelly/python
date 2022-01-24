from collections import UserList
from flask import Flask, request                 # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource   # Api 구현을 위한 Api 객체 import

app = Flask(__name__)   # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌
api = Api(app)          # Flask 객체에 Api 객체 등록

receive_data = {}
count = 0

@api.route('/hello')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        return {
            "response" : "OK",
            "hello": "world!"}

@api.route('/hello/<string:name>')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def get(self, name):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        return {"hello": name,
                "name" : name}

@api.route('/hello/json')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        return {
            "success":False,
            "message":"Dialect needs to be explicitly supplied as of v4.0.0",
            "datas":{"value":{"data" : 1},"raws":["hello world"]}
            }

user = "Nobody"
address = "korea"

@api.route('/test')
class testMethod(Resource):

    def get(self):
        global user
        global address
        

        return {
            "Hello" : user, "address" : address, 
            "userheader" : request.headers.get("user"), 
            "Restrict-Access-To-Tenants" : request.headers.get('Restrict-Access-To-Tenants'),
            "Restrict-Access-" : request.headers.get('Restrict-Access-To-Tenants'),
            "Str Request" : str(request.headers)
            }

    def post(self):
        global user
        global address
        
        receive_data = request.get_json()
        print(str(receive_data))
        user = receive_data["user"]
        address = receive_data["address"]
        
        return {"method" : "POST", "success" : True, "user" : user, "address" : address}

    def put(self):
        global user
        global address

        receive_data = request.get_json()
        user = receive_data["user"]
        address = receive_data["address"]

        return {"method" : "PUT", "success" : True, "user" : user, "address" : address}

    def delete(self):
        global user
        global address

        user = "Nobody"
        address = "korea"

        return {"method" : "DELETE", "success" : True, "user" : user, "address" : address}

    def patch(self):
        global user
        global address

        receive_data = request.get_json()
        
        user = receive_data["user"]
        address = receive_data["address"]

        return {"method" : "PATCH", "success" : True, "user" : user, "address" : address}


@api.route('/testpost')
class PostTest(Resource):
    def post(self):
        global receive_data
        global count

        idx = count 
        count += 1
        
        receive_data = request.get_json()
        
        return {
            "idx_" : idx,
            "receive data" : receive_data,
            "result" : "ok"
        }

@api.route('/testput')
class PutTest(Resource):
    def put(self):
        global receive_data
        global count
        
        idx = count
        count += 1

        old_data = receive_data
        receive_data = request.get_json()

        print("NOW DATA : ", receive_data)

        return {
            "idx" : idx,
            "old data" : old_data,
            "receive data" : receive_data,
            "result" : "ok"
        }

@api.route('/testdelete')
class DeleteTest(Resource):
    def delete(self):
        global receive_data
        global count

        idx = count
        count += 1

        old_data = receive_data
        receive_data = {}

        print("NOW DATA : ", receive_data)

        return {
            "idx" : idx,
            "old data" : old_data,
            "receive data" : receive_data,
            "result" : "ok"
        }

@api.route('/testpatch')
class PatchTest(Resource):
    def patch(self):
        return request.get_json()

@api.route('/testjson')
class GetJsonTest(Resource):
    def get(self):
        return {
            "success":True,
            "message":"",
            "datas":{
                "value":{
                    "count":2
                    },
                "raws":[
                    {"menu_id":0,
                    "menu_cd":"mat_receive",
                    "menu_nm":"자재입하",
                    "report_fg":True},
                    {"menu_id":1,
                    "menu_cd":"sal_outgo",
                    "menu_nm":"제품출하",
                    "report_fg":True}
                    ]
                }
            }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=30000)