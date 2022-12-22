import datetime
def timelimit(time): # time = obj.created_at
    url_limit_time = time + datetime.timedelta(seconds=30) # 단축 url 만든 시점 부터 3시간
    now_time = datetime.datetime.utcnow()
    
    # 단축url 만든 시간+3시간 >= 지금시간이면 True반환 , 아니면 False반환
    if now_time.strftime('%Y-%m-%d %H:%M:%S') <= url_limit_time.strftime('%Y-%m-%d %H:%M:%S'):
        return True
    else:
        return False