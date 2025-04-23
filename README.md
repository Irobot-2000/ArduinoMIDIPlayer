#Arduino midi player

credits : some code was copied from [https://www.build-electronic-circuits.com/arduino-speaker/](https://www.build-electronic-circuits.com/arduino-speaker/)

##How to run
1.install python dependency "mido" with
    ```pip install mido```
2. connect a speaker to the arduino (earphone also works) ,
 One end to the gnd pin, the other to the gpio 8 pin though an ~500ohm resistor
3. Paste the midi file in the midi folder and run midireader.py
4. The notes.cpp file should now be generated
5. Write the program from the ino file into the arduino with the arduino ide

