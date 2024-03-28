import qrcode
img = qrcode.make('https://youtu.be/5QzzeYHApV0?si=EUHXXa-ay-l-WyxV')
img.save('myQRcode.png')
img.show()