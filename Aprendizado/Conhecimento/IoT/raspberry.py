from sense_emu import SenseHat
import time

sense = SenseHat()
sense.clear()
sense.show_message("Projeto IoT Raspberry", text_colour=(0,255,0), back_colour=(0,0,0))

def relatorio(temp, pres, humi):
    print(f"Temperatura atual: {temp}")
    print(f"Pressão atual: {pres}")
    print(f"Umidade atual: {humi}")
    print("-------------------------")
    time.sleep(2)

while True:
    temp = sense.get_temperature()
    pres = sense.get_pressure()
    humi = sense.get_humidity()
    if humi > 70.0 or humi < 50.0:
        print('Umidade critica')
        sense.show_message("Unidade critica", text_colour=(255,0,0), back_colour=(0,0,0))
    else:
        print('Umidade normal')
        sense.show_message("Umidade normal", text_colour=(0,255,0), back_colour=(0,0,0))
    relatorio(temp,pres,humi)
