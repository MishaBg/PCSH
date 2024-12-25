import unittest
from unittest.mock import patch
from traffic_light import TrafficLight
from adapter import TrafficLightAdapter


class TestTrafficLight(unittest.TestCase):
    def setUp(self):
        self.traffic_light = TrafficLight()
        self.adapter = TrafficLightAdapter(self.traffic_light)

    def test_singleton(self):
        traffic_light2 = TrafficLight()
        self.assertIs(self.traffic_light, traffic_light2, "TrafficLight is not a singleton")

    def test_state_transition(self):
        with patch('builtins.print') as mocked_print:
            self.assertEqual(self.traffic_light.get_state(), "RED")
            self.traffic_light.change_state()
            mocked_print.assert_called_with("Switching from RED to YELLOW")
            self.assertEqual(self.traffic_light.get_state(), "YELLOW")
            self.traffic_light.change_state()
            mocked_print.assert_called_with("Switching from YELLOW to GREEN")
            self.assertEqual(self.traffic_light.get_state(), "GREEN")
            self.traffic_light.change_state()
            mocked_print.assert_called_with("Switching from GREEN to RED")
            self.assertEqual(self.traffic_light.get_state(), "RED")

    def test_adapter(self):
        with patch('builtins.print') as mocked_print:
            self.assertEqual(self.adapter.current_light(), "RED")
            self.adapter.switch()
            mocked_print.assert_called_with("Switching from RED to YELLOW")
            self.assertEqual(self.adapter.current_light(), "YELLOW")
