# -*- coding: utf-8 -*-
"""
验证码获取
"""

import time
import pytesseract
from PIL import Image


# 获取验证码
def get_pictures(driver1, xpath, element):
    # 整个页面截图的图片存放路径
    driver = driver1
    driver.save_screenshot(r'./BasePages/verifyCodePic/poo.png')
    # id是验证码在页面上的id
    pg = driver.find_element(xpath, element)
    left = pg.location['x']
    top = pg.location['y']
    right = pg.size['width'] + left
    height = pg.size['height'] + top
    im = Image.open(r'./BasePages/verifyCodePic/poo.png')
    image_obj = im.crop((left, top + 2, right, height))
    # 验证码截图的图片存放路径
    image_obj.save(r'./BasePages/verifyCodePic/poo2.png')
    time.sleep(2)
    image = Image.open(r'./BasePages/verifyCodePic/poo2.png')
    images = image_obj.convert("L")  # 转灰度
    PixData = images.load()
    w, h = images.size
    # 像素值
    threshold = 140
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if PixData[x, y] < threshold:
                PixData[x, y] = 0
            else:
                PixData[x, y] = 255
    data = images.getdata()
    w, h = images.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]  # 中央像素点像素值
            if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                # 判断上下左右的黑色像素点总个数
                if top_pixel < 10:
                    black_point += 1
                if left_pixel < 10:
                    black_point += 1
                if down_pixel < 10:
                    black_point += 1
                if right_pixel < 10:
                    black_point += 1
                if black_point < 1:
                    images.putpixel((x, y), 255)
                black_point = 0
    images.save(r'./BasePages/verifyCodePic/poo3.png')
    result = pytesseract.image_to_string(images, config='--psm 7')  # 图片转文字
    # print('识别结果：' + result)
    return result
