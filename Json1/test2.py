import http.server
import socketserver
import urllib.request
import urllib.parse
import json

API_key='6848f5c3ec784faa833a0e687af83d91'
API_URL='https://devapi.qweather.com/v7/weather/now'

class WeatherHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # query_string=self.path.split('?',1)[-1]if '?' in self.path else ''
        # query_params=urllib.parse.parse_qs(query_string)
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        # self.wfile.write(weather_data.encode('utf-8'))
        data = {"name": "zhangsan", 'age': 20}
        self.wfile.write(json.dumps(data).encode('utf-8'))
        # location=query_params.get('location',[None])[0]
        
        # if location:
        #     weather_api_url=f"{API_URL}?location={location}&key={API_key}"
            
        #     with urllib.request.urlopen(weather_api_url) as response:
        #         weather_data = response.read()
        #         print(weather_data)
        #         print(type(weather_data))
                
                
        #         weather_dict = json.loads(weather_data)
                
        #         self.send_response(200)
        #         self.send_header('Content-type','appliction/json')
        #         self.end_headers()
        #         # self.wfile.write(weather_data.encode('utf-8'))
        #         self.wfile.write("{\"name\":\"123\"}")
                
        # else:
        #     self.send_error(400,"Missing 'location' parameter in request" )
        
server_address = ('localhost',9093)
httpd = socketserver.TCPServer(server_address,WeatherHandler)


print("Starting dynamic weather API server on port 9093")
httpd.serve_forever()