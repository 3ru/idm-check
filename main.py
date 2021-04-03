import nfc
import binascii

print('起動中...')

with nfc.ContactlessFrontend("usb") as clf:
    print('カードをタッチしてください↓\n')
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
    ID = binascii.hexlify(tag.identifier).decode().upper()
    print(f'あなたのIDは{ID}です。')
