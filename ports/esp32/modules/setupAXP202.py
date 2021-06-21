import axp202
import constants

a = axp202.PMU(address=axp202.AXP192_SLAVE_ADDRESS)
# a.setDCDC1Voltage(3300) # esp32 core VDD    3v3
a.setLDO2Voltage(3300)   # T-Beam LORA VDD   3v3
a.setLDO3Voltage(3300)   # T-Beam GPS  VDD    3v3
a.enablePower(axp202.AXP192_LDO3)
a.enablePower(axp202.AXP192_LDO2)

a.setChgLEDMode(axp202.AXP20X_LED_BLINK_1HZ)
a.enableADC(axp202.AXP202_ADC1, axp202.AXP202_VBUS_VOL_ADC1)
a.enableADC(axp202.AXP202_ADC1, axp202.AXP202_VBUS_CUR_ADC1)
a.enableADC(axp202.AXP202_ADC1, axp202.AXP202_BATT_VOL_ADC1)
a.enableADC(axp202.AXP202_ADC1, axp202.AXP202_BATT_CUR_ADC1)

voltage = a.getVbusVoltage()
current = a.getVbusCurrent()
battVoltage = a.getBattVoltage()
battCurrent = a.getBattChargeCurrent()
enabledCharging = a.isChargeingEnable()
battConnected = a.isBatteryConnect()
isCharging = a.isChargeing()
perce = a.getBattPercentage()
temp = a.getTemp()

print("isChargeing: V: %f C:%f  BC:%f  perce:%d" % (voltage, current, battCurrent, perce))
