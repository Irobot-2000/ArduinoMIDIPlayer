#include "include.h"


// Define the buzzer pin
int buzzerPin = 8;

void setup() {
  // Iterate over the notes of the melody:
  
}

void loop() {
for (int thisNote = 0; thisNote < length; thisNote++) {
    int noteDuration = noteDurations[thisNote] * 4  ;
    tone(buzzerPin, melody[thisNote] * 3, noteDuration);

    // To distinguish the notes, set a minimum time between them.
    int pauseBetweenNotes = noteDuration  * 1.2;
    delay(pauseBetweenNotes);

    // Stop the tone playing:
    noTone(buzzerPin);
  }
}