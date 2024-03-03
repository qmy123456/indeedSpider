import pandas as pd
from dataclasses import dataclass


@dataclass
class InviteInfo:
    job_name: str = '信息暂无'
    job_post: str = '信息暂无'
    company_link: str = '信息暂无'
    company_name: str = '信息暂无'
    company_address: str = '信息暂无'
    tanto_name: str = '信息暂无'
    tanto_phone: str = '信息暂无'


def remove_duplicates(invites):
    unique = {}
    for invite in invites:
        # 使用job_name和job_post作为唯一键
        key = (invite.job_name, invite.job_post)
        if key not in unique:
            unique[key] = invite
    return list(unique.values())


def invites_to_csv(invites, filepath):
    # 将InviteInfo对象列表转换为字典列表，这样pandas就可以处理它们
    data = [invite.__dict__ for invite in invites]
    df = pd.DataFrame(data)
    # 导出到CSV
    df.to_csv(filepath, index=False, encoding='utf_8_sig')


# 示例使用
if __name__ == '__main__':
    # 假设这是你的初始列表
    invites = [
        InviteInfo(job_name='开发工程师', job_post='前端', company_name='公司A'),
        InviteInfo(job_name='开发工程师', job_post='前端', company_name='公司B'),  # 这条应该被去除
        InviteInfo(job_name='项目经理', job_post='管理', company_name='公司C')
    ]

    # 去重
    invites_unique = remove_duplicates(invites)

    # 输出到CSV
    invites_to_csv(invites_unique, '../output/test_csv.csv')
