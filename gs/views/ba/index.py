# -*- coding:utf-8 -*-
import logging
from flask import render_template

from gs.common.cresponse import common_json_response, jsonify_response
from gs.common.pager import Pager
from gs.conf import apicode
from gs.conf import const
from gs.service.record import PaperSvc
from gs.util import myreq
from gs.views import ba

logger = logging.getLogger('index')


@ba.route('/')
def index():
    try:
        curr_page = myreq.getvalue_from_request('curr_page', 1)
        limit = const.DEFAULT_LIMIT
        start = (curr_page - 1) * limit
        count, paper_list = PaperSvc().blog_list(start=start, limit=limit)
        last_paper = PaperSvc().last_paper()
        pager = Pager()
        pager.page = curr_page
        pager.total = (count + limit - 1) / limit
        pager.size = limit
        pager.set_nums(pager.def_show_page_num)
        tag_list = PaperSvc().tag_list()
        print paper_list
        return render_template('index.html', total_num=count, paper_list=paper_list, pager=pager, last_paper=last_paper,
                               tag_list=tag_list)
    except Exception as e:
        print e
        return render_template('404.html')


@ba.route('/ba/list', methods=['GET'])
def blog_list():
    try:
        start = myreq.getvalue_from_request('start', 0)
        limit = myreq.getvalue_from_request('limit', const.DEFAULT_LIMIT)
        count, paper_list = PaperSvc().blog_list(start=start, limit=limit)
        for paper in paper_list:
            paper.short_content = __short_content(paper.content)
            paper.content = None
        return common_json_response(total_num=count, paper_list=paper_list)
    except Exception as e:
        print e
        return jsonify_response(apicode.ERROR)


def __short_content(content):
    return content[:400] if content else ''


@ba.route('/tag/list', methods=['GET'])
def tag_list():
    try:
        tag_list = PaperSvc().tag_list()
        return common_json_response(tag_list=tag_list)
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)


@ba.route('/ba/detail', methods=['GET'])
def blog_detail():
    try:
        blog_id = myreq.getvalue_from_request('blog_id')
        blog = PaperSvc().get_paper(blog_id)
        return common_json_response(blog=blog)
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)
