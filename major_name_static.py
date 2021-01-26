
import pandas as pd
import re

def sort_major(x):
    new_x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

    return

def load_post_list(file_path):
    # df = pd.read_excel(file_path, sheet_name="")
    dfs = pd.read_excel(file_path, sheet_name=[0,1,2,3], header=0, skiprows=1, usecols=['专业'])

    # data = df.head()  # 默认读取前5行的数据
    # print(df.head())
    majors = []
    for k, df in dfs.items():
        # print(k) k为sheet名称
        data = df['专业'].tolist()
        majors += data

    # print(majors, len(majors))
    # data = df.values().tolist()

    # data = df.ix[:, ['专业']].values  # 读所有行的title以及data列的值，这里需要嵌套列表

    # print(data)

    major_count = dict()
    for major in majors:
        # tmp_major_list = major.split('、')
        tmp_major_list = re.split("[、，,]", major)
        for m in tmp_major_list:
            if re.match(".*专业(除外)?$", m):
                # print(m)
                m = re.sub("专业(除外)?", "", m)
                # print(m)
            if re.match("法学（.*）", m):
                # 法学（0301）
                m = "法学"
            if m in major_count:
                major_count[m] += 1
            else:
                major_count[m] = 1

    sorted_major_count = {k: v for k, v in sorted(major_count.items(), key=lambda item: item[1], reverse=1)}

    print(sorted_major_count)
    return sorted_major_count

# def save_result()



if __name__ == "__main__":
    load_post_list("data/中央机关及其直属机构2021年度考试录用公务员招考简章.xls")
