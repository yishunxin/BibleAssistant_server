# -*- coding:utf-8 -*-
import json

from gs.common.cstore import get_token
from qiniu import put_file

if __name__ == '__main__':
    a = [u"创世记", u"出埃及记", u"利未记", u"民数记", u"申命记", u"约书亚记", u"士师记", u"路得记", u"撒母耳记上", u"撒母耳记下", u"列王纪上", u"列王记下",
         u"历代志上", u"历代志下", u"以斯拉记", u"尼希米记", u"以斯帖记", u"约伯记", u"诗篇", u"箴言", u"传道书", u"雅歌", u"以赛亚书", u"耶利米书", u"耶利米哀歌",
         u"以西结书", u"但以理书", u"何阿西书", u"约珥书", u"阿摩司书", u"俄巴底亚书", u"约拿书", u"弥迦书", u"那鸿书", u"哈巴谷书", u"西番雅书", u"哈该书",
         u"撒迦利亚书", u"玛拉基书", u"马太福音", u"马可福音", u"路加福音", u"约翰福音", u"使徒行传",u"罗马书", u"哥林多前书", u"哥林多后书", u"加拉太书", u"以弗所书", u"腓力比书",
         u"歌罗西书", u"帖撒罗尼迦前书", u"帖撒罗尼迦后书", u"提摩太前书", u"提摩太后书", u"提多书", u"腓利门书", u"希伯来书", u"雅各书", u"彼得前书", u"彼得后书",
         u"约翰一书", u"约翰二书", u"约翰三书", u"犹大书", u"启示录"]
    b = [u"创", u"出", u"利", u"民", u"申", u"书", u"士", u"得", u"撒上", u"撒下", u"王上", u"王下", u"代上", u"代下", u"拉", u"尼", u"斯",
         u"伯", u"诗", u"箴", u"传", u"歌", u"赛", u"耶", u"哀", u"结", u"但", u"何", u"珥", u"摩", u"俄", u"拿", u"弥", u"鸿", u"哈",
         u"番", u"该", u"亚", u"玛", u"太", u"可", u"路", u"约", u"徒", u"罗", u"林前", u"林后", u"加", u"弗", u"腓", u"西", u"帖前", u"帖后",
         u"提前", u"提后", u"多", u"门", u"来", u"雅", u"彼前", u"彼后", u"约一", u"约二", u"约三", u"犹", u"启"]
    new = [28, 16, 24, 21, 28, 18, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]
    old = [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14,
           3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4]
    old.extend(new)
    for i in old:
        print range(1,i+1)
    exit()
    old_dict = []
    new_dict = []
    print len(a)
    print len(b)
    for i in range(len(old)):
        old_dict.append({"fullname": a[i], "shortname": b[i], "chapter": old[i]})
    for i in range(len(new)):
        new_dict.append({"fullname": a[i + 39], "shortname": b[i + 39], "chapter": new[i]})
    for i in old_dict:
        print json.dumps(i, ensure_ascii=False)
    for i in new_dict:
        print json.dumps(i, ensure_ascii=False)
    pass
