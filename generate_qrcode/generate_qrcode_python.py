#  pip install pyqrcode
#  pip install pypng
import pyqrcode
import png
from pyqrcode import QRCode

# Link de la pagina de la que se quiere generar el QR
QRString = 'https://www.instagram.com/lily_devcode/'

# Monta el QRCode #
url = pyqrcode.create(QRString)

# Salva el QRCode generdao en un archivo PNG local
url.png(r'qr.png', scale=6)
