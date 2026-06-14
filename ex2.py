room = [
  # id, type, price
  (1, "Single", 89),
  (2, "Double", 149),
  (3, "Suite", 299),
]

booking = [
  # guest, room, nights, check-in date
  (3, 1, 3, "05-10-2025"),
  (12, 2, 7, "12-10-2024"),
  (15, 3, 2, "20-03-2025"),
  (15, 3, 5, "30-09-2024"),
  (18, 1, 10, "01-03-2025")
]

occupancy = [
  # id, year, available nights
  (1, 2024, 280),
  (1, 2025, 310),
  (2, 2025, 240),
  (3, 2024, 180),
  (3, 2025, 195)
]

guest = [
  # id, name
  (3, "Bob"),
  (12, "Alice"),
  (15, "Tom"),
  (18, "Ben")
]

guest_dict = {g[0]: g[1] for g in guest}

# booking { "_id": 1, "guest_id": 3, "guest_name": "Bob", "room": 1, "nights": 3, "check_in": "2025-10-05", "year": 2025 }

def transform_booking(booking, guest):
    transformed = []
    for b in booking:
        guest_id = b[0]
        room_id = b[1]
        nights = b[2]
        check_in = b[3]
        year = int(check_in.split("-")[2]) # extract year from check-in date
        
        guest_name = guest_dict.get(guest_id)
        
        transformed.append({
            "_id": len(transformed) + 1,
            "guest_id": guest_id,
            "guest_name": guest_name,
            "room": room_id,
            "nights": nights,
            "check_in": check_in,
            "year": year
        })
    return transformed

# room { "_id": 1, "type": "Single", "price": 89, "occupancy": [ {"year": 2024, "available_nights": 280}, {"year": 2025, "available_nights": 310} ] }
def transform_room(room, occupancy):
    transformed = []
    for r in room:
        room_id = r[0]
        room_type = r[1]
        price = r[2]
        
        room_occupancy = [ {"year": o[1], "available_nights": o[2]} for o in occupancy if o[0] == room_id ]
        
        transformed.append({
            "_id": room_id,
            "type": room_type,
            "price": price,
            "occupancy": room_occupancy
        })
    return transformed

# guest { "_id": 3, "name": "Bob" }
def transform_guest(guest):
    transformed = []
    for g in guest:
        guest_id = g[0]
        guest_name = g[1]
        
        transformed.append({
            "_id": guest_id,
            "name": guest_name
        })
    return transformed

booking = transform_booking(booking, guest),
room = transform_room(room, occupancy),
guest = transform_guest(guest)

# save the converted data to a JSON file
import json

with open("ex2_booking.json", "w") as f:
  json.dump(booking, f, indent=4)
with open("ex2_room.json", "w") as f:
  json.dump(room, f, indent=4)
with open("ex2_guest.json", "w") as f:
  json.dump(guest, f, indent=4)