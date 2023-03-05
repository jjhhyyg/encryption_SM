# SM2算法
> SM2算法主要分为三个部分——数字签名、密钥交换和公钥加密

选择素域，设置椭圆曲线参数
~~~python
sm2_N = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123', 16)
sm2_P = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF', 16)
sm2_G = '32c4ae2c1f1981195f9904466a39c9948fe30bbff2660be1715a4589334c74c7bc3736a2f4f6779c59bdcee36b692153d0a9877cc62a474002df32e52139f0a0'  # G点
sm2_G_number = int(sm2_G, 16)
sm2_a = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC', 16)
sm2_b = int('28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93', 16)
sm2_a_3 = (sm2_a + 3) % sm2_P  # 倍点用到的中间值
Fp = 256
letterlist = "0123456789abcdef"
~~~

## 数字签名
1. 将输入的消息转换为16进制字符串
    ~~~python
    if Hexstr:
        e = int(E, 16)  # 输入消息本身是16进制字符串
    else:
        if isinstance(E, str):
            E = E.encode(encoding)
        E = E.hex()  # 消息转化为16进制字符串
        e = int(E, 16)
    if isinstance(DA, str):
        d = int(DA, 16)
    elif isinstance(DA, (bytes, bytearray)):
        d = int(DA.hex(), 16)
    else:
        raise ValueError('DA must be str or bytes')
    k = int(K, 16)
    ~~~
2. 进行KP运算
    ~~~python
    P1 = kG(k, sm2_G, len_para)

    x = int(P1[:len_para], 16)
    R = (e + x) % sm2_N
    if R == 0 or R + k == sm2_N:
        return None
    d_1 = pow(d + 1, sm2_N - 2, sm2_N)
    S = (d_1 * (k + R) - R) % sm2_N
    s = '%0{}x%0{}x'.format(len_para, len_para) % (R, S) if S else None
    return bytes.fromhex(s)
    ~~~

## 签名验证
~~~python
P1 = kG(s, sm2_G, len_para)
P2 = kG(t, PA, len_para)
~~~
s：16进制的签名前len_para位
sm2_G：基点  
t：16禁止的签名len_para至len_para*2位  
PA：公钥

## 公钥加密算法
用随机数k和基点计算C1，用随机数k和公钥PA计算xy
~~~python
C1 = kG(int(k, 16), sm2_G, len_para)
xy = kG(int(k, 16), PA, len_para)
x2 = xy[0:len_para]
y2 = xy[len_para:2 * len_para]
ml = len(msg)
t = KDF(xy, ml / 2)
~~~