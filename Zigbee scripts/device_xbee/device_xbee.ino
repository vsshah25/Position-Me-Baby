#include <XBee.h>
#include <Printers.h>

XBee xbee = XBee()

Rx16Response rx16 = Rx16Response();

void setup()
{
    xbee.begin(9600);
    Serial.begin(9600);
}

void loop()
{
    
    xbee.readPacket(100);
    if (xbee.getResponse().isAvailable())
    {
        if (xbee.getResponse().getApiId() == RX_16_RESPONSE)
        {
            xbee.getResponse().getRx16Response(rx16);
            //Serial.print( rx16.getRssi() );
            for (int i = 0; i < rx16.getDataLength(); i++)
                  {
                    Serial.print( rx16.getData(i), HEX );
                  }
        }
    }
}

