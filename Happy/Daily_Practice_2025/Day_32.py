import pytest


class TestReaddirPerfImprovment:

    # @pytest.fixture(scope='class',autouse=True)
    # @ir_test.logging.context.fixture
    def system_setup(self,request,st_config,testbed,testsuit_config):

        test_object = {
            'testsuite_config' : testsuit_config,
            'logger': testsuit_config.fb,
            'testbed':testbed,
            'datavip_list': testsuit_config.fb.get_data_vips(),
            'vms':testsuit_config['vms']
        }


        # Assign all object to test class
        for attr_name,obj in test_object.items():
            setattr(request.cls,attr_name,obj)

        print(self.testbed)


object = TestReaddirPerfImprovment()
object.system_setup('request', 'st_config', 'testbed', 'testsuit_config')
