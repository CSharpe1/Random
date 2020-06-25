import qrcode
#import Image

img = qrcode.make('MKAKJANFJKNCJKNSCKJSncJASNCJKANCJKNj najcnacnakjsncjks nKJNSC KJN CKAJNSCKNAC KNASKJ CNAJKCN KAJNCAKJNCKAJNCKJANCKANCKANC')

print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (290, 290)

img.save(r"C:\Users\charles.sharpe\Desktop\QRTEST\qrcode_test.png")


#im = Image.open("C:\\Users\\charles.sharpe\\Desktop\\QRTEST\\qrcode_test.png")
#im.save("C:\\Users\\charles.sharpe\\Desktop\\QRTEST\\qrcode_TIF_test.tif")