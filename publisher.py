from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)


class Handler(SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			html = """
				<!DOCTYPE html>
				<html lang="en">
				<head>
    				<meta charset="UTF-8">
    				<meta name="viewport" content="width=device-width, initial-scale=1.0">
       				<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    			<title>Control Your IoT Device</title>
				</head>

				<body style="background-color: #f2f2f2; background-image: url('simpl.jpg'); background-size: cover; font-family: Arial, sans-serif; justify-content: center; align-items: center; height: 100vh; margin: 0; padding-top:15%;">
    					<div class="container" style="color: #333;">
        				<h1 style="color: #1a73e8; font-size: 3.5rem; font-weight: bold; margin-bottom: 10px;">Control Your Device from Anywhere in the World</h1>
        				<p style="font-size: 1.5rem; margin-top: 0;">Take charge of your IoT device with ease.
						</p>

      					<div class="form-check form-switch mx-auto" style="margin-top: 2rem; align-items: center;">
            			<input id="btn" class="form-check-input" type="checkbox" style="width: 8rem; height: 3rem;>
            			<label class="form-check-label" for="btn" style="font-size: 1.2rem; font-weight: bold; position: absolute; top: 50%; transform: translateY(-50%); left: 110%; transition: left 0.3s ease;"></label>
        				</div>

				   <script>
					   function clicked(bid) {
						   var btn = document.getElementById(bid);
						   var xml_req = new XMLHttpRequest();
						   xml_req.open("GET", "/" + btn.checked, true);
						   xml_req.send();
					   }
				   </script>
				   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
				</body>
				</html>
		   """
		    
			self.wfile.write(html.encode())
	    
		else:
			btn_id = self.path[1:]
			if btn_id in ['true', 'false']:
				message = '0'
				if btn_id == 'true':
					message = '1'

				topic = "Bilal_Yousaf"
				client.publish(topic, message)


if __name__ == "__main__":
	with TCPServer(("localhost", 8000), Handler) as httpd:
		httpd.serve_forever()
