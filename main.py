from ppadb.client import Client
import time

def tap(device, x, y):
    device.shell(f'input tap {x} {y}')

def cekDevices(device):
    if (len(device) == 0):
        print('device tidak ditemukan')
        exit()

def findTapViewReplies(device, t):
    try:
        find_coor = t.index('com.ss.android.ugc.trill:id/f5r')+302
        x, y = t[find_coor:find_coor+8].split(',')
        tap(device, x, y)
        return 1
    except:
        return 0

def clickLike(device, t):
    try:
        count = t.count('com.ss.android.ugc.trill:id/bw5')
        for i in range(count):
            i = t.index('com.ss.android.ugc.trill:id/bw5')+277
            t = t[i:]
            if 'false' in t[:t.index('bounds')]:
                s = t[:t.index(']')].split('[')[1]
                x,y = s.split(',')
                tap(device, x, y)
    except:
        print('not found like')

def swipeUp(device,xs,ys,xd,yd,time=1000):
    device.shell(f'input swipe {xs} {ys} {xd} {yd} {time}')

def main():
    adb = Client(host='localhost', port=5037)
    devices = adb.devices()
    cekDevices(devices)
    while 1:
        text_ui = devices[0].shell('uiautomator dump /dev/tty')

        if findTapViewReplies(devices[0], text_ui):
            text_ui = devices[0].shell('uiautomator dump /dev/tty')
            time.sleep(2)

        clickLike(devices[0], text_ui)
        swipeUp(devices[0], 500, 1650, 500, 1000, 400)


if __name__=='__main__':
    main()




