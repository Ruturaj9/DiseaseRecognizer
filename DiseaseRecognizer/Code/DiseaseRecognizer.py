from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector

app=Tk()
app.title("Disease Recognizer")
app.geometry("800x600")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="diseaserecognizer"
)
db_cursor=mydb.cursor()

def identify():
    # Use parameterized query to prevent SQL injection
    query = "SELECT diseasename FROM diseaseinfo WHERE sym1=%s AND sym2=%s AND sym3=%s AND sym4=%s"
    db_cursor.execute(query, (sym1choose.get(), sym2choose.get(), sym3choose.get(), sym4choose.get()))
    diseasename = db_cursor.fetchall()
    
    # Assuming you expect only one result
    if diseasename:
        label_var.set(diseasename[0][0])
    else:
        label_var.set("Disease not found")


background_image = Image.open("bImage.jpg")  # Replace with your image path
background_image = background_image.resize((800,600))
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(app, image=background_photo)
background_label.place(relwidth=1, relheight=1)

font2=('Times new Romen',16,'bold')
headding=Label(text="Disease Prediction System",width=800,height=3,bg="black",fg="white",font=('Times new Romen',18,'bold')).pack(side=TOP)
Nameuser=Label(app,bg="black",font=font2,fg="yellow",text="Name of the patient:",padx=30,pady=3).place(x=30,y=100)
sym1=Label(app,bg="black",font=font2,fg="yellow",text="Symptoms 1",padx=30,pady=3).place(x=30,y=150)
sym2=Label(app,bg="black",font=font2,fg="yellow",text="Symptoms 2",padx=30,pady=3).place(x=30,y=200)
sym3=Label(app,bg="black",font=font2,fg="yellow",text="Symptoms 3",padx=30,pady=3).place(x=30,y=250)
sym4=Label(app,bg="black",font=font2,fg="yellow",text="Symptoms 4",padx=30,pady=3).place(x=30,y=300)
sym5=Label(app,bg="black",font=font2,fg="yellow",text="Symptoms 5",padx=30,pady=3).place(x=30,y=350)

patient_entry=Entry(app,width=25,fg="black",border=2,bg="white",font=('Times new Romen',15))
patient_entry.place(x=320,y=100)

# symptoms_array = [
#     "Fever", "Cough", "Headache", "Fatigue", "Nausea",
#     "Shortness of breath", "Muscle aches", "Chills", "Sore throat",
#     # Add more symptoms as needed
# ]

symptoms_array1= ['Fever', 'Sneezing', 'High Blood Pressure', 'Frequent Urination', 'Headache', 'Cough', 'Joint Pain', 'Shortness of Breath', 'Runny Nose', 'Chest Pain']
symptoms_array2= ['Cough', 'Sore Throat', 'Headache', 'Excessive Thirst', 'Nausea', 'Shortness of Breath', 'Swelling', 'Coughing', 'Itchy Eyes', 'Fever']
symptoms_array3=['Fatigue', 'Runny Nose', 'Dizziness', 'Blurry Vision', 'Sensitivity to Light', 'Mucus Production', 'Stiffness', 'Wheezing', 'Sneezing', 'Cough']
symptoms_array4= ['Body Aches', 'Congestion', 'Chest Pain', 'Weight Loss', 'Nausea', 'Fever', 'Joint Swelling', 'Chest Tightness', 'Skin Rash', 'Difficulty Breathing']
symptoms_array5=[]



sym1choose=ttk.Combobox(app,width=25,values=symptoms_array1,font=('Times new Romen',12,'bold'))
sym1choose.place(x=320,y=150)

sym2choose=ttk.Combobox(app,width=25,values=symptoms_array2,font=('Times new Romen',12,'bold'))
sym2choose.place(x=320,y=200)

sym3choose=ttk.Combobox(app,width=25,values=symptoms_array3,font=('Times new Romen',12,'bold'))
sym3choose.place(x=320,y=250)

sym4choose=ttk.Combobox(app,width=25,values=symptoms_array4,font=('Times new Romen',12,'bold'))
sym4choose.place(x=320,y=300)

sym5choose=ttk.Combobox(app,width=25,values=symptoms_array5,font=('Times new Romen',12,'bold'))
sym5choose.place(x=320,y=350)



label_var = StringVar()
analysis=Button(app,text="Analyse",width=20,height=3,padx=50,pady=4,bg="green",fg="yellow",font=('Times new Romen',12,'bold'),
                command=identify
                ).place(x=30,y=400)
exit=Button(app,text="Exit",width=20,height=3,padx=50,pady=4,bg="red",fg="yellow",font=('Times new Romen',12,'bold'),command=app.destroy).place(x=350,y=400)
result=Label(app,bg="red",font=font2,fg="white",text="Result",padx=50,pady=3).place(x=30,y=500)
resultData=Label(app,bg="yellow",font=font2,fg="black",padx=50,pady=3,width=15,textvariable=label_var).place(x=320,y=500)


app.mainloop()