# -*- coding:utf-8 -*-
from gs.conf import const

NODULE_RECIPE_TREE = [
    {
        'size': (8, 0),
        'size_name': u'大于8mm',
        'volume': '>250m3',
        'children': [
            {
                'status': const.NODULE_STATUS_SOLID,
                'status_name': u'实性',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'3个月内考虑进行CT/穿刺活检/PET-CT',
                            'high_risk': u'3个月内考虑进行CT/穿刺活检/PET-CT'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'3-6个月复查CT，18-24个月考虑再次复查CT',
                            'high_risk': u'3-6个月复查CT，18-24个月再次复查CT'
                        }
                    },
                ]
            },
            {
                'status': const.NODULE_STATUS_PARTSOLID,
                'status_name': u'半实性',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'3-6个月复查CT，如持续存在且实性成分<6mm，5年内每年复查CT（如部分实性结节内实性成分>6mm且随访持续存在的，高度怀疑恶性）',
                            'high_risk': u'3-6个月复查CT，如持续存在且实性成分<6mm，5年内每年复查CT（如部分实性结节内实性成分>6mm且随访持续存在的，高度怀疑恶性）'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'3-6个月复查CT，根据其中恶性程度最高的结节指定方案',
                            'high_risk': u'3-6个月复查CT，根据其中恶性程度最高的结节指定方案'
                        }
                    },
                ]
            },
            {
                'status': const.NODULE_STATUS_GROUNDGLASS,
                'status_name': u'磨玻璃',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'6-12个月复查CT，如持续存在，5年内每2年复查CT（如复查增长或产生实性成分，考虑手术）',
                            'high_risk': u'6-12个月复查CT，如持续存在，5年内每2年复查CT（如复查增长或产生实性成分，考虑手术）'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'3-6个月复查CT，根据其中恶性程度最高的结节指定方案',
                            'high_risk': u'3-6个月复查CT，根据其中恶性程度最高的结节指定方案'
                        }
                    },
                ]
            },

        ]
    },
    {
        'size': (6, 8),
        'size_name': '6-8mm',
        'volume': '100-250m3',
        'children': [
            {
                'status': const.NODULE_STATUS_SOLID,
                'status_name': u'实性',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'6-8月复查CT，18-24月考虑再次复查CT',
                            'high_risk': u'6-8月复查CT，18-24月再次复查CT'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'6-8月复查CT，18-24月考虑再次复查CT',
                            'high_risk': u'6-8月复查CT，18-24月再次复查CT'
                        }
                    },
                ]
            },
            {
                'status': const.NODULE_STATUS_PARTSOLID,
                'status_name': u'半实性',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'3-6个月复查CT，如持续存在且实性成分<6mm，5年内每年复查CT（如部分实性结节内实性成分>6mm且随访持续存在的，高度怀疑恶性）',
                            'high_risk': u'3-6个月复查CT，如持续存在且实性成分<6mm，5年内每年复查CT（如部分实性结节内实性成分>6mm且随访持续存在的，高度怀疑恶性）'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'3-6个月复查CT，根据其中恶性程度最高的结节指定方案',
                            'high_risk': u'3-6个月复查CT，根据其中恶性程度最高的结节指定方案'
                        }
                    },
                ]
            },
            {
                'status': const.NODULE_STATUS_GROUNDGLASS,
                'status_name': u'磨玻璃',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'6-12个月复查CT，如持续存在，5年内每2年复查CT（如复查增长或产生实性成分，考虑手术）',
                            'high_risk': u'6-12个月复查CT，如持续存在，5年内每2年复查CT（如复查增长或产生实性成分，考虑手术）'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'3-6个月复查CT，根据其中恶性程度最高的结节指定方案',
                            'high_risk': u'3-6个月复查CT，根据其中恶性程度最高的结节指定方案'
                        }
                    },
                ]
            },

        ]
    },
    {
        'size': (0, 6),
        'size_name': u'小于6mm',
        'volume': '<100m3',
        'children': [
            {
                'status': const.NODULE_STATUS_SOLID,
                'status_name': u'实性',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'无需随访（如形态可疑或位于上叶，可12个月后复查）',
                            'high_risk': u'12个月后复查CT'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'无需随访（如形态可疑或位于上叶，可12个月后复查）',
                            'high_risk': u'12个月后复查CT'
                        }
                    },
                ]
            },
            {
                'status': const.NODULE_STATUS_PARTSOLID,
                'status_name': u'半实性',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'无需随访',
                            'high_risk': u'无需随访'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'3-6个月复查CT，如复查无变化，2-4年后随访',
                            'high_risk': u'3-6个月复查CT，如复查无变化，2-4年后随访'
                        }
                    },
                ]
            },
            {
                'status': const.NODULE_STATUS_GROUNDGLASS,
                'status_name': u'磨玻璃',
                'children': [
                    {
                        'number': 'solitary',
                        'number_name': u'单个',
                        'report': {
                            'low_risk': u'无需随访（如可疑恶性，可2-4年后随访，如增大或产生实性成分，建议手术）',
                            'high_risk': u'无需随访（如可疑恶性，可2-4年后随访，如增大或产生实性成分，建议手术）'
                        }
                    },
                    {
                        'number': 'multiple',
                        'number_name': u'多发',
                        'report': {
                            'low_risk': u'3-6个月复查CT，如复查无变化，2-4年后随访',
                            'high_risk': u'3-6个月复查CT，如复查无变化，2-4年后随访'
                        }
                    },
                ]
            },

        ]
    }
]
