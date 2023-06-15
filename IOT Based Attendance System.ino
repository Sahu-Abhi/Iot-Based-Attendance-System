#include <SPI.h>
#include <MFRC522.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <WiFiClientSecureBearSSL.h>

const uint8_t fingerprint[20] = {0xc1, 0x28, 0xb0, 0x5e, 0xf8, 0x50, 0x51, 0x3c, 0x3e, 0x18, 0x38, 0xc4, 0x87, 0x9f, 0xdd, 0xde, 0x5b, 0xc4, 0x00, 0x77};
// c1 28 b0 5e f8 50 51 3c 3e 18 38 c4 87 9f dd de 5b c4 00 77
#define RST_PIN  D3     // Configurable, see typical pin layout above
#define SS_PIN   D4     // Configurable, see typical pin layout above
#define green_led D1
#define red_led D2
     

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Instance of the class
MFRC522::MIFARE_Key key;  
ESP8266WiFiMulti WiFiMulti;
MFRC522::StatusCode status;      

String data2;
String NAME;
const String data1 = "https://script.google.com/macros/s/AKfycbw80ktbTteJOHmWu0a4d59yJLESf6x_wqCA3WY19z42Mjbv_EGe0cAWxmWNjbPsA2cj/exec?name=";
                      
void setup() 
{
  /* Initialize serial communications with the PC */
  Serial.begin(9600);
  // Serial.setDebugOutput(true);

  Serial.println();
  Serial.println();
  Serial.println();

  WiFi.mode(WIFI_STA);
  WiFi.begin("Abhi", "3134sahu@");
  while(WiFi.status() != WL_CONNECTED)
  {
    delay(200);
    Serial.print("..");
  }
  Serial.println();
  Serial.println("NodeMCU is Connected!");
  Serial.println(WiFi.localIP());

  /* Set BUZZER as OUTPUT */
     pinMode(green_led, OUTPUT);
     pinMode(red_led, OUTPUT);
  /* Initialize SPI bus */
  SPI.begin();
  
  Serial.println("Approximate your card to the reader...");
  Serial.println();
}
void write_data()
{
  digitalWrite(green_led, HIGH);
  delay(2000);
  digitalWrite(green_led, LOW);
  std::unique_ptr<BearSSL::WiFiClientSecure>client(new BearSSL::WiFiClientSecure);

    client->setFingerprint(fingerprint);
    
   data2 = data1 + NAME;
    data2.trim();
    Serial.println(data2);
    
    HTTPClient https;
    Serial.print(F("[HTTPS] begin...\n"));
    if (https.begin(*client, (String)data2))
    {  
      // HTTP
      Serial.print(F("[HTTPS] GET...\n"));
      // start connection and send HTTP header
      int httpCode = https.GET();
      // httpCode will be negative on error
      if (httpCode > 0) 
      {
        // HTTP header has been send and Server response header has been handled
        Serial.printf("[HTTPS] GET... code: %d\n", httpCode);
        // file found at server
      }
      else 
      {
        Serial.printf("[HTTPS] GET... failed, error: %s\n", https.errorToString(httpCode).c_str());
      }
      https.end();
      delay(1000);
    } 
    else 
    {
      Serial.printf("[HTTPS} Unable to connect\n");
    }
}

void loop()
{
  mfrc522.PCD_Init();   // Initiate MFRC522
  /* Look for new cards */
  /* Reset the loop if no new card is present on RC522 Reader */
  if ( ! mfrc522.PICC_IsNewCardPresent())
  {
    return;
  }
  /* Select one of the cards */
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  
  Serial.println();
  //Show UID on serial monitor
  Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Message : ");
  content.toUpperCase();
 

  
  // wait for WiFi connection
  if ((WiFiMulti.run() == WL_CONNECTED)) 
  {
     if (content.substring(1) == "D0 6D 5D 4D") //change here the UID of the card/cards that you want to give access
  {
    Serial.println("Authorized access");
    NAME = "Student%201";
    write_data();
   
  }
     if (content.substring(1) == "82 C3 80 CB") //change here the UID of the card/cards that you want to give access
  {
    Serial.println("Authorized access");
    NAME = "Student%202";
    write_data();
  }
    if (content.substring(1) == "D3 E1 F4 94") //change here the UID of the card/cards that you want to give access
  {
    Serial.println("Authorized access");
    NAME = "Student%202";
    write_data();
  }
    if(content.substring(1) != "82 C3 80 CB"|| content.substring(1) != "D0 6D 5D 4D" || content.substring(1) != "D3 E1 F4 94")  {
    digitalWrite(red_led, HIGH);
    delay(2000);
    digitalWrite(red_led, LOW);
    Serial.println(" Access denied");
  } 
 }
}
