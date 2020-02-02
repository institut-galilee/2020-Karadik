#include "LedControl.h"
LedControl lc = LedControl(4,5,6,1);

int count = 1000;

void setup()
{
    lc.shutdown(0,false);
    lc.setIntensity(0,5);
    lc.clearDisplay(0);
}

void loop()
{
    String t = String(count++);
    lc.setDigit(0,0,(int)(t[0]-'0'),true);
    lc.setDigit(0,1,(int)(t[1]-'0'),false);
    lc.setDigit(0,2,(int)(t[2]-'0'),false);
    lc.setDigit(0,3,(int)(t[3]-'0'),false);
    delay(100);
    lc.shutdown(0,true);
    lc.shutdown(0,false);
}
