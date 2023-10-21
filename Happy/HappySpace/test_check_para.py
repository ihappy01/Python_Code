
import pytest


class Test_Parameter:

    @pytest.mark.parametrize("geometry",["Test1","Test2","Test3"])
    def test_method1(self,geometry):
        print("Geometry is called for data")
