from tkinter import *
import subprocess
from tkinter import messagebox
from tkinter.ttk import Combobox
import pandas as pd


# Creating the window
window_1 = Tk()
window_1.title("Whatsapp Chat")
window_1.geometry("1000x500")
window_1.resizable(
                   height=False,
                   width=False
                  )
window_1.config(bg="#189dc9")


# Labels
label_1 = Label(
                window_1, 
                text="Abre un Chat de Whatsapp sin Añadir un Contacto",
                bg="#189dc9",
                fg="#610cc9",
                font=("arial", 20)
               )
label_1.place(x=230, y=40)

label_2 = Label(
                window_1, 
                text="Elige un navegador",
                bg="#189dc9",
                fg="#4f4e52",
                font=("arial", 18)
               )
label_2.place(x=410, y=100)

label_3 = Label(
                window_1, 
                text="Ingresa el número celular",
                bg="#189dc9",
                fg="#4f4e52",
                font=("arial", 18)
               )
label_3.place(x=380, y=280)

label_4 = Label(
                window_1, 
                text='Elige un país',
                bg="#189dc9",
                fg="#4f4e52",
                font=("arial", 18)
               )
label_4.place(x=440, y=190)

label_5 = Label(
                window_1, 
                text="By Bryan Quille",
                bg="#189dc9",
                fg="#800575",
                font=("arial", 15)
               )
label_5.place(x=435, y=460)


# Creating the function with code
def wcwac():

    # Choosing a navigator
    # Dictionary with navigators
    nav = {
           'Microsoft Edge':'microsoftedge.exe',
           'Google Chrome':'chrome.exe',
           'Mozilla Firefox':'firefox.exe'
          }
    na_choose = combo_1.get()
    n_choose = nav[na_choose]

    # Choosing a country
    #Getting data
    dcc = pd.read_excel(
                        'E:/CURSOS/Programming Courses/Python Courses/Projects/Whatsapp Chat/data/pais_codigo.xlsx', 
                        index_col=False, 
                        engine='openpyxl'
                       )
    dcc_df = pd.DataFrame(dcc)  # Convert to DataFrame
    dcc_list = dcc_df.to_numpy().tolist()  # Convert rows on lists
    # Convert a list on a dictionary
    dcc_dic = {}
    for i in range(0, len(dcc_list)):
        dcc_dic[dcc_list[i][0]] = dcc_list[i][1]
    cc_choose = combo_2.get()
    c_choose = dcc_dic[cc_choose]

    # Getting The phone number
    p_n = entry_1.get()

    # Opening the chat on choosen navigator
    if p_n.isnumeric():
        # url_c: whatsapp chat url
        url_c = 'http://wa.me/'

        # Country code choosen
        country_code = str(c_choose)
        
        # Concatenate url
        url_cw = url_c + country_code + p_n
        
        subprocess.call(
                        f'start {n_choose} {url_cw}', 
                        shell=True
                       )
    else:
        entry_1.delete(0, END)
        messagebox.showerror(
                             "Error", 
                             "El número ingresado está incorrecto!"
                            )


# Creating a combobox with navigators
combo_1 = Combobox(
                   window_1, 
                   font=("arial", 20),
                   justify="center"
                  )
combo_1["values"] = (
                     'Microsoft Edge', 
                     'Google Chrome', 
                     'Mozilla Firefox'
                    )
combo_1.current(0)
combo_1.place(x=355, y=140)


# Creating a combobox with countries
combo_2 = Combobox(
                   window_1, 
                   font=("arial", 20),
                   justify="center"
                  )
combo_2["values"] = (
                     'Afganistán', 'Albania', 'Alemania', 
                     'Andorra', 'Angola', 'Antigua y Barbuda', 
                     'Arabia Saudita', 'Argelia', 'Argentina', 
                     'Armenia', 'Australia', 'Austria', 
                     'Azerbaiyán', 'Bahamas', 'Bangladés', 
                     'Barbados', 'Baréin', 'Bélgica', 
                     'Belice', 'Benin', 'Bielorrusia', 
                     'Bolivia', 'Bosnia y Herzegovina', 'Botsuana', 
                     'Brasil', 'Brunéi', 'Bulgaria', 
                     'Burkina Faso', 'Burundi', 'Bután', 
                     'Cabo Verde', 'Camboya', 'Camerún', 
                     'Canadá', 'Catar', 'Chad', 
                     'Chile', 'China', 'Chipre', 
                     'Colombia', 'Comoras', 'Corea del Norte', 
                     'Corea del Sur', 'Costa de Marfil', 'Costa Rica', 
                     'Croacia', 'Cuba', 'Dinamarca', 
                     'Dominica', 'Ecuador', 'Egipto', 
                     'El Salvador', 'Emiratos Árabes Unidos', 'Eritrea', 
                     'Eslovaquia', 'Eslovenia', 'España', 
                     'Estados Unidos', 'Estonia', 'Etiopía', 
                     'Fiji', 'Filipinas', 'Finlandia', 
                     'Francia', 'Gabón', 'Gambia', 
                     'Georgia', 'Ghana', 'Granada', 
                     'Grecia', 'Guatemala', 'Guinea', 
                     'Guinea Ecuatorial', 'Guinea-Bisáu', 'Guyana', 
                     'Haití', 'Honduras', 'Hungría', 
                     'India', 'Indonesia', 'Irak', 
                     'Irán', 'Irlanda', 'Islandia', 
                     'Islas Marshall', 'Islas Salomón', 'Israel', 
                     'Italia', 'Jamaica', 'Japón', 
                     'Jordania', 'Kazajistán', 'Kenia', 
                     'Kirguistán', 'Kiribati', 'Kuwait', 
                     'Laos', 'Lesoto', 'Letonia', 
                     'Líbano', 'Liberia', 'Libia', 
                     'Liechtenstein', 'Lituania', 'Luxemburgo', 
                     'Macedonia', 'Madagascar', 'Malasia', 
                     'Malaui', 'Maldivas', 'Malí', 
                     'Malta', 'Marruecos', 'Mauricio', 
                     'Mauritania', 'México', 'Micronesia', 
                     'Moldavia', 'Mónaco', 'Mongolia', 
                     'Montenegro', 'Mozambique', 'Myanmar', 
                     'Namibia', 'Nauru', 'Nepal', 
                     'Nicaragua', 'Niger', 'Nigeria', 
                     'Noruega', 'Nueva Zelanda', 'Omán', 
                     'Países Bajos', 'Pakistán', 'Palaos', 
                     'Panamá', 'Papúa Nueva Guinea', 'Paraguay', 
                     'Perú', 'Polonia', 'Portugal', 
                     'Reino Unido', 'República Centroafricana', 'República Checa', 
                     'República del Congo', 'República Democratica del Congo', 'República Dominicana', 
                     'Ruanda', 'Rumania', 'Rusia', 
                     'Samoa', 'San Cristóbal y Nieves', 'San Marino', 
                     'San Vicente y las Granadinas', 'Santa Lucía', 'Santo Tomé y Príncipe', 
                     'Senegal', 'Serbia', 'Seychelles', 'Sierra Leona', 
                     'Singapur', 'Siria', 'Somalia', 
                     'Sri Lanka', 'Suazilandia', 'Sudáfrica', 
                     'Sudán', 'Sudán del Sur', 'Suecia', 
                     'Suiza', 'Surinam', 'Tailandia', 
                     'Tanzania', 'Tayikistán', 'Timor Oriental', 
                     'Togo', 'Tonga', 'Trinidad y Tobago', 
                     'Túnez', 'Turkmenistán', 'Turquía', 
                     'Tuvalu', 'Ucrania', 'Uganda', 
                     'Uruguay', 'Uzbekistán', 'Vanuatu', 
                     'Venezuela', 'Vietnam', 'Yemen', 
                     'Yibuti', 'Zambia', 'Zimbabue'
                    )
combo_2.current(49)
combo_2.place(x=355, y=230)


#Creating the entry
entry_1 = Entry(
                window_1, 
                font=("arial", 25),
                justify="center"
               )
entry_1.place(x=325, y=320)


# Creating the Button
button_1 = Button(
                  window_1, 
                  text="Abrir Chat", 
                  font=("arial", 20), 
                  justify="center",
                  bg="#0fd655",
                  command=wcwac
                 )
button_1.place(x=430, y=380)


window_1.mainloop()