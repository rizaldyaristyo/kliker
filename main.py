import os, pyaudio, wave
from pynput.mouse import Listener
# from pynput.keyboard import Key, Listener
OS_SLASH = '\\' if os.name == 'nt' else '/'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))+OS_SLASH
pya = pyaudio.PyAudio()
mbhalf1,mbhalf2 = wave.open(DIR_PATH+'cl.wav', 'rb'), wave.open(DIR_PATH+'ick.wav', 'rb')
# mscroll = wave.open(DIR_PATH+'scroll.wav', 'rb')
# kbpresses = [wave.open(DIR_PATH+'key'+str(i)+'.wav', 'rb') for i in range(1, 27)]

mbdata1,mbdata2 = mbhalf1.readframes(mbhalf1.getnframes()), mbhalf2.readframes(mbhalf2.getnframes())
# mscrolldata = mscroll.readframes(mscroll.getnframes())
# kbpressdata = [kbpresses[i].readframes(kbpresses[i].getnframes()) for i in range(0, 26)]

stream1 = pya.open(format=pya.get_format_from_width(mbhalf1.getsampwidth()), channels=mbhalf1.getnchannels(), rate=mbhalf1.getframerate(), output=True)
stream2 = pya.open(format=pya.get_format_from_width(mbhalf2.getsampwidth()), channels=mbhalf2.getnchannels(), rate=mbhalf2.getframerate(), output=True)
# stream3 = pya.open(format=pya.get_format_from_width(mscroll.getsampwidth()), channels=mscroll.getnchannels(), rate=mscroll.getframerate(), output=True)
# stream4 = [pya.open(format=pya.get_format_from_width(kbpresses[i].getsampwidth()), channels=kbpresses[i].getnchannels(), rate=kbpresses[i].getframerate(), output=True) for i in range(0, 26)]

def on_click(x, y, button, pressed):
    print(x, y, button, pressed)
    stream1.write(mbdata1) if pressed else stream2.write(mbdata2)

# MOUSE SCROLL WIP
# def on_scroll(x, y, dx, dy):
#     print(x, y, dx, dy)
#     stream3.write(mscrolldata)
# with Listener(on_click=on_click,on_scroll=on_scroll) as listener: listener.join()

with Listener(on_click=on_click) as listener: listener.join()

# KEYBOARD PRESSES WIP
# def on_press(key):
#     print(key)
#     # enter, shift, capslk, bksp, ctrl, space = special audio
#     # else = randomize audio
#     if key == Key.enter: stream4[0].write(kbpressdata[0])
#     elif key == Key.shift: stream4[1].write(kbpressdata[1])
#     elif key == Key.caps_lock: stream4[2].write(kbpressdata[2])
#     elif key == Key.backspace: stream4[3].write(kbpressdata[3])
#     elif key == Key.ctrl: stream4[4].write(kbpressdata[4])
#     elif key == Key.space: stream4[5].write(kbpressdata[5])
#     else: stream4[6].write(kbpressdata[6])