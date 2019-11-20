/*********
  Justin Christenson | https://github.com/justincdotme
  A set of Python and C++ scripts for controlling an Arduino with attached relays over a serial connection.

  https://github.com/justincdotme/arduino-relay
*********/

int relayCount = 12;
int i;
int r;
int s;
String readString;

void setup() {
  Serial.begin(9600);

  //init pins
  for (int i=1; i<= relayCount; ++i) {
    int p = i+1;
    pinMode(p, OUTPUT);
    digitalWrite(p, HIGH); //turn /em off
    delay(50);
  }
}

void loop() {
  while (!Serial.available()) {}

  while (Serial.available()) {
    delay(60);  //delay to allow buffer to fill
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }

  if (readString.length() >0) {
      i = readString.toInt();
      r = (i / 10);
      s = (i % 10);

      if (getIntCount(i>=2)) {
          if (setRelay(r, s)) {
            Serial.println("TRUE");
          } else {
            Serial.println("FALSE");
          }

      } else {
        Serial.println("EXCEPTION");
        Serial.println(i);
        Serial.println(r);
        Serial.println(s);
      }
      readString = ""; //Clear
  }

  delay(500);
}

bool setRelay(int r, bool s) {
      int rPin = (r + 1); //relays 1-n

      if (s==1 && digitalRead(rPin)==HIGH) {
        digitalWrite(rPin, LOW); //on
        return true;
      }

      if (s==0 && digitalRead(rPin)==LOW) {
        digitalWrite(rPin, HIGH); //off
        return true;
      }
       return false;
}

int getIntCount(int i) {
  if (i<=0) {
    return 0;
  } else if (i < 10) {
    return 1;
  } else if (i < 100) {
    return 2;
  } else if (i < 1000) {
    return 3;
  }

  return 0;
}