# -*- coding:utf-8 -*-
# 常量定义 比如 是=1 否=2

COMMON_NO = 1
COMMON_YES = 2

PASS_CONST_KEY = 'lxp^poiu^qq#ll'
DEFAULT_AVATAR = '/get/data/url/%s'

DEFAULT_PASSWORD = '123456'

RKEY_VCODE = 'VCODE'
RKEY_TOKEN = 'TOKEN_'
RKEY_STUDYSTACK = 'STUDYSTACK_'

STUDY_STACK_EXPIRE = 60 * 3
TOKEN_EXPIRE = 60 * 60 * 24 * 30

NOT_LOGIN_PATH = ['/login', '/vtk3d/generate']
NOT_LOGIN_PREFIX = ['/static', '/hello', '/user/vcode', '/get/data/url', '/mips/generate', '/study/push', '/iptest',
                    '/vtk3d/generate', '/version/validate', '/config/get', '/mip/get', '/frequentlytypes']

DEFAULT_LIMIT = 10

ROLE_WRITE = 'write'
ROLE_REVIEW = 'review'
ROLE_PVIEW = 'pview'

IMAGELINK_PRE = 'imagelink_pre'
FILELINK_PRE = 'filelink_pre'

MAX_FOLDER = 20
MAX_MIPCACHE = 500

STUDY_STATUS_UNPVIEW = 0
STUDY_STATUS_PVIEWED = 1
STUDY_STATUS_SUBMIT = 2

STUDY_STATUS_UNASSIGN = 1
STUDY_STATUS_UNWRITE = 2
STUDY_STATUS_WRITED = 3
STUDY_STATUS_REVIEWED = 4

STUDY_PREDICT_NORMAL = 1
STUDY_PREDICT_ABNORMAL = 2

DEFAULT_NODULE_SIZE = (20, 20, 20)

NODULE_STATUS_SOLID = [3]
NODULE_STATUS_PARTSOLID = [0, 2]
NODULE_STATUS_GROUNDGLASS = [1]
NODULE_STATUS_DELETED = -1
NODULE_STATUS_INITIAL = 0

NODULE_SOLITARY = 'solitary'
NODULE_MULTIPLE = 'mutiple'

CREATE_TYPE_MACHINE = 1
CREATE_TYPE_MAN = 2

NODULE_GROUP_DISTANCE = 10

STYPE_CT = 'CT'
STYPE_ONE = 'ONE'

PLATFORM_DARWIN = 'darwin'
PLATFORM_WIN32 = 'win32'

WLWW_SHORT_KEY_LIST = [5, 6, 7, 8, 9, 0]

PVIEWONLY = False

DEFAULT_NODULETYPE = [u'磨玻璃结节', u'实性结节', u'钙化灶', u'肿块', u'磨玻璃影', u'结节',u'其他']

DEFAULT_SID = 3393
