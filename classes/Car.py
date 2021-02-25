class Car:
    def __init__(self, id, num_streets_planned, planned_streets, current_street, next_street):
        self.id = id
        self.num_streets_planned = num_streets_planned
        self.planned_streets = planned_streets
        self.current_street = current_street
        self.next_street = next_street
        self.num_travelled = 0
        self.streets_travelled = []
