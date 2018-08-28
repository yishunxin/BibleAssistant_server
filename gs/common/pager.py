# -*- coding:utf-8 -*-

class Pager(object):
    def __init__(self):
        self.def_size = 9
        self.def_show_page_num = 5
        self.page = 0
        self.total = 0
        self.size = 0
        self.has_next = True
        self.has_pre = True
        self.nums = None

    def set_nums(self, show_page_num):
        if self.page == 1:
            self.has_pre = False
        if self.page == self.total or self.total == 0:
            self.has_next = False
        self.nums = list()
        if self.total <= show_page_num:
            self.nums = range(1, self.total + 1)
        else:
            # 先初始化list
            for i in range(0, show_page_num):
                self.nums.append(0)
            # 把page放入合适的中间位置
            if self.page <= (show_page_num / 2):
                page_index = self.page - 1
                self.nums[page_index] = self.page
            elif self.page >= (self.total - (show_page_num / 2)):
                page_index = show_page_num - (self.total - self.page) - 1
                self.nums[page_index] = self.page
            else:
                page_index = show_page_num / 2
                self.nums[page_index] = self.page
            # 前面
            ec = 1
            for i in list(reversed(range(0, page_index))):
                self.nums[i] = self.page - ec
                ec += 1
            # 后面
            ec = 1
            for i in range(page_index + 1, show_page_num):
                self.nums[i] = self.page + ec
                ec += 1
