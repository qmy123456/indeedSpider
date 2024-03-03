import pandas as pd


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
