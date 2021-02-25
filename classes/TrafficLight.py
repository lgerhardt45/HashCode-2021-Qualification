class TrafficLight:
    def __init__(self, incoming_street, green, queue, remaining_time_on, schedule):
        self.incoming_street = incoming_street
        self.green = green
        self.queue = queue
        self.remaining_time_on = remaining_time_on
        self.schedule = schedule
