import pytest


# @pytest.fixture()
# def cc_fixture():
#     print('开始操作')
#     yield
#     print('操作结束')
def abc():
    a = 1
    b = 2
    result = a + b
    print(result == 4)
    return '打印成功'

print(abc())