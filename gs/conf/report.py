# -*- coding:utf-8 -*-
OK_TEMPLATE = u'胸廓两侧对称，气管居中，纵隔无移位。两肺纹理清晰，两肺门影未见明显增大，两侧胸膜未见异常，两侧胸腔未见明显积液，纵隔内未见明显肿大淋巴结。心影未见明显增大。'
SUB_TEMPLATE = u'胸廓两侧对称，气管居中，纵隔无移位。两肺纹理清晰，两肺门影未见明显增大，两侧胸膜未见异常，两侧胸腔未见明显积液，纵隔内未见明显肿大淋巴结。心影未见明显增大。'

BIG_NODULE_DESC = u"{locate}{texture}，长径约{diameter}，"
SMALL_NODULE_DESC = u"{locate}{desc}，"

TEXURE_MAP = {
    0: u'磨玻璃结节影',
    1: u'磨玻璃结节',
    2: u'半实性结节',
    3: u'实性结节',
    4: u'钙化灶',
    5: u'钙化结节'
}

BIGBIG_MIN = 8
BIG_MIN = 4
BIG_CNT = 3
