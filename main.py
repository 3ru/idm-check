import nfc
import binascii

print('起動中...')
clf = nfc.ContactlessFrontend('usb')
print('カードをタッチしてください:')
try:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
finally:
    clf.close()
idm = binascii.hexlify(tag.idm)
print(idm)
print('カードを離して下さい')