import pytest


# @pytest.fixture()
# def cc_fixture():
#     print('开始操作')
#     yield
#     print('操作结束')

class TestCal_cc_new:

    # @pytest.mark.usefixtures('cc_calculator_shuju')
    # @pytest.mark.usefixtures('cc_calculator_func')
    @pytest.mark.run(order=1)
    def test_fixture_zcc(self, cc_calculator_func, cc_calculator_shuju):
        try:
            result = cc_calculator_func.add(cc_calculator_shuju[0], cc_calculator_shuju[1])
            print('这是测试用例1')
            print(f'实际值为{result}')
            print(f'预期值为{cc_calculator_shuju[2]}')
            # assert result == cc_calculator_shuju[2]  写在else里才能断言成功
        except Exception as e:
            print(e)
        else:
            assert result == cc_calculator_shuju[2]

    @pytest.mark.run(order=4)
    def test_fixture_zcc2(self, cc_calculator_func, cc_calculator_shuju):
        result = cc_calculator_func.div(cc_calculator_shuju[0], cc_calculator_shuju[1])
        print('这是测试用例2')
        # print(result)
        assert result == cc_calculator_shuju[2]

    @pytest.mark.run(order=2)
    def test_fixture_zcc3(self, cc_calculator_func, cc_calculator_shuju):
        result = cc_calculator_func.sub(cc_calculator_shuju[0], cc_calculator_shuju[1])
        print('这是测试用例3')
        # print(result)
        assert result == cc_calculator_shuju[2]

    @pytest.mark.run(order=3)
    def test_fixture_zcc4(self, cc_calculator_func, cc_calculator_shuju):
        result = cc_calculator_func.mul(cc_calculator_shuju[0], cc_calculator_shuju[1])
        print('这是测试用例4')
        # print(result)
        assert result == cc_calculator_shuju[2]

