let Water_lev = 0
let Tem = 0
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("MC-DT-2.4G", "mcdt1234")
let Light_lev = 0
if (ESP8266_IoT.wifiState(true)) {
    basic.showIcon(IconNames.Yes)
} else {
    basic.showIcon(IconNames.No)
}
basic.forever(function () {
    ESP8266_IoT.connectThingSpeak()
    Light_lev = pins.analogReadPin(AnalogReadWritePin.P1)
    Tem = Environment.dht11value(Environment.DHT11Type.DHT11_temperature_C, DigitalPin.P2)
    Water_lev = pins.analogReadPin(AnalogReadWritePin.P10)
    ESP8266_IoT.setData(
    "BXXYBCYE2Y6OFV7Z",
    Light_lev,
    Tem,
    Water_lev
    )
    ESP8266_IoT.uploadData()
    basic.pause(15000)
})
