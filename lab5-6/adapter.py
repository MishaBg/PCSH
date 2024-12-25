class TrafficLightAdapter:
    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def switch(self):
        self.traffic_light.change_state()

    def current_light(self):
        return self.traffic_light.get_state()
