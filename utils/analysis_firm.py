# coding = utf-8
# author = zhouxin
# date = 2017.8.12
# description
# 分析 公司信息

import os, django
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruitment.settings")
django.setup()

from collections import Counter
import jieba
import re

from backend.models import Recruit, Firm
class AnaFirm:

    def __init__(self):

        self.cities = ['北京', '上海', '广州', '深圳', '杭州', '苏州', '西安', '成都', '天津', '南京']
        self.scale = [0, 50, 100, 500, 1000, 5000, 10000, 100000]

    def main(self):

        query = Firm.objects.all()

        scale_dct = {}
        ll_dct = {}
        for item in query:

            loc_ = item.firm_place
            loc = loc_.split('-')[0]
            if loc not in self.cities:
                continue

            scale_f = item.firm_scale_from
            scale_t = item.firm_scale_to

            lng = item.firm_lng
            lat = item.firm_lat

            if lng != -1 and lat != -1:

                ll_city = ll_dct.setdefault(loc, [])
                ll_city.append({'value': [lng, lat, 1]})

            token = scale_f
            if scale_t != 100000:
                token = scale_t

            if token != 0:
                for idx in range(1, len(self.scale)):
                    if token < self.scale[idx]:
                        s = str(self.scale[idx-1]) + '-' + str(self.scale[idx])
                        val = scale_dct.setdefault(s, 0)
                        scale_dct[s] = val + 1

        return [scale_dct, ll_dct]

if __name__ == '__main__':
    a = AnaFirm()
    r = a.main()
    print(r[0])
    print(r[1]['上海'])
