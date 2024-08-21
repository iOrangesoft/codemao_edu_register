from requests import Session
session = Session()

print("编程猫 教师账号注册器")
print("GitHub https://github.com/iOrangesoft")
print("\n注意：你需要有一个没有被封禁的编程猫账号才能进行接下来的操作。\n")
while True:
    mode = input("请输入登录方式：[1] 账号密码登录 [2] token(authorization)登录\n")
    if mode == "1":
        username = input("请输入账号：")
        password = input("请输入密码：")
        res_login = session.post("https://api.codemao.cn/tiger/v3/web/accounts/login", json={"identity": username, "password": password,"pid":"65edCTyg"})
        if (res_login.status_code != 200):
            # print(res_login.json())
            print('账号密码有误,请重试。\n')
        else:
            info = username + "  " + password
            break;
    elif mode == "2":
        token = input("请输入token(authorization)：")
        session.cookies.update({'authorization': token})
        if (session.get('https://api.codemao.cn/web/users/details').status_code != 200):
            print('token(authorization)有误,请重试。\n')
        else:
            info = "user"+token
            break;
    else:
        print("输入格式有误，请输入1或2。\n")

err = 0

try:
    uid = session.get('https://api.codemao.cn/web/users/details').json()['id']
except Exception as e:
    err = 1

if (err != 1):
    res_teacher = session.post('https://eduzone.codemao.cn/edu/zone/sign/login/teacher/info/improve',json={
        "id": int(uid),
        "real_name": "教师",
        "grade": [
            "2",
            "3",
            "4"
        ],
        "schoolId": 11000161,
        "schoolName": "北京景山学校",
        "schoolType": 1,
        "country_id": "156",
        "province_id": 1,
        "city_id": 1,
        "district_id": 1,
        "teacherCardNumber": "20234400171011626"
    })
    if (res_teacher.status_code == 404):
        print("教师号注册失败，原因：该账户是学生账户，无法注册教师号。")
    elif (res_teacher.status_code == 403):
        print("教师号注册失败，原因：你的ip地址被封禁。")
    elif (res_teacher.status_code == 200):
        print(res_teacher.content.decode('utf-8'))
        print("用户为",info,"的账户注册教师号成功。")
    else:
        print(res_teacher.content.decode('utf-8'))
        print("教师号注册失败，原因：未知，请自行排查。")
else:
    print("教师号注册失败，原因：获取账户信息失败")
    print("解决方法:1.检查你的账户是否被封禁 2.检查你的网络连接是否正常")

input("\n按回车键退出...")