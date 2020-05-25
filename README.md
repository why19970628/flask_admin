### user_restful_api
这是一个通用的用户、部门、角色、权限管理的API接口

##### 1.项目依赖

```
aniso8601==8.0.0  
Click==7.0    
DBUtils==1.3    
Flask==1.1.1  
Flask-Cors==3.0.8  
Flask-JWT==0.3.2  
Flask-RESTful==0.3.7  
itsdangerous==1.1.0  
Jinja2==2.10.3 
MarkupSafe==1.1.1  
PyJWT==1.4.2  
PyMySQL==0.9.3  
xmltodict==0.12.0
```

 安装依赖，请切换到项目工程目录下面。然后使用如下命令进行安装：

```
pip install -r requirements.txt
```

##### 2. 项目的启动文件

```
start.py
```

##### 3. 项目配置文件

```
config.ini
```

##### 4 .项目数据sql

```
user_api.sql
```

>数据库中默认有一个用户名为：super 密码为：123456

### api
```
# 部门管理
'http://{host}:{port}/why/<version>/department',
'http://{host}:{port}/why/<version>/department/<int:dpt_id>'

# 部门人员
'http://{host}:{port}/why/<version>/department/staff/<int:dpt_id>'
# 用户
'http://{host}:{port}/why/<version>/user',
'http://{host}:{port}/why/<version>/user/<int:user_id>',

# 密码
'http://{host}:{port}/why/<version>/user/<int:user_id>/password'

# 基本信息修改
'http://{host}:{port}/why/<version>/user/<int:user_id>/base/info'

# 角色
'http://{host}:{port}/why/<version>/role',
'http://{host}:{port}/why/<version>/role/<int:role_id>'

#  角色权限
'http://{host}:{port}/why/<version>/role/<role_id>/permission'


# 权限
'http://{host}:{port}/why/<version>/permission'

# 用户组
'http://{host}:{port}/why/<version>/user/group',
'http://{host}:{port}/why/<version>/user/group/<int:group_id>'

# 用户组成员
'http://{host}:{port}/why/<version>/user/group/<int:group_id>/staff'

# 获取用户组的角色信息
'http://{host}:{port}/why/<version>/user/group/<int:group_id>/role'

# 登陆
'http://{host}:{port}/why/<version>/login'

```