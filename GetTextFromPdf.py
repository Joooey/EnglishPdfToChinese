#  -*- encoding: utf-8 -*-
from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
import pytesseract


def getTxtFromPdf(PdfPath):
    #  用来保存图像和对应的文字
    req_image = []
    final_text = []
    #  打开pdf文件，并转为图像，替换./xxx.pdf
    image_pdf = Image(filename=PdfPath, resolution=300)
    image_jpeg = image_pdf.convert('jpeg')
    image_jpeg.save(filename='demo.jpeg')


    #  把图片放到req_image中
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))
    #  为每个图像运行OCR，识别图像中的文本
        for img in req_image:
            code = pytesseract.image_to_string(PI.open(io.BytesIO(img)), lang='chi_sim')
            print(code)



if __name__ == "__main__":
    PdfPath = '/home/dmrfcoder/Document/CSI/IOT.pdf'
    getTxtFromPdf(PdfPath)
