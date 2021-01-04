class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.is_connected = True
    
    def __str__(self):
        return f"Device {self.name}, connected by {self.connected_by}"
    
    def disconnect(self):
        self.is_connected = False

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.remaining_pages = capacity
        self.capacity = capacity
    
    def __str__(self):
        return f"{super().__str__()} (remaining pages: {self.remaining_pages})"
    
    def printPages(self, pages):
        if not self.is_connected:
            print("Device not connected, can't print")
        self.remaining_pages -= pages
        print("printed", pages, "pages")

printer1 = Printer("Canon", "USB", 500)
print(printer1)

    