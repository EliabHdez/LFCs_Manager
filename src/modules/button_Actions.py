#========================================================================================#
#     FUNCION PARA RESETEAR LOS CAMPOS DE TEXTO DEL PLANEADOR CON EL BOTON REINICIAR     #
#========================================================================================#

# --- Reiniciar ---
def reiniciar_Planeador(ui):
    # --- Personal ---

    # Supervisores
    ui.sup_Pers_PDV.hint_text = "Ivette Herrera"
    ui.sup_Ops.hint_text = "Efrain Hernández"
    ui.sup_CDO.hint_text = "Zully Brena"

    # Vendedores
    ui.ven_Vips.value = ""
    ui.ven_SanMiguel.value = ""
    ui.ven_SanAntonio.value = ""
    ui.ven_Ensuenos.value = ""
    ui.ven_Cofradia2.value = ""
    ui.ven_Glorieta.value = ""

    ui.ven_Vips.hint_text = ""
    ui.ven_SanMiguel.hint_text = ""
    ui.ven_SanAntonio.hint_text = ""
    ui.ven_Ensuenos.hint_text = ""
    ui.ven_Cofradia2.hint_text = ""
    ui.ven_Glorieta.hint_text = "---"

    # Operadores
    ui.ruta_unica.value = ""
    ui.ruta1.value = ""
    ui.ruta2.value = ""

    ui.ruta_unica.hint_text = ""
    ui.ruta1.hint_text = ""
    ui.ruta2.hint_text = ""

    # Personal CDO
    ui.cdo_1.value = ""
    ui.cdo_2.value = ""
    ui.cdo_3.value = ""
    ui.cdo_4.value = ""

    ui.cdo_1.hint_text = ""
    ui.cdo_2.hint_text = ""
    ui.cdo_3.hint_text = ""
    ui.cdo_4.hint_text = ""
    
    #Ventas minimas
    ui.vm_Vips.value = "$"
    ui.vm_SanMiguel.value = "$"
    ui.vm_SanAntonio.value = "$"
    ui.vm_Ensuenos.value = "$"
    ui.vm_Cofradia2.value = "$"
    ui.vm_Glorieta.value = "---"

    ui.update()

#=================================================================================================#
#     FUNCIONES PARA RESETEAR LOS CAMPOS DE TEXTO DEL PLANEADOR DEACUERDO AL DIA DE LA SEMANA     #
#=================================================================================================#

# --- Lunes ---
def planeador_Lunes(ui):
    # --- Personal ---

    # Supervisores
    ui.sup_Pers_PDV.hint_text = "Ivette Herrera"
    ui.sup_Ops.hint_text = "Efrain Hernandez"
    ui.sup_CDO.hint_text = "Zully Brena"

    # Vendedores
    ui.ven_Vips.value = ""
    ui.ven_SanMiguel.value = ""
    ui.ven_SanAntonio.value = ""
    ui.ven_Ensuenos.value = ""
    ui.ven_Cofradia2.value = ""
    ui.ven_Glorieta.value = ""

    ui.ven_Vips.hint_text = "Sayuri"
    ui.ven_SanMiguel.hint_text = "Carmen"
    ui.ven_SanAntonio.hint_text = "Ivette"
    ui.ven_Ensuenos.hint_text = "Berenice"
    ui.ven_Cofradia2.hint_text = "---"
    ui.ven_Glorieta.hint_text = "---"

    # Operadores
    ui.ruta_unica.value = ""
    ui.ruta1.value = ""
    ui.ruta2.value = ""

    ui.ruta_unica.hint_text = "Efrain"
    ui.ruta1.hint_text = ""
    ui.ruta2.hint_text = ""

    # Personal CDO
    ui.cdo_1.value = ""
    ui.cdo_2.value = ""
    ui.cdo_3.value = ""
    ui.cdo_4.value = ""

    ui.cdo_1.hint_text = "Ahidet"
    ui.cdo_2.hint_text = ""
    ui.cdo_3.hint_text = ""
    ui.cdo_4.hint_text = ""
    
    # Ventas minimas
    ui.vm_Vips.value = ""
    ui.vm_SanMiguel.value = ""
    ui.vm_SanAntonio.value = ""
    ui.vm_Ensuenos.value = ""
    ui.vm_Cofradia2.value = ""
    ui.vm_Glorieta.value = ""

    ui.vm_Vips.hint_text = "$3,900"
    ui.vm_SanMiguel.hint_text = "$4,800"
    ui.vm_SanAntonio.hint_text = "$6,500"
    ui.vm_Ensuenos.hint_text = "$4,800"
    ui.vm_Cofradia2.hint_text = "$3,900"
    ui.vm_Glorieta.hint_text = "$3,500"

    ui.update()

# --- Martes ---
def planeador_Martes(ui):
    # --- Personal ---

    # Supervisores
    ui.sup_Pers_PDV.hint_text = "Ivette Herrera"
    ui.sup_Ops.hint_text = "Efrain Hernandez"
    ui.sup_CDO.hint_text = "Zully Brena"

    # Vendedores
    ui.ven_Vips.value = ""
    ui.ven_SanMiguel.value = ""
    ui.ven_SanAntonio.value = ""
    ui.ven_Ensuenos.value = ""
    ui.ven_Cofradia2.value = ""
    ui.ven_Glorieta.value = ""

    ui.ven_Vips.hint_text = "Berenice"
    ui.ven_SanMiguel.hint_text = "Carmen"
    ui.ven_SanAntonio.hint_text = "Ivette"
    ui.ven_Ensuenos.hint_text = "Cesar"
    ui.ven_Cofradia2.hint_text = "---"
    ui.ven_Glorieta.hint_text = "---"

    # Operadores
    ui.ruta_unica.value = ""
    ui.ruta1.value = ""
    ui.ruta2.value = ""

    ui.ruta_unica.hint_text = "Efrain"
    ui.ruta1.hint_text = ""
    ui.ruta2.hint_text = ""

    # Personal CDO
    ui.cdo_1.value = ""
    ui.cdo_2.value = ""
    ui.cdo_3.value = ""
    ui.cdo_4.value = ""

    ui.cdo_1.hint_text = "Mishelle"
    ui.cdo_2.hint_text = ""
    ui.cdo_3.hint_text = ""
    ui.cdo_4.hint_text = ""
    
    # Ventas minimas
    ui.vm_Vips.value = ""
    ui.vm_SanMiguel.value = ""
    ui.vm_SanAntonio.value = ""
    ui.vm_Ensuenos.value = ""
    ui.vm_Cofradia2.value = ""
    ui.vm_Glorieta.value = ""
   
    ui.vm_Vips.hint_text = "$3,900"
    ui.vm_SanMiguel.hint_text = "$4,800"
    ui.vm_SanAntonio.hint_text = "$6,500"
    ui.vm_Ensuenos.hint_text = "$4,800"
    ui.vm_Cofradia2.hint_text = "$3,900"
    ui.vm_Glorieta.hint_text = "$3,500"

    ui.update()

# --- Miercoles ---
def planeador_Miercoles(ui):
    # --- Personal ---

    # Supervisores
    ui.sup_Pers_PDV.hint_text = "Ivette Herrera"
    ui.sup_Ops.hint_text = "Efrain Hernandez"
    ui.sup_CDO.hint_text = "Zully Brena"

    # Vendedores
    ui.ven_Vips.value = ""
    ui.ven_SanMiguel.value = ""
    ui.ven_SanAntonio.value = ""
    ui.ven_Ensuenos.value = ""
    ui.ven_Cofradia2.value = ""
    ui.ven_Glorieta.value = ""

    ui.ven_Vips.hint_text = "Sayuri"
    ui.ven_SanMiguel.hint_text = "Carmen"
    ui.ven_SanAntonio.hint_text = "Ivette"
    ui.ven_Ensuenos.hint_text = "Cesar"
    ui.ven_Cofradia2.hint_text = "---"
    ui.ven_Glorieta.hint_text = "---"

    # Operadores
    ui.ruta_unica.value = ""
    ui.ruta1.value = ""
    ui.ruta2.value = ""

    ui.ruta_unica.hint_text = "Efrain"
    ui.ruta1.hint_text = ""
    ui.ruta2.hint_text = ""

    # Personal CDO
    ui.cdo_1.value = ""
    ui.cdo_2.value = ""
    ui.cdo_3.value = ""
    ui.cdo_4.value = ""

    ui.cdo_1.hint_text = "Ahidet"
    ui.cdo_2.hint_text = "Mishelle"
    ui.cdo_3.hint_text = ""
    ui.cdo_4.hint_text = ""
    
    # Ventas minimas
    ui.vm_Vips.value = ""
    ui.vm_SanMiguel.value = ""
    ui.vm_SanAntonio.value = ""
    ui.vm_Ensuenos.value = ""
    ui.vm_Cofradia2.value = ""
    ui.vm_Glorieta.value = ""
    
    ui.vm_Vips.hint_text = "$3,900"
    ui.vm_SanMiguel.hint_text = "$4,800"
    ui.vm_SanAntonio.hint_text = "$6,500"
    ui.vm_Ensuenos.hint_text = "$4,800"
    ui.vm_Cofradia2.hint_text = "$3,900"
    ui.vm_Glorieta.hint_text = "$3,500"

    ui.update()

# --- Jueves ---
def planeador_Jueves(ui):
    # --- Personal ---

    # Supervisores
    ui.sup_Pers_PDV.hint_text = "Ivette Herrera"
    ui.sup_Ops.hint_text = "Efrain Hernandez"
    ui.sup_CDO.hint_text = "Zully Brena"

    # Vendedores
    ui.ven_Vips.value = ""
    ui.ven_SanMiguel.value = ""
    ui.ven_SanAntonio.value = ""
    ui.ven_Ensuenos.value = ""
    ui.ven_Cofradia2.value = ""
    ui.ven_Glorieta.value = ""

    ui.ven_Vips.hint_text = "Sayuri"
    ui.ven_SanMiguel.hint_text = "Berenice"
    ui.ven_SanAntonio.hint_text = "Ivette"
    ui.ven_Ensuenos.hint_text = "Cesar"
    ui.ven_Cofradia2.hint_text = "---"
    ui.ven_Glorieta.hint_text = "---"

    # Operadores
    ui.ruta_unica.value = ""
    ui.ruta1.value = ""
    ui.ruta2.value = ""

    ui.ruta_unica.hint_text = "Efrain"
    ui.ruta1.hint_text = ""
    ui.ruta2.hint_text = ""

    # Personal CDO
    ui.cdo_1.value = ""
    ui.cdo_2.value = ""
    ui.cdo_3.value = ""
    ui.cdo_4.value = ""

    ui.cdo_1.hint_text = "Ahidet"
    ui.cdo_2.hint_text = "Mishelle"
    ui.cdo_3.hint_text = ""
    ui.cdo_4.hint_text = ""
    
    # Ventas minimas
    ui.vm_Vips.value = ""
    ui.vm_SanMiguel.value = ""
    ui.vm_SanAntonio.value = ""
    ui.vm_Ensuenos.value = ""
    ui.vm_Cofradia2.value = ""
    ui.vm_Glorieta.value = ""
    
    ui.vm_Vips.hint_text = "$4,100"
    ui.vm_SanMiguel.hint_text = "$5,000"
    ui.vm_SanAntonio.hint_text = "$7,100"
    ui.vm_Ensuenos.hint_text = "$5,000"
    ui.vm_Cofradia2.hint_text = "$4,100"
    ui.vm_Glorieta.hint_text = "$3,700"

    ui.update()

# --- Viernes ---
def planeador_Viernes(ui):
    # --- Personal ---

    # Supervisores
    ui.sup_Pers_PDV.hint_text = "Ivette Herrera"
    ui.sup_Ops.hint_text = "Efrain Hernandez"
    ui.sup_CDO.hint_text = "Zully Brena"

    # Vendedores
    ui.ven_Vips.value = ""
    ui.ven_SanMiguel.value = ""
    ui.ven_SanAntonio.value = ""
    ui.ven_Ensuenos.value = ""
    ui.ven_Cofradia2.value = ""
    ui.ven_Glorieta.value = ""

    ui.ven_Vips.hint_text = "Berenice"
    ui.ven_SanMiguel.hint_text = "Carmen"
    ui.ven_SanAntonio.hint_text = "Ivette - Sayuri"
    ui.ven_Ensuenos.hint_text = "Cesar"
    ui.ven_Cofradia2.hint_text = ""
    ui.ven_Glorieta.hint_text = "---"

    # Operadores
    ui.ruta_unica.value = ""
    ui.ruta1.value = ""
    ui.ruta2.value = ""

    ui.ruta_unica.hint_text = "Efrain"
    ui.ruta1.hint_text = ""
    ui.ruta2.hint_text = ""

    # Personal CDO
    ui.cdo_1.value = ""
    ui.cdo_2.value = ""
    ui.cdo_3.value = ""
    ui.cdo_4.value = ""

    ui.cdo_1.hint_text = "Ahidet"
    ui.cdo_2.hint_text = "Mishelle"
    ui.cdo_3.hint_text = ""
    ui.cdo_4.hint_text = ""
    
    # Ventas minimas
    ui.vm_Vips.value = ""
    ui.vm_SanMiguel.value = ""
    ui.vm_SanAntonio.value = ""
    ui.vm_Ensuenos.value = ""
    ui.vm_Cofradia2.value = ""
    ui.vm_Glorieta.value = ""
    
    ui.vm_Vips.hint_text = "$5,100"
    ui.vm_SanMiguel.hint_text = "$5,500"
    ui.vm_SanAntonio.hint_text = "$9,500"
    ui.vm_Ensuenos.hint_text = "$5,500"
    ui.vm_Cofradia2.hint_text = "$5,100"
    ui.vm_Glorieta.hint_text = "$4,100"

    ui.update()

# --- Sabado ---
def planeador_Sabado(ui):
    # --- Personal ---

    # Supervisores
    ui.sup_Pers_PDV.hint_text = "Ivette Herrera"
    ui.sup_Ops.hint_text = "Efrain Hernandez"
    ui.sup_CDO.hint_text = "Zully Brena"

    # Vendedores
    ui.ven_Vips.value = ""
    ui.ven_SanMiguel.value = ""
    ui.ven_SanAntonio.value = ""
    ui.ven_Ensuenos.value = ""
    ui.ven_Cofradia2.value = ""
    ui.ven_Glorieta.value = ""

    ui.ven_Vips.hint_text = "Berenice"
    ui.ven_SanMiguel.hint_text = "Carmen"
    ui.ven_SanAntonio.hint_text = "Ivette - Sayuri"
    ui.ven_Ensuenos.hint_text = "Cesar"
    ui.ven_Cofradia2.hint_text = ""
    ui.ven_Glorieta.hint_text = "---"

    # Operadores
    ui.ruta_unica.value = ""
    ui.ruta1.value = ""
    ui.ruta2.value = ""

    ui.ruta_unica.hint_text = "Efrain"
    ui.ruta1.hint_text = ""
    ui.ruta2.hint_text = ""

    # Personal CDO
    ui.cdo_1.value = ""
    ui.cdo_2.value = ""
    ui.cdo_3.value = ""
    ui.cdo_4.value = ""

    ui.cdo_1.hint_text = "Ahidet"
    ui.cdo_2.hint_text = "Mishelle"
    ui.cdo_3.hint_text = ""
    ui.cdo_4.hint_text = ""
    
    # Ventas minimas
    ui.vm_Vips.value = ""
    ui.vm_SanMiguel.value = ""
    ui.vm_SanAntonio.value = ""
    ui.vm_Ensuenos.value = ""
    ui.vm_Cofradia2.value = ""
    ui.vm_Glorieta.value = ""
    
    ui.vm_Vips.hint_text = "$5,600"
    ui.vm_SanMiguel.hint_text = "$6,000"
    ui.vm_SanAntonio.hint_text = "$10,500"
    ui.vm_Ensuenos.hint_text = "$6,000"
    ui.vm_Cofradia2.hint_text = "$5,800"
    ui.vm_Glorieta.hint_text = "$4,800"

    ui.update()

# --- Domingo ---
def planeador_Domingo(ui):
    # --- Personal ---

    # Supervisores
    ui.sup_Pers_PDV.hint_text = "Ivette Herrera"
    ui.sup_Ops.hint_text = "Efrain Hernandez"
    ui.sup_CDO.hint_text = "Zully Brena"

    # Vendedores
    ui.ven_Vips.value = ""
    ui.ven_SanMiguel.value = ""
    ui.ven_SanAntonio.value = ""
    ui.ven_Ensuenos.value = ""
    ui.ven_Cofradia2.value = ""
    ui.ven_Glorieta.value = ""

    ui.ven_Vips.hint_text = "Berenice"
    ui.ven_SanMiguel.hint_text = "Carmen"
    ui.ven_SanAntonio.hint_text = "Ivette - Sayuri"
    ui.ven_Ensuenos.hint_text = "Cesar"
    ui.ven_Cofradia2.hint_text = ""
    ui.ven_Glorieta.hint_text = "---"

    # Operadores
    ui.ruta_unica.value = ""
    ui.ruta1.value = ""
    ui.ruta2.value = ""

    ui.ruta_unica.hint_text = "Efrain"
    ui.ruta1.hint_text = ""
    ui.ruta2.hint_text = ""

    # Personal CDO
    ui.cdo_1.value = ""
    ui.cdo_2.value = ""
    ui.cdo_3.value = ""
    ui.cdo_4.value = ""
    
    ui.cdo_1.hint_text = "Ahidet"
    ui.cdo_2.hint_text = "Mishelle"
    ui.cdo_3.hint_text = ""
    ui.cdo_4.hint_text = ""
    
    # Ventas minimas
    ui.vm_Vips.value = ""
    ui.vm_SanMiguel.value = ""
    ui.vm_SanAntonio.value = ""
    ui.vm_Ensuenos.value = ""
    ui.vm_Cofradia2.value = ""
    ui.vm_Glorieta.value = ""
    
    ui.vm_Vips.hint_text = "$5,600"
    ui.vm_SanMiguel.hint_text = "$6,000"
    ui.vm_SanAntonio.hint_text = "$10,500"
    ui.vm_Ensuenos.hint_text = "$6,000"
    ui.vm_Cofradia2.hint_text = "$5,800"
    ui.vm_Glorieta.hint_text = "$4,800"

    ui.update()