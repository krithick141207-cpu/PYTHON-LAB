stations = [
    {"id": "S1", "name": "GreenCharge", "location": "Anna Nagar",
     "type": "DC Fast", "price": 20, "status": "Available"},
    {"id": "S2", "name": "EV Point", "location": "K.K. Nagar",
     "type": "AC Level 2", "price": 12, "status": "Available"},
    {"id": "S3", "name": "ChargeHub", "location": "Vadapalani",
     "type": "DC Fast", "price": 20, "status": "Occupied"},
    {"id": "S4", "name": "PowerEV", "location": "T. Nagar",
     "type": "AC Level 2", "price": 12, "status": "Available"}
]
bookings = []
next_booking_id = 1

def view_stations():
    print("\n----- AVAILABLE CHARGING STATIONS -----")
    print(f"{'ID':<5}{'Name':<15}{'Location':<15}{'Type':<13}{'Price/kWh':<12}{'Status'}")
    for s in stations:
        print(f"{s['id']:<5}{s['name']:<15}{s['location']:<15}"
              f"{s['type']:<13}Rs.{s['price']:<9}{s['status']}")

def search_station():
    sid = input("Enter station ID to search: ").strip().upper()
    for s in stations:
        if s["id"] == sid:
            print("\nStation Found")
            print("ID :", s["id"])
            print("Name :", s["name"])
            print("Location :", s["location"])
            print("Type :", s["type"])
            print("Price/kWh: Rs.", s["price"])
            print("Status :", s["status"])
            return
    print("Station not found.")

def book_slot():
    global next_booking_id
    sid = input("Enter station ID to book: ").strip().upper()
    for s in stations:
        if s["id"] == sid:
            if s["status"] != "Available":
                print("Sorry! This station is not available.")
                return
            name = input("Enter customer name: ").strip()
            if not name:
                print("Customer name cannot be empty.")
                return
            booking = {"booking_id": f"B{next_booking_id:03d}",
                       "customer": name, "station_id": sid,
                       "station_name": s["name"], "status": "Confirmed"}
            bookings.append(booking)
            next_booking_id += 1
            s["status"] = "Occupied"
            print("\nCharging slot booked successfully!")
            print("Booking ID :", booking["booking_id"])
            print("Customer :", name)
            print("Station :", s["name"])
            print("Status : Confirmed")
            return
    print("Invalid station ID.")

def view_bookings():
    print("\n----- BOOKING HISTORY -----")
    if not bookings:
        print("No bookings found.")
        return
    for b in bookings:
        print("------------------------------")
        print("Booking ID :", b["booking_id"])
        print("Customer :", b["customer"])
        print("Station ID :", b["station_id"])
        print("Station :", b["station_name"])
        print("Status :", b["status"])

def admin_menu():
    while True:
        print("\n----- ADMIN MENU -----")
        print("1. Add Station")
        print("2. Update Station Status")
        print("3. Remove Station")
        print("4. List All Stations")
        print("5. Return to Main Menu")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            sid = input("New station ID: ").strip().upper()
            if any(s["id"] == sid for s in stations):
                print("Station ID already exists.")
                continue
            name = input("Station name: ").strip()
            location = input("Location: ").strip()
            charger = input("Charger type (AC Level 2 / DC Fast): ").strip()
            try:
                price = float(input("Price per kWh (Rs.): "))
            except ValueError:
                print("Invalid price.")
                continue
            stations.append({"id": sid, "name": name, "location": location,
                             "type": charger, "price": price, "status": "Available"})
            print("Station added successfully.")
        elif choice == "2":
            sid = input("Enter station ID: ").strip().upper()
            station = next((s for s in stations if s["id"] == sid), None)
            if station is None:
                print("Station not found.")
                continue
            status = input("Enter status (Available/Occupied): ").strip().title()
            if status not in ("Available", "Occupied"):
                print("Invalid status.")
            else:
                station["status"] = status
                print("Station status updated successfully.")
        elif choice == "3":
            sid = input("Enter station ID to remove: ").strip().upper()
            station = next((s for s in stations if s["id"] == sid), None)
            if station is None:
                print("Station not found.")
            else:
                stations.remove(station)
                print("Station removed successfully.")
        elif choice == "4":
            view_stations()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

while True:
    print("\n======================================")
    print(" EV CHARGING STATION MANAGER")
    print("======================================")
    print("1. View Charging Stations")
    print("2. Search Station")
    print("3. Book Charging Slot")
    print("4. View Booking History")
    print("5. Admin Menu")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        view_stations()
    elif choice == "2":
        search_station()
    elif choice == "3":
        book_slot()
    elif choice == "4":
        view_bookings()
    elif choice == "5":
        admin_menu()
    elif choice == "6":
        print("Thank you for using EV Charging Station Manager!")
        break
    else:
        print("Invalid choice!")

