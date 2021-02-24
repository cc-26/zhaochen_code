import os
import pytest
import yaml

# print(os.getcwd())
# c_path = os.getcwd()
# print(type(c_path))
# local_path = c_path + '\cc_data.yml'
# print(local_path)
from cc_work.pytest_fixture.calculator_cc import Calculator

file_cc = os.path.dirname(__file__)
file_path = file_cc + '/cc_data.yml'
#print(file_path)

def shuju():
    with open(file_path, encoding='utf-8') as f:
        datas_cc = yaml.safe_load(f)
        # print(datas_cc)
        datas = datas_cc['datas']
        myids = datas_cc['myids']
        # print(datas)
    return datas,myids
# print(shuju()[0])


@pytest.fixture(scope='module', params=shuju()[0])
def cc_calculator_shuju(request):
    print('计算开始')
    cc_shuju = request.param
    # print(cc_shuju)
    yield cc_shuju
    print('计算结束')


@pytest.fixture()
def cc_calculator_func():
    cla_cc = Calculator()
    return cla_cc

# @pytest.mark.usefixtures('cc_calculator_shuju')
# def test_c1():
#     pass


# @pytest.mark.usefixtures('cc_calculator_func')
# def test_c2(cc_calculator_func):
    # result = cc_calculator_func.add(1,1)
    # assert result == 2