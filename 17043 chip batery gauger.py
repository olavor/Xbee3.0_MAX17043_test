import binascii,time
from machine import I2C,Pin
from micropython import const
Pin("P1", Pin.OUT, value=0);Pin("D1", Pin.OUT, value=0);
from bh1750 import BH1750
i2c = I2C(1)
s = BH1750(i2c)
ilu = s.luminance(BH1750.ONCE_HIRES_1)
ilumina = int(ilu)
buf3 = bytearray(2)
i2c.readfrom_mem_into(50,2,buf3,addrsize=16)
time.sleep_ms(300)
v = (buf3[0] << 4 | buf3[1] >> 4) /1000
print(v)#tensao
time.sleep_ms(360)
REGISTER_CONFIG = const(0x0C)
REGISTER_VCELL = const(0x02);REGISTER_SOC = const(0x04);REGISTER_MODE = const(0x06);
y1 = binascii.unhexlify('971C')
i2c.writeto_mem(50,REGISTER_CONFIG,y1,addrsize=8)
y1 = binascii.unhexlify('7C00');time.sleep_ms(260);#4000
i2c.writeto_mem(50,REGISTER_MODE,y1,addrsize=8);time.sleep_ms(260);
i2c.readfrom_mem_into(50,4,buf3, addrsize=8)
time.sleep_ms(220)
w= (buf3[0] + (buf3[1] / 256.0) )
print(w);#porcentagem de carga, valores melhores
y1 = binascii.unhexlify('979C')#SLEEP
i2c.writeto_mem(50,REGISTER_CONFIG,y1,addrsize=8)
Pin("P1", Pin.OUT, value=0);Pin("D1", Pin.OUT, value=0);
