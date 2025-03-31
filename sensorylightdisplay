import adafruit_lis3dh
import busio
import board
from lightdisplay import LightDisplay

class SensorLightDisplay(LightDisplay):
    def __init__(self, brightness):
        super().__init__(brightness)  

        try:
            i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)

            try:
                self.accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x18)
                print("Accelerometer initialized at 0x18")
            except ValueError:
                self.accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
                print("Accelerometer initialized at 0x19")


            self.accelerometer.range = adafruit_lis3dh.RANGE_2_G  

        except RuntimeError as e:
            print("Error initializing accelerometer:", e)
            self.accelerometer = None  

    def light(self, colour):
        
        
        if self.accelerometer is None:
            print("Accelerometer not initialized!")  
            return  

        
        x, y, _ = self.accelerometer.acceleration
        print(f"Acceleration X: {x}, Y: {y}")  
        
        if x < -3 and x < y:
            positions = [6, 7, 8]  
        elif x > 3 and x > y:
            positions = [1, 2, 3] 
        elif y > 3 and y > x:
            positions = [4, 5] 
        elif y < -3 and y < x:
            positions = [0, 9]  
        else:
            self.pixels.fill(self.BLACK)
            self.pixels.show()
            return

        for pos in positions:
            self.pixels[pos] = colour
        self.pixels.show()




    
    
    def control_feedback_y(self, acceleration_y):
        if -9.81 <= acceleration_y <= 9.81:
            intensity = int((acceleration_y + 9.81) / 19.62 * 255)  
            self.pixels.fill((0, 0, intensity))  
            self.pixels.show()

