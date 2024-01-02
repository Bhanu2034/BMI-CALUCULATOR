import tkinter as tk
from tkinter import messagebox
class BMI:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("BMI CALCULATOR")
        #Give the labels for height and weight
        height=tk.Label(self.window,text="HEIGHT(cm):")
        weight=tk.Label(self.window,text="WEIGHT(Kg)")
        #entry for the above labels
        self.height=tk.Entry(self.window)
        self.weight=tk.Entry(self.window)
        #Set a button for calculate BMI
        button=tk.Button(self.window,text="Caluculate BMI",command=self.set_bmi)
        #write the grid view setup
        height.grid(row=0,column=0)
        self.height.grid(row=0,column=1)
        weight.grid(row=1,column=0)
        self.weight.grid(row=1,column=1)
        button.grid(row=2,column=0,columnspan=2)
    def set_bmi(self):
        try:
            height=float(self.height.get())
            weight=float(self.weight.get())
            #the converstion
            height=height/100
            bmi=weight/(height**2)
            messagebox.showinfo("BMI Result",f"your BMI is {bmi:.2f} ({self.get_bmi_message(bmi)})")
            #raise the valueerror exception
        except ValueError:
            messagebox.showerror("Invalid Input","please enter valid inputs")
        
    def get_bmi_message(self,bmi):
        #write the conditionalstatements
        if bmi<18.5:
            return "Under weight"
        elif bmi<25:
            return "Normal"
        elif bmi>25:
            return "Over weight"
        else:
            return 0
if __name__=="__main__":
    calculate=BMI()
    calculate.window.mainloop()

            
        
        
        
        
    









