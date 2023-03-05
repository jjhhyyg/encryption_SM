# 基于国密算法的安全通信加密模块
结合开源库GmSSL和snowland-smx实现了SM2、SM3、SM4、ZUC、SM9算法，并优化了SM2算法，实现了轻量化证书和批量签名算法

main.py: 调用SM2模块下的功能实现调优参数加密和解密结果展示

加密示例数据：
~~~json
{
  "db_name": "postgres",  # 数据库名
  "db_user": "dba",       # 登录到数据库上的用户名
  "host": "127.0.0.1",    # 数据库宿主机的IP地址
  "host_user": "dba",     # 登录到数据库宿主机的用户名
  "port": 5432,           # 数据库的侦听端口号
  "ssh_port": 22          # 数据库宿主机的SSH侦听端口号
}
~~~

SM2:  
-- key_generator.py: 生成公钥和私钥  
-- sign.py：生成签名  
-- verify.py: 验证签名  
-- encryption.py: 加密  
-- decryption:py: 解密