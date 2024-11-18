Water_lev = 0
Tem = 0
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("MC-DT-2.4G", "mcdt1234")
Light_lev = 0
if ESP8266_IoT.wifi_state(True):
    basic.show_icon(IconNames.YES)
else:
    basic.show_icon(IconNames.NO)

def on_forever():
    global Light_lev, Tem, Water_lev
    ESP8266_IoT.connect_thing_speak()
    Light_lev = pins.analog_read_pin(AnalogReadWritePin.P1)
    Tem = Environment.dht11value(Environment.DHT11Type.DHT11_TEMPERATURE_C, DigitalPin.P2)
    Water_lev = pins.analog_read_pin(AnalogReadWritePin.P10)
    ESP8266_IoT.set_data("BXXYBCYE2Y6OFV7Z", Light_lev, Tem, Water_lev)
    ESP8266_IoT.upload_data()
    basic.pause(15000)
basic.forever(on_forever)
