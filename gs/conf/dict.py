# -*- coding:utf-8 -*-
from gs.conf import server
# from gs.model.process import InPaper, Letter, OutPaper
# from gs.model.other import Fine, Hire
# from gs.model.oa import AssetUsage, Attendance, RegisterRecord, Train, CarUsage, Meeting
from gs.conf import const
MYDICT = {
    'Auth': {
        'ALL_INPAPER': u'收文列表',
        'TRAIN': u'培训管理',
        'LETTER': u'信访列表',
        'FINE': u'罚款管理',
    },
    'Inpaper_Status': {
        1: u'审批中',
        2: u'通过',
        3: u'拒绝',
        4: u'已撤销',
        5: u'已下发'
    },
    'message': {
        # const.IN_PAPER: u'您有新的收文需要审批',
        # const.LETTER_APPROVE: u'您有新的信访需要审批',
        # const.LETTER_CONFIRM: u'您有信访结案报告需要确认',
        # const.NUCLEAR_DRAFT: u'您有新的发文需要核稿',
        # const.JOINTLY_SIGN: u'您有新的发文需要会签',
        # const.ITEM_TYPE_ASSET: u'您有新的资产申请需要审批',
        # const.ITEM_TYPE_CAR: u'您有新的用车申请需要审批',
        # const.ITEM_TYPE_MEETING: u'您有新的外出会议申请需要审批',
        # const.FINE: u'您有新的%s款需要核稿',
        # const.ITEM_TYPE_HIRE: u'您有新的外聘人员申请需要审批',
        # const.ITEM_TYPE_ABROAD: u'您有新的出国申请需要审批',
        # const.ITEM_TYPE_EXTERNAL_ATTENDANCE: u'您有新的外聘考勤需要审批',
        # const.ITEM_TYPE_TRAIN_OPE: u'您有新的培训申请需要审批'
    },
    'DEAL_URL': {
        # 'IN_PAPER': server.pre_url+'/deal/in/paper/pc',
        # 'LETTER_APPROVE': server.pre_url+'/deal/letter/pc',
        # 'LETTER_CONFIRM': server.pre_url+'/deal/letter/pc',
        # 'NUCLEAR_DRAFT': server.pre_url+'/deal/out/paper/pc',
        # 'JOINTLY_SIGN': server.pre_url+'/deal/out/paper/pc'
    },
    'Letter_Status': {
        1: u'审批中',
        2: u'审批通过',
        3: u'拒绝',
        4: u'已撤销',
        5: u'结果确认中',
        6: u'确认拒绝',
        7: u'确认通过',
        8: u'承办中',
        9: u'内勤提交中',
        10: u'部长分配中',
        11: u'承办完成'
    },
    'Fine_Status': {
        1: u'核稿中',
        2: u'告知书审核中',
        3: u'告知书已审核',
        4: u'回证签收中',
        5: u'回证已签收',
        6: u'处罚决定书审核中',
        7: u'处罚决定书审核通过',
        8: u'等待到账',
        9: u'已到账',
        10: u'归档',
        11: u'延时到账',
        12: u'撤销',
        13: u'核稿完成',
        14: u'核稿拒绝'
    },
    'MODEL_KIND': {
        # const.IN_PAPER: InPaper,
        # const.LETTER_APPROVE: Letter,
        # const.LETTER_CONFIRM: Letter,
        # const.LETTER: Letter,
        # const.ITEM_TYPE_ASSET: AssetUsage,
        # const.ITEM_TYPE_CAR: CarUsage,
        # const.ITEM_TYPE_MEETING: Meeting,
        # const.FINE: Fine,
        # const.JOINTLY_SIGN: OutPaper,
        # const.NUCLEAR_DRAFT: OutPaper,
        # const.SIGN_ISSUE: OutPaper,
        # const.OUT_PAPER: OutPaper,
        # const.ITEM_TYPE_HIRE: Hire,
        # const.ITEM_TYPE_ABROAD: Attendance,
        # const.ITEM_TYPE_ATTENDANCE: Attendance,
        # const.ITEM_TYPE_EXTERNAL_ATTENDANCE: RegisterRecord,
        # const.org_check: RegisterRecord,
        # const.ITEM_TYPE_TRAIN_OPE: Train
    },
    'TODO_DTYPE': {
        # const.APPROVE: u'审批',
        # const.MEETING: u'会议',
        # const.TASK: u'任务',
        # const.TRAIN: u'培训',
        # const.TRAIN_ASSIGN: u'培训分配'
    },
    'COMMON_FUNC': {
        1: u'收文',
        2: u'信访',
        3: u'罚款',
        4: u'公告',
        5: u'会议',
        6: u'我的培训',
        7: u'邮件',
        8: u'协作',
        9: u'党建',
        10: u'用户管理',
        11: u'权限',
        12: u'流程配置',
        13: u'职责配置',
        14: u'发文',
        15: u'政策法规',
        16: u'规章制度',
        17: u'人员',
        18: u'任职晋升',
        19: u'考勤',
        20: u'工资',
        21: u'考核',
        22: u'党员信息',
        23: u'党员发展',
        24: u'党员培训',
        25: u'机构检查',
        26: u'领导工作安排',
        27: u'车辆',
        28: u'资产',
        29: u'常用功能',
        30: u'节假日',
        31: u'封面',
        32: u'项目管理',
        33: u'统计',
        34: u'培训信息',

        35: u'创建会议',
        36: u'新增收文',
        37: u'我要发文',
        38: u'新增信访',
        39: u'发起培训',
        40: u'用车申请',
        41: u'固定资产申请',
        42: u'办公用品申请',
        43: u'发邮件',
        44: u'创建任务',
        45: u'新增罚款',
        46: u'新增追款',
        47: u'发起请假',
        48: u'外聘人员申请',
        49: u'外聘考勤提交',
        50: u'上传工资表',
        51: u'提交机构检测'
    },
    'FUNC_TYPE': {
        'IN_PAPER': 1,
        'LETTER': 2,
        'FINE': 3,
        'NOTICE': 4,
        'MEETING': 5,
        'TRAIN': 6,
        'MAIL': 7,
        'ASSIGNMENT': 8,
        'ARCHIVE': 9,
        'USER': 10,
        'AUTH': 11,
        'PROCESS': 12,
        'GROUP_CONFIG': 13,
        'OUT_PAPER': 14,
        'PUB_A': 15,
        'PUB_B': 16,
        'PERSON': 17,
        'DUTY_CHANGE': 18,
        'ATTENDANCE': 19,
        'SALARY': 20,
        'ASSESSMENT': 21,
        'MEMBERINFO': 22,
        'MEMBERDEV': 23,
        'PARTY_TRAIN': 24,
        'ORG_CHECK': 25,
        'LEADER_TASK': 26,
        'CAR': 27,
        'ASSET': 28,
        'FUNC': 29,
        'HOLIDAY': 30,
        'COVER': 31,
        'PROJECT': 32,
        'STATISTICS': 33,
        'TRAIN_INFO': 34,
        'MEETING_LAUNCH': 35,
        'IN_PAPER_LAUNCH': 36,
        'OUT_PAPER_LAUNCH': 37,
        'LETTER_LAUNCH': 38,
        'TRAIN_LAUNCH': 39,
        'PARK': 40
    },
    'OutPaper_Status': {
        1: u'核稿中',
        2: u'核稿通过',
        3: u'核稿拒绝',
        4: u'会签中',
        5: u'会签通过',
        6: u'会签拒绝',
        7: u'签发中',
        8: u'已签发',
        9: u'办公室审批中',
        10: u'办公室审批完成'
    },
    'TYPE': {
        'red': u'红头文件',
        'white': u'白头文件',
        'party': u'党务文件',
    },
    'KIND': {
        'emergency': u'急件',
        'urgent': u'特急'
    },
    'CONFIDENTIALITY': {
        'secret': u'秘密',
        'confidential': u'机密',
        'topsecret': u'绝密',
    },
    'INFO_OPEN': {
        'active': u'主动公开',
        'request': u'依申请公开',
        'no': u'免于公开'
    },
    'TEMPLATE_TYPE': {
        'person_doc': u'个人文稿',
        'person_prenotice': u'个人事先告知书',
        'person_draft': u'个人草稿',
        'person_formal': u'个人正式稿',
        'person_prenotice_receipt': u'个人事先告知书送达回执',
        'person_formal_receipt': u'个人正式稿送达回执',
        'person_hearnotice': u'个人听证告知书',
        'person_hearnotice_receipt': u'个人听证告知书送达回执',
        'hospital_doc': u'医院文稿',
        'hospital_formal': u'医院正式稿',
        'drugstore_doc': u'药店文稿',
        'drugstore_formal': u'药店正式稿',
        'medical_doc': u'内设医疗机构文稿',
        'medical_formal': u'内设医疗机构正式稿',
    },
    'target_type': {
        'person': u'个人',
        'hospital': u'医疗机构',
        'drugstore': u'定点药店',
        'medical': u'内设医疗机构'
    },
    'target_fine_type_doc': {
        'hospital': 'hospital_doc',
        'drugstore': 'drugstore_doc',
        'medical': 'medical_doc'
    },
    'target_fine_type_formal': {
        'hospital': 'hospital_formal',
        'drugstore': 'drugstore_formal',
        'medical': 'medical_formal'
    },
    'target_doc_name': {
        'hospital': u'（新）追款决定书发文稿纸打印样张——区县追款(医院）.docx',
        'drugstore': u'（新）追款决定书发文稿纸打印样张——区县追款（药店）.docx',
        'medical': u'（新）追款决定书发文稿纸打印样张——区县追款(内设医疗机构）.docx'
    },
    'target_formal_name': {
        'hospital': u'责令退回费用决定书（医院）已签发.docx',
        'drugstore': u'责令退回费用决定书（药店）已签发.docx',
        'medical': u'责令退回费用决定书（内设医疗机构）已签发.docx'
    },
    'TEMPLATE_TYPE_FUNC': {
        'person_doc': 'fine_doc.person_doc',
        'person_prenotice': 'fine_doc.person_pre_notice',
        'person_draft': 'fine_doc.person_draft',
        'person_formal': 'fine_doc.person_formal',
        'person_prenotice_receipt': 'fine_doc.person_pre_notice_receipt',
        'person_formal_receipt': 'fine_doc.person_formal_receipt',
        'person_hearnotice': 'fine_doc.person_hear_notice',
        'person_hearnotice_receipt': 'fine_doc.person_hear_notice_receipt',
        'hospital_doc': 'fine_doc.hospital_doc',
        'hospital_formal': 'fine_doc.hospital_formal',
        'drugstore_doc': 'fine_doc.drugstore_doc',
        'drugstore_formal': 'fine_doc.drugstore_formal',
        'medical_doc': 'fine_doc.medical_doc',
        'medical_formal': 'fine_doc.medical_formal',
    },
    'fine_zip_file_name': {
        'person_formal_receipt': u'行政处罚决定书(正式稿)送达回证-{}.docx',
        'person_formal': u'行政处罚决定书(正式稿)-{}.docx',
        'person_draft': u'行政处罚决定书(草稿)-{}.docx',
        'person_doc': u'行政处罚决定书-文稿-{}.docx'
    },
    'asset_status': {
        1: u'库存中',
        2: u'申请中',
        3: u'使用中',
        4: u'已报废'
    },
    'asset_usage_status': {
        1: u'审批中',
        2: u'审批通过',
        3: u'已拒绝',
        4: u'已返还'
    },
    'action_type': {
        1: u'年假',
        2: u'病假',
        3: u'事假',
        4: u'婚假',
        5: u'产假',
        6: u'丧假',
        7: u'调休',
        8: u'工伤',
        9: u'产前假',
        10: u'探亲假',
        11: u'哺乳假',
    },
    'attendance_status': {
        1: u'审批中',
        2: u'已同意',
        3: u'已拒绝',
        4: u'已撤回'
    },
    'car_usage_status': {
        1: u'审批中',
        2: u'审批通过',
        3: u'审批拒绝',
        4: u'已返还'
    },
    'hire_status': {
        1: u'审批中',
        2: u'审批通过',
        3: u'已拒绝'
    },
    'meeting_status': {
      1: u'审批中',
      2: u'审批通过',
      3: u'审批拒绝',
      4: u'撤销'
    },
    'agree_message': {
        # const.ITEM_TYPE_ASSET: u'您发起的资产申请已审批完成',
        # const.ITEM_TYPE_CAR: u'您发起的用车申请已审批完成',
        # const.ITEM_TYPE_MEETING: u'您发起的外出会议申请已审批完成',
        # const.FINE: u'您发起的%s款已核稿完成',
        # const.ITEM_TYPE_HIRE: u'您发起的外聘人员申请已审批完成',
        # const.ITEM_TYPE_ABROAD: u'您发起的出国申请已审批完成',
        # const.ITEM_TYPE_EXTERNAL_ATTENDANCE: u'您提交的外聘考勤已审批完成',
        # const.ITEM_TYPE_TRAIN_OPE: u'您提交的培训申请已审批完成'
    },
    'refuse_message': {
        # const.ITEM_TYPE_ASSET: u'您发起的资产申请已被拒绝',
        # const.ITEM_TYPE_CAR: u'您发起的用车申请已被拒绝',
        # const.ITEM_TYPE_MEETING: u'您发起的外出会议申请已被拒绝',
        # const.FINE: u'您发起的%s款核稿已被拒绝',
        # const.ITEM_TYPE_HIRE: u'您发起的外聘人员申请已被拒绝',
        # const.ITEM_TYPE_ABROAD: u'您发起的出国申请已被拒绝',
        # const.ITEM_TYPE_EXTERNAL_ATTENDANCE: u'您提交的外聘考勤已被拒绝',
        # const.ITEM_TYPE_TRAIN_OPE: u'您提交的培训申请已被拒绝'
    },
    'agree_status': {
        # const.ITEM_TYPE_ASSET: const.a_agree,
        # const.ITEM_TYPE_CAR: const.a_agree,
        # const.ITEM_TYPE_MEETING: const.a_agree,
        # const.FINE: const.f_jointly_finish,
        # const.ITEM_TYPE_HIRE: const.h_agree,
        # const.ITEM_TYPE_ABROAD: const.at_agree,
        # const.ITEM_TYPE_EXTERNAL_ATTENDANCE: const.ex_agree,
        # const.ITEM_TYPE_TRAIN_OPE: const.t_agree
    },
    'refuse_status': {
        # const.ITEM_TYPE_ASSET: const.a_refuse,
        # const.ITEM_TYPE_CAR: const.a_refuse,
        # const.ITEM_TYPE_MEETING: const.a_refuse,
        # const.FINE: const.f_refuse,
        # const.ITEM_TYPE_HIRE: const.h_refuse,
        # const.ITEM_TYPE_ABROAD: const.at_refuse,
        # const.ITEM_TYPE_EXTERNAL_ATTENDANCE: const.ex_refuse,
        # const.ITEM_TYPE_TRAIN_OPE: const.t_refuse
    },
    'remind_title': {
        # const.IN_PAPER: u'您收到收文审批提醒',
        # const.LETTER_APPROVE: u'您收到信访审批提醒',
        # const.LETTER_CONFIRM: u'您收到信访结案报告确认提醒',
        # const.NUCLEAR_DRAFT: u'您收到发文核稿提醒',
        # const.JOINTLY_SIGN: u'您收到发文会签提醒',
        # const.ITEM_TYPE_ASSET: u'您收到资产申请审批提醒',
        # const.ITEM_TYPE_CAR: u'您收到用车申请审批提醒',
        # const.ITEM_TYPE_MEETING: u'您收到外出会议申请审批提醒',
        # const.FINE: u'您收到%s款核稿提醒',
        # const.ITEM_TYPE_HIRE: u'您收到外聘人员申请审批提醒',
        # const.ITEM_TYPE_ABROAD: u'您收到出国申请审批提醒',
        # const.ITEM_TYPE_EXTERNAL_ATTENDANCE: u'您收到外聘考勤审批提醒',
        # const.ITEM_TYPE_TRAIN_OPE: u'您收到培训审批提醒'
    },
    'remind_pagepath': {
        # const.IN_PAPER: 'pages/approve/inpaper/inpaper-view?paper_id=%s',
        # const.LETTER_APPROVE: 'pages/approve/letter/letter-view?letter_id=%s',
        # const.LETTER_CONFIRM: 'pages/approve/letter/letter-view?letter_id=%s',
        # const.NUCLEAR_DRAFT: 'pages/approve/outpaper/outpaper-view?paper_id=%s',
        # const.JOINTLY_SIGN: 'pages/approve/outpaper/outpaper-view?paper_id=%s',
        # const.ITEM_TYPE_ASSET: 'pages/approve/asset/asset-view?usage_id=%s',
        # const.ITEM_TYPE_CAR: 'pages/approve/carusage/carusage-view?usage_id=%s',
        # const.FINE: 'pages/approve/fine/fine-view?fine_id=%s',
        # const.ITEM_TYPE_HIRE: 'pages/approve/hire/hire-view?hire_id=%s',
        # const.ITEM_TYPE_ABROAD: "pages/approve/abroad/abroad-view?attendance_id=%s",
        # const.ITEM_TYPE_EXTERNAL_ATTENDANCE: 'pages/approve/external/external-view?record_id=%s',
        # const.ITEM_TYPE_TRAIN_OPE: "pages/approve/train/train-view?train_id=%s"
    },
    'train_status': {
        1: u'已发布',
        2: u'分配完成',
        3: u'审批中',
        4: u'审批拒绝',
        5: u'通过',
    },
    'assessment_type': {
        1: u'新员工',
        2: u'公务员考核',
        3: u'奖励',
    },
    'org_type': {
        1: u'三级医院',
        2: u'二级医院',
        3: u'一级医院',
        4: u'内设医疗机构',
        5: u'定点药店',
        6: u'其他'
    },
    'cover_dtype': {
        1: u'公告',
        2: u'党建'
    },
    'check_type': {
        1: u'常规检查',
        2: u'专项检查',
        3: u'举报检查',
        4: u'审核延伸'
    },
    'FINE_KIND': {
        'recover': u'追回款',
        'fine': u'罚款',
        'administrative': u'行政罚款',
        'refund': u'退款'
    },
    'inpaper_urgent': {
        1: u'急件',
        2: u'普通'
    },
    'inpaper_secret': {
        1: u'普通',
        2: u'秘密',
        3: u'机密'
    },
    'inpaper_dtype': {
        1: u'报告',
        2: u'请示',
        3: u'函',
        4: u'通知',
        5: u'批复',
        6: u'通报',
        7: u'简报',
        8: u'专报',
        9: u'会议纪要',
        10: u'处理意见'
    },
    'inpaper_classification': {
        1: u'市人保局',
        2: u'局属事业单位',
        3: u'外来单位',
        4: u'区县医保办'
    },
    'train_dtype': {
        1: u'所内培训',
        2: u'局培训',
        3: u'部培训'
    }
}
