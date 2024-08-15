import http.server  
import socketserver  
import json  
import requests
  
# 和风天气API的基础URL  
WEATHER_API_BASE_URL = 'https://geoapi.qweather.com/v2/city/lookup' 
API_Search='https://devapi.qweather.com/v7/weather/now' 
# 和风天气API密钥  
API_KEY = '6848f5c3ec784faa833a0e687af83d91'  
  
class WeatherHandler(http.server.BaseHTTPRequestHandler):  
    def do_GET(self):    
        location = 'wuhan' 
        id=None
        
        print(location)
        if location:  
            # 构建完整的API URL  
            weather_api_url = f"{WEATHER_API_BASE_URL}?location={location}&key={API_KEY}"  
            print(weather_api_url)
            try:  
                # 发送请求到和风天气API  
                res = requests.get(weather_api_url)
                print(res.content)
                print(res.status_code)
                weather_data = res.content
                # print()
                weather_dict = json.loads(weather_data.decode('utf-8'))
                print(weather_dict)
                
                for locat in weather_dict['location']:
                    print(locat)
                    if locat['name']=='武汉':
                        id=locat['id']
                        print(id)
                        break
                
                weather_api_url = f"{API_Search}?location={id}&key={API_KEY}" 
                    
                res = requests.get(weather_api_url)
                print(res.content)
                print(res.status_code)
                weather_data = res.content
                # print()
                weather_dict = json.loads(weather_data.decode('utf-8'))
                print(weather_dict)
                
                new_weather_dict={
                    "code":weather_dict["code"],
                    "data": {  
                        "obsTime": weather_dict["now"]["obsTime"],  
                        "temp": weather_dict["now"]["temp"],  
                        "feelsLike": weather_dict["now"]["feelsLike"],  
                        "text": weather_dict["now"]["text"],  
                        "windDir": weather_dict["now"]["windDir"],  
                        "windScale": weather_dict["now"]["windScale"],  
                        "windSpeed": weather_dict["now"]["windSpeed"],  
                        "humidity": weather_dict["now"]["humidity"],  
                        "pressure": weather_dict["now"]["pressure"]  
                    },  
                    "msg":"查询成功"
                }  
                  
                # 发送响应给客户端  
                self.send_response(200)  
                self.send_header('Content-type', 'application/json')  
                self.end_headers()  
                self.wfile.write(json.dumps(new_weather_dict).encode('utf-8'))  
                
  
            except Exception as e:  
                # 处理请求异常  
                self.send_error(500, f"Failed to retrieve weather data for {location}: {e}")  
  
        else:  
            # 如果没有提供location参数，则返回错误  
            self.send_error(400, "Missing 'location' parameter in request")  
  
# 创建HTTPServer实例，监听端口9091  
server_address = ('localhost', 9091)  
httpd = socketserver.TCPServer(server_address, WeatherHandler)  
  
# 启动HTTP服务器  
print("Starting dynamic weather API server on port 9091...")  
httpd.serve_forever()