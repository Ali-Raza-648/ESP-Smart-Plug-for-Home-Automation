#include <WiFi.h>
#include <ESPAsyncWebServer.h>

const char *ssid = "your-ssid";
const char *password = "your-password";
const int ledPin = 2; // GPIO pin connected to the LED

AsyncWebServer server(80);

void setup() {
  // Serial port for debugging purposes
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Route to control GPIO
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    String html = "<html><body>";
    html += "<h1>ESP32 Web Control</h1>";
    html += "<p>Click the button to toggle LED:</p>";
    html += "<form action=\"/toggle\" method=\"post\"><input type=\"submit\" value=\"Toggle LED\"></form>";
    html += "</body></html>";
    request->send(200, "text/html", html);
  });

  // Route to handle LED toggle
  server.on("/toggle", HTTP_POST, [](AsyncWebServerRequest *request){
    // Toggle the LED
    digitalWrite(ledPin, !digitalRead(ledPin));
    request->send(200, "text/plain", "Toggle successful");
  });

  // Start server
  server.begin();

  // Set the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Nothing to do here
}
