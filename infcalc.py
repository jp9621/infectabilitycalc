from tkinter import *

# Defining the Window
root = Tk()
root.title("Infectability Calculator")
root.configure(bg='#36393E')

# Creating some default appearance related settings for window elements
padx = 5
pady = 5
bg = '#4A4D52'
bgi = '#8ADBC8'
fg = '#9EF8AE'
font = ('Arial', 14)
lightblack = '#5D636C'
gray = '#DBE5E3'


# Create lists for the overweight and underweight thresholds for male and female babies ranging from 0-24 months of age
mhighWeightList = [3.9, 5.1, 6.3, 7.2, 7.9, 8.4, 8.9, 9.3, 9.6, 10.0, 10.3, 10.5, 10.8, 11.1, 11.3, 11.6, 11.8, 12.0, 12.3, 12.5, 12.7, 13.0, 13.2, 13.4, 13.7]
mlowWeightList = [2.9, 3.9, 4.9, 5.6, 6.2, 6.7, 7.1, 7.4, 7.7, 7.9, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.7, 9.9, 10.1, 10.3, 10.5, 10.6, 10.8]

fhighWeightList = [3.7, 4.8, 5.9, 6.7, 7.3, 7.8, 8.3, 8.7, 9.0, 9.3, 9.6, 9.9, 10.2, 10.4, 10.7, 10.9, 11.2, 11.4, 11.6, 11.9, 12.1, 12.4, 12.6, 12.8, 13.1]
flowWeightList = [2.9, 3.6, 4.5, 5.1, 5.6, 6.1, 6.4, 6.7, 7.0, 7.3, 7.5, 7.7, 7.9, 8.1, 8.3, 8.5, 8.7, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 9.9, 10.1]   

# Defining Label
virionLabel = Label(root, text="Virion Count:", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
bmiLabel = Label(root, text="Weight: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
ageLabel = Label(root, text="Age: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
genderLabel = Label(root, text="Sex: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
symptomOnsetLabel = Label(root, text="Symptom Onset: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)

# Defining Input
virionInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
bmiInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
bmiInput.insert(0, "kg")
ageInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
ageInput.insert(0, "0-24 Months")
genderInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
genderInput.insert(0, "Male or Female")
symptomOnsetInput = Entry(root, bg=gray, font=font, highlightbackground=bgi, highlightthickness=3)
symptomOnsetInput.insert(0, "Old or Recent")

# Gridding Widgets
virionLabel.grid(row=0, column=0)
virionInput.grid(row=0, column=1)
bmiLabel.grid(row=1, column=0)
bmiInput.grid(row=1, column=1)
ageLabel.grid(row=2, column=0)
ageInput.grid(row=2, column=1)
genderLabel.grid(row=3, column=0)
genderInput.grid(row=3, column=1)
symptomOnsetLabel.grid(row=4, column=0)
symptomOnsetInput.grid(row=4, column=1)


def calculate():

    # Checking for old output data and destroying it if present
    for widget in root.grid_slaves():
        if widget.grid_info()['row'] == 6 or widget.grid_info()['row'] == 7:
            widget.destroy()

    
    virionCount = virionInput.get()
    virionCount = float(virionCount)
    bmi = bmiInput.get()
    bmi = float(bmi)
    age = ageInput.get()
    age = int(age)
    gender = genderInput.get()
    gender = str(gender)
    symptomOnset = symptomOnsetInput.get()
    symptomOnset = str(symptomOnset)
    


    # Point system to determine severity based on age, weight, and virion count

    severityPoints = 0

    if gender == "Male":
        
        if bmi > mhighWeightList[age] or bmi < mlowWeightList[age]:
            severityPoints += 1
    
    if gender == "Female":
        if bmi > fhighWeightList[age] or bmi < flowWeightList[age]:
            severityPoints += 1

    if virionCount >= 1.0e7:
        severityPoints += 1
    
    if age > 18:
        severityPoints -= 1
    elif age < 6:
        severityPoints += 1
    
    if severityPoints == 3:
        infectabilityReport = "High"
    elif severityPoints == 2:
        infectabilityReport = "Moderate"
    elif severityPoints == 1 or severityPoints == 0 or severityPoints == -1:
        infectabilityReport = "Low"
    

    # Determining duration of the disease
    
    if virionCount >= 1e7:
        durationReport = "Peak"
    elif symptomOnset == "Recent":
        durationReport = "Early"
    elif symptomOnset == "Old":
        durationReport = "Late"

    # Declaring and gridding all the output labels necessary
    infectabilityLabel = Label(root, text="Infectability: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    durationLabel = Label(root, text="Duration: ", fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    infectabilityOutput = Label(root, text= infectabilityReport, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    durationOutput = Label(root, text= durationReport, fg=fg, bg=bg, font=font, padx=padx, pady=pady)
    infectabilityLabel.grid(row=6, column=0)
    durationLabel.grid(row=7, column=0)
    infectabilityOutput.grid(row=6, column=1)
    durationOutput.grid(row=7, column=1)

# Declaring and Gridding Calculate Button
calculateButton = Button(root, text="Calculate", command=calculate, fg=fg, bg=bg,font=font)
calculateButton.grid(row=5, column=0)

root.mainloop() 
