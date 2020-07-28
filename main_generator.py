from key_generator import Generator
import cv2

g = Generator(40, 40)
trigger_img = g.get_trigger_image()
cv2.imwrite('img/trigger_image.jpg', trigger_img)
verification_img = g.get_verification_image(trigger_img)
cv2.imwrite('img/verification_image.jpg', verification_img)
