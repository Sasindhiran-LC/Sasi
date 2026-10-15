import pytest
from datetime import datetime

@pytest.mark.usefixtures('setup_and_teardown','log_on_failure')
class BaseTest:
    def generate_job_tilte(self):
        time_stamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        return 'Data' + time_stamp
