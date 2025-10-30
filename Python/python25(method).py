class student:
    roll=""
    gpa=""
    
    def set_value(self, roll, gpa):
        self.roll=roll
        self.gpa=gpa
        
    def display(self):
        print(f"Roll: {self.roll} , GPA:{self.gpa}")    
   
    
    
    
rahim=student()
rahim.set_value(2400028, 3.89)
rahim.display()



    
Karim=student()
Karim.set_value(2400089, 3.93)
Karim.display()


    
Sadika=student()
Sadika.set_value(2400789, 3.54)
Sadika.display()



    
    