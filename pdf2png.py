import datetime
import os
import cv2
import fitz  # fitz就是pip install PyMuPDF


def pyMuPDF_fitz(pdfPath, imagePath):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.page_count):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 3.137  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 3.137
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.save((imagePath + '/' + str(pg+1)+'.png'))  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)
    text = str(pdfDoc.page_count)
    saveFile = open('./calc.txt', 'w')
    saveFile.write(text)
    saveFile.close()
def c():
    num = os.listdir("./imgs/") # num为list类型，存储着每张图片的名字
    print('共{}张图片'.format(len(num))) # 计算机当前目录有几张图片
    ori_path = "./imgs/"
    save_path = "./save/"
    for i in range(len(num)):
        img = cv2.imread(ori_path+str(i+1)+".png")  # 读取
        resize = cv2.resize(img, (1200, 1600))  # resize
        #resize = img
        cv2.imwrite(save_path+str(i+1)+'.jpg',resize)  # 保存


if __name__ == "__main__":
    # 1、PDF地址
    pdfPath = 'test.pdf'
    # 2、需要储存图片的目录
    imagePath = './imgs'
    #pyMuPDF_fitz(pdfPath, imagePath)
    c()
    

