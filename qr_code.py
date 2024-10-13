import qrcode

from PIL import Image


qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4,)
qr.add_data("https://www.linkedin.com/in/arman-alam-bb8516276/")
qr.make(fit = True)
img = qr.make_image(fill_color = "aqua", back_color = "brown")
img.save("LinkedIn.png")