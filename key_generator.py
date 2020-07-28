import numpy as np
from scipy import ndimage


class Generator:
    def __init__(self, m, n):
        """
        @param m: height of the image that the generator takes as input
        @param n: width of the image that the generator takes as input
        """
        self.m = m
        self.n = n

    def get_trigger_image(self):
        trigger_img = np.random.uniform(0, 255, (self.m, self.n))
        return trigger_img

    def get_verification_image(self, trigger_img):
        filter_img = ndimage.median_filter(trigger_img, (self.m, self.n))
        verification_img = np.subtract(trigger_img, filter_img)
        return verification_img
