# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Inherited Class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}...")
    
    def charge(self):
        print(f"🔋 Charging {self.device_info()}... Battery at {self.battery}%")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 85)
phone2 = Smartphone("Apple", "iPhone 14", "128GB", 60)

phone1.make_call("0712345678")
phone2.charge()
