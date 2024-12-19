from tkinter import *

def bereken_bmi():
    try:
        gewicht = float(gewicht_entry.get())
        lengte = float(lengte_entry.get()) / 100
        bmi = gewicht / (lengte ** 2)

        result_label.config(text=f"Je BMI is: {bmi:.2f}")

        if bmi < 18.5:
            result_label.config(bg="orange", text="Ondergewicht")
        elif bmi < 25:
            result_label.config(bg="green", text="Gezond gewicht")
        else:
            result_label.config(bg="black", text="Overgewicht")
    except ValueError:
        result_label.config(text="Voer alleen cijfers in.")

root = Tk()
root.title("BMI berekenen")

gewicht_label = Label(root, text="Gewicht (kg):")
lengte_label = Label(root, text="Lengte (cm):")
bmi_label = Label(root, text="Je BMI:")
result_label = Label(root)

gewicht_entry = Entry(root)
lengte_entry = Entry(root)

gewicht_label.grid(row=0, column=0)
gewicht_entry.grid(row=0, column=1)
lengte_label.grid(row=1, column=0)
lengte_entry.grid(row=1, column=1)
bmi_label.grid(row=2, column=0)
result_label.grid(row=2, column=1)

bereken_knop = Button(root, text="Bereken BMI", command=bereken_bmi)
bereken_knop.grid(row=3, columnspan=2)

root.mainloop()