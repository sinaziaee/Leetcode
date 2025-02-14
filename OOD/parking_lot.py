import time
import uuid

class Car():
    def __init__(self, plate):
        self.plate = plate
        self.ticket = None
class ParkingSpot():
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_occupied = False
    def park_car(self):
        self.is_occupied = True
    def remove_car(self):
        self.is_occupied = False
class Ticket():
    def __init__(self, spot_id, plate):
        self.ticket_id = str(uuid.uuid4())
        self.spot_id = spot_id
        self.plate = plate
        self.start_time = time.time()
        self.end_time = None
        self.fee = 0
    def close_ticket(self, rate=2):
        self.end_time = time.time()
        duration_in_hours = (self.end_time - self.start_time) // 3600
        self.fee = 5 + duration_in_hours * rate
        return self.fee
class ParkingLot():
    def __init__(self, total_spots):
        self.spots = []
        for i in range(total_spots):
            self.spots.append(ParkingSpot(i))
        self.free_spot_ids = [spot.spot_id for spot in self.spots]
        self.active_tickets = {}
    def park(self, car:Car):
        if not self.free_spot_ids:
            return None
        spot_id = self.free_spot_ids.pop(0)
        spot = ParkingSpot(spot_id)
        spot.park_car()
        
        ticket = Ticket(spot_id, car)
        self.active_tickets[ticket.ticket_id] = ticket
        car.ticket = ticket
        return ticket
    def unpark(self, ticket_id):
        # ticket = car.ticket
        ticket = self.active_tickets.get(ticket_id)
        if ticket is None:
            return ticket
    
        spot_id = ticket.spot_id
        spot = self.spots[spot_id]
        spot.remove_car()
        self.free_spot_ids.append(spot.spot_id)
        self.free_spot_ids.sort()
        
        fee = ticket.close_ticket()
        self.active_tickets.pop(ticket_id)
        return fee

lot = ParkingLot(100)
car1 = Car("ABC-234")
ticket1 = lot.park(car1)
if ticket1:
    print(f"Car {car1.plate} parked with ticket {ticket1.ticket_id}")
else:
    print("No spots available for Car1")

time.sleep(5)

if ticket1:
    fee = lot.unpark(ticket1.ticket_id)
    if fee is not None:
        print(f"Car {car1.plate} left. Parking fee: ${fee:.2f}")
    else:
        print("Invalid ticket for unpark operation.")