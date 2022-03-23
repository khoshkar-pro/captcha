from captcha.image import ImageCaptcha
import os
captcha_value = int.from_bytes(os.urandom(2), byteorder='big')
ImageCaptcha(width=150, height=50).write(str(captcha_value), './captcha/captcha.png')
print(captcha_value)