from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        """Abstract method that must be implemented by all child classes."""
        pass

class PHSensor(Sensor):
    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")
    
class TempSensor(Sensor):
    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")
        

if __name__ == "__main__":
    print("--- Lab Inventory System ---")
    
    #testtest
    ph_device = PHSensor()
    ph_device.get_reading()
    
    temp_device = TempSensor()
    temp_device.get_reading()
    
    print("\n----------------------------")
    
    my_sensor = Sensor()
