#include <LiquidCrystal.h>

// 1. LCD Display Pins (as per your Table 2)
const int LCD_RS = 2;  // RS  -> D2
const int LCD_E  = 3;  // EN  -> D3
const int LCD_D4 = 4;  // DB4 -> D4
const int LCD_D5 = 5;  // DB5 -> D5
const int LCD_D6 = 6;  // DB6 -> D6
const int LCD_D7 = 7;  // DB7 -> D7

// 2. Sensor Pin
const int SENSOR_PIN = A0; // Sensor connected to Analog Pin A0

// 3. Number of samples to average for smoothing
const int NUM_READINGS = 10;

// --- FINAL CALIBRATION COEFFICIENTS ---
const float a1 = -7125.844;
const float a0 = 6307.547;
const float a2 = 2023.175;

// Initialize the LCD library with your pin numbers
LiquidCrystal lcd(LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

void setup() {
  lcd.begin(16, 2);
  lcd.print("PT100 Thermometer");
  lcd.setCursor(0, 1);
  lcd.print("Re-Calibrated...");
  delay(2000);
}

void loop() {
  
  // --- Averaging Loop ---
  float totalValue = 0;
  for (int i = 0; i < NUM_READINGS; i++) {
    totalValue += analogRead(SENSOR_PIN);
    delay(1); // Small delay between readings
  }
  
  // 1. Get the average raw value
  float averageValue = totalValue / NUM_READINGS;
  
  // 2. Convert the average raw value to a voltage
  float voltage = averageValue * (5.0 / 1023.0);
  
  // 3. Compute the temperature using your FINAL equation
  float temperature = (a2*voltage*voltage)+(a1 * voltage) + a0;

  // 4. Display the results on the LCD
  lcd.clear();
  
  // Print Voltage on the first line
  lcd.setCursor(0, 0);
  lcd.print("Volt: ");
  lcd.print(voltage, 3); // Print voltage with 3 decimal places
  lcd.print(" V");
  
  // Print Temperature on the second line
  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.print(temperature, 1); // Print temperature with 1 decimal place
  lcd.print((char)223); // Print the degree symbol
  lcd.print("C");
  
  // Wait 1 second before the next loop
  delay(1000); 
}