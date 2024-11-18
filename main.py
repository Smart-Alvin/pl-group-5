ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("MC-DT-2.4G", "mcdt1234")
let Light_level = 0
if (ESP8266_IoT.wifiState(true)) {
    basic.showIcon(IconNames.Yes)
}
basic.forever(function () {
    ESP8266_IoT.connectThingSpeak()
    Light_level = input.lightLevel()
    ESP8266_IoT.setData(
    "BXXYBCYE2Y6OFV7Z",
    Light_level
    )
    ESP8266_IoT.uploadData()
    basic.pause(5000)
    if (ESP8266_IoT.wifiState(false)) {
        basic.showIcon(IconNames.Yes)
    }
    basic.showString("" + (Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C)))
})
