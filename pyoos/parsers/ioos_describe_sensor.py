from pyoos.utils.etree import etree
from owslib.sml import SensorML

class IoosDescribeSensor(SensorML):
    def get_true(self):
        return True