import serial
import serial.tools.list_ports
import threading

class SerialReader:
    def __init__(self):
        self.ser = None
        self.latest_data = "Not Connected"
        self.running = False
        self.port = None

    def list_ports(self):
        return [port.device for port in serial.tools.list_ports.comports()]

    def connect(self, port, baudrate=9600):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            self.port = port
            self.latest_data = ""
            self.running = True
            threading.Thread(target=self.read_loop, daemon=True).start()
            return True
        except serial.SerialException:
            self.ser = None
            self.latest_data = "Not Connected"
            return False

    def read_loop(self):
        while self.running and self.ser:
            try:
                if self.ser.in_waiting:
                    line = self.ser.readline().decode(errors='ignore').strip()
                    self.latest_data = line
            except:
                self.latest_data = "Error Reading"
                break

    def get_data(self):
        return self.latest_data