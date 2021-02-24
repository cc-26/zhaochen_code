import pytest as pytest


@pytest.fixture(params=['1a','2b','3c'])
def ccz(request):
    ccz_data = request.param
    print(ccz_data)
    # yield ccz_data
    # print('打印结束')
# def test_datas_cc(ccz):
#     print(ccz)


