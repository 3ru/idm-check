import nfc
import binascii

print('起動中...')
clf = nfc.ContactlessFrontend('usb')
print('カードをタッチしてください↓\n')
try:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
finally:
    clf.close()
ID = binascii.hexlify(tag.identifier).decode().upper()
print(f'あなたのIDは{ID}です。')


