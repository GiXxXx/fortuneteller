class LiuYaoData:
    yao = [{"yao": "000", "coin": "无背", "name": "老阴", "image": "0", "dong": 1, "reverse": "1"},
           {"yao": "001", "coin": "一背", "name": "少阳", "image": "1", "dong": 0, "reverse": "0"},
           {"yao": "110", "coin": "二背", "name": "少阴", "image": "0", "dong": 0, "reverse": "1"},
           {"yao": "111", "coin": "三背", "name": "老阳", "image": "1", "dong": 1, "reverse": "0"}]

    wuxing = [{"wuxing": "土", "sheng": "金", "ke": "水", "beisheng": "火", "beike": "木"},
              {"wuxing": "木", "sheng": "火", "ke": "土", "beisheng": "水", "beike": "金"},
              {"wuxing": "水", "sheng": "木", "ke": "火", "beisheng": "金", "beike": "土"},
              {"wuxing": "火", "sheng": "土", "ke": "金", "beisheng": "木", "beike": "水"},
              {"wuxing": "金", "sheng": "水", "ke": "木", "beisheng": "土", "beike": "火"}]

    liushen = [
        {"rigan": "丁", "liuyao": "青龙", "wuyao": "玄武", "siyao": "白虎", "sanyao": "螣蛇", "eryao": "勾陈", "chuyao": "朱雀"},
        {"rigan": "丙", "liuyao": "青龙", "wuyao": "玄武", "siyao": "白虎", "sanyao": "螣蛇", "eryao": "勾陈", "chuyao": "朱雀"},
        {"rigan": "乙", "liuyao": "玄武", "wuyao": "白虎", "siyao": "螣蛇", "sanyao": "勾陈", "eryao": "朱雀", "chuyao": "青龙"},
        {"rigan": "壬", "liuyao": "白虎", "wuyao": "螣蛇", "siyao": "勾陈", "sanyao": "朱雀", "eryao": "青龙", "chuyao": "玄武"},
        {"rigan": "己", "liuyao": "勾陈", "wuyao": "朱雀", "siyao": "青龙", "sanyao": "玄武", "eryao": "白虎", "chuyao": "螣蛇"},
        {"rigan": "庚", "liuyao": "螣蛇", "wuyao": "勾陈", "siyao": "朱雀", "sanyao": "青龙", "eryao": "玄武", "chuyao": "白虎"},
        {"rigan": "戊", "liuyao": "朱雀", "wuyao": "青龙", "siyao": "玄武", "sanyao": "白虎", "eryao": "螣蛇", "chuyao": "勾陈"},
        {"rigan": "癸", "liuyao": "白虎", "wuyao": "螣蛇", "siyao": "勾陈", "sanyao": "朱雀", "eryao": "青龙", "chuyao": "玄武"},
        {"rigan": "辛", "liuyao": "螣蛇", "wuyao": "勾陈", "siyao": "朱雀", "sanyao": "青龙", "eryao": "玄武", "chuyao": "白虎"},
        {"rigan": "甲", "liuyao": "玄武", "wuyao": "白虎", "siyao": "螣蛇", "sanyao": "勾陈", "eryao": "朱雀", "chuyao": "青龙"}]

    liuqin = [{"liuqin": "兄弟", "sheng": "子孙", "ke": "妻财", "beisheng": "父母", "beike": "官鬼"},
              {"liuqin": "妻财", "sheng": "官鬼", "ke": "父母", "beisheng": "子孙", "beike": "兄弟"},
              {"liuqin": "子孙", "sheng": "妻财", "ke": "官鬼", "beisheng": "兄弟", "beike": "父母"},
              {"liuqin": "官鬼", "sheng": "父母", "ke": "兄弟", "beisheng": "妻财", "beike": "子孙"},
              {"liuqin": "父母", "sheng": "兄弟", "ke": "子孙", "beisheng": "官鬼", "beike": "妻财"}]

    huntianjiazi = [{"id": 1, "gua": "乾", "neiwai": "内", "chu": "子", "er": "寅", "san": "辰"},
                    {"id": 2, "gua": "坤", "neiwai": "内", "chu": "未", "er": "巳", "san": "卯"},
                    {"id": 3, "gua": "震", "neiwai": "内", "chu": "子", "er": "寅", "san": "辰"},
                    {"id": 4, "gua": "艮", "neiwai": "内", "chu": "辰", "er": "午", "san": "申"},
                    {"id": 5, "gua": "离", "neiwai": "内", "chu": "卯", "er": "丑", "san": "亥"},
                    {"id": 6, "gua": "坎", "neiwai": "内", "chu": "寅", "er": "辰", "san": "午"},
                    {"id": 7, "gua": "兑", "neiwai": "内", "chu": "巳", "er": "卯", "san": "丑"},
                    {"id": 8, "gua": "巽", "neiwai": "内", "chu": "丑", "er": "亥", "san": "酉"},
                    {"id": 9, "gua": "乾", "neiwai": "外", "chu": "午", "er": "申", "san": "戌"},
                    {"id": 10, "gua": "坤", "neiwai": "外", "chu": "丑", "er": "亥", "san": "酉"},
                    {"id": 11, "gua": "震", "neiwai": "外", "chu": "午", "er": "申", "san": "戌"},
                    {"id": 12, "gua": "艮", "neiwai": "外", "chu": "戌", "er": "子", "san": "寅"},
                    {"id": 13, "gua": "离", "neiwai": "外", "chu": "酉", "er": "未", "san": "巳"},
                    {"id": 14, "gua": "坎", "neiwai": "外", "chu": "申", "er": "戌", "san": "子"},
                    {"id": 15, "gua": "兑", "neiwai": "外", "chu": "亥", "er": "酉", "san": "未"},
                    {"id": 16, "gua": "巽", "neiwai": "外", "chu": "未", "er": "巳", "san": "卯"}]

    dizhi = [{"dizhi": "丑", "yinyang": "阴", "wuxing": "土"}, {"dizhi": "亥", "yinyang": "阳", "wuxing": "水"},
             {"dizhi": "午", "yinyang": "阳", "wuxing": "火"}, {"dizhi": "卯", "yinyang": "阳", "wuxing": "木"},
             {"dizhi": "子", "yinyang": "阳", "wuxing": "水"}, {"dizhi": "寅", "yinyang": "阳", "wuxing": "木"},
             {"dizhi": "巳", "yinyang": "阳", "wuxing": "火"}, {"dizhi": "戌", "yinyang": "阳", "wuxing": "土"},
             {"dizhi": "未", "yinyang": "阳", "wuxing": "土"}, {"dizhi": "申", "yinyang": "阳", "wuxing": "金"},
             {"dizhi": "辰", "yinyang": "阳", "wuxing": "土"}, {"dizhi": "酉", "yinyang": "阳", "wuxing": "金"}]

    bagua = [
        {"gua": "乾", "fangwei": "西北", "qinshu": "父", "yuzhou": "天", "yinyang": "阳", "wuxing": "金", "guaxiang": "111"},
        {"gua": "兑", "fangwei": "西", "qinshu": "少女", "yuzhou": "泽", "yinyang": "阴", "wuxing": "金", "guaxiang": "011"},
        {"gua": "坎", "fangwei": "北", "qinshu": "中男", "yuzhou": "水", "yinyang": "阳", "wuxing": "水", "guaxiang": "010"},
        {"gua": "坤", "fangwei": "西南", "qinshu": "母", "yuzhou": "地", "yinyang": "阴", "wuxing": "土", "guaxiang": "000"},
        {"gua": "巽", "fangwei": "东南", "qinshu": "长女", "yuzhou": "风", "yinyang": "阴", "wuxing": "木", "guaxiang": "110"},
        {"gua": "离", "fangwei": "南", "qinshu": "中女", "yuzhou": "火", "yinyang": "阴", "wuxing": "火", "guaxiang": "101"},
        {"gua": "艮", "fangwei": "东北", "qinshu": "少男", "yuzhou": "山", "yinyang": "阳", "wuxing": "土", "guaxiang": "100"},
        {"gua": "震", "fangwei": "东", "qinshu": "长男", "yuzhou": "雷", "yinyang": "阳", "wuxing": "木", "guaxiang": "001"}]

    liushisigua = [
        {"xu": 1, "gua": "乾为天", "gong": "乾", "waigua": "乾", "neigua": "乾", "shi": 6, "ying": 3, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 2, "gua": "坤为地", "gong": "坤", "waigua": "坤", "neigua": "坤", "shi": 6, "ying": 3, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 3, "gua": "水雷屯", "gong": "坎", "waigua": "坎", "neigua": "震", "shi": 2, "ying": 5, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 4, "gua": "山水蒙", "gong": "离", "waigua": "艮", "neigua": "坎", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 5, "gua": "水天需", "gong": "坤", "waigua": "坎", "neigua": "乾", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 1, "guihun": 0},
        {"xu": 6, "gua": "天水讼", "gong": "离", "waigua": "乾", "neigua": "坎", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 1, "guihun": 0},
        {"xu": 7, "gua": "地水师", "gong": "坎", "waigua": "坤", "neigua": "坎", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 1},
        {"xu": 8, "gua": "水地比", "gong": "坤", "waigua": "坎", "neigua": "坤", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 1},
        {"xu": 9, "gua": "风天小畜", "gong": "巽", "waigua": "巽", "neigua": "乾", "shi": 1, "ying": 4, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 10, "gua": "天泽履", "gong": "艮", "waigua": "乾", "neigua": "兑", "shi": 5, "ying": 2, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 11, "gua": "地天泰", "gong": "坤", "waigua": "坤", "neigua": "乾", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 1, "youhun": 0, "guihun": 0},
        {"xu": 12, "gua": "天地否", "gong": "乾", "waigua": "乾", "neigua": "坤", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 1, "youhun": 0, "guihun": 0},
        {"xu": 13, "gua": "天火同人", "gong": "离", "waigua": "乾", "neigua": "离", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 1},
        {"xu": 14, "gua": "火天大有", "gong": "乾", "waigua": "离", "neigua": "乾", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 1},
        {"xu": 15, "gua": "地山谦", "gong": "兑", "waigua": "坤", "neigua": "艮", "shi": 5, "ying": 2, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 16, "gua": "雷地豫", "gong": "震", "waigua": "震", "neigua": "坤", "shi": 1, "ying": 4, "liuchong": 0,
         "liuhe": 1, "youhun": 0, "guihun": 0},
        {"xu": 17, "gua": "泽雷随", "gong": "震", "waigua": "兑", "neigua": "震", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 1},
        {"xu": 18, "gua": "山风蛊", "gong": "巽", "waigua": "艮", "neigua": "巽", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 1},
        {"xu": 19, "gua": "地泽临", "gong": "坤", "waigua": "坤", "neigua": "兑", "shi": 2, "ying": 5, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 20, "gua": "风地观", "gong": "乾", "waigua": "巽", "neigua": "坤", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 21, "gua": "火雷噬嗑", "gong": "巽", "waigua": "离", "neigua": "震", "shi": 5, "ying": 2, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 22, "gua": "山火贲", "gong": "艮", "waigua": "艮", "neigua": "离", "shi": 1, "ying": 4, "liuchong": 0,
         "liuhe": 1, "youhun": 0, "guihun": 0},
        {"xu": 23, "gua": "山地剥", "gong": "乾", "waigua": "艮", "neigua": "坤", "shi": 5, "ying": 2, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 24, "gua": "地雷复", "gong": "坤", "waigua": "坤", "neigua": "震", "shi": 1, "ying": 4, "liuchong": 0,
         "liuhe": 1, "youhun": 0, "guihun": 0},
        {"xu": 25, "gua": "天雷无妄", "gong": "巽", "waigua": "乾", "neigua": "震", "shi": 4, "ying": 1, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 26, "gua": "山天大畜", "gong": "艮", "waigua": "艮", "neigua": "乾", "shi": 2, "ying": 5, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 27, "gua": "山雷颐", "gong": "巽", "waigua": "艮", "neigua": "震", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 1, "guihun": 0},
        {"xu": 28, "gua": "泽风大过", "gong": "震", "waigua": "兑", "neigua": "巽", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 1, "guihun": 0},
        {"xu": 29, "gua": "坎为水", "gong": "坎", "waigua": "坎", "neigua": "坎", "shi": 6, "ying": 3, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 30, "gua": "离为火", "gong": "离", "waigua": "离", "neigua": "离", "shi": 6, "ying": 3, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 31, "gua": "泽山咸", "gong": "兑", "waigua": "兑", "neigua": "艮", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 32, "gua": "雷风恒", "gong": "震", "waigua": "震", "neigua": "巽", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 33, "gua": "天山遯", "gong": "乾", "waigua": "乾", "neigua": "艮", "shi": 2, "ying": 5, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 34, "gua": "雷天大壮", "gong": "坤", "waigua": "震", "neigua": "乾", "shi": 4, "ying": 1, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 35, "gua": "火地晋", "gong": "乾", "waigua": "离", "neigua": "坤", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 1, "guihun": 0},
        {"xu": 36, "gua": "地火明夷", "gong": "坎", "waigua": "坤", "neigua": "离", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 1, "guihun": 0},
        {"xu": 37, "gua": "风火家人", "gong": "巽", "waigua": "巽", "neigua": "离", "shi": 2, "ying": 5, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 38, "gua": "火泽睽", "gong": "艮", "waigua": "离", "neigua": "兑", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 39, "gua": "水山蹇", "gong": "兑", "waigua": "坎", "neigua": "艮", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 40, "gua": "雷水解", "gong": "震", "waigua": "震", "neigua": "坎", "shi": 2, "ying": 5, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 41, "gua": "山泽损", "gong": "艮", "waigua": "艮", "neigua": "兑", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 42, "gua": "风雷益", "gong": "巽", "waigua": "巽", "neigua": "震", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 43, "gua": "泽天夬", "gong": "坤", "waigua": "兑", "neigua": "乾", "shi": 5, "ying": 2, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 44, "gua": "天风姤", "gong": "乾", "waigua": "乾", "neigua": "巽", "shi": 1, "ying": 4, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 45, "gua": "泽地萃", "gong": "兑", "waigua": "兑", "neigua": "坤", "shi": 2, "ying": 5, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 46, "gua": "地风升", "gong": "震", "waigua": "坤", "neigua": "巽", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 47, "gua": "泽水困", "gong": "兑", "waigua": "兑", "neigua": "坎", "shi": 1, "ying": 4, "liuchong": 0,
         "liuhe": 1, "youhun": 0, "guihun": 0},
        {"xu": 48, "gua": "水风井", "gong": "震", "waigua": "坎", "neigua": "巽", "shi": 5, "ying": 2, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 49, "gua": "泽火革", "gong": "坎", "waigua": "兑", "neigua": "离", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 50, "gua": "火风鼎", "gong": "离", "waigua": "离", "neigua": "巽", "shi": 2, "ying": 5, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 51, "gua": "震为雷", "gong": "震", "waigua": "震", "neigua": "震", "shi": 6, "ying": 3, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 52, "gua": "艮为山", "gong": "艮", "waigua": "艮", "neigua": "艮", "shi": 6, "ying": 3, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 53, "gua": "风山渐", "gong": "艮", "waigua": "巽", "neigua": "艮", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 1},
        {"xu": 54, "gua": "雷泽归妹", "gong": "兑", "waigua": "震", "neigua": "兑", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 1},
        {"xu": 55, "gua": "雷火丰", "gong": "坎", "waigua": "震", "neigua": "离", "shi": 5, "ying": 2, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 56, "gua": "火山旅", "gong": "离", "waigua": "离", "neigua": "艮", "shi": 1, "ying": 4, "liuchong": 0,
         "liuhe": 1, "youhun": 0, "guihun": 0},
        {"xu": 57, "gua": "巽为风", "gong": "巽", "waigua": "巽", "neigua": "巽", "shi": 6, "ying": 3, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 58, "gua": "兑为泽", "gong": "兑", "waigua": "兑", "neigua": "兑", "shi": 6, "ying": 3, "liuchong": 1,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 59, "gua": "风水涣", "gong": "离", "waigua": "巽", "neigua": "坎", "shi": 5, "ying": 2, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 60, "gua": "水泽节", "gong": "坎", "waigua": "坎", "neigua": "兑", "shi": 1, "ying": 4, "liuchong": 0,
         "liuhe": 1, "youhun": 0, "guihun": 0},
        {"xu": 61, "gua": "风泽中孚", "gong": "艮", "waigua": "巽", "neigua": "兑", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 1, "guihun": 0},
        {"xu": 62, "gua": "雷山小过", "gong": "兑", "waigua": "震", "neigua": "艮", "shi": 4, "ying": 1, "liuchong": 0,
         "liuhe": 0, "youhun": 1, "guihun": 0},
        {"xu": 63, "gua": "水火既济", "gong": "坎", "waigua": "坎", "neigua": "离", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0},
        {"xu": 64, "gua": "火水未济", "gong": "离", "waigua": "离", "neigua": "坎", "shi": 3, "ying": 6, "liuchong": 0,
         "liuhe": 0, "youhun": 0, "guihun": 0}]