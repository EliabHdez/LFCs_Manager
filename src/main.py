import datetime as dt
import flet as ft
from fpdf import FPDF
import modules.create_Elements as ce
import modules.button_Actions as ba
import modules.create_Reports as cr
import asyncio
import os
import sys

def get_resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        # Si está empaquetado, usa la ruta temporal
        base_path = sys._MEIPASS
    else:
        # Si está en desarrollo, sube desde src hasta la raíz
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)

class UI(ft.ResponsiveRow):
    def __init__(self, page):
        super().__init__(expand=True)

        """
        ===========================================
        #          VARIABLES DEL SISTEMA          #
        ===========================================
         """

        #================================#
        #     VARIABLES FECHA Y HORA     #
        #================================#

        self.days = {
            "Monday" : "LUNES",
            "Tuesday" : "MARTES",
            "Wednesday" : "MIERCOLES",
            "Thursday" : "JUEVES",
            "Friday" : "VIERNES",
            "Saturday" : "SABADO",
            "Sunday" : "DOMINGO"
        }

        self.months = {
            "January" : "ENERO",
            "February" : "FEBRERO",
            "March" : "MARZO",
            "April" : "ABRIL",
            "May" : "MAYO",
            "June" : "JUNIO",
            "July" : "JULIO",
            "August" : "AGOSTO",
            "September" : "SSPTIEMBRE",
            "October" : "OCTUBRE",
            "November" : "NOVIEMBRE",
            "December" : "DICIEMBRE"
        }

        self.num_months = {
            "January" : "01",
            "February" : "02",
            "March" : "03",
            "April" : "04",
            "May" : "05",
            "June" : "06",
            "July" : "07",
            "August" : "08",
            "September" : "09",
            "October" : "10",
            "November" : "11",
            "December" : "12"
        }

        self.today = dt.datetime.now()

        self.mayus_weekend_day = self.days[self.today.strftime("%A")]
        self.mayus_month = self.months[self.today.strftime("%B")]
        self.num_month = self.num_months[self.today.strftime("%B")]
        self.today_1 = dt.datetime.today().date()
        self.today_2 = self.today_1.strftime(f"{self.mayus_weekend_day} %d°{self.num_month}°%Y")
        self.today_3 = self.today_1.strftime(f"{self.mayus_weekend_day} %d-{self.mayus_month}-%Y")

        self.today_main = self.today_2
        self.today_main_hor = self.today_3

        self.date_onList=[]

        for element in self.today_main:
            self.date_onList.append(element)
            # print(element)
            # print(self.date_onList)
        # print(len(self.date_onList))

        #===========================#
        #     VARIABLES COLORES     #
        #===========================#

        # self.color_teal = "teal"
        self.color_teal = "#00ebab"
        self.color_teal_2 = "#11b78a"

        #=======================================#
        #     VARIABLE BOTON CAMBIO DE TEMA     #
        #=======================================#

        self.mode_switch = ce.create_Button_Switch()

        #====================================================================#
        #     VARIABLES ICONOS INFERIORES EN BARRA DE NAVEGACION LATERAL     #
        #====================================================================#

        self.profiles = ft.IconButton(# Ventana Perfiles / Cuentas
            icon=ft.Icons.ACCOUNT_CIRCLE_SHARP,
            icon_color="000000",
            tooltip="Cuenta",
            on_click=lambda e: page.open(
                ft.CupertinoAlertDialog(
                    # title=ft.Text("Cuentas"),
                    content=ft.Text('Sección no disponible por el momento'),
                    actions=[
                        ft.CupertinoDialogAction("OK", is_destructive_action=True, on_click=lambda e: page.close(e.control.parent))
                    ]
                ),
            )
        )

        self.configuration = ft.IconButton(# Ventana Configuraciones
            icon=ft.Icons.SETTINGS,
            icon_color="000000",
            tooltip="Configuraciones",
            on_click=lambda e: page.open(
                ft.AlertDialog(
                    modal=True,
                    # title=ft.Text("Cuentas"),
                    content=ft.Text('Por el momento no hay configuraciones disponibles'),
                    actions=[
                        ft.TextButton("Ok", on_click=lambda e: page.close(e.control.parent))
                    ]
                ),
            )
        )

        """ 
        ================================================
        #          "VARIABLES VENTANA INICIO"          #
        ================================================
        """
        
        #========================================#
        #     VARIABLES PERSONAL SUPERVISION     #
        #========================================#

        self.sup_Pers_PDV = ce.create_textfield_planeador(hint_Text="Ivette Herrera", hint_Style=ft.TextStyle(color="black", size=14, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, italic=True, weight=ft.FontWeight.BOLD))
        self.sup_Ops = ce.create_textfield_planeador(hint_Text="Efrain Hernandez", hint_Style=ft.TextStyle(color="black", size=14, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, italic=True, weight=ft.FontWeight.BOLD))
        self.sup_CDO = ce.create_textfield_planeador(hint_Text="Zully Brena", hint_Style=ft.TextStyle(color="black", size=14, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, italic=True, weight=ft.FontWeight.BOLD))

        #==================================#
        #     VARIABLES PERSONAL PDV'S     #
        #==================================#

        self.ven_Vips = ce.create_textfield_planeador(hint_Text="Berenice", hint_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.ven_SanMiguel = ce.create_textfield_planeador(hint_Text="Carmen", hint_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.ven_SanAntonio = ce.create_textfield_planeador(hint_Text="Ivette", hint_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.ven_Ensuenos = ce.create_textfield_planeador(hint_Text="Cesar", hint_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.ven_Cofradia2 = ce.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.ven_Glorieta = ce.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))

        #======================================#
        #     VARIABLES OPERADORES DE RUTA     #
        #======================================#

        self.ruta_unica = ce.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.ruta1 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.ruta2 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))

        #=========================================#
        #     VARIABLES CENTRO DE OPERACIONES     #
        #=========================================#

        self.cdo_1 = ce.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.cdo_2 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.cdo_3 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.cdo_4 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))

        #==========================================#
        #     VARIABLES SECCION VENTAS MINIMAS     #
        #==========================================#

        self.vm_Vips = ce.create_textfield_planeador(hint_Text="$3,900", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.vm_SanMiguel = ce.create_textfield_planeador(hint_Text="$4,800", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.vm_SanAntonio = ce.create_textfield_planeador(hint_Text="$6,500", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.vm_Ensuenos = ce.create_textfield_planeador(hint_Text="$4,800", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.vm_Cofradia2 = ce.create_textfield_planeador(hint_Text="$3,900", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.vm_Glorieta = ce.create_textfield_planeador(hint_Text="$3,500", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))

        #=============================== ====#
        #     VARIABLES SECCION PROMEDIO     #
        #====================================#

        self.prom_Vips = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.prom_SanMiguel = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.prom_SanAntonio = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.prom_Ensuenos = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.prom_Cumbria = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.prom_Cofradia2 = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))
        self.prom_Glorieta = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=14, weight="bold"), text_Style=ft.TextStyle(color="black", size=14, weight=ft.FontWeight.BOLD))

        #==============================#
        #     VARIABLES SUCURSALES     #
        #==============================#

        self.vips = ce.create_radio("vips", "Vips")
        self.sanmiguel = ce.create_radio("sanmiguel", "San Miguel")
        self.sanantonio = ce.create_radio("sanantonio", "San Antonio")
        self.ensuenos = ce.create_radio("ensueños", "Ensueños")
        # self.cumbria = ce.create_radio("cumbria", "Cumbria")
        self.cofradia2 = ce.create_radio("cofradia2", "Cofradía 2")
        self.glorieta = ce.create_radio("glorieta", "Glorieta")

        #=========================================================#
        #     VARIABLE GRUPO DE BOTONES TIPO RADIO SUCURSALES     #
        #=========================================================#

        self.pdv = ft.RadioGroup(# Grupo de Botones tipo Radio de las Sucursales
            on_change=self.pdv_selection,
            content=ft.Container(
                alignment=ft.alignment.center,
                padding=ft.Padding(top=0, bottom=0, left=2, right=4),
                # bgcolor="blue",
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    # expand=True,
                    controls=[
                        self.vips,
                        self.sanmiguel,
                        self.sanantonio,
                        self.ensuenos,
                        self.cofradia2,
                        # self.cumbria,
                        self.glorieta,
                        # self.cumbria,
                        # self.palomas,
                        # self.colinas,
                    ]
                )
            )
        )

        self.pdv_suc = ""

        #================================#
        #     VARIABLES VASOS CHICOS     #
        #================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tci = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus)
        self.tcf = ce.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=ce.Focus)
        # self.tcdif = ce.create_textfield("Diferencia de...", suffix_Text="Tapas", read_Only=True)
        self.vci = ce.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vc)
        self.vcf = ce.create_textfield("Finales", suffix_Text="Vasos Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vc)
        # self.vcdif = ce.create_textfield("Diferencia", suffix_Text="Vasos", read_Only=True)
        # self.vcsv = ce.create_textfield("Sin vender", suffix_Text="Vasos", Color="#ffffff", read_Only=True)
        self.vcven = ce.create_textfield(Label="Vendidos", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="VASOS", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), focused_Border_Color="#08f5a9", read_Only=True)
        self.vcvt = ce.create_textfield(Label="Venta Total", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="MX", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), border_Color="#fd0000", focused_Border_Color="#08f5a9", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#0d0d0d", size=12), read_Only=True, on_Change=self.values_types_comprobation_vc)

        #======================================#
        #     VARIABLES VASOS INDIVIDUALES     #
        #======================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tii = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus)
        self.tif = ce.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=ce.Focus)
        # self.tcdif = ce.create_textfield("Diferencia de...", suffix_Text="Tapas", read_Only=True)
        self.vii = ce.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vi)
        self.vif = ce.create_textfield("Finales", suffix_Text="Vasos Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vi)
        # self.vcdif = ce.create_textfield("Diferencia", suffix_Text="Vasos", read_Only=True)
        # self.vcsv = ce.create_textfield("Sin vender", suffix_Text="Vasos", Color="#ffffff", read_Only=True)
        self.viven = ce.create_textfield(Label="Vendidos", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="VASOS", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), focused_Border_Color="#08f5a9", read_Only=True)
        self.vivt = ce.create_textfield(Label="Venta Total", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="MX", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), border_Color="#fd0000", focused_Border_Color="#08f5a9", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#0d0d0d", size=12), read_Only=True, on_Change=self.values_types_comprobation_vi)

        #==================================#
        #     VARIABLES VASOS MEDIANOS     #
        #==================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tmi = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus)
        self.tmf = ce.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=ce.Focus)
        # self.tmdif = ce.create_textfield("Diferencia", read_Only=True)
        self.vmi = ce.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vm)
        self.vmf = ce.create_textfield("Finales", suffix_Text=" Vasos Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vm)
        # self.vmdif = ce.create_textfield("Diferencia", read_Only=True)
        # self.vmsv = ce.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vmven = ce.create_textfield(Label="Vendidos", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="VASOS", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), focused_Border_Color="#08f5a9", read_Only=True)
        self.vmvt = ce.create_textfield(Label="Venta Total", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="MX", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), border_Color="#fd0000", focused_Border_Color="#08f5a9", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#0d0d0d", size=12), read_Only=True, on_Change=self.values_types_comprobation_vm)

        #=================================#
        #     VARIABLES VASOS GRANDES     #
        #=================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tgi = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus)
        self.tgf = ce.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=ce.Focus)
        # self.tgdif = ce.create_textfield("Diferencia", read_Only=True)
        self.vgi = ce.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vg)
        self.vgf = ce.create_textfield("Finales", suffix_Text="Vasos Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vg)
        # self.vgdif = ce.create_textfield("Diferencia", read_Only=True)
        # self.vgsv = ce.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vgven = ce.create_textfield(Label="Vendidos", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="VASOS", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), focused_Border_Color="#08f5a9", read_Only=True)
        self.vgvt = ce.create_textfield(Label="Venta Total", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="MX", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), border_Color="#fd0000", focused_Border_Color="#08f5a9", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#0d0d0d", size=12), read_Only=True, on_Change=self.values_types_comprobation_vg)

        #==================================#
        #     VARIABLES VASOS MEGAS     #
        #==================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tmgi = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus)
        self.tmgf = ce.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=ce.Focus)
        # self.tmdif = ce.create_textfield("Diferencia", read_Only=True)
        self.vmgi = ce.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vmg)
        self.vmgf = ce.create_textfield("Finales", suffix_Text=" Vasos Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vmg)
        # self.vmdif = ce.create_textfield("Diferencia", read_Only=True)
        # self.vmsv = ce.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vmgven = ce.create_textfield(Label="Vendidos", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="VASOS", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), focused_Border_Color="#08f5a9", read_Only=True)
        self.vmgvt = ce.create_textfield(Label="Venta Total", label_Style=ft.TextStyle(size=12), Color="#fd0000", text_Size=20, suffix_Text="MX", suffix_Style=ft.TextStyle(color="#0d0d0d", size=12), border_Color="#fd0000", focused_Border_Color="#08f5a9", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#0d0d0d", size=12), read_Only=True, on_Change=self.values_types_comprobation_vmg)

        #=====================================#
        #     VARIABLES VENTA TOTAL VASOS     #
        #=====================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.vtv = ce.create_textfield_WB(Label="Total Vasos", Color="#FF0000", text_Size=24, border_Color="#000000", border_Width=1, focused_Border_Color="#FF0000", suffix_Text="Vasos ", suffix_Style=ft.TextStyle(color="#000000", size=20), read_Only=True)
        self.vvmt = ce.create_textfield_WB(Label="Total Venta", Color="#FF0000", text_Size=24, border_Color="#000000", border_Width=1, focused_Border_Color="#FF0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#000000", size=20), suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=20), read_Only=True)

        #==========================#
        #     VARIABLES FRUTAS     #
        #==========================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        # --- Fresa ---

        # self.tgi = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vg)
        self.fi = ce.create_textfield("Inicial", label_Style=ft.TextStyle(size=12), text_Size=17, suffix_Text="Bote(s)", Width=100, on_Change=self.conversion_n_capture_fr)
        self.f1s = ce.create_textfield("1er Surtido", label_Style=ft.TextStyle(size=9), suffix_Text="Bote(s)", Width=90, on_Change=self.conversion_n_capture_fr)
        self.f2s = ce.create_textfield("2do Surtido", label_Style=ft.TextStyle(size=9), suffix_Text="Bote(s)", Width=90, on_Change=self.conversion_n_capture_fr)
        self.f3s = ce.create_textfield("3er Surtido", label_Style=ft.TextStyle(size=9), suffix_Text="Bote(s)", Width=90, on_Change=self.conversion_n_capture_fr)
        self.f4s = ce.create_textfield("4to Surtido", label_Style=ft.TextStyle(size=9), suffix_Text="Bote(s)", Width=90, on_Change=self.conversion_n_capture_fr)
        self.ff = ce.create_textfield("Final", label_Style=ft.TextStyle(size=12), text_Size=17, suffix_Text="Bote(s)", Width=100, on_Change=self.conversion_n_capture_fr)
        self.fv = ce.create_textfield(Label="Vendidos", suffix_Text="Bote(s)", Color="#ff0000", text_Size=19, label_Style=ft.TextStyle(size=14), suffix_Style=ft.TextStyle(color="#000000", size=11), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", read_Only=True, on_Change=self.values_Fresa)
        # self.fr = ce.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

        # --- Uva ---

        self.ui = ce.create_textfield("Inicial", label_Style=ft.TextStyle(size=12), text_Size=17, suffix_Text="Bote(s)", Width=100, on_Change=self.conversion_n_capture_uva)
        self.u1s = ce.create_textfield("1er Surtido", label_Style=ft.TextStyle(size=9), suffix_Text="Bote(s)", Width=90, on_Change=self.conversion_n_capture_uva)
        self.u2s = ce.create_textfield("2do Surtido", label_Style=ft.TextStyle(size=9), suffix_Text="Bote(s)", Width=90, on_Change=self.conversion_n_capture_uva)
        self.u3s = ce.create_textfield("3er Surtido", label_Style=ft.TextStyle(size=9), suffix_Text="Bote(s)", Width=90, on_Change=self.conversion_n_capture_uva)
        self.u4s = ce.create_textfield("4to Surtido", label_Style=ft.TextStyle(size=9), suffix_Text="Bote(s)", Width=90, on_Change=self.conversion_n_capture_uva)
        self.uf = ce.create_textfield("Final", label_Style=ft.TextStyle(size=12), text_Size=17, suffix_Text="Bote(s)", Width=100, on_Change=self.conversion_n_capture_uva)
        self.uv = ce.create_textfield(Label="Vendidos", suffix_Text="Bote(s)", Color="#ff0000", text_Size=19, label_Style=ft.TextStyle(size=14), suffix_Style=ft.TextStyle(color="#000000", size=11), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", read_Only=True, on_Change=self.values_Uva)
        # self.ur = ce.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

        #==========================#
        #     VARIABLES CREMAS     #
        #==========================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        # --- Crema Original ---

        self.coi = ce.create_textfield("Inicial", suffix_Text="Bote(s)", Width=95, on_Change=self.conversion_n_capture_co)
        self.cof = ce.create_textfield("Final", suffix_Text="Bote(s)", Width=95, on_Change=self.conversion_n_capture_co)
        self.cov = ce.create_textfield(Label="Vendidos", suffix_Text="Bote(s)", Color="#ff0000", text_Size=18, Width=110, label_Style=ft.TextStyle(size=12), suffix_Style=ft.TextStyle(size=10), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaOriginal, read_Only=True)
        self.co1s = ce.create_textfield("1er Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.co2s = ce.create_textfield("2do Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.co3s = ce.create_textfield("3er Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.co4s = ce.create_textfield("4to Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)

        # --- Crema Chocolate ---

        self.cchi = ce.create_textfield("Inicial", suffix_Text="Bote(s)", Width=95, on_Change=self.conversion_n_capture_cch)
        self.cchf = ce.create_textfield("Final", suffix_Text="Bote(s)", Width=95, on_Change=self.conversion_n_capture_cch)
        self.cchv = ce.create_textfield(Label="Vendidos", suffix_Text="Bote(s)", Color="#ff0000", text_Size=18, Width=110, label_Style=ft.TextStyle(size=12), suffix_Style=ft.TextStyle(size=10), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaChocolate, read_Only=True)
        self.cch1s = ce.create_textfield("1er Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.cch2s = ce.create_textfield("2do Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.cch3s = ce.create_textfield("3er Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.cch4s = ce.create_textfield("4to Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)

        # --- Crema Cafe ---

        self.ccai = ce.create_textfield("Inicial", suffix_Text="Bote(s)", Width=95, on_Change=self.conversion_n_capture_cca)
        self.ccaf = ce.create_textfield("Final", suffix_Text="Bote(s)", Width=95, on_Change=self.conversion_n_capture_cca)
        self.ccav = ce.create_textfield(Label="Vendidos", suffix_Text="Bote(s)", Color="#ff0000", text_Size=18, Width=110, label_Style=ft.TextStyle(size=12), suffix_Style=ft.TextStyle(size=10), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaCafe, read_Only=True)
        self.cca1s = ce.create_textfield("1er Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.cca2s = ce.create_textfield("2do Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.cca3s = ce.create_textfield("3er Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)
        self.cca4s = ce.create_textfield("4to Surtido", label_Style=ft.TextStyle(size=9), text_Size=14, suffix_Text="Bote(s)", Width=85)

        #==========================================#
        #     VARIABLES FRUTA Y CREMA VENDIDAS     #
        #==========================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.fruven = ce.create_textfield_WB(Label="Fruta", Color="#FF0000", text_Size=24, border_Color="#000000", border_Width=1, focused_Border_Color="#FF0404", suffix_Text="Bote(s) ", read_Only=True)
        self.creven = ce.create_textfield_WB(Label="Cremas", Color="#FF0000", text_Size=24, border_Color="#000000", border_Width=1, focused_Border_Color="#FF0000", suffix_Text="Bote(s) ", read_Only=True)

        #==========================#
        #     VARIABLES EXTRAS     #
        #==========================#

        # >>> Opciones a configurar en la funcion create_textfield_Extras: Width, Height, Color="#d3d3d3", text_Size=12, border_Color=None, read_Only=False, on_Change=False

        # --- Toppings Extras ---

        self.t5 = ce.create_textField_Extras(text_Size=18, text_Style=None, Width=None, Height=40, read_Only=False, on_Change=self.validation_toppingsExtras)
        self.t10 = ce.create_textField_Extras(text_Size=18, text_Style=None, Width=None, Height=40, read_Only=False, on_Change=self.validation_toppingsExtras)
        self.tet = ce.create_textField_Extras(text_Size=20, text_Style=None, Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True, on_Change=self.balance_General)

        # --- Servicios a Domicilio ---

        self.sdxtr = ft.Text("TR")
        self.sdxef = ft.Text("EF")
        self.sd20 = ce.create_textField_Extras(text_Size=18, text_Style=None, Width=None, Height=40, read_Only=False, on_Change=self.validation_serviciosDomicilio)
        self.sd35 = ce.create_textField_Extras(text_Size=18, text_Style=None, Width=None, Height=40, read_Only=False, on_Change=self.validation_serviciosDomicilio)
        self.sdt = ce.create_textField_Extras(text_Size=20, text_Style=None, Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True, on_Change=self.balance_General)
        # self.sd20tr = ce.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.validation_serviciosDomicilioTR)
        # self.sd35tr = ce.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.validation_serviciosDomicilioTR)
        # self.sdttr = ce.create_textField_Extras(text_Size=18, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True)
        

        self.total_t5 = ""
        self.total_t10 = ""
        self.total_sd20 = ""
        self.total_sd35 = ""

        # --- Transferencias ---

        self.trn = ce.create_textField_Extras(text_Size=20, text_Style=None, Width=80, Height=40, read_Only=True)
        self.trt = ce.create_textField_Extras(text_Size=22, text_Style=None, Width=120, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#FF0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#000000", size=18), suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True, on_Change=self.balance_General)
        
        self.tr1 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr2 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr3 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr4 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr5 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr6 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr7 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr8 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr9 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr10 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr11 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr12 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr13 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr14 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr15 = ce.create_textField_Extras(Value="", text_Size=14, Width=70, Height=28, border_Color="black", border_Width=.5, focused_Border_Width=1, cursor_Height=14, prefix_Text="$", prefix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)

        # --- Gastos / Retiros ---

        self.grn = ce.create_textField_Extras(text_Size=20, text_Style=None, Width=80, Height=40, read_Only=True)
        self.grt = ce.create_textField_Extras(text_Size=22, text_Style=None, Width=120, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#FF0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#000000", size=18), suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=12), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True, on_Change=self.balance_General)

        self.gr1 = ce.create_textField_Extras(Value="", text_Size=15, Width=80, Height=30, border_Width=.5, focused_Border_Width=1, cursor_Height=15, read_Only=False, on_Change=self.plus_gasRes)
        self.gr2 = ce.create_textField_Extras(Value="", text_Size=15, Width=80, Height=30, border_Width=.5, focused_Border_Width=1, cursor_Height=15, read_Only=False, on_Change=self.plus_gasRes)
        self.gr3 = ce.create_textField_Extras(Value="", text_Size=15, Width=80, Height=30, border_Width=.5, focused_Border_Width=1, cursor_Height=15, read_Only=False, on_Change=self.plus_gasRes)
        self.gr4 = ce.create_textField_Extras(Value="", text_Size=15, Width=80, Height=30, border_Width=.5, focused_Border_Width=1, cursor_Height=15, read_Only=False, on_Change=self.plus_gasRes)
        self.gr5 = ce.create_textField_Extras(Value="", text_Size=15, Width=80, Height=30, border_Width=.5, focused_Border_Width=1, cursor_Height=15, read_Only=False, on_Change=self.plus_gasRes)
        self.gr6 = ce.create_textField_Extras(Value="", text_Size=15, Width=80, Height=30, border_Width=.5, focused_Border_Width=1, cursor_Height=15, read_Only=False, on_Change=self.plus_gasRes)
        self.gr7 = ce.create_textField_Extras(Value="", text_Size=15, Width=80, Height=30, border_Width=.5, focused_Border_Width=1, cursor_Height=15, read_Only=False, on_Change=self.plus_gasRes)
        self.gr8 = ce.create_textField_Extras(Value="", text_Size=15, Width=80, Height=30, border_Width=.5, focused_Border_Width=1, cursor_Height=15, read_Only=False, on_Change=self.plus_gasRes)

        #===================================#
        #     VARIABLES BALANCE GENERAL     #
        #===================================#

        # --- Balance ---

        # self.bging = ce.create_textField_Extras(text_Size=25, text_Style=None, Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=15), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True)
        self.bgegr = ce.create_textField_Extras(text_Size=25, text_Style=None, Width=None, Height=50, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=16), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), prefix_Text=" $ ", prefix_Style=ft.TextStyle(color="#000000", size=20), read_Only=True)
        self.bgte = ce.create_textField_Extras(text_Size=25, text_Style=None, Width=None, Height=50, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=16), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), prefix_Text=" $ ", prefix_Style=ft.TextStyle(color="#000000", size=20), read_Only=True)
        self.bgtd = ce.create_textField_Extras(text_Size=28, Color="#FF0000", text_Style=ft.TextStyle(italic=True), Width=170, Height=60, border_Color="#00FF11", border_Width=2.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#000000", size=20), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), prefix_Text=" $ ", prefix_Style=ft.TextStyle(color="#000000", size=25), read_Only=True)

        
        #=====================================#
        #     VARIABLES TOTALES GENERALES     #
        #=====================================#

        # self.report_field_totales = ce.create_textField_RyV("REPORTE TOTALES", text_Size=10, min_Lines=30, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=5, size=12, color="black"), read_Only=True)

        # --- Vasos ---

        self.total_vc = ce.create_textfield_totales(text_Size=15, Width=50, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_vi = ce.create_textfield_totales(text_Size=15, Width=50, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_vm = ce.create_textfield_totales(text_Size=15, Width=50, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_vg = ce.create_textfield_totales(text_Size=15, Width=50, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_vm = ce.create_textfield_totales(text_Size=15, Width=50, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_vasos = ce.create_textfield_totales(text_Size=30, Width=80, Height=50, content_Padding=ft.padding.only(left=0, bottom=2, right=0, top=0))

        # --- Fruta ---

        self.total_fresa = ce.create_textfield_totales(text_Size=15, Width=50, Height=19.5, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_uva = ce.create_textfield_totales(text_Size=15, Width=50, Height=19.5, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_fruta = ce.create_textfield_totales(text_Size=30, Width=80, Height=50, content_Padding=ft.padding.only(left=0, bottom=2, right=0, top=0))

        # --- Cremas ---

        self.total_or = ce.create_textfield_totales(text_Size=15, Width=50, Height=22.5, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_ch = ce.create_textfield_totales(text_Size=15, Width=50, Height=22.5, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_ca = ce.create_textfield_totales(text_Size=15, Width=50, Height=22.5, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_cremas = ce.create_textfield_totales(text_Size=30, Width=80, Height=50, content_Padding=ft.padding.only(left=0, bottom=2, right=0, top=0))

        # --- Toppings extras ---

        self.total_T5 = ce.create_textfield_totales(text_Size=15, Width=40, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_T10 = ce.create_textfield_totales(text_Size=15, Width=40, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_TT = ce.create_textfield_totales(text_Size=30, Width=60, Height=50, content_Padding=ft.padding.only(left=6, bottom=2, right=0, top=0))

        # --- Servicios a domicilio ---

        self.total_SD20 = ce.create_textfield_totales(text_Size=15, Width=40, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_SD35 = ce.create_textfield_totales(text_Size=15, Width=40, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_SD = ce.create_textfield_totales(text_Size=30, Width=60, Height=50, content_Padding=ft.padding.only(left=6, bottom=2, right=0, top=0))

        # --- Transferencias ---

        self.total_nTR = ce.create_textfield_totales(text_Size=15, Width=40, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_mTR = ce.create_textfield_totales(text_Size=30, Width=60, Height=50, content_Padding=ft.padding.only(left=6, bottom=2, right=0, top=0))

        # --- Gastos | Retiros ---

        self.total_nGR = ce.create_textfield_totales(text_Size=15, Width=40, Height=20, content_Padding=ft.padding.only(left=3, bottom=2, right=0, top=0))
        self.total_mGR = ce.create_textfield_totales(text_Size=30, Width=60, Height=50, content_Padding=ft.padding.only(left=6, bottom=2, right=0, top=0))

        #======================================#
        #     VARIABLE INDICADOR DE ESTADO     #
        #======================================#

        # --- Validación venta-consumo ---

        self.validation_vc = ft.Container(
                col=1.9,
                border_radius=150,
                padding=5,
                border=ft.border.all(width=1, color=ft.Colors.BLACK),
                content=ft.Container(
                    alignment=ft.alignment.center,
                    padding=2,
                    border_radius=150,
                    bgcolor="#2F2F2F",
                    # bgcolor="#00FF0D",
                    content=ft.Text("Validación", size=12, color="white")
                )
            )

        #=======================================================#
        #     VARIABLES BOTONES INFERIORES VENTANA REGISTRO     #
        #=======================================================#

        self.add_report_field = ce.created_Button(Text="Crear Reporte", Width=150, bgColor=self.color_teal, Icon=ft.Icons.NOTE_ADD_OUTLINED, on_Click=self.show_report_tf)
        self.button_reset_fields = ce.created_Button(Text="Limpiar Campos", Width=150, bgColor=self.color_teal, Icon=ft.Icons.CLEAR_ALL, on_Click=self.reset_Fields)
        self.delete_target = ce.created_Button(Text="Borrado puntual", Width=150, bgColor=self.color_teal, Icon=ft.Icons.CLEAR, on_Click=self.reset_Fields)
        self.calendary_register = ce.created_Button_Calendary(bgColor=self.color_teal, on_Click=lambda e: page.open(
                ft.DatePicker(
                    first_date=dt.datetime(year=2000, month=1, day=1),
                    last_date=dt.datetime(year=2050, month=12, day=31),
                    on_change=self.change_date
                )
            )
        )

        #==============================================================#
        #     SECCION DE BOTONES INFERIORES DE LA VENTANA REGISTRO     #
        #==============================================================#

        self.actions_Buttons = ft.Container(# BOTONES INFERIORES DE LA VENTANA DE REGISTRO
            alignment=ft.alignment.center,
            # bgcolor=ft.Colors.BLUE_GREY_900,
            bgcolor="#CFF4FF",
            border_radius=10,
            content=ft.ResponsiveRow(
                vertical_alignment="center",
                alignment="center",
                controls=[
                    ft.Container(# BOTON PARA DESPLEGAR EL CALENDARIO DE LA VENTANA DE REGISTRO
                        col=2.5,
                        padding=ft.padding.symmetric(horizontal=50, vertical=10),
                        content=ft.Container(
                            # alignment=ft.alignment.center,
                            border_radius=25,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=6,
                                color=ft.Colors.BLUE_GREY_100,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                            content=self.calendary_register
                        ),
                    ),
                    ft.Container(# BOTON PARA LA CREACION DE REPORTE EN VENTANA DE VENTAS
                        col=2.5,
                        # bgcolor=ft.Colors.BLUE_GREY_900,
                        # border_radius=10,
                        padding=ft.padding.symmetric(horizontal=50, vertical=10),
                        content=ft.Container(
                            # alignment=ft.alignment.center,
                            border_radius=25,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=6,
                                color=ft.Colors.BLUE_GREY_100,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                            content=self.add_report_field
                        ),
                    ),
                    ft.Container(# BOTON DE VISTA PREVIA
                        col=2,
                        # bgcolor=ft.Colors.BLUE_GREY_900,
                        # border_radius=10,
                        padding=ft.padding.symmetric(horizontal=30, vertical=10),
                        content=ft.Container(
                            # alignment=ft.alignment.center,
                            border_radius=25,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=6,
                                color=ft.Colors.BLUE_GREY_100,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                            content=ce.created_Button(
                                Text="Vista previa",
                                Width=150,
                                bgColor=self.color_teal,
                                Icon=ft.Icons.DOCUMENT_SCANNER_OUTLINED,
                                on_Click=lambda e: page.open(
                                    # ft.CupertinoAlertDialog(
                                    ft.AlertDialog(
                                        # title=ft.Text(f"Reporte  {self.pdv}\n"),
                                        content=ft.Container(
                                            width=420,
                                            content=ft.Column(
                                                alignment=ft. MainAxisAlignment.CENTER,
                                                horizontal_alignment="center",
                                                spacing=30,
                                                controls=[
                                                    ft.Text(color="black", size=20, value=f'"Reporte {self.pdv_suc}"', weight="bold"),
                                                    ft.Text(color="black", size=10, value=(
                                                        f"→  VASOS\n"
                                                        f"     •  Chicos - TI: {self.tci.value} | TP: {self.tcf.value} | VI: {self.vci.value} | VF: {self.vcf.value} | VV: {self.vcven.value} | VENTA: $ {self.vcvt.value}\n"
                                                        f"     •  Individuales - TI: {self.tii.value} | TP: {self.tif.value} | VI: {self.vii.value} | VF: {self.vif.value} | VV: {self.viven.value} | VENTA: $ {self.vivt.value}\n"
                                                        f"     •  Medianos - TI: {self.tmi.value} | TP: {self.tmf.value} | VI: {self.vmi.value} | VF: {self.vmf.value} | VV: {self.vmven.value} | VENTA: $ {self.vmvt.value}\n"
                                                        f"     •  Grandes - TI: {self.tgi.value} | TP: {self.tgf.value} | VI: {self.vgi.value} | VF: {self.vgf.value} | VV: {self.vgven.value} | VENTA: $ {self.vgvt.value}\n"
                                                        f"     •  Megas - TI: {self.tmgi.value} | TP: {self.tmgf.value} | VI: {self.vmgi.value} | VF: {self.vmgf.value} | VV: {self.vmgven.value} | VENTA: $ {self.vmgvt.value}\n\n"
                                                        f"→  FRUTA\n"
                                                        f"     •  Fresa - FI: {self.fi.value} | 1S: {self.f1s.value} | 2S: {self.f2s.value} | 3S: {self.f3s.value} | 4S: {self.f4s.value} | FF: {self.ff.value} | FV: {self.fv.value} bote(s)\n"
                                                        f"     •  Uva - UI: {self.ui.value} | 1S: {self.u1s.value} | 2S: {self.u2s.value} | 3S: {self.u3s.value} | 4S: {self.u4s.value} | UF: {self.uf.value} | UV: {self.uv.value} bote(s)\n\n"
                                                        f"→  CREMAS\n"
                                                        f"     •  Original - In: {self.coi.value} | 1S: {self.co1s.value} | 2S: {self.co2s.value} | 3S: {self.co3s.value} | Fi: {self.cof.value} | COV: {self.cov.value} bote(s)\n"
                                                        f"     •  Chocolate - In: {self.cchi.value} | 1S: {self.cch1s.value} | 2S: {self.cch2s.value} | 3S: {self.cch3s.value} | Fi: {self.cchf.value} | CCHV: {self.cchv.value} bote(s)\n"
                                                        f"     •  Cafe - In: {self.ccai.value} | 1S: {self.cca1s.value} | 2S: {self.cca2s.value} | 3S: {self.cca3s.value} | Fi: {self.ccaf.value} | CCV: {self.ccav.value} bote(s)\n\n"
                                                        f"→  TOPPINGS EXTRAS\n"
                                                        f"     •  TE5: {self.t5.value} | TE10: {self.t10.value} | Total: $ {self.tet.value}\n\n"
                                                        f"→  SERVICIOS A DOMICILIO\n"
                                                        f"     •  SD20: {self.sd20.value} | SD35: {self.sd35.value} | Total: $ {self.sdt.value}\n\n"
                                                        f"→  TRANSFERENCIAS\n"
                                                        f"     •  No Transferencias: {self.trn.value} | Total: $ {self.trt.value}\n\n"
                                                        f"→  GASTOS | RETIROS\n"
                                                        f"     •  Cantidad: {self.grn.value} | Total: $ {self.grt.value}\n\n"
                                                        f"→  INGRESOS | DEDUCCIONES\n"
                                                        # f"     •  Ingresos efectivo PDV: $ {self.bging.value}\n"
                                                        f"     •  Ingresos PDV: $ {self.bgtd.value}\n"
                                                        f"     •  Deducciones: $ {self.bgegr.value}\n\n"
                                                        f"→  TOTAL DIA PDV\n"
                                                        f"     •  Efectivo: $ {self.bgte.value}\n"
                                                        f"     •  Venta Total: $ {self.bgtd.value}\n\n"
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                        actions=[
                                            ft.TextButton("CERRAR VISTA PREVIA",
                                                # is_destructive_action=True,
                                                on_click=lambda e: page.close(e.control.parent)
                                            )
                                        ]
                                    )
                                )
                            )
                        ),
                    ),
                    ft.Container(# BOTON DE RESETEADO GENERAL
                        col=2.5,
                        padding=ft.padding.symmetric(horizontal=50, vertical=10),
                        content=ft.Container(
                            # alignment=ft.alignment.center,
                            border_radius=25,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=6,
                                color=ft.Colors.BLUE_GREY_100,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                            content=self.button_reset_fields
                        ),
                    ),
                    ft.Container(# BOTON DE RESETEADO ESPECIFICO O PUNTUAL
                        col=2.5,
                        # bgcolor=ft.Colors.BLUE_GREY_900,
                        padding=ft.padding.symmetric(horizontal=50, vertical=10),
                        content=ft.Container(
                            # alignment=ft.alignment.center,
                            border_radius=25,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=6,
                                color=ft.Colors.BLUE_GREY_100,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                            content=self.delete_target
                        ),
                    ),
                ]
            )
        )

        #==========================================================================#
        #     VARIABLES PARA LA SECCION DE ENCARGADO EN LA VENTANA DE REGISTRO     #
        #==========================================================================#

        self.encSuc = ce.create_textField_Extras(text_Size=12, text_Style=ft.TextStyle(italic=True), Color="black", Width=100, Height=25, border_Color="#C90045", border_Width=1.5, cursor_Height=12, focused_Border_Color="#9B0137", focused_Border_Width=1, read_Only=False, bgColor="#CFF4FF")
        self.ajustadorTamanio = ce.create_radio_AT()

        #==========================================================================#
        #     SECCION DE PUNTOS DE VENTA Y ENCARGADO EN LA VENTANA DE REGISTRO     #
        #==========================================================================#

        self.select_Bar_Sucursales = ft.ResponsiveRow(# BARRA PRINCIPAL PUNTOS DE VENTA Y ENCARGADO
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment="center",
            controls=[
                ft.Container(# CONTENEDOR DE LOS PUNTOS DE VENTA"
                    col=9.5,
                    alignment=ft.alignment.center,
                    # bgcolor=ft.Colors.BLUE_GREY_900,
                    bgcolor="#CFF4FF",
                    border_radius=10,
                    content=self.pdv,
                ),
                ft.Container(# CONTENEDOR DEL TEXTO Y CAMPO DE TEXTO PARA INGRESO DEL NOMBRE DEL ENCARGADO
                    col=2.5,
                    # height=40,
                    alignment=ft.alignment.center,
                    # bgcolor=ft.Colors.BLUE_GREY_900,
                    bgcolor="#CFF4FF",
                    border_radius=10,
                    content=ft.ResponsiveRow(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment="center",
                        controls=[
                            ft.Container(
                                col=6,
                                alignment=ft.alignment.center,
                                padding=ft.padding.only(left=10),
                                content=ft.Text("E N C A R G A D O : ", size=12, weight=ft.FontWeight.BOLD),
                            ),
                            ft.Container(
                                col=5.9,
                                alignment=ft.alignment.center,
                                padding=ft.padding.only(right=10),
                                content=self.encSuc,
                            ),
                            ft.Container(
                                col=.1,
                                alignment=ft.alignment.center_right,
                                content=self.ajustadorTamanio
                            ),
                        ]
                    )
                ),
            ]
        )

        """ 
        ================================================
        #          "VARIABLES VENTANA VENTAS"          #
        ================================================
        """
        
        #========================================================#
        #     VARIABLES CAMPOS DE TEXTO, BOTONES Y DROPDOWNS     #
        #========================================================#

        self.date_receiver = "SIN FECHA"

        # --- Campos de texto ---

        self.report_field = ce.create_textField_RyV("REPORTE", text_Size=10, min_Lines=50, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=5, size=12, color="black"), read_Only=True)
        self.sales_field = ce.create_textField_RyV("EXTRAS", text_Size=10, min_Lines=50, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=5, size=12, color="black"), read_Only=False)

        # --- Botones ---

        self.update_report = ce.created_Button(Text="Actualizar Reporte", Width=150, bgColor=self.color_teal, Icon=ft.Icons.UPDATE, on_Click=self.show_report_tf)
        self.export_PDF = ce.created_Button(Text="Exportar en PDF", Width=150, bgColor=self.color_teal, Icon=ft.Icons.UPLOAD, on_Click=self.pdf_created)
        self.delete_file = ce.created_Button(Text="Borrar Archivo", Width=150, bgColor=self.color_teal, Icon=ft.Icons.DELETE)
        self.clean_Fields = ce.created_Button(Text="Limpiar Campos", Width=150, bgColor=self.color_teal, Icon=ft.Icons.CLEAR_ALL, on_Click=self.reset_textFields)
        self.enable_edition = ce.created_Button(Text="Habilitar edición", Width=150, bgColor=self.color_teal, Icon=ft.Icons.EDIT, on_Click=self.enable_Edition_Button)
        self.calendary_sales = ce.created_Button_Calendary(bgColor=self.color_teal, on_Click=lambda e: page.open(
                ft.DatePicker(
                    first_date=dt.datetime(year=2000, month=1, day=1),
                    last_date=dt.datetime(year=2050, month=12, day=31),
                    on_change=self.change_date
                )
            )
        )
        

        """ 
        ===============================================
        #          FIN VARIABLES DEL SISTEMA          #
        ===============================================
        """
        
        # <<<<<<<<<<<<<<< DIVISOR DE SECCIONES >>>>>>>>>>>>>>> #

        """ 
        =====================================
        #         INTERFAZ GRAFICA          #
        =====================================
        """

        #===============================================#
        #     BARRA DE NAVEGACION LATERAL IZQUIERDA     #
        #===============================================#

        self.navigation_bar = ft.Container(# BARRA LATERAL DE NAVEGACION PRINCIPAL
            col=.75,
            # bgcolor=self.color_teal,
            # bgcolor=ft.Colors.BLUE_GREY_900,
            bgcolor="#CFF4FF",
            # border=ft.border.all(width=2, color=ft.Colors.BLUE_GREY_900),
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        border_radius=10,
                        expand=True,
                        content=ft.NavigationRail(
                            # bgcolor=ft.Colors.BLUE_GREY_900,
                            bgcolor="#CFF4FF",
                            # bgcolor="#181818",
                            expand=True,
                            on_change=self.change_page,
                            selected_index=0,
                            # indicator_color=self.color_teal_2,
                            indicator_color=self.color_teal,
                            # indicator_color="#08f5a9",
                            # selected_label_text_style=ft.TextStyle(color=self.color_teal_2),
                            destinations=[
                                ft.NavigationRailDestination(
                                    icon = ft.Icons.HOME,
                                    label_content=ft.Text("INICIO", size=8),
                                    selected_icon=ft.Icon(ft.Icons.HOME, color="#2e2e2e")
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.Icons.APP_REGISTRATION,
                                    label_content=ft.Text("REGISTRO", size=8),
                                    selected_icon=ft.Icon(ft.Icons.APP_REGISTRATION, color="#2e2e2e")
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.Icons.POINT_OF_SALE_SHARP,
                                    label_content=ft.Text("VENTAS", size=8),
                                    selected_icon=ft.Icon(ft.Icons.POINT_OF_SALE_SHARP, color="#2e2e2e")
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.Icons.ACCOUNT_TREE_ROUNDED,
                                    label_content=ft.Text("PDV's", size=8),
                                    selected_icon=ft.Icon(ft.Icons.ACCOUNT_TREE_ROUNDED, color="#2e2e2e")
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.Icons.INVENTORY,
                                    label_content=ft.Text("STOCK", size=8),
                                    selected_icon=ft.Icon(ft.Icons.INVENTORY, color="#2e2e2e")
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        margin=ft.margin.only(bottom=3),
                        alignment=ft.alignment.center,
                        expand=True,
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                self.profiles,
                                self.configuration,
                                self.mode_switch
                            ]
                        )
                    ),
                ]
            )
        )

        #===============================================#
        #     VENTANA DE INICIO / SECCION PLANEADOR     #
        #===============================================#

        self.home = ft.Container(# VENTANA HOME O INICIAL
            col=12,
            # bgcolor=ft.Colors.BLUE_GREY_900,
            bgcolor="#CFF4FF",
            border_radius=10,
            content=ft.Container(
                margin=3,
                # bgcolor="pink",
                content=ft.ResponsiveRow(
                    controls=[
                        ft.Tabs(
                            selected_index=0,
                            label_text_style=ft.TextStyle(size=20, italic=True),
                            # label_color="#08f5a9",
                            label_color="#000000",
                            unselected_label_color="#5C5C5C",
                            unselected_label_text_style=ft.TextStyle(size=14, italic=False),
                            animation_duration=150,
                            scrollable=False,
                            indicator_tab_size=True,
                            # indicator_color="#08f5a9",
                            indicator_color=self.color_teal_2,
                            # overlay_color={
                            #     ft.ControlState.HOVERED: "#181818",
                            #     ft.ControlState.PRESSED: "#181818"
                            # },
                            tabs=[
                                ft.Tab( # CONTROL MAESTRO
                                    text="Control Maestro",
                                    content=ft.Container(
                                        alignment=ft.alignment.center,
                                        content=ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Text("Construcción en", size=25),
                                                ft.Text("proceso...", size=25),
                                                ft.Text("3%", size=20),
                                                ft.Container(
                                                    alignment=ft.alignment.center_left,
                                                    bgcolor="#000000",
                                                    width=200,
                                                    height=5,
                                                    content=ft.Container(
                                                        bgcolor="#13ffd4",
                                                        width=7,
                                                        height=3
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ),
                                ft.Tab( # PLANEADOR
                                    text="Planeador",
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            # ft.Container(
                                            #             # padding=10,
                                            #             padding=ft.padding.only(top=20, bottom=5),
                                            #             # bgcolor="black",
                                            #             content=ft.Text("PLANEADOR GENERAL", size=30, color="#101010", weight=ft.FontWeight.BOLD)
                                            #         ),
                                                    # ft.Divider(# Separador de seccion con Divider
                                                    #     height=1,
                                                    #     # color=self.color_teal,
                                                    #     color="#ff1765",
                                                    #     thickness=2,
                                                    #     leading_indent=30,
                                                    #     trailing_indent=30,
                                                    # ),
                                            ft.ResponsiveRow(# Planeador del dia
                                                expand=True,
                                                controls=[
                                                    ft.Container(# Contenedor Principal
                                                        col=12,
                                                        alignment=ft.alignment.center,
                                                        margin=ft.Margin(top=30, bottom=15, left=35, right=35),
                                                        padding=10,
                                                        # bgcolor="yellow",
                                                        # border=ft.border.all(width=2, color=ft.Colors.BLUE_GREY_700),
                                                        border=ft.border.all(width=2, color="#ff1765"),
                                                        border_radius=1,
                                                        content=ft.Column(
                                                            alignment=ft.alignment.center,
                                                            controls=[
                                                                ft.Container(# Fecha
                                                                    border_radius=3,
                                                                    #bgcolor="#1b89ff",
                                                                    bgcolor="#006ADB",
                                                                    alignment=ft.alignment.center,
                                                                    padding=5,
                                                                    content=ft.Column(
                                                                        alignment=ft.alignment.center,
                                                                        horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text(value="PLANEACIÓN Y ESTRUCTURA LABORAL", size=22, color="white", weight=ft.FontWeight.BOLD, style=ft.TextStyle(letter_spacing=15)),
                                                                            ft.Container(
                                                                                bgcolor="white",
                                                                                width=1100,
                                                                                height=.75,
                                                                            ),
                                                                            ft.Text(self.today_main_hor, size=18, color="white", weight=ft.FontWeight.BOLD, style=ft.TextStyle(letter_spacing=18, italic=True))
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.ResponsiveRow(# Fila Principal
                                                                    expand=True,
                                                                    controls=[
                                                                        # ft.Container(# Fecha vertical
                                                                        #     col=.5,
                                                                        #     padding=ft.padding.symmetric(horizontal=5, vertical=20),
                                                                        #     border_radius=3,
                                                                        #     alignment=ft.alignment.center,
                                                                        #     expand=True,
                                                                        #     #bgcolor="#1b89ff",
                                                                        #     bgcolor="#006ADB",
                                                                        #     content=ft.Column(
                                                                        #         # spacing=0,
                                                                        #         alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                        #         horizontal_alignment="center",
                                                                        #         controls=[
                                                                        #             ft.Text(value=self.date_onList[0], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[1], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[2], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[3], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[4], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[5], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[6], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[7], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[8], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[9], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[10], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[11], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[12], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[15], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #             ft.Text(value=self.date_onList[16], color="white", weight=ft.FontWeight.BOLD, size=12),
                                                                        #         ]
                                                                        #     )
                                                                        # ),
                                                                        ft.Container(# Supervisores y Sucursales
                                                                            # expand=True,
                                                                            # height=300,
                                                                            # bgcolor="blue",
                                                                            alignment=ft.alignment.center,
                                                                            col=4.5,
                                                                            content=ft.Column(
                                                                                # expand=True,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        # expand=True,
                                                                                        height=140,
                                                                                        border=ft.border.all(width=.5, color="black"),
                                                                                        bgcolor="white",
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.ResponsiveRow(
                                                                                            expand=True,
                                                                                            spacing=0,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    col=1,
                                                                                                    border_radius=ft.border_radius.only(top_left=3),
                                                                                                    #bgcolor="#6adb00",
                                                                                                    bgcolor="#00DA16",
                                                                                                    alignment=ft.alignment.center,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    content=ft.Column(
                                                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                                                        horizontal_alignment="center",
                                                                                                        spacing=-2,
                                                                                                        controls=[
                                                                                                            ft.Text("S", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("U", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("P", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("E", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("R", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("V", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("I", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("S", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("I", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("O", color="black", size=9, weight="bold"),
                                                                                                            ft.Text("N", color="black", size=9, weight="bold"),
                                                                                                        ]
                                                                                                    ),
                                                                                                ),
                                                                                                ft.Column(
                                                                                                    expand=True,
                                                                                                    col=6,
                                                                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                    horizontal_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center_left,
                                                                                                            border=ft.border.all(color="black", width=.5),
                                                                                                            padding=5,
                                                                                                            # height=45,
                                                                                                            #bgcolor="#6adb00",
                                                                                                            # bgcolor="#00B112",
                                                                                                            bgcolor="#00DA16",
                                                                                                            content=ft.Text("Supervisor(a) de Personal Puntos de Venta", color="black", size=11, weight="bold")
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center_left,
                                                                                                            border=ft.border.all(color="black", width=.5),
                                                                                                            padding=5,
                                                                                                            # height=45,
                                                                                                            #bgcolor="#6adb00",
                                                                                                            bgcolor="#00DA16",
                                                                                                            content=ft.Text("Supervisor de Operaciones Logísticas", color="black", size=11, weight="bold")
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center_left,
                                                                                                            border=ft.border.all(color="black", width=.5),
                                                                                                            padding=5,
                                                                                                            # height=45,
                                                                                                            #bgcolor="#6adb00",
                                                                                                            # bgcolor="#00C715",
                                                                                                            bgcolor="#00DA16",
                                                                                                            content=ft.Text("Supervisor(a) Centro de Operaciones", color="black", size=11, weight="bold")
                                                                                                        )
                                                                                                    ]
                                                                                                ),
                                                                                                ft.Column(
                                                                                                    col=5,
                                                                                                    horizontal_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            # height=45,
                                                                                                            bgcolor="white",
                                                                                                            content=self.sup_Pers_PDV
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            # height=45,
                                                                                                            bgcolor="white",
                                                                                                            content=self.sup_Ops
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            # height=45,
                                                                                                            bgcolor="white",
                                                                                                            content=self.sup_CDO
                                                                                                        ),
                                                                                                    ]
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        border=ft.border.all(width=.5, color="black"),
                                                                                        # bgcolor="white",
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.ResponsiveRow(
                                                                                            expand=True,
                                                                                            spacing=0,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    # expand=True,
                                                                                                    # height=250,
                                                                                                    col=1,
                                                                                                    border_radius=ft.border_radius.only(top_left=3),
                                                                                                    bgcolor="#fe0f7c",
                                                                                                    alignment=ft.alignment.center,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    content=ft.Column(
                                                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                                                        horizontal_alignment="center",
                                                                                                        spacing=1,
                                                                                                        controls=[
                                                                                                            ft.Text("S", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("U", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("C", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("U", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("R", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("S", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("A", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("L", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("E", color="white", size=13, weight="bold"),
                                                                                                            ft.Text("S", color="white", size=13, weight="bold"),
                                                                                                        ]
                                                                                                    ),
                                                                                                ),
                                                                                                # --- Sucursales ---
                                                                                                ft.Column(
                                                                                                    expand=True,
                                                                                                    col=6,
                                                                                                    horizontal_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            bgcolor="blue",
                                                                                                            content=ft.Column(
                                                                                                                spacing=0,
                                                                                                                controls=[
                                                                                                                    ft.Container(
                                                                                                                        expand=True,
                                                                                                                        alignment=ft.alignment.center_left,
                                                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                                                        # height=25,
                                                                                                                        bgcolor="#fe0f7c",
                                                                                                                        padding=ft.padding.only(left=5),
                                                                                                                        content=ft.Text("1 - VP Vips", color="white", size=13, weight="bold")
                                                                                                                    ),
                                                                                                                    ft.Container(
                                                                                                                        expand=True,
                                                                                                                        alignment=ft.alignment.center_left,
                                                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                                                        # height=25,
                                                                                                                        bgcolor="#fe0f7c",
                                                                                                                        padding=ft.padding.only(left=5),
                                                                                                                        content=ft.Text("2 - VP San Miguel", color="white", size=13, weight="bold")
                                                                                                                    ),
                                                                                                                    ft.Container(
                                                                                                                        expand=True,
                                                                                                                        alignment=ft.alignment.center_left,
                                                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                                                        # height=25,
                                                                                                                        bgcolor="#fe0f7c",
                                                                                                                        padding=ft.padding.only(left=5),
                                                                                                                        content=ft.Text("3 - VP San Antonio", color="white", size=13, weight="bold")
                                                                                                                    ),
                                                                                                                    ft.Container(
                                                                                                                        expand=True,
                                                                                                                        alignment=ft.alignment.center_left,
                                                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                                                        # height=25,
                                                                                                                        bgcolor="#fe0f7c",
                                                                                                                        padding=ft.padding.only(left=5),
                                                                                                                        content=ft.Text("4 - VP Ensueños", color="white", size=13, weight="bold")
                                                                                                                    ),
                                                                                                                    ft.Container(
                                                                                                                        expand=True,
                                                                                                                        alignment=ft.alignment.center_left,
                                                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                                                        # height=25,
                                                                                                                        bgcolor="#fe0f7c",
                                                                                                                        padding=ft.padding.only(left=5),
                                                                                                                        content=ft.Text("5 - VP Cofradía 2", color="white", size=13, weight="bold")
                                                                                                                    ),
                                                                                                                    ft.Container(
                                                                                                                        expand=True,
                                                                                                                        alignment=ft.alignment.center_left,
                                                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                                                        # height=25,
                                                                                                                        bgcolor="#fe0f7c",
                                                                                                                        padding=ft.padding.only(left=5),
                                                                                                                        content=ft.Text("6 - FS Glorieta", color="white", size=13, weight="bold")
                                                                                                                    ),
                                                                                                                ]
                                                                                                            )
                                                                                                        )
                                                                                                    ]
                                                                                                ),
                                                                                                # --- Encargado / Vendedor Punto de Venta ---
                                                                                                ft.Column(
                                                                                                    col=5,
                                                                                                    horizontal_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            # height=25,
                                                                                                            bgcolor="white",
                                                                                                            content=self.ven_Vips
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            # height=25,
                                                                                                            bgcolor="white",
                                                                                                            content=self.ven_SanMiguel
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            # height=25,
                                                                                                            bgcolor="white",
                                                                                                            content=self.ven_SanAntonio
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            # height=25,
                                                                                                            bgcolor="white",
                                                                                                            content=self.ven_Ensuenos
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            # height=25,
                                                                                                            bgcolor="white",
                                                                                                            content=self.ven_Cofradia2
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            bgcolor="white",
                                                                                                            content=self.ven_Glorieta
                                                                                                        ),
                                                                                                    ]
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ),
                                                                        # --- Ventas Minimas ---
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=2,
                                                                            # bgcolor="blue",
                                                                            content=ft.Column(
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        height=140,
                                                                                        content=ft.Container(
                                                                                            border=ft.border.all(width=.5, color="black"),
                                                                                            bgcolor="white",
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.Text("Ventas mínimas\ndel día", size=20, color="black", text_align="center", italic=True, weight="bold"),
                                                                                        ),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        border=ft.border.all(width=.5, color="black"),
                                                                                        # bgcolor="white",
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.Column(
                                                                                            spacing=0,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.vm_Vips
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.vm_SanMiguel
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.vm_SanAntonio
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.vm_Ensuenos
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.vm_Cofradia2
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.vm_Glorieta
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                    )

                                                                                ]
                                                                            )
                                                                        ),
                                                                        # --- Promedio ---
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=1,
                                                                            content=ft.Column(
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        height=140,
                                                                                        content=ft.Container(
                                                                                            border=ft.border.all(width=.5, color="black"),
                                                                                            alignment=ft.alignment.center,
                                                                                            bgcolor="white",
                                                                                            content=ft.Text("Promedio", color="black", weight="bold")
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        border=ft.border.all(width=.5, color="black"),
                                                                                        # bgcolor="white",
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.Column(
                                                                                            spacing=0,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.prom_Vips
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.prom_SanMiguel
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.prom_SanAntonio
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.prom_Ensuenos
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.prom_Cofradia2
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # border=ft.border.all(color="black", width=1),
                                                                                                    bgcolor="white",
                                                                                                    content=self.prom_Glorieta
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                    ),

                                                                                ]
                                                                            )
                                                                        ),
                                                                        # --- Rutas y CDO ---
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4.5,
                                                                            content=ft.Column(
                                                                                expand=True,
                                                                                controls=[
                                                                                    ft.Container(# Rutas
                                                                                        expand=True,
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.ResponsiveRow(
                                                                                            spacing=0,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    col=5,
                                                                                                    bgcolor="#00b687",
                                                                                                    alignment=ft.alignment.center,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    content=ft.Text("Operaciones\ny Transporte", color="white",size=25)
                                                                                                ),
                                                                                                ft.Column(
                                                                                                    col=3,
                                                                                                    horizontal_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            border=ft.border.all(color="black", width=.5),
                                                                                                            height=90,
                                                                                                            bgcolor="#ff1919",
                                                                                                            content=ft.Text("Ruta Única", color="white")
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            border=ft.border.all(color="black", width=.5),
                                                                                                            height=70,
                                                                                                            bgcolor="#ff1919",
                                                                                                            content=ft.Text("Ruta 1", color="white")
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            border=ft.border.all(color="black", width=.5),
                                                                                                            bgcolor="#ff1919",
                                                                                                            content=ft.Text("Ruta 2", color="white")
                                                                                                        )
                                                                                                    ]
                                                                                                ),
                                                                                                ft.Column(
                                                                                                    col=4,
                                                                                                    horizontal_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            border_radius=ft.border_radius.only(top_right=3),
                                                                                                            height=90,
                                                                                                            bgcolor="white",
                                                                                                            content=self.ruta_unica
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            height=70,
                                                                                                            bgcolor="white",
                                                                                                            content=self.ruta1
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            bgcolor="white",
                                                                                                            content=self.ruta2
                                                                                                        ),
                                                                                                    ]
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                    ),
                                                                                    ft.Container(# CDO
                                                                                        height=170,
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.ResponsiveRow(
                                                                                            expand=True,
                                                                                            spacing=0,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    col=8,
                                                                                                    bgcolor="#fe8410",
                                                                                                    alignment=ft.alignment.center,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    content=ft.Text("Centro de Operaciones", color="white",size=26)
                                                                                                ),
                                                                                                ft.Column(
                                                                                                    col=4,
                                                                                                    horizontal_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            height=40,
                                                                                                            bgcolor="white",
                                                                                                            content=self.cdo_1
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            height=40,
                                                                                                            bgcolor="white",
                                                                                                            content=self.cdo_2
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            height=40,
                                                                                                            bgcolor="white",
                                                                                                            content=self.cdo_3
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            expand=True,
                                                                                                            border_radius=ft.border_radius.only(bottom_right=3),
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # border=ft.border.all(color="black", width=.5),
                                                                                                            bgcolor="white",
                                                                                                            content=self.cdo_4
                                                                                                        ),
                                                                                                    ]
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            # --- Botones inferiores Planeador ---
                                            ft.Container(
                                                # bgcolor="blue",
                                                margin=ft.margin.only(bottom=10),
                                                content=ft.ResponsiveRow(
                                                    vertical_alignment="center",
                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                    controls=[
                                                        ft.Container(
                                                            col=1,
                                                            border_radius=50,
                                                            alignment=ft.alignment.center,
                                                            shadow=ft.BoxShadow(
                                                                spread_radius=.5,
                                                                blur_radius=5,
                                                                color=ft.Colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),
                                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                            ),
                                                            content=ce.created_Button(Text="Reiniciar", Width=150, bgColor=self.color_teal, Icon=None, on_Click=self.reset_planeador)
                                                        ),
                                                        ft.Container(
                                                            col=1,
                                                            border_radius=50,
                                                            alignment=ft.alignment.center,
                                                            shadow=ft.BoxShadow(
                                                                spread_radius=.5,
                                                                blur_radius=5,
                                                                color=ft.Colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),
                                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                            ),
                                                            content=ce.created_Button(Text="Lunes", Width=150, bgColor=self.color_teal, Icon=None, on_Click=self.planeador_lunes)
                                                        ),
                                                        ft.Container(
                                                            col=1,
                                                            border_radius=50,
                                                            alignment=ft.alignment.center,
                                                            shadow=ft.BoxShadow(
                                                                spread_radius=.5,
                                                                blur_radius=5,
                                                                color=ft.Colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),
                                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                            ),
                                                            content=ce.created_Button(Text="Martes", Width=150, bgColor=self.color_teal, Icon=None, on_Click=self.planeador_martes)
                                                        ),
                                                        ft.Container(
                                                            col=1,
                                                            border_radius=50,
                                                            alignment=ft.alignment.center,
                                                            shadow=ft.BoxShadow(
                                                                spread_radius=.5,
                                                                blur_radius=5,
                                                                color=ft.Colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),
                                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                            ),
                                                            content=ce.created_Button(Text="Miércoles", Width=150, bgColor=self.color_teal, Icon=None, on_Click=self.planeador_miercoles)
                                                        ),
                                                        ft.Container(
                                                            col=1,
                                                            border_radius=50,
                                                            alignment=ft.alignment.center,
                                                            shadow=ft.BoxShadow(
                                                                spread_radius=.5,
                                                                blur_radius=5,
                                                                color=ft.Colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),
                                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                            ),
                                                            content=ce.created_Button(Text="Jueves", Width=150, bgColor=self.color_teal, Icon=None, on_Click=self.planeador_jueves)
                                                        ),
                                                        ft.Container(
                                                            col=1,
                                                            border_radius=50,
                                                            alignment=ft.alignment.center,
                                                            shadow=ft.BoxShadow(
                                                                spread_radius=.5,
                                                                blur_radius=5,
                                                                color=ft.Colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),
                                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                            ),
                                                            content=ce.created_Button(Text="Viernes", Width=150, bgColor=self.color_teal, Icon=None, on_Click=self.planeador_viernes)
                                                        ),
                                                        ft.Container(
                                                            col=1,
                                                            border_radius=50,
                                                            alignment=ft.alignment.center,
                                                            shadow=ft.BoxShadow(
                                                                spread_radius=.5,
                                                                blur_radius=5,
                                                                color=ft.Colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),
                                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                            ),
                                                            content=ce.created_Button(Text="Sábado", Width=150, bgColor=self.color_teal, Icon=None, on_Click=self.planeador_sabado)
                                                        ),
                                                        ft.Container(
                                                            col=1,
                                                            border_radius=50,
                                                            alignment=ft.alignment.center,
                                                            shadow=ft.BoxShadow(
                                                                spread_radius=.5,
                                                                blur_radius=5,
                                                                color=ft.Colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),
                                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                                            ),
                                                            content=ce.created_Button(Text="Domingo", Width=150, bgColor=self.color_teal, Icon=None, on_Click=self.planeador_domingo)
                                                        ),
                                                    ]
                                                ),
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                    ]
                ),
            ),
        )

        #==========================================================#
        #     VENTANA DE REGISTRO / SECCION CONTROL DE INSUMOS     #
        #==========================================================#

        self.register = ft.Container(# VENTANA DE CAPTURA Y REGISTRO
            # bgcolor=ft.Colors.BLUE_GREY_900,
            bgcolor="#CFF4FF",
            expand=True,
            # height=638,
            # width=1500,
            # padding=10,
            border_radius=10,
            content=ft.ResponsiveRow(
                # alignment="start"
                # scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Tabs(
                        selected_index=0,
                        label_text_style=ft.TextStyle(size=20, italic=True),
                        # label_color="#08f5a9",
                        label_color="#000000",
                        unselected_label_color="#5C5C5C",
                        unselected_label_text_style=ft.TextStyle(size=14, italic=False),
                        animation_duration=150,
                        scrollable=False,
                        indicator_tab_size=True,
                        # indicator_color="#08f5a9",
                        indicator_color=self.color_teal_2,
                        # overlay_color={
                        #     # ft.ControlState.HOVERED: "#F70000",
                        #     ft.ControlState.PRESSED: "#FF0000",
                        # },
                        # indicator_color="#ff1765",
                        # indicator_thickness=10,
                        tabs=[
                            ft.Tab(# VASOS
                                text="Vasos",
                                content=ft.Container(# Vasos
                                    margin=ft.Margin(top=20, bottom=20, left=30, right=30),
                                    # bgcolor="blue",
                                    content=ft.ResponsiveRow(
                                        controls=[
                                            ft.Container(
                                                col=9,
                                                margin=ft.margin.only(right=10),
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Container( # VASOS CHICOS
                                                            expand=True,
                                                            bgcolor="#B2E7FF",
                                                            alignment=ft.alignment.center,
                                                            border_radius=5,
                                                            border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                            padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                controls=[
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        # bgcolor="#1E1E1E",
                                                                        content=ft.Text("CHICOS", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=15)),
                                                                    ),
                                                                    ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Tapas chicas iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tci
                                                                            ),
                                                                            ft.Container(# Tapas chicas finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tcf
                                                                            ),
                                                                            ft.Container(# Vasos chicos iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vci
                                                                            ),
                                                                            ft.Container(# Vasos chicos finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vcf
                                                                            ),
                                                                            ft.Container(# Vasos chicos vendidos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vcven
                                                                            ),
                                                                            ft.Container(# Vasos chicos venta total
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vcvt
                                                                            ),
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ),
                                                        ft.Container( # VASOS INDIVIDUALES
                                                            expand=True,
                                                            bgcolor="#B2E7FF",
                                                            alignment=ft.alignment.center,
                                                            border_radius=5,
                                                            border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                            padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                controls=[
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        # bgcolor="#1E1E1E",
                                                                        content=ft.Text("INDIVIDUALES", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=15)),
                                                                    ),
                                                                    ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Tapas individuales iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tii
                                                                            ),
                                                                            ft.Container(# Tapas individuales finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tif
                                                                            ),
                                                                            ft.Container(# Vasos individuales iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vii
                                                                            ),
                                                                            ft.Container(# Vasos individuales finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vif
                                                                            ),
                                                                            ft.Container(# Vasos individuales vendidos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.viven
                                                                            ),
                                                                            ft.Container(# Vasos individuales venta total
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vivt
                                                                            ),
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ),
                                                        ft.Container( # VASOS MEDIANOS
                                                            expand=True,
                                                            bgcolor="#B2E7FF",
                                                            alignment=ft.alignment.center,
                                                            border_radius=5,
                                                            border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                            padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                controls=[
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        # bgcolor="#1E1E1E",
                                                                        content=ft.Text("MEDIANOS", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=15)),
                                                                    ),
                                                                    ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Tapas medianas iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tmi
                                                                            ),
                                                                            ft.Container(# Tapas medianas finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tmf
                                                                            ),
                                                                            ft.Container(# Vasos medianos iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vmi
                                                                            ),
                                                                            ft.Container(# Vasos medianos finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vmf
                                                                            ),
                                                                            ft.Container(# Vasos medianos vendidos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vmven
                                                                            ),
                                                                            ft.Container(# Vasos medianos venta total
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vmvt
                                                                            ),
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ),
                                                        ft.Container( # VASOS GRANDES
                                                            expand=True,
                                                            bgcolor="#B2E7FF",
                                                            alignment=ft.alignment.center,
                                                            border_radius=5,
                                                            border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                            padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                controls=[
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        # bgcolor="#1E1E1E",
                                                                        content=ft.Text("GRANDES", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=15)),
                                                                    ),
                                                                    ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Tapas grandes iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tgi
                                                                            ),
                                                                            ft.Container(# Tapas grandes finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tgf
                                                                            ),
                                                                            ft.Container(# Vasos grandes iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vgi
                                                                            ),
                                                                            ft.Container(# Vasos grandes finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vgf
                                                                            ),
                                                                            ft.Container(# Vasos grandes vendidos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vgven
                                                                            ),
                                                                            ft.Container(# Vasos grandes venta total
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vgvt
                                                                            ),
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ),
                                                        ft.Container( # VASOS MEGAS
                                                            expand=True,
                                                            bgcolor="#B2E7FF",
                                                            alignment=ft.alignment.center,
                                                            border_radius=5,
                                                            border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                            padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                controls=[
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        # bgcolor="#1E1E1E",
                                                                        content=ft.Text("MEGAS", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=15)),
                                                                    ),
                                                                    ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Tapas megas iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tmgi
                                                                            ),
                                                                            ft.Container(# Tapas megas finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.tmgf
                                                                            ),
                                                                            ft.Container(# Vasos megas iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vmgi
                                                                            ),
                                                                            ft.Container(# Vasos megas finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vmgf
                                                                            ),
                                                                            ft.Container(# Vasos megas vendidos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vmgven
                                                                            ),
                                                                            ft.Container(# Vasos megas venta total
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=self.vmgvt
                                                                            ),
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            ft.Container(# Venta Total Vasos en General
                                                # bgcolor="yellow",
                                                padding=40,
                                                col=3,
                                                alignment=ft.alignment.center,
                                                border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                border_radius=5,
                                                bgcolor="#B2E7FF",
                                                content=ft.Column(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(# Venta Total Vasos en General
                                                            alignment=ft.alignment.top_center,
                                                            # bgcolor="blue",
                                                            padding=5,
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.START,
                                                                horizontal_alignment="center",
                                                                spacing=0,
                                                                controls=[
                                                                    ft.Text("TOTAL", color="#ff1765", weight=ft.FontWeight.BOLD, size=40, style=ft.TextStyle(letter_spacing=10)),
                                                                    ft.Text("GENERAL", color="#ff1765", weight=ft.FontWeight.BOLD, size=30, style=ft.TextStyle(letter_spacing=5)),
                                                                ]
                                                            )
                                                        ),
                                                        ft.Container(# Venta Total Vasos en General
                                                            alignment=ft.alignment.center,
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text("VASOS", color="#ff1765", weight=ft.FontWeight.BOLD, size=25, style=ft.TextStyle(letter_spacing=10)),
                                                                    ft.Container(# Total Vasos Vendidos
                                                                        alignment=ft.alignment.center,
                                                                        border=ft.border.all(width=2, color="#4ed3ff"),
                                                                        border_radius=5,
                                                                        padding=10,
                                                                        shadow=ft.BoxShadow(
                                                                            spread_radius=.5,
                                                                            blur_radius=20,
                                                                            color="#4ed3ff",
                                                                            offset=ft.Offset(0, 0),
                                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                                        ),
                                                                        content=self.vtv
                                                                    ),
                                                                ]
                                                            )
                                                        ),
                                                        ft.Container(# Venta Total Vasos en General
                                                            alignment=ft.alignment.center,
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text("VENTA", color="#ff1765", weight=ft.FontWeight.BOLD, size=25, style=ft.TextStyle(letter_spacing=10)),
                                                                    ft.Container(# Total Vasos Vendidos
                                                                        alignment=ft.alignment.center,
                                                                        border=ft.border.all(width=2, color="#4ed3ff"),
                                                                        border_radius=5,
                                                                        padding=10,
                                                                        shadow=ft.BoxShadow(
                                                                            spread_radius=.5,
                                                                            blur_radius=20,
                                                                            color="#4ed3ff",
                                                                            offset=ft.Offset(0, 0),
                                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                                        ),
                                                                        content=self.vvmt
                                                                    ),
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]
                                    ),
                                ),
                            ),
                            ft.Tab(# FRUTA Y CREMAS
                                text="Frutas y Cremas",
                                content=ft.Container(
                                    expand=True,
                                    # bgcolor="red",
                                    margin=ft.Margin(top=20, bottom=20, left=30, right=30),
                                    content=ft.Column(
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                # bgcolor="green",
                                                content=ft.ResponsiveRow(# FRUTA Y VENTA GENERAL
                                                    expand=True,
                                                    controls=[
                                                        ft.Container(# FRUTA
                                                            col=9,
                                                            # bgcolor="yellow",
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Container(# CONTENEDOR PRINCIPAL FRESA
                                                                        expand=True,
                                                                        bgcolor="#B2E7FF",
                                                                        # bgcolor="#292929",
                                                                        alignment=ft.alignment.center,
                                                                        border_radius=5,
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                                        padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Text("FRESA", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                                ft.Container(# CAMPOS FRESA
                                                                                    alignment=ft.alignment.center,
                                                                                    # bgcolor="pink",
                                                                                    content=ft.ResponsiveRow(
                                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                        vertical_alignment="center",
                                                                                        controls=[
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.fi
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=6.5,
                                                                                                # bgcolor="yellow",
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                    vertical_alignment="center",
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.f1s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.f2s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.f3s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.f4s
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.ff
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=2,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.fv
                                                                                            ),
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(# CONTENEDOR PRINCIPAL UVA
                                                                        expand=True,
                                                                        bgcolor="#B2E7FF",
                                                                        # bgcolor="#292929",
                                                                        alignment=ft.alignment.center,
                                                                        border_radius=5,
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                                        padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Text("UVA", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                                ft.Container(# UVA
                                                                                    alignment=ft.alignment.center,
                                                                                    # bgcolor="pink",
                                                                                    content=ft.ResponsiveRow(
                                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                        vertical_alignment="center",
                                                                                        controls=[
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.ui
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=6.5,
                                                                                                # bgcolor="yellow",
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                    vertical_alignment="center",
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.u1s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.u2s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.u3s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.u4s
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.uf
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=2,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.uv
                                                                                            ),
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(# CONTENEDOR PRINCIPAL CREMA ORIGINAL
                                                                        expand=True,
                                                                        bgcolor="#B2E7FF",
                                                                        # bgcolor="#292929",
                                                                        alignment=ft.alignment.center,
                                                                        border_radius=5,
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                                        padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Text("CREMA ORIGINAL", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=8)),
                                                                                ft.Container(# Crema Original
                                                                                    alignment=ft.alignment.center,
                                                                                    # bgcolor="pink",
                                                                                    content=ft.ResponsiveRow(
                                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                        vertical_alignment="center",
                                                                                        controls=[
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.coi
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=6.5,
                                                                                                # bgcolor="yellow",
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                    vertical_alignment="center",
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.co1s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.co2s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.co3s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.co4s
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.cof
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=2,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.cov
                                                                                            ),
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(# CONTENEDOR PRINCIPAL CREMA CHOCOLATE
                                                                        expand=True,
                                                                        bgcolor="#B2E7FF",
                                                                        # bgcolor="#292929",
                                                                        alignment=ft.alignment.center,
                                                                        border_radius=5,
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                                        padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Text("CREMA CHOCOLATE", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=8)),
                                                                                ft.Container(# Crema Original
                                                                                    alignment=ft.alignment.center,
                                                                                    # bgcolor="pink",
                                                                                    content=ft.ResponsiveRow(
                                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                        vertical_alignment="center",
                                                                                        controls=[
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.cchi
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=6.5,
                                                                                                # bgcolor="yellow",
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                    vertical_alignment="center",
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.cch1s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.cch2s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.cch3s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.cch4s
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.cchf
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=2,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.cchv
                                                                                            ),
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(# CONTENEDOR PRINCIPAL CREMA CAFE
                                                                        expand=True,
                                                                        bgcolor="#B2E7FF",
                                                                        # bgcolor="#292929",
                                                                        alignment=ft.alignment.center,
                                                                        border_radius=5,
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_500),
                                                                        padding=ft.padding.only(top=5, bottom=10, left=10, right=10),
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Text("CREMA CAFE", color="#ff1765", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=8)),
                                                                                ft.Container(# Crema Original
                                                                                    alignment=ft.alignment.center,
                                                                                    # bgcolor="pink",
                                                                                    content=ft.ResponsiveRow(
                                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                        vertical_alignment="center",
                                                                                        controls=[
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.ccai
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=6.5,
                                                                                                # bgcolor="yellow",
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                    vertical_alignment="center",
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.cca1s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.cca2s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.cca3s
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            col=3,
                                                                                                            # bgcolor="yellow",
                                                                                                            content=self.cca4s
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=1.75,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.ccaf
                                                                                            ),
                                                                                            ft.Container(
                                                                                                alignment=ft.alignment.center,
                                                                                                col=2,
                                                                                                # bgcolor="yellow",
                                                                                                content=self.ccav
                                                                                            ),
                                                                                        ]
                                                                                    )
                                                                                ),
                                                                            ]
                                                                        )
                                                                    ),
                                                                ]
                                                            )
                                                        ),
                                                        ft.Container(# VENTA GENERAL
                                                            col=3,
                                                            alignment=ft.alignment.center,
                                                            # margin=ft.margin.only(left=4),
                                                            border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                            padding=ft.padding.symmetric(horizontal=50, vertical=5),
                                                            border_radius=5,
                                                            bgcolor="#B2E7FF",
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Column(
                                                                        alignment=ft.MainAxisAlignment.START,
                                                                        horizontal_alignment="center",
                                                                        spacing=-5,
                                                                        controls=[
                                                                            ft.Text("CONSUMO", color="#ff1765", weight=ft.FontWeight.BOLD, size=28, style=ft.TextStyle(letter_spacing=5)),
                                                                            ft.Text("GENERAL", color="#ff1765", weight=ft.FontWeight.BOLD, size=28, style=ft.TextStyle(letter_spacing=8)),
                                                                        ]
                                                                    ),
                                                                    ft.Container(# Fruta total vendida (botes)
                                                                        alignment=ft.alignment.center,
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Text("FRUTA", color="#ff1765", weight=ft.FontWeight.BOLD, size=25, style=ft.TextStyle(letter_spacing=7)),
                                                                                ft.Container(
                                                                                    alignment=ft.alignment.center,
                                                                                    border=ft.border.all(width=2, color="#4ed3ff"),
                                                                                    border_radius=5,
                                                                                    padding=10,
                                                                                    shadow=ft.BoxShadow(
                                                                                        spread_radius=.5,
                                                                                        blur_radius=20,
                                                                                        color="#4ed3ff",
                                                                                        offset=ft.Offset(0, 0),
                                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                    ),
                                                                                    content=self.fruven
                                                                                ),
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Text("CREMAS", color="#ff1765", weight=ft.FontWeight.BOLD, size=25, style=ft.TextStyle(letter_spacing=7)),
                                                                                ft.Container(# Crema total vendida (botes)
                                                                                    alignment=ft.alignment.center,
                                                                                    border=ft.border.all(width=2, color="#4ed3ff"),
                                                                                    border_radius=5,
                                                                                    padding=10,
                                                                                    shadow=ft.BoxShadow(
                                                                                        spread_radius=.5,
                                                                                        blur_radius=20,
                                                                                        color="#4ed3ff",
                                                                                        offset=ft.Offset(0, 0),
                                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                    ),
                                                                                    content=self.creven
                                                                                ),
                                                                            ]
                                                                        )
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                ),
                                            ),
                                            # ft.Container(
                                            #     expand=True,
                                            #     # bgcolor="green",
                                            #     content=ft.ResponsiveRow(# CREMAS
                                            #         alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                            #         controls=[
                                            #              ft.Container(
                                            #                 col=4,
                                            #                 expand=True,
                                            #                 alignment=ft.alignment.center,
                                            #                 # bgcolor="#292929",
                                            #                 bgcolor="#B2E7FF",
                                            #                 border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                            #                 border_radius=5,
                                            #                 padding=ft.Padding(top=20, bottom=20, left=0, right=0),
                                            #                 margin=ft.Margin(top=8, bottom=0, left=0, right=0),
                                            #                 content=ft.Column(
                                            #                     alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                     horizontal_alignment="center",
                                            #                     controls=[
                                            #                         ft.Text("CREMA ORIGINAL", color="#ff1765", weight=ft.FontWeight.BOLD, size=20, style=ft.TextStyle(letter_spacing=10)),
                                            #                         ft.Container(# Botes Dia
                                            #                             alignment=ft.alignment.center,
                                            #                             # bgcolor="pink",
                                            #                             content=ft.ResponsiveRow(
                                            #                                 alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                                 vertical_alignment="center",
                                            #                                 controls=[
                                            #                                     ft.Container(# Botes Iniciales
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.coi
                                            #                                     ),
                                            #                                     ft.Container(# Botes Finales
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cof
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cov
                                            #                                     ),
                                            #                                 ]
                                            #                             )
                                            #                         ),
                                            #                         ft.Container(# Venta Botes
                                            #                             alignment=ft.alignment.center,
                                            #                             # bgcolor="pink",
                                            #                             content=ft.ResponsiveRow(
                                            #                                 alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                                 vertical_alignment="center",
                                            #                                 controls=[
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.co1s
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.co2s
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.co3s
                                            #                                     ),
                                            #                                 ]
                                            #                             )
                                            #                         ),
                                            #                     ]
                                            #                 )
                                            #             ),
                                            #             ft.Container( # Crema Chocolate
                                            #                 col=4,
                                            #                 expand=True,
                                            #                 alignment=ft.alignment.center,
                                            #                 # bgcolor="#292929",
                                            #                 bgcolor="#B2E7FF",
                                            #                 border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                            #                 border_radius=5,
                                            #                 padding=ft.Padding(top=20, bottom=20, left=0, right=0),
                                            #                 margin=ft.Margin(top=8, bottom=0, left=4, right=4),
                                            #                 content=ft.Column(
                                            #                     alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                     horizontal_alignment="center",
                                            #                     controls=[
                                            #                         ft.Text("CREMA CHOCOLATE", color="#ff1765", weight=ft.FontWeight.BOLD, size=20, style=ft.TextStyle(letter_spacing=10)),
                                            #                         ft.Container(# Botes Dia
                                            #                             alignment=ft.alignment.center,
                                            #                             # bgcolor="pink",
                                            #                             content=ft.ResponsiveRow(
                                            #                                 alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                                 vertical_alignment="center",
                                            #                                 controls=[
                                            #                                     ft.Container(# Botes Iniciales
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cchi
                                            #                                     ),
                                            #                                     ft.Container(# Botes Finales
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cchf
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cchv
                                            #                                     ),
                                            #                                 ]
                                            #                             )
                                            #                         ),
                                            #                         ft.Container(# Venta Botes
                                            #                             alignment=ft.alignment.center,
                                            #                             # bgcolor="pink",
                                            #                             content=ft.ResponsiveRow(
                                            #                                 alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                                 vertical_alignment="center",
                                            #                                 controls=[
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cch1s
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cch2s
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cch3s
                                            #                                     ),
                                            #                                 ]
                                            #                             )
                                            #                         ),
                                            #                     ]
                                            #                 )
                                            #             ),
                                            #             ft.Container(
                                            #                 col=4,
                                            #                 expand=True,
                                            #                 alignment=ft.alignment.center,
                                            #                 # bgcolor="#292929",
                                            #                 bgcolor="#B2E7FF",
                                            #                 border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                            #                 border_radius=5,
                                            #                 padding=ft.Padding(top=20, bottom=20, left=0, right=0),
                                            #                 margin=ft.Margin(top=8, bottom=0, left=0, right=0),
                                            #                 content=ft.Column(
                                            #                     alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                     horizontal_alignment="center",
                                            #                     controls=[
                                            #                         ft.Text("CREMA CAFE", color="#ff1765", weight=ft.FontWeight.BOLD, size=20, style=ft.TextStyle(letter_spacing=10)),
                                            #                         ft.Container(# Botes Dia
                                            #                             alignment=ft.alignment.center,
                                            #                             # bgcolor="pink",
                                            #                             content=ft.ResponsiveRow(
                                            #                                 alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                                 vertical_alignment="center",
                                            #                                 controls=[
                                            #                                     ft.Container(# Botes Iniciales
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.ccai
                                            #                                     ),
                                            #                                     ft.Container(# Botes Finales
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.ccaf
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=4,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.ccav
                                            #                                     ),
                                            #                                 ]
                                            #                             )
                                            #                         ),
                                            #                         ft.Container(# Venta Botes
                                            #                             alignment=ft.alignment.center,
                                            #                             # bgcolor="pink",
                                            #                             content=ft.ResponsiveRow(
                                            #                                 alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            #                                 vertical_alignment="center",
                                            #                                 controls=[
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cca1s
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                        content=self.cca2s
                                            #                                     ),
                                            #                                     ft.Container(
                                            #                                         alignment=ft.alignment.center,
                                            #                                         col=3.5,
                                            #                                         # bgcolor="yellow",
                                            #                                         content=self.cca3s
                                            #                                     ),
                                            #                                 ]
                                            #                             )
                                            #                         ),
                                            #                     ]
                                            #                 )
                                            #             ),
                                            #         ]
                                            #     )
                                            # ),
                                        ]
                                    )
                                )
                            ),
                            ft.Tab(# EXTRAS Y ADICIONALES
                                text="Extras",
                                content=ft.Container(
                                    margin=ft.Margin(top=20, bottom=20, left=30, right=30),
                                    alignment=ft.alignment.center,
                                    # bgcolor="red",
                                    # border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                    # border_radius=5,
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.alignment.center,
                                        controls=[
                                            ft.ResponsiveRow(
                                                expand=35,
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                vertical_alignment=ft.alignment.center,
                                                controls=[
                                                    ft.Container(# Toppings
                                                        col=6,
                                                        padding=ft.padding.symmetric(horizontal=30, vertical=5),
                                                        alignment=ft.alignment.center,
                                                        bgcolor="#B2E7FF",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    margin=ft.margin.symmetric(horizontal=0, vertical=5),
                                                                    alignment=ft.alignment.center,
                                                                    content=ft.Text("TOPPINGS EXTRAS", size=18, style=ft.TextStyle(letter_spacing=5))
                                                                ),
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            col=4,
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            height=40,
                                                                            content=ft.Text("$5", size=16),
                                                                        ),
                                                                        ft.Container(
                                                                            col=4,
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            height=40,
                                                                            content=ft.Text("$10", size=16),
                                                                        ),
                                                                        ft.Container(
                                                                            col=4,
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            height=40,
                                                                            content=ft.Text("TOTAL", size=16),
                                                                        ),
                                                                        
                                                                    ]
                                                                ),
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            col=2.5,
                                                                            content=self.t5
                                                                        ),
                                                                        ft.Container(
                                                                            col=2.5,
                                                                            content=self.t10
                                                                        ),
                                                                        ft.Container(
                                                                            col=2.5,
                                                                            content=self.tet
                                                                        ),
                                                                    ]
                                                                ),
                                                                # ft.ResponsiveRow(
                                                                #     controls=[
                                                                        
                                                                #         ft.Container(
                                                                #             col=1,
                                                                #             alignment=ft.alignment.center_right,
                                                                #             # bgcolor="blue",
                                                                #             height=40,
                                                                #             content=ft.Text("$", size=16),
                                                                #         ),
                                                                #     ]
                                                                # ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Servicios a domicilio
                                                        col=6,
                                                        padding=ft.padding.symmetric(horizontal=30, vertical=5),
                                                        alignment=ft.alignment.center,
                                                        bgcolor="#B2E7FF",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    margin=ft.margin.symmetric(horizontal=0, vertical=5),
                                                                    alignment=ft.alignment.center,
                                                                    content=ft.Text("SERVICIOS A DOMICILIO", size=18, style=ft.TextStyle(letter_spacing=5))
                                                                ),
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            col=4,
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            height=40,
                                                                            content=ft.Text("$20", size=16),
                                                                        ),
                                                                        ft.Container(
                                                                            col=4,
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            height=40,
                                                                            content=ft.Text("$35", size=16),
                                                                        ),
                                                                        ft.Container(
                                                                            col=4,
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            height=40,
                                                                            content=ft.Text("TOTAL", size=16),
                                                                        ),
                                                                        
                                                                    ]
                                                                ),
                                                                ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            col=2.5,
                                                                            content=self.sd20
                                                                        ),
                                                                        ft.Container(
                                                                            col=2.5,
                                                                            content=self.sd35
                                                                        ),
                                                                        ft.Container(
                                                                            col=2.5,
                                                                            content=self.sdt
                                                                        ),
                                                                    ]
                                                                ),
                                                                # ft.ResponsiveRow(
                                                                #     controls=[
                                                                        
                                                                #         ft.Container(
                                                                #             col=1,
                                                                #             alignment=ft.alignment.center_right,
                                                                #             # bgcolor="blue",
                                                                #             height=40,
                                                                #             content=ft.Text("$", size=16),
                                                                #         ),
                                                                #     ]
                                                                # ),
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            ),
                                            ft.ResponsiveRow(
                                                expand=65,
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                vertical_alignment=ft.alignment.center,
                                                controls=[
                                                    ft.Container(# Transferencias
                                                        col=6,
                                                        padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                                        alignment=ft.alignment.center,
                                                        bgcolor="#B2E7FF",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    alignment=ft.alignment.center,
                                                                    content=ft.Text("TRANSFERENCIAS", size=18, style=ft.TextStyle(letter_spacing=5))
                                                                ),
                                                                ft.ResponsiveRow(
                                                                    expand=True,
                                                                    controls=[
                                                                        ft.Container(
                                                                            col=12,
                                                                            # bgcolor="red",
                                                                            margin=ft.margin.only(right=10),
                                                                            alignment=ft.alignment.center,
                                                                            content=ft.ResponsiveRow(
                                                                                expand=True,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        col=5,
                                                                                        # bgcolor="blue",
                                                                                        padding=ft.padding.symmetric(horizontal=10, vertical=0),
                                                                                        content=ft.Column(
                                                                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    # bgcolor="blue",
                                                                                                    alignment=ft.alignment.center,
                                                                                                    content=ft.Column(
                                                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                                                        horizontal_alignment="center",
                                                                                                        controls=[
                                                                                                            ft.Container(
                                                                                                                # bgcolor="blue",
                                                                                                                content=ft.Text("NO. TRANSFERENCIAS"),
                                                                                                            ),
                                                                                                            ft.Container(
                                                                                                                content=self.trn
                                                                                                            ),
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    # bgcolor="blue",
                                                                                                    alignment=ft.alignment.center,
                                                                                                    content=ft.Column(
                                                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                                                        horizontal_alignment="center",
                                                                                                        controls=[
                                                                                                            ft.Container(
                                                                                                                # bgcolor="blue",
                                                                                                                content=ft.Text("TOTAL TRANSFERENCIAS"),
                                                                                                            ),
                                                                                                            ft.Row(
                                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                                vertical_alignment="center",
                                                                                                                controls=[
                                                                                                                    ft.Container(
                                                                                                                        content=self.trt
                                                                                                                    ),
                                                                                                                ]
                                                                                                            )
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(
                                                                                        col=7,
                                                                                        # bgcolor="blue",
                                                                                        padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                                                        content=ft.Column(
                                                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    # bgcolor=self.color_teal,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    border_radius=5,
                                                                                                    # padding=5,
                                                                                                    shadow=ft.BoxShadow(
                                                                                                        spread_radius=1,
                                                                                                        blur_radius=15,
                                                                                                        color=ft.Colors.BLUE_GREY_100,
                                                                                                        offset=ft.Offset(0, 0),
                                                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                                    ),
                                                                                                    content=ft.Column(
                                                                                                        spacing=0,
                                                                                                        controls=[
                                                                                                            ft.Container(
                                                                                                                expand=True,
                                                                                                                alignment=ft.alignment.center,
                                                                                                                padding=10,
                                                                                                                border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_900),
                                                                                                                border_radius=ft.border_radius.only(top_left=5, top_right=5),
                                                                                                                # bgcolor="blue",
                                                                                                                content=ft.ResponsiveRow(
                                                                                                                    expand=True,
                                                                                                                    # alignment=ft.MainAxisAlignment.CENTER,
                                                                                                                    # vertical_alignment=ft.alignment.center,
                                                                                                                    controls=[
                                                                                                                        ft.Container(
                                                                                                                            expand=True,
                                                                                                                            col=4,
                                                                                                                            alignment=ft.alignment.center,
                                                                                                                            # bgcolor="red",
                                                                                                                            content=ft.Column(
                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                                                horizontal_alignment="center",
                                                                                                                                controls=[
                                                                                                                                    self.tr1,
                                                                                                                                    self.tr4,
                                                                                                                                    self.tr7,
                                                                                                                                    self.tr10,
                                                                                                                                    self.tr13,
                                                                                                                                ]
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        ft.Container(
                                                                                                                            expand=True,
                                                                                                                            col=4,
                                                                                                                            alignment=ft.alignment.center,
                                                                                                                            # bgcolor="red",
                                                                                                                            content=ft.Column(
                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                                                horizontal_alignment="center",
                                                                                                                                controls=[
                                                                                                                                    self.tr2,
                                                                                                                                    self.tr5,
                                                                                                                                    self.tr8,
                                                                                                                                    self.tr11,
                                                                                                                                    self.tr14,
                                                                                                                                ]
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        ft.Container(
                                                                                                                            expand=True,
                                                                                                                            col=4,
                                                                                                                            alignment=ft.alignment.center,
                                                                                                                            # bgcolor="red",
                                                                                                                            content=ft.Column(
                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                                                horizontal_alignment="center",
                                                                                                                                controls=[
                                                                                                                                    self.tr3,
                                                                                                                                    self.tr6,
                                                                                                                                    self.tr9,
                                                                                                                                    self.tr12,
                                                                                                                                    self.tr15,
                                                                                                                                ]
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                )
                                                                                                            ),
                                                                                                            ft.Container(
                                                                                                                alignment=ft.alignment.center_right,
                                                                                                                padding=ft.Padding(top=5, right=10, bottom=0, left=0),
                                                                                                                # bgcolor="blue",
                                                                                                                bgcolor="#292929",
                                                                                                                content=ft.Text("M O N T O S     T R A N S F E R E N C I A S", size=10, italic=True, weight=ft.FontWeight.BOLD, color="white")
                                                                                                            )
                                                                                                        ]
                                                                                                    )
                                                                                                )
                                                                                            ]
                                                                                        )
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Gastos / Retiros
                                                        col=6,
                                                        alignment=ft.alignment.center,
                                                        padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                                        bgcolor="#B2E7FF",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    alignment=ft.alignment.center,
                                                                    content=ft.Text("GASTOS | RETIROS", size=16, style=ft.TextStyle(letter_spacing=5))
                                                                ),
                                                                ft.ResponsiveRow(
                                                                    expand=True,
                                                                    controls=[
                                                                        ft.Container(
                                                                            col=12,
                                                                            # bgcolor="red",
                                                                            margin=ft.margin.only(right=10),
                                                                            alignment=ft.alignment.center,
                                                                            content=ft.ResponsiveRow(
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        col=5,
                                                                                        # bgcolor="blue",
                                                                                        padding=ft.padding.symmetric(horizontal=10, vertical=0),
                                                                                        content=ft.Column(
                                                                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    # bgcolor="blue",
                                                                                                    alignment=ft.alignment.center,
                                                                                                    content=ft.Column(
                                                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                                                        horizontal_alignment="center",
                                                                                                        controls=[
                                                                                                            ft.Container(
                                                                                                                # bgcolor="blue",
                                                                                                                content=ft.Text("NO. GASTOS | RETIROS"),
                                                                                                            ),
                                                                                                            ft.Row(
                                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                                vertical_alignment="center",
                                                                                                                controls=[
                                                                                                                    ft.Container(
                                                                                                                        content=self.grn
                                                                                                                    ),
                                                                                                                ]
                                                                                                            )
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    # bgcolor="blue",
                                                                                                    alignment=ft.alignment.center,
                                                                                                    content=ft.Column(
                                                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                                                        horizontal_alignment="center",
                                                                                                        controls=[
                                                                                                            ft.Container(
                                                                                                                # bgcolor="blue",
                                                                                                                content=ft.Text("TOTAL GASTOS | RETIROS"),
                                                                                                            ),
                                                                                                            ft.Row(
                                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                                vertical_alignment="center",
                                                                                                                controls=[
                                                                                                                    ft.Container(
                                                                                                                        content=self.grt
                                                                                                                    ),
                                                                                                                ]
                                                                                                            )
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                            ]
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(
                                                                                        col=7,
                                                                                        # bgcolor="blue",
                                                                                        padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                                                        content=ft.Column(
                                                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    # bgcolor=self.color_teal,
                                                                                                    alignment=ft.alignment.center,
                                                                                                    border_radius=5,
                                                                                                    # padding=5,
                                                                                                    shadow=ft.BoxShadow(
                                                                                                        spread_radius=1,
                                                                                                        blur_radius=15,
                                                                                                        color=ft.Colors.BLUE_GREY_100,
                                                                                                        offset=ft.Offset(0, 0),
                                                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                                    ),
                                                                                                    content=ft.Column(
                                                                                                        spacing=0,
                                                                                                        controls=[
                                                                                                            ft.Container(
                                                                                                                expand=True,
                                                                                                                alignment=ft.alignment.center,
                                                                                                                padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                                                                                                border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_900),
                                                                                                                border_radius=ft.border_radius.only(top_left=5, top_right=5),
                                                                                                                # bgcolor="blue",
                                                                                                                # bgcolor="#292929",
                                                                                                                content=ft.ResponsiveRow(
                                                                                                                    expand=True,
                                                                                                                    spacing=0,
                                                                                                                    # alignment=ft.MainAxisAlignment.CENTER,
                                                                                                                    # vertical_alignment=ft.alignment.center,
                                                                                                                    controls=[
                                                                                                                        ft.Container(
                                                                                                                            expand=True,
                                                                                                                            col=1,
                                                                                                                            alignment=ft.alignment.center_right,
                                                                                                                            # bgcolor="red",
                                                                                                                            content=ft.Column(
                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                                                horizontal_alignment="center",
                                                                                                                                controls=[
                                                                                                                                    ft.Text("$", size=14, color="#000000"),
                                                                                                                                    ft.Text("$", size=14, color="#000000"),
                                                                                                                                    ft.Text("$", size=14, color="#000000"),
                                                                                                                                    ft.Text("$", size=14, color="#000000")
                                                                                                                                ]
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        ft.Container(
                                                                                                                            expand=True,
                                                                                                                            col=5,
                                                                                                                            alignment=ft.alignment.center,
                                                                                                                            # bgcolor="red",
                                                                                                                            content=ft.Column(
                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                                                horizontal_alignment="center",
                                                                                                                                controls=[
                                                                                                                                    self.gr1,
                                                                                                                                    self.gr3,
                                                                                                                                    self.gr5,
                                                                                                                                    self.gr7,
                                                                                                                                ]
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        ft.Container(
                                                                                                                            expand=True,
                                                                                                                            col=1,
                                                                                                                            alignment=ft.alignment.center_right,
                                                                                                                            # bgcolor="red",
                                                                                                                            content=ft.Column(
                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                                                horizontal_alignment="center",
                                                                                                                                controls=[
                                                                                                                                    ft.Text("$", size=14, color="#000000"),
                                                                                                                                    ft.Text("$", size=14, color="#000000"),
                                                                                                                                    ft.Text("$", size=14, color="#000000"),
                                                                                                                                    ft.Text("$", size=14, color="#000000")
                                                                                                                                ]
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        ft.Container(
                                                                                                                            expand=True,
                                                                                                                            col=5,
                                                                                                                            alignment=ft.alignment.center,
                                                                                                                            # bgcolor="red",
                                                                                                                            content=ft.Column(
                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                                                                horizontal_alignment="center",
                                                                                                                                controls=[
                                                                                                                                    self.gr2,
                                                                                                                                    self.gr4,
                                                                                                                                    self.gr6,
                                                                                                                                    self.gr8,
                                                                                                                                ]
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                )
                                                                                                            ),
                                                                                                            ft.Container(
                                                                                                                    alignment=ft.alignment.center_right,
                                                                                                                    padding=ft.Padding(top=5, right=10, bottom=0, left=0),
                                                                                                                    # bgcolor="blue",
                                                                                                                    bgcolor="#292929",
                                                                                                                    content=ft.Text("M O N T O S     G A S T O S   |   R E T I R O S", size=10, italic=True, weight=ft.FontWeight.BOLD, color="white")
                                                                                                                )
                                                                                                        ]
                                                                                                    )
                                                                                                )
                                                                                            ]
                                                                                        )
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            ),
                                        ]
                                    )
                                )
                            ),
                            ft.Tab(# BALANCE GENERAL
                                text="Balance General",
                                content=ft.Container(
                                    margin=ft.Margin(top=20, bottom=20, left=30, right=30),
                                    alignment=ft.alignment.center,
                                    # bgcolor="red",
                                    # border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                    # border_radius=5,
                                    content=ft.ResponsiveRow(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        vertical_alignment="center",
                                        controls=[
                                            # ft.Container(
                                            #     col=.5,
                                            #     alignment=ft.alignment.center,
                                            #     padding=ft.padding.symmetric(horizontal=2, vertical=15),
                                            #     bgcolor="#B2E7FF",
                                            #     border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                            #     border_radius=5,
                                            #     content=ft.Column(
                                            #         alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                            #         horizontal_alignment="center",
                                            #         controls=[
                                            #             ft.Text("B", size=13, weight="bold", italic=True),
                                            #             ft.Text("A", size=13, weight="bold", italic=True),
                                            #             ft.Text("L", size=13, weight="bold", italic=True),
                                            #             ft.Text("A", size=13, weight="bold", italic=True),
                                            #             ft.Text("N", size=13, weight="bold", italic=True),
                                            #             ft.Text("C", size=13, weight="bold", italic=True),
                                            #             ft.Text("E", size=13, weight="bold", italic=True),
                                            #             ft.Text("", size=15),
                                            #             ft.Text("G", size=13, weight="bold", italic=True),
                                            #             ft.Text("E", size=13, weight="bold", italic=True),
                                            #             ft.Text("N", size=13, weight="bold", italic=True),
                                            #             ft.Text("E", size=13, weight="bold", italic=True),
                                            #             ft.Text("R", size=13, weight="bold", italic=True),
                                            #             ft.Text("A", size=13, weight="bold", italic=True),
                                            #             ft.Text("L", size=13, weight="bold", italic=True),
                                            #         ]
                                            #     )
                                            # ),
                                            ft.Container(# Balance General
                                                col=4.85,
                                                alignment=ft.alignment.center,
                                                padding=ft.padding.symmetric(horizontal=0, vertical=10),
                                                bgcolor="#B2E7FF",
                                                border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                border_radius=5,
                                                content=ft.Column(
                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                    horizontal_alignment="center",
                                                    controls=[
                                                        # ft.Container(
                                                        #     alignment=ft.alignment.center,
                                                        #     content=ft.Text("BALANCE GENERAL", size=18, style=ft.TextStyle(letter_spacing=3.5))
                                                        # ),
                                                        ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            vertical_alignment="center",
                                                            controls=[
                                                                ft.Container(# Texto vertical
                                                                    col=1.2,
                                                                    padding=ft.padding.symmetric(horizontal=2, vertical=15),
                                                                    alignment=ft.alignment.center,
                                                                    margin=ft.margin.only(right=12, left=12),
                                                                    # margin=ft.margin.only(left=12),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                        horizontal_alignment="center",
                                                                        spacing=5,
                                                                        controls=[
                                                                            ft.Text("B", size=13, weight="bold", italic=True),
                                                                            ft.Text("A", size=13, weight="bold", italic=True),
                                                                            ft.Text("L", size=13, weight="bold", italic=True),
                                                                            ft.Text("A", size=13, weight="bold", italic=True),
                                                                            ft.Text("N", size=13, weight="bold", italic=True),
                                                                            ft.Text("C", size=13, weight="bold", italic=True),
                                                                            ft.Text("E", size=13, weight="bold", italic=True),
                                                                            ft.Text("", size=15),
                                                                            ft.Text("G", size=13, weight="bold", italic=True),
                                                                            ft.Text("E", size=13, weight="bold", italic=True),
                                                                            ft.Text("N", size=13, weight="bold", italic=True),
                                                                            ft.Text("E", size=13, weight="bold", italic=True),
                                                                            ft.Text("R", size=13, weight="bold", italic=True),
                                                                            ft.Text("A", size=13, weight="bold", italic=True),
                                                                            ft.Text("L", size=13, weight="bold", italic=True),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Separador
                                                                    col=.27,
                                                                    # bgcolor="#FF0000",
                                                                    # bgcolor="#01FF23",
                                                                    bgcolor="#FF7C01",
                                                                    width=1,
                                                                    height=400,
                                                                ),
                                                                ft.Container(# Campos totales y textos
                                                                    col=10,
                                                                    expand=True,
                                                                    # bgcolor="red",
                                                                    alignment=ft.alignment.center,
                                                                    padding=20,
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        horizontal_alignment="center",
                                                                        spacing=50,
                                                                        controls=[
                                                                            ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        col=4,
                                                                                        # bgcolor="blue",
                                                                                        alignment=ft.alignment.center_left,
                                                                                        height=40,
                                                                                        content=ft.Text("DEDUCCIONES", size=15),
                                                                                    ),
                                                                                    # ft.Container(
                                                                                    #     col=1,
                                                                                    #     # bgcolor="blue",
                                                                                    #     alignment=ft.alignment.center_right,
                                                                                    #     height=40,
                                                                                    #     content=ft.Text("$", size=20),
                                                                                    # ),
                                                                                    ft.Container(
                                                                                        col=5,
                                                                                        # bgcolor="blue",
                                                                                        alignment=ft.alignment.center,
                                                                                        content=self.bgegr
                                                                                    )
                                                                                ]
                                                                            ),
                                                                            ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        col=4,
                                                                                        alignment=ft.alignment.center_left,
                                                                                        # bgcolor="blue",
                                                                                        height=40,
                                                                                        content=ft.Text("EFECTIVO PDV", size=15),
                                                                                    ),
                                                                                    # ft.Container(
                                                                                    #     col=1,
                                                                                    #     alignment=ft.alignment.center_right,
                                                                                    #     # bgcolor="blue",
                                                                                    #     height=40,
                                                                                    #     content=ft.Text("$", size=20),
                                                                                    # ),
                                                                                    ft.Container(
                                                                                        col=5,
                                                                                        content=self.bgte
                                                                                    )
                                                                                ]
                                                                            ),
                                                                            ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        col=10,
                                                                                        expand=True,
                                                                                        # bgcolor="#222222",
                                                                                        border_radius=10,
                                                                                        border=ft.border.all(width=1, color="#4ed3ff"),
                                                                                        alignment=ft.alignment.center,
                                                                                        padding=10,
                                                                                        shadow=ft.BoxShadow(
                                                                                            spread_radius=.5,
                                                                                            blur_radius=20,
                                                                                            color="#4ed3ff",
                                                                                            offset=ft.Offset(0, 0),
                                                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                        ),
                                                                                        content=ft.Column(
                                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                            horizontal_alignment="center",
                                                                                            spacing=20,
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # bgcolor="blue",
                                                                                                    # height=50,
                                                                                                    content=ft.Column(
                                                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                        horizontal_alignment="center",
                                                                                                        # spacing=-3,
                                                                                                        controls=[
                                                                                                            ft.Text("VENTA TOTAL DEL DÍA", size=24, color="#fe0000", weight=ft.FontWeight.BOLD, italic=True),
                                                                                                            # ft.Text("DEL DÍA", size=22, color="#ff1765", weight=ft.FontWeight.BOLD),
                                                                                                        ]
                                                                                                    )
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    alignment=ft.alignment.center,
                                                                                                    # bgcolor="blue",
                                                                                                    content=self.bgtd
                                                                                                )
                                                                                            ]
                                                                                        )
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                                
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            ),
                                            ft.Column(# Campo de reporte de totales
                                                col=7.15,
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                horizontal_alignment="center",
                                                controls=[
                                                    ft.Container(
                                                        expand=75,
                                                        alignment=ft.alignment.center,
                                                        padding=ft.padding.symmetric(horizontal=8, vertical=8),
                                                        bgcolor="#B2E7FF",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        # content=self.report_field_totales
                                                        content=ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                            vertical_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    col=.5,
                                                                    # bgcolor="green",
                                                                    padding=ft.padding.symmetric(horizontal=2, vertical=15),
                                                                    alignment=ft.alignment.center_right,
                                                                    # margin=ft.margin.only(right=12),
                                                                    content=ft.Column(
                                                                        # col=.8,
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        horizontal_alignment="center",
                                                                        spacing=0,
                                                                        controls=[
                                                                            ft.Text("C", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("I", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("F", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("R", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("A", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("S", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("", size=12, color="black", weight="bold"),
                                                                            ft.Text("T", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("O", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("T", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("A", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("L", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("E", size=12, color="black", weight="bold", italic= True),
                                                                            ft.Text("S", size=12, color="black", weight="bold", italic= True),
                                                                        ]
                                                                    ),
                                                                ),
                                                                ft.Container(
                                                                    col=.35,
                                                                    # bgcolor="blue",
                                                                    alignment=ft.alignment.center_left,
                                                                    content=ft.Container(
                                                                        bgcolor="#FF7C01",
                                                                        width=1,
                                                                        height=300,
                                                                    )
                                                                ),
                                                                ft.Column(# Totales lado izquierdo
                                                                    col=6.5,
                                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                    horizontal_alignment="center",
                                                                    controls=[
                                                                        ft.Container(# Vasos
                                                                            expand=45,
                                                                            border=ft.border.all(width=1, color="#ff1c1c"),
                                                                            border_radius=10,
                                                                            # bgcolor="red",
                                                                            padding=2.5,
                                                                            content=ft.Column(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                horizontal_alignment="center",
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        expand=15,
                                                                                        bgcolor="#ff008c",
                                                                                        border_radius=8,
                                                                                        # padding=2,
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.Text("VASOS", size=13, color="white", weight=ft.FontWeight.BOLD, italic=True, style=ft.TextStyle(letter_spacing=5)),
                                                                                    ),
                                                                                    ft.ResponsiveRow(
                                                                                        expand=85,
                                                                                        spacing=0,
                                                                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                        vertical_alignment="center",
                                                                                        controls=[
                                                                                            ft.Container(# Totales por tamaño de vasos
                                                                                                col=6.5,
                                                                                                # bgcolor="yellow",
                                                                                                padding=5,
                                                                                                alignment=ft.alignment.center,
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                                    vertical_alignment="center",
                                                                                                    controls=[
                                                                                                        ft.Column(
                                                                                                            col=8,
                                                                                                            spacing=0,
                                                                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                            horizontal_alignment="center",
                                                                                                            controls=[
                                                                                                                ft.Text("CHICOS", size=12, color="black", weight="bold"),
                                                                                                                ft.Text("INDIVIDUALES", size=12, color="black", weight="bold"),
                                                                                                                ft.Text("MEDIANOS", size=12, color="black", weight="bold"),
                                                                                                                ft.Text("GRANDES", size=12, color="black", weight="bold"),
                                                                                                                ft.Text("MEGAS", size=12, color="black", weight="bold"),
                                                                                                            ]
                                                                                                        ),
                                                                                                        ft.Column(
                                                                                                            col=4,
                                                                                                            spacing=1.5,
                                                                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                            horizontal_alignment="center",
                                                                                                            controls=[
                                                                                                                self.total_vc,
                                                                                                                self.total_vi,
                                                                                                                self.total_vm,
                                                                                                                self.total_vg,
                                                                                                                self.total_vm,
                                                                                                            ]
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(
                                                                                                col=.5,
                                                                                                # bgcolor="blue",
                                                                                                padding=ft.padding.only(top=4),
                                                                                                alignment=ft.alignment.center,
                                                                                                content=ft.Container(
                                                                                                    bgcolor="#FF0101",
                                                                                                    width=.5,
                                                                                                    height=105,
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(# Totales de vasos en general
                                                                                                col=4.5,
                                                                                                alignment=ft.alignment.center,
                                                                                                padding=ft.padding.only(top=10),
                                                                                                # bgcolor="yellow",
                                                                                                content=ft.Column(
                                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                                    horizontal_alignment="center",
                                                                                                    spacing=-5,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # bgcolor="blue",
                                                                                                            content=ft.Column(
                                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                                horizontal_alignment="center",
                                                                                                                spacing=-2,
                                                                                                                controls=[
                                                                                                                    ft.Text("VASOS", size=15, color="black", weight="bold", italic=True),
                                                                                                                    ft.Text("TOTALES", size=15, color="black", weight="bold", italic=True)
                                                                                                                ]
                                                                                                            )
                                                                                                        ),
                                                                                                        # ft.Container(
                                                                                                        #     alignment=ft.alignment.center,
                                                                                                        #     # bgcolor="green",
                                                                                                        #     # padding=5,
                                                                                                        #     content=self.total_vasos
                                                                                                        # )
                                                                                                        self.total_vasos
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                        ]
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(# Frutas
                                                                            expand=23,
                                                                            border=ft.border.all(width=1, color="#ff1c1c"),
                                                                            border_radius=10,
                                                                            # bgcolor="red",
                                                                            padding=2.5,
                                                                            content=ft.Column(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                horizontal_alignment="center",
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        expand=28,
                                                                                        bgcolor="#ff008c",
                                                                                        border_radius=8,
                                                                                        # padding=2,
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.Text("FRUTA", size=13, color="white", weight=ft.FontWeight.BOLD, italic=True, style=ft.TextStyle(letter_spacing=5)),
                                                                                    ),
                                                                                    ft.ResponsiveRow(
                                                                                        expand=72,
                                                                                        spacing=0,
                                                                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                        vertical_alignment="center",
                                                                                        controls=[
                                                                                            ft.Container(# Totales de botes por fruta
                                                                                                col=4.5,
                                                                                                # bgcolor="yellow",
                                                                                                padding=5,
                                                                                                alignment=ft.alignment.center,
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                                    vertical_alignment="center",
                                                                                                    controls=[
                                                                                                        ft.Column(
                                                                                                            col=6,
                                                                                                            spacing=0,
                                                                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                            horizontal_alignment="center",
                                                                                                            controls=[
                                                                                                                ft.Text("FRESA", size=12, color="black", weight="bold"),
                                                                                                                ft.Text("UVA", size=12, color="black", weight="bold"),
                                                                                                            ]
                                                                                                        ),
                                                                                                        ft.Column(
                                                                                                            col=5.5,
                                                                                                            spacing=0,
                                                                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                            horizontal_alignment="center",
                                                                                                            controls=[
                                                                                                                self.total_fresa,
                                                                                                                self.total_uva,
                                                                                                            ]
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(
                                                                                                col=.5,
                                                                                                # bgcolor="blue",
                                                                                                padding=ft.padding.only(top=4),
                                                                                                alignment=ft.alignment.center,
                                                                                                content=ft.Container(
                                                                                                    bgcolor="#FF0101",
                                                                                                    width=.5,
                                                                                                    height=40,
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(# Totales de botes de fruta en general
                                                                                                col=7,
                                                                                                alignment=ft.alignment.center,
                                                                                                # bgcolor="yellow",
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                                    vertical_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            col=5,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            margin=ft.margin.only(left=5),
                                                                                                            # bgcolor="blue",
                                                                                                            content=ft.Column(
                                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                                horizontal_alignment="center",
                                                                                                                spacing=0,
                                                                                                                controls=[
                                                                                                                    ft.Text("BOTES", size=14, color="black", weight="bold", italic=True),
                                                                                                                    ft.Text("FRUTA", size=14, color="black", weight="bold", italic=True)
                                                                                                                ]
                                                                                                            )
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            col=7,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # bgcolor="blue",
                                                                                                            content=self.total_fruta
                                                                                                        )
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                        ]
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(# Cremas
                                                                            expand=32,
                                                                            border=ft.border.all(width=1, color="#ff1c1c"),
                                                                            border_radius=10,
                                                                            # bgcolor="red",
                                                                            padding=2.5,
                                                                            content=ft.Column(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                horizontal_alignment="center",
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        expand=20,
                                                                                        bgcolor="#ff008c",
                                                                                        border_radius=8,
                                                                                        # padding=2,
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.Text("CREMAS", size=13, color="white", weight=ft.FontWeight.BOLD, italic=True, style=ft.TextStyle(letter_spacing=5)),
                                                                                    ),
                                                                                    ft.ResponsiveRow(
                                                                                        expand=80,
                                                                                        spacing=0,
                                                                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                        vertical_alignment="center",
                                                                                        controls=[
                                                                                            ft.Container(# Totales por tamaño de vasos
                                                                                                col=5.5,
                                                                                                # bgcolor="yellow",
                                                                                                padding=5,
                                                                                                alignment=ft.alignment.center,
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                                    vertical_alignment="center",
                                                                                                    controls=[
                                                                                                        ft.Column(
                                                                                                            col=7,
                                                                                                            spacing=0,
                                                                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                            horizontal_alignment="center",
                                                                                                            controls=[
                                                                                                                ft.Text("ORIGINAL", size=12, color="black", weight="bold"),
                                                                                                                ft.Text("CHOCOLATE", size=12, color="black", weight="bold"),
                                                                                                                ft.Text("CAFE", size=12, color="black", weight="bold"),
                                                                                                            ]
                                                                                                        ),
                                                                                                        ft.Column(
                                                                                                            col=4.5,
                                                                                                            spacing=.4,
                                                                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                                            horizontal_alignment="center",
                                                                                                            controls=[
                                                                                                                self.total_or,
                                                                                                                self.total_ch,
                                                                                                                self.total_ca,
                                                                                                            ]
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(
                                                                                                col=.5,
                                                                                                # bgcolor="blue",
                                                                                                padding=ft.padding.only(top=2),
                                                                                                alignment=ft.alignment.center,
                                                                                                content=ft.Container(
                                                                                                    bgcolor="#FF0101",
                                                                                                    width=.5,
                                                                                                    height=65,
                                                                                                )
                                                                                            ),
                                                                                            ft.Container(# Totales de vasos en general
                                                                                                col=6,
                                                                                                alignment=ft.alignment.center,
                                                                                                # bgcolor="yellow",
                                                                                                content=ft.ResponsiveRow(
                                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                                    vertical_alignment="center",
                                                                                                    spacing=0,
                                                                                                    controls=[
                                                                                                        ft.Container(
                                                                                                            col=5,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # bgcolor="blue",
                                                                                                            content=ft.Column(
                                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                                horizontal_alignment="center",
                                                                                                                spacing=0,
                                                                                                                controls=[
                                                                                                                    ft.Text("BOTES", size=14, color="black", weight="bold", italic=True),
                                                                                                                    ft.Text("CREMAS", size=14, color="black", weight="bold", italic=True)
                                                                                                                ]
                                                                                                            )
                                                                                                        ),
                                                                                                        ft.Container(
                                                                                                            col=7,
                                                                                                            alignment=ft.alignment.center,
                                                                                                            # bgcolor="blue",
                                                                                                            content=self.total_cremas
                                                                                                        )
                                                                                                    ]
                                                                                                )
                                                                                            ),
                                                                                        ]
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                                ft.Column(# Totales lado derecho
                                                                    col=4.5,
                                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                    horizontal_alignment="center",
                                                                    controls=[
                                                                        ft.Container(# Toppings
                                                                            expand=30,
                                                                            bgcolor="red",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Total toppings por precio
                                                                                        col=7,
                                                                                        bgcolor="yellow",
                                                                                        
                                                                                    ),
                                                                                    ft.Container(# Total de toppings en general
                                                                                        col=5,
                                                                                        bgcolor="yellow",
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(# Servicios a domicilio
                                                                            expand=30,
                                                                            bgcolor="red",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Total de SD por precio
                                                                                        col=7,
                                                                                        bgcolor="yellow",
                                                                                    ),
                                                                                    ft.Container(# Total de SD en general
                                                                                        col=5,
                                                                                        bgcolor="yellow",
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(# Transferencias y Gastos | Retiros
                                                                            expand=40,
                                                                            bgcolor="red",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Transferencias
                                                                                        col=6,
                                                                                        bgcolor="yellow",
                                                                                    ),
                                                                                    ft.Container(# Gastos | Retiros
                                                                                        col=6,
                                                                                        bgcolor="yellow",
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Campo de validacion venta-consumo
                                                        expand=25,
                                                        alignment=ft.alignment.center,
                                                        padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                                        bgcolor="#B2E7FF",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        content=ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                            vertical_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    col=10,
                                                                ),
                                                                self.validation_vc
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        ]
                                    )
                                )
                            )
                        ]
                    ),

                ]
            )
        )

        #===================================#
        #     VENTANA SECCION DE VENTAS     #
        #===================================#

        self.sales = ft.Container(# VENTANA VENTAS
            col=12,
            bgcolor="#CFF4FF",
            border_radius=10,
            content=ft.Container(
                margin=3,
                # bgcolor="pink",
                content=ft.Column(
                    controls=[
                        ft.ResponsiveRow(
                            controls=[
                                ft.Column(# Titulo ventana
                                    col=12,
                                    horizontal_alignment="center",
                                    controls=[
                                        ft.Container(
                                            padding=ft.padding.only(top=10, bottom=4),
                                            # bgcolor="black",
                                            content=ft.Text("VENTAS Y REPORTES", size=30, color="#000000", weight=ft.FontWeight.BOLD)
                                        )
                                    ]
                                ),
                                ft.Divider(# Separador de seccion con Divider
                                    height=1,
                                    color="#ff1765",
                                    thickness=1,
                                    leading_indent=25,
                                    trailing_indent=25
                                ),
                            ]
                        ),
                        ft.Container(
                            margin=ft.margin.symmetric(horizontal=80, vertical=0),
                            # bgcolor="black",
                            expand=True,
                            content=ft.ResponsiveRow(
                                controls=[
                                    ft.Container(# Campo de texto para reportes
                                        padding=20,
                                        alignment=ft.alignment.center,
                                        # col=4.75,
                                        col=5.5,
                                        # bgcolor=self.color_teal,
                                        content=ft.Container(
                                            bgcolor="#C3F1FF",
                                            alignment=ft.alignment.center,
                                            border_radius=5,
                                            padding=1,
                                            shadow=ft.BoxShadow(
                                                spread_radius=1,
                                                blur_radius=15,
                                                # color=ft.Colors.BLUE_GREY_100,
                                                color=ft.Colors.BLUE_GREY_900,
                                                offset=ft.Offset(0, 0),
                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                            ),
                                            content=self.report_field
                                        )
                                    ),
                                    ft.Container(# Botones interactivos para archivos
                                        col=2,
                                        # bgcolor="black",
                                        alignment=ft.alignment.center,
                                        content=ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    padding=15,
                                                    content=self.calendary_sales
                                                ),
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    padding=15,
                                                    content=self.update_report
                                                ),
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    padding=15,
                                                    content=self.export_PDF
                                                ),
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    padding=15,
                                                    content=self.enable_edition
                                                ),
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    padding=15,
                                                    content=self.clean_Fields
                                                ),
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    padding=15,
                                                    content=self.delete_file
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(# Campo de texto para ventas
                                        padding=20,
                                        alignment=ft.alignment.center,
                                        col=4.5,
                                        # bgcolor=self.color_teal,
                                        content=ft.Container(
                                            bgcolor="#C3F1FF",
                                            alignment=ft.alignment.center,
                                            border_radius=5,
                                            padding=1,
                                            shadow=ft.BoxShadow(
                                                spread_radius=1,
                                                blur_radius=15,
                                                color=ft.Colors.BLUE_GREY_900,
                                                offset=ft.Offset(0, 0),
                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                            ),
                                            content= self.sales_field
                                        )
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )
        )

        #=========================================#
        #     VENTANA SECCION PUNTOS DE VENTA     #
        #=========================================#

        self.sp = ft.Container(# VENTANA PUNTOS DE VENTA
            expand=True,
            bgcolor="#CFF4FF",
            border_radius=10,
            content=ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment="center",
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment="center",
                            controls=[
                                ft.Text("Construcción en", size=25),
                                ft.Text("proceso...", size=25),
                                ft.Text("2%", size=20),
                                ft.Container(
                                    alignment=ft.alignment.center_left,
                                    bgcolor="#000000",
                                    width=200,
                                    height=2,
                                    content=ft.Container(
                                        bgcolor="#ff2525",
                                        width=5,
                                        height=2
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )

        #=======================================#
        #     VENTANA SECCION DE INVENTARIO     #
        #=======================================#

        self.stock = ft.Container(# VENTANA DE STOCK
            expand=True,
            bgcolor="#CFF4FF",
            border_radius=10,
            content=ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment="center",
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment="center",
                            controls=[
                                ft.Text("Construcción en", size=25),
                                ft.Text("proceso...", size=25),
                                ft.Text("2%", size=20),
                                ft.Container(
                                    alignment=ft.alignment.center_left,
                                    bgcolor="#000000",
                                    width=200,
                                    height=2,
                                    content=ft.Container(
                                        bgcolor="#ff2525",
                                        width=5,
                                        height=2
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )

        #========================#
        #     ARRAY VENTANAS     #
        #========================#

        # >>> Paginas de los respectivos elementos laterales encerrados en una lista para el control de estas con los elementos laterales

        # >>> Array de las ventanas / secciones para la asignación de cada una de estas con respecto a los iconos de la barra lateral izquierda, para su selección al hacer click en cada uno de los iconos.

        self.pages_containers = [self.home, ft.Column(controls=[self.select_Bar_Sucursales, self.register, self.actions_Buttons]), self.sales, self.sp, self.stock]

        #====================================================#
        #     ASIGNACION DE LA VENTANA INICIAL A MOSTRAR     #
        #====================================================#

        # >>> Seleccion de la pagina a mostrar mediante el index relacionado con el NavigationRail

        self.main_container = ft.Container(content=self.pages_containers[0], expand=True)

        #==============================================#
        #     CONTENEDOR PRINCIPAL DE LAS VENTANAS     #
        #==============================================#

        # >>> Variable principal encargada de almacenar las diferentes paginas relacionadas con los elementos laterales

        self.pages = ft.Container(
            col=11.25,
            # expand=True,
            content=ft.Column(
                controls=[
                    self.main_container,
                ]
            )
        )

        #=================================================#
        #     FILA PRINCIPAL INTERFAZ GRAFICA GENERAL     #
        #=================================================#
        
        # >>> FILA PRINCIPAL DE LA PAGINA (ABARCA TODA LA VENTANA Y ES DONDE SE PONE CADA UNA DE LAS SECCIONES QUE VAN A VERSE EN LA PAGINA)

        self.main_pages = ft.ResponsiveRow(
            controls=[
                self.navigation_bar,
                self.pages
            ]
        )

        self.controls.append(self.main_pages)

    """ 
    =========================================
    #         FIN INTERFAZ GRAFICA          #
    =========================================
    """

    # <<<<<<<<<<<<<<< DIVISOR DE SECCIONES >>>>>>>>>>>>>>> #

    """ 
    ==============================
    #         FUNCIONES          #
    ==============================
    """

    #============================================================#
    #     CAPTURA DE FECHA MEDIANTE CALENDARIO PARA REPORTES     #
    #============================================================#

    def change_date(self, e):
        date_to_report = e.control.value.strftime("%d-%m-%Y")
        self.date_receiver = date_to_report

    #=============================================================================#
    #     CAMBIO DE VENTANA MEDIANTE ICONOS DE LA BARRA LATERAL DE NAVEGACION     #
    #=============================================================================#

    def change_page(self, e):
        index = e.control.selected_index
        self.main_container.content = self.pages_containers[index]
        self.update()

    #=============================================================================#
    #     MANEJO DE LOS BOTONES DE TIPO RADIO PARA LA SELECCION DE SUCURSALES     #
    #=============================================================================#

    def pdv_selection(self, e):
        mapa = {
        "glorieta": "Suc. Glorieta",
        "sanmiguel": "Suc. San Miguel",
        "vips": "Suc. Vips",
        "cofradia2": "Suc. Cofradía 2",
        "ensueños": "Suc. Ensueños",
        "sanantonio": "Suc. San Antonio",
        }

        self.pdv_suc = mapa.get(e.control.value, "")

    #===================================================================================#
    #     CARGA DE INFORMACION REPORTE EN EL CAMPO DE TEXTO DE LA VENTANA DE VENTAS     #
    #===================================================================================#

    def show_report_tf(self, e):
        cr.generar_Reporte(self)
        self.update()

    #==============================================================#
    #     FUNCION CREADORA DEL REPORTE DEL DIA EN FORMATO PDF      #
    #==============================================================#

    def pdf_created(self, e):
        cr.create_ReportPDF(self)

    #========================================================================================#
    #     FUNCION PARA RESETEAR LOS CAMPOS DE TEXTO DEL PLANEADOR CON EL BOTON REINICIAR     #
    #========================================================================================#

    def reset_planeador(self, e):
        ba.reiniciar_Planeador(self)

    def planeador_lunes(self, e):
        ba.planeador_Lunes(self)

    def planeador_martes(self, e):
        ba.planeador_Martes(self)

    def planeador_miercoles(self, e):
        ba.planeador_Miercoles(self)

    def planeador_jueves(self, e):
        ba.planeador_Jueves(self)

    def planeador_viernes(self, e):
        ba.planeador_Viernes(self)

    def planeador_sabado(self, e):
        ba.planeador_Sabado(self)

    def planeador_domingo(self, e):
        ba.planeador_Domingo(self)

    """
    =========================================================
    #     MANEJO CAMPOS DE TEXTO DE LA SECCION DE VASOS     #
    =========================================================
    """

    #==================================================================#
    #     CONVERSION Y CAPTURA DEL TIPO DE DATO INGRESADO EN VASOS     #
    #==================================================================#

    # --- Vasos Chicos ---

    # ---> Conversion del tipo de dato a numero y suma de valores para el total
    def conversion_n_capture_vc(self, e):
        try:
            self.num_tci = int(self.tci.value)
            self.num_tcf = int(self.tcf.value)
        except Exception:
            # print("Campos de tapas chicas vacios o con valores NO numericos")
            pass

        self.values_types_comprobation_vc()
        
        try:
            self.vci.value = int(self.vci.value)
            self.vcf.value = int(self.vcf.value)
            self.vcven.value = self.vci.value - self.vcf.value
            self.vcvt.value = int(self.vcven.value * 50)
            self.vtv.value = self.vcven.value
            self.total_vasos.value = self.vtv.value
            self.vvmt.value = self.vcvt.value
            # self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            self.vtv.update()
            self.total_vasos.update()
            self.vvmt.update()
            # self.bging.update()
            self.bgtd.update()
            self.venta_totalVasos()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos chicos: ", ex)
            pass
        finally:
            self.update()
            self.balance_General(e)


    # ---> Comprobacion del tipo de valor en los campos
    def values_types_comprobation_vc(self):
        if self.vci.value == "" or self.vcf.value == "":
            self.vcven.value = ""
            self.vcvt.value = ""
            self.vcven.update()
            self.vcvt.update()
            if self.vcven.value == "":
                if type(self.viven.value) != str and type(self.vmven.value) != str and type(self.vgven.value) != str and type(self.vmgven.value) != str:
                    try:
                        self.vtv.value = self.viven.value + self.vmven.value + self.vgven.value + self.vmgven.value
                        self.total_vasos.value = self.vtv.value
                        self.vvmt.value = self.vivt.value + self.vmvt.value + self.vgvt.value + self.vmgvt.value
                        self.vtv.update()
                        self.total_vasos.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma de vasos individuales, medianos, grandes y megas totales - Error:", ex)
                    return
                elif type(self.viven.value) != str:
                    self.vtv.value = self.viven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vivt.value
                elif type(self.vmven.value) != str:
                    self.vtv.value = self.vmven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vmvt.value
                elif type(self.vgven.value) != str:
                    self.vtv.value = self.vgven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vgvt.value
                elif type(self.vmgven.value) != str:
                    self.vtv.value = self.vmgven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vmgvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
                self.total_vasos.update()
                self.vvmt.update()
            return

    # --- Vasos Individuales ---

    # ---> Conversion del tipo de dato a numero y suma de valores para el total
    def conversion_n_capture_vi(self, e):
        try:
            self.num_tii = int(self.tii.value)
            self.num_tif = int(self.tif.value)
        except Exception:
            # print("Campos de tapas chicas vacios o con valores NO numericos")
            pass

        self.values_types_comprobation_vi()
        
        try:
            self.vii.value = int(self.vii.value)
            self.vif.value = int(self.vif.value)
            self.viven.value = self.vii.value - self.vif.value
            self.vivt.value = int(self.viven.value * 75)
            self.vtv.value = self.viven.value
            self.total_vasos.value = self.vtv.value
            self.vvmt.value = self.vivt.value
            # self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            self.vtv.update()
            self.total_vasos.update()
            self.vvmt.update()
            # self.bging.update()
            self.bgtd.update()
            self.venta_totalVasos()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos individuales: ", ex)
            pass
        finally:
            self.update()
            self.balance_General(e)


    # ---> Comprobacion del tipo de valor en los campos
    def values_types_comprobation_vi(self):
        if self.vii.value == "" or self.vif.value == "":
            self.viven.value = ""
            self.vivt.value = ""
            self.viven.update()
            self.vivt.update()
            if self.viven.value == "":
                if type(self.vcven.value) != str and type(self.vmven.value) != str and type(self.vgven.value) != str and type(self.vmgven.value) != str:
                    try:
                        self.vtv.value = self.vcven.value + self.vmven.value + self.vgven.value + self.vmgven.value
                        self.total_vasos.value = self.vtv.value
                        self.vvmt.value = self.vcvt.value + self.vmvt.value + self.vgvt.value + self.vmgvt.value
                        self.vtv.update()
                        self.total_vasos.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma de vasos chicos, medianos, grandes y megas totales - Error:", ex)
                    return
                elif type(self.vcven.value) != str:
                    self.vtv.value = self.vcven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vcvt.value
                elif type(self.vmven.value) != str:
                    self.vtv.value = self.vmven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vmvt.value
                elif type(self.vgven.value) != str:
                    self.vtv.value = self.vgven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vgvt.value
                elif type(self.vmgven.value) != str:
                    self.vtv.value = self.vmgven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vmgvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
                self.total_vasos.update()
                self.vvmt.update()
            return

    # --- Vasos Medianos ---

    def conversion_n_capture_vm(self, e):
        try:
            self.num_tmi = int(self.tmi.value)
            self.num_tmf = int(self.tmf.value)
        except Exception:
            print("Campos de tapas medianas vacios o con valores NO numericos")
            pass

        self.values_types_comprobation_vm()
        
        try:
            self.vmi.value = int(self.vmi.value)
            self.vmf.value = int(self.vmf.value)
            self.vmven.value = self.vmi.value - self.vmf.value
            self.vmvt.value = int(self.vmven.value * 100)
            self.vtv.value = self.vmven.value
            self.total_vasos.value = self.vtv.value
            self.vvmt.value = self.vmvt.value
            # self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            self.vtv.update()
            self.total_vasos.update()
            self.vvmt.update()
            # self.bging.update()
            self.bgtd.update()
            self.venta_totalVasos()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos medianos: ", ex)
            pass
        finally:
            self.update()
            self.balance_General(e)

    # ---> Comprobacion del tipo de valor en los campos
    def values_types_comprobation_vm(self):
        if self.vmi.value == "" or self.vmf.value == "":
            self.vmven.value = ""
            self.vmvt.value = ""
            self.vmven.update()
            self.vmvt.update()
            if self.vmven.value == "":
                if type(self.vcven.value) != str and type(self.viven.value) != str and type(self.vgven.value) != str and type(self.vmgven.value) != str:
                    try:
                        self.vtv.value = self.vcven.value + self.viven.value + self.vgven.value + self.vmgven.value
                        self.total_vasos.value = self.vtv.value
                        self.vvmt.value = self.vcvt.value + self.vivt.value + self.vgvt.value + self.vmgvt.value
                        self.vtv.update()
                        self.total_vasos.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma de vasos chicos, individuales, grandes y megas totales - Error:", ex)
                    return
                elif type(self.vcven.value) != str:
                    self.vtv.value = self.vcven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vcvt.value
                elif type(self.viven.value) != str:
                    self.vtv.value = self.viven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vivt.value
                elif type(self.vgven.value) != str:
                    self.vtv.value = self.vgven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vgvt.value
                elif type(self.vmgven.value) != str:
                    self.vtv.value = self.vmgven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vmgvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
                self.total_vasos.update()
                self.vvmt.update()
            return

    # --- Vasos Grandes ---

    def conversion_n_capture_vg(self, e):
        try:
            self.num_tgi = int(self.tgi.value)
            self.num_tgf = int(self.tgf.value)
        except Exception:
            print("Campos de tapas grandes vacios o con valores NO numericos")
            pass

        self.values_types_comprobation_vg()
        
        try:
            self.vgi.value = int(self.vgi.value)
            self.vgf.value = int(self.vgf.value)
            self.vgven.value = self.vgi.value - self.vgf.value
            self.vgvt.value = int(self.vgven.value * 150)
            self.vtv.value = self.vgven.value
            self.total_vasos.value = self.vtv.value
            self.vvmt.value = self.vgvt.value
            # self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            self.vtv.update()
            self.total_vasos.update()
            self.vvmt.update()
            # self.bging.update()
            self.bgtd.update()
            self.venta_totalVasos()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos grandes: ", ex)
            pass
        finally:
            self.update()
            self.balance_General(e)

    # ---> Comprobacion del tipo de valor en los campos
    def values_types_comprobation_vg(self):
        if self.vgi.value == "" or self.vgf.value == "":
            self.vgven.value = ""
            self.vgvt.value = ""
            self.vgven.update()
            self.vgvt.update()
            if self.vgven.value == "":
                if type(self.vcven.value) != str and type(self.viven.value) != str and type(self.vmven.value) != str and type(self.vmgven.value) != str:
                    try:
                        self.vtv.value = self.vcven.value + self.viven.value + self.vmven.value + self.vmgven.value
                        self.total_vasos.value = self.vtv.value
                        self.vvmt.value = self.vcvt.value + self.vivt.value + self.vmvt.value + self.vmgvt.value
                        self.vtv.update()
                        self.total_vasos.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma de vasos chicos, individuales, medianos y megas totales - Error:", ex)
                    return
                elif type(self.vcven.value) != str:
                    self.vtv.value = self.vcven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vcvt.value
                elif type(self.viven.value) != str:
                    self.vtv.value = self.viven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vivt.value
                elif type(self.vmven.value) != str:
                    self.vtv.value = self.vmven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vmvt.value
                elif type(self.vmgven.value) != str:
                    self.vtv.value = self.vmgven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vmgvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
                self.total_vasos.update()
                self.vvmt.update()
            return

    # --- Vasos Megas ---

    def conversion_n_capture_vmg(self, e):
        try:
            self.num_tmgi = int(self.tmgi.value)
            self.num_tmgf = int(self.tmgf.value)
        except Exception:
            print("Campos de tapas grandes vacios o con valores NO numericos")
            pass

        self.values_types_comprobation_vmg()
        
        try:
            self.vmgi.value = int(self.vmgi.value)
            self.vmgf.value = int(self.vmgf.value)
            self.vmgven.value = self.vmgi.value - self.vmgf.value
            self.vmgvt.value = int(self.vmgven.value * 200)
            self.vtv.value = self.vmgven.value
            self.total_vasos.value = self.vtv.value
            self.vvmt.value = self.vmgvt.value
            # self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            self.vtv.update()
            self.total_vasos.update()
            self.vvmt.update()
            # self.bging.update()
            self.bgtd.update()
            self.venta_totalVasos()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos grandes: ", ex)
            pass
        finally:
            self.update()
            self.balance_General(e)

    # ---> Comprobacion del tipo de valor en los campos
    def values_types_comprobation_vmg(self):
        if self.vmgi.value == "" or self.vmgf.value == "":
            self.vmgven.value = ""
            self.vmgvt.value = ""
            self.vmgven.update()
            self.vmgvt.update()
            if self.vmgven.value == "":
                if type(self.vcven.value) != str and type(self.viven.value) != str and type(self.vmven.value) != str and type(self.vgven.value) != str:
                    try:
                        self.vtv.value = self.vcven.value + self.viven.value + self.vmven.value + self.vgven.value
                        self.total_vasos.value = self.vtv.value
                        self.vvmt.value = self.vcvt.value + self.vivt.value + self.vmvt.value + self.vgvt.value
                        self.vtv.update()
                        self.total_vasos.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma de vasos chicos, individuales, medianos y grandes - Error:", ex)
                    return
                elif type(self.vcven.value) != str:
                    self.vtv.value = self.vcven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vcvt.value
                elif type(self.viven.value) != str:
                    self.vtv.value = self.viven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vivt.value
                elif type(self.vmven.value) != str:
                    self.vtv.value = self.vmven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vmvt.value
                elif type(self.vgven.value) != str:
                    self.vtv.value = self.vgven.value
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.vgvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
                self.total_vasos.update()
                self.vvmt.update()
            return

    # --- Venta Total Vasos ---

    def venta_totalVasos(self):
        self.num_vtv = 0
        self.num_vvmt = 0

        # Bloques: verificar si hay al menos una cadena en cada grupo
        self.bloque_or_1 = (type(self.vcven.value) == str or type(self.viven.value) == str or type(self.vmven.value) == str or type(self.vgven.value) == str or type(self.vmgven.value) == str)
        self.bloque_or_2 = (type(self.vcvt.value) == str or type(self.vivt.value) == str or type(self.vmvt.value) == str or type(self.vgvt.value) == str or type(self.vmgvt.value) == str)

        # Caso 1: todos los valores son cadenas -> limpiar salidas
        if type(self.vcven.value) == str and type(self.viven.value) == str and type(self.vmven.value) == str and type(self.vgven.value) == str and type(self.vmgven.value) == str and type(self.vcvt.value) == str and type(self.vivt.value) == str and type(self.vmvt.value) == str and type(self.vgvt.value) == str and type(self.vmgvt.value) == str:
            self.vtv.value = ""
            self.vvmt.value = ""
            self.vtv.update()
            self.vvmt.update()

        # Caso 2: en ambos bloques hay al menos una cadena
        elif self.bloque_or_1 and self.bloque_or_2:
            self.values_bloque1 = [self.vcven.value, self.viven.value, self.vmven.value, self.vgven.value, self.vmgven.value]
            self.values_bloque2 = [self.vcvt.value, self.vivt.value, self.vmvt.value, self.vgvt.value, self.vmgvt.value]
            self.values_numericos_bloque1 = []
            self.values_numericos_bloque2 = []

            # Emparejar y filtrar solo si ambos no son str
            for e1, e2 in zip(self.values_bloque1, self.values_bloque2):
                if type(e1) != str and type(e2) != str:
                    self.values_numericos_bloque1.append(e1)
                    self.values_numericos_bloque2.append(e2)

            # Si hay entre 2 y 4 campos con valores numericos
            if (len(self.values_numericos_bloque1) >= 2) and (len(self.values_numericos_bloque2) >= 2) and (len(self.values_numericos_bloque1) < 5) and (len(self.values_numericos_bloque2) < 5):
                if (len(self.values_numericos_bloque1) == 2) and (len(self.values_numericos_bloque2) == 2):
                    self.values_numericos_1 = self.values_numericos_bloque1[0] + self.values_numericos_bloque1[1]
                    self.values_numericos_2 = self.values_numericos_bloque2[0] + self.values_numericos_bloque2[1]
                    self.vtv.value = self.values_numericos_1
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.values_numericos_2
                    # self.bging.value = self.vvmt.value
                    self.bgtd.value = self.vvmt.value
                    self.vtv.update()
                    self.total_vasos.update()
                    self.vvmt.update()
                    # self.bging.update()
                    self.bgtd.update()
                    self.update()
                elif (len(self.values_numericos_bloque1) == 3) and (len(self.values_numericos_bloque2) == 3):
                    self.values_numericos_1 = self.values_numericos_bloque1[0] + self.values_numericos_bloque1[1] + self.values_numericos_bloque1[2]
                    self.values_numericos_2 = self.values_numericos_bloque2[0] + self.values_numericos_bloque2[1] + self.values_numericos_bloque2[2]
                    self.vtv.value = self.values_numericos_1
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.values_numericos_2
                    # self.bging.value = self.vvmt.value
                    self.bgtd.value = self.vvmt.value
                    self.vtv.update()
                    self.total_vasos.update()
                    self.vvmt.update()
                    # self.bging.update()
                    self.bgtd.update()
                    self.update()
                elif (len(self.values_numericos_bloque1) == 4) and (len(self.values_numericos_bloque2) == 4):
                    self.values_numericos_1 = self.values_numericos_bloque1[0] + self.values_numericos_bloque1[1] + self.values_numericos_bloque1[2] + self.values_numericos_bloque1[3]
                    self.values_numericos_2 = self.values_numericos_bloque2[0] + self.values_numericos_bloque2[1] + self.values_numericos_bloque2[2] + self.values_numericos_bloque2[3]
                    self.vtv.value = self.values_numericos_1
                    self.total_vasos.value = self.vtv.value
                    self.vvmt.value = self.values_numericos_2
                    # self.bging.value = self.vvmt.value
                    self.bgtd.value = self.vvmt.value
                    self.vtv.update()
                    self.total_vasos.update()
                    self.vvmt.update()
                    # self.bging.update()
                    self.bgtd.update()
                    self.update()

        # Caso general: intentar sumar todos los valores
        else:
            try:
                self.num_vtv = self.vcven.value + self.viven.value + self.vmven.value + self.vgven.value + self.vmgven.value
                self.num_vvmt = self.vcvt.value + self.vivt.value + self.vmvt.value + self.vgvt.value + self.vmgvt.value
                self.vtv.value = self.num_vtv
                self.total_vasos.value = self.vtv.value
                self.vvmt.value = self.num_vvmt
                # self.bging.value = self.vvmt.value
                self.bgtd.value = self.vvmt.value
                self.vtv.update()
                self.total_vasos.update()
                self.vvmt.update()
                # self.bging.update()
                self.bgtd.update()
                self.update()
            except Exception as ex:
                print("Error: ", ex)

    """
    ==================================================================
    #     MANEJO CAMPOS DE TEXTO DE LA SECCION DE FRUTA Y CREMAS     #
    ==================================================================
    """

    #==================================================================#
    #     CONVERSION Y CAPTURA DEL TIPO DE DATO INGRESADO EN FRUTA     #
    #==================================================================#

    def conversion_n_capture_fr(self, e):
        self.values_fr = [self.fi, self.f1s, self.f2s, self.f3s, self.f4s, self.ff]

        if all(vf.value == "" for vf in self.values_fr):
            self.fv.value = ""
            self.fv.update()
            if self.fv.value == "" and self.uv.value != "":
                self.fruven.value = self.uv.value
                self.total_fruta.value = self.fruven.value
                self.fruven.update()
                self.total.fruta.update()
            return

        self.supply_fr = [self.fi, self.f1s, self.f2s, self.f3s, self.f4s]
        self.float_arrayValues = []
        self.int_arrayValues = []
        self.float_values = 0
        self.int_values = 0

        for sf in self.supply_fr:
            if sf.value.strip() != "":
                if sf.value not in ("", "."):
                    try:
                        float_num = float(sf.value)
                        self.float_arrayValues.append(float_num)
                        self.float_values = self.float_values + float_num
                    except Exception as ex:
                        print("SF FLOAT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass
                else:
                    try:
                        int_num = int(sf.value)
                        self.int_arrayValues.append(int_num)
                        self.int_values = self.int_values + int_num
                    except Exception as ex:
                        print("SF INT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass

        self.total_supplyValues = self.float_values + self.int_values

        if self.ff.value != "":
            if self.ff.value not in ("", "."):
                try:
                    ff_val = float(self.ff.value) # convertir el valor a float
                    self.less_valuesFr = self.total_supplyValues - ff_val

                    # Si el valor es un entero (aunque esté en float, o muy, muy cerca de un entero (toleracion o epsilon), ej 5.0 o 4.9999999999898), convertira el numero a entero (5).
                    if abs(self.less_valuesFr - round(self.less_valuesFr)) < 1e-9: # Tolerancia (epsilon)
                        self.less_valuesFr = int(round(self.less_valuesFr))
                        self.fv.value = self.less_valuesFr
                        self.total_fresa.value = self.fv.value
                    else:
                        # Mostrar como máximo 2 decimales
                        self.fv.value = round(self.less_valuesFr, 2)
                        self.total_fresa.value = self.fv.value

                    self.fv.update()
                    self.total_fresa.update()
                    self.update()
                except Exception as ex:
                    ff_val = "" # por si acaso se mete algo raro
                    print("FF: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                    pass
            else:
                ff_val = "" # si está vacío o solo con ".", lo tratamos como 0
        else:
            self.fv.value = ""
            self.fv.update()
            self.update()

        self.fv.on_change(e)

    def conversion_n_capture_uva(self, e):
        self.values_uva = [self.ui, self.u1s, self.u2s, self.u3s, self.u4s, self.uf]

        if all(uf.value == "" for uf in self.values_uva):
            self.uv.value = ""
            self.uv.update()
            if self.uv.value == "" and self.fv.value != "":
                self.fruven.value = self.fv.value
                self.total_fruta.value = self.fruven.value
                self.fruven.update()
                self.total.fruta.update()
            return

        self.supply_uva = [self.ui, self.u1s, self.u2s, self.u3s, self.u4s]
        self.float_arrayValues = []
        self.int_arrayValues = []
        self.float_values = 0
        self.int_values = 0

        for su in self.supply_uva:
            if su.value.strip() != "":
                if su.value not in ("", "."):
                    try:
                        float_num = float(su.value)
                        self.float_arrayValues.append(float_num)
                        self.float_values = self.float_values + float_num
                    except Exception as ex:
                        print("SU FLOAT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass
                else:
                    try:
                        int_num = int(su.value)
                        self.int_arrayValues.append(int_num)
                        self.int_values = self.int_values + int_num
                    except Exception as ex:
                        print("SF INT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass

        self.total_supplyValues = self.float_values + self.int_values

        if self.uf.value != "":
            if self.uf.value not in ("", "."):
                try:
                    uf_val = float(self.uf.value) # Convertir el valor a float
                    self.less_valuesUva = self.total_supplyValues - uf_val

                    # Si el valor es un entero (aunque esté en float, o muy, muy cerca de un entero (toleracion o epsilon), ej 5.0 o 4.9999999999898), convertira el numero a entero (5).
                    if abs(self.less_valuesUva - round(self.less_valuesUva)) < 1e-9: # Tolerancia (epsilon)
                        self.less_valuesUva = int(round(self.less_valuesUva))
                        self.uv.value = self.less_valuesUva
                        self.total_uva.value = self.uv.value
                    else:
                        # Mostrar como máximo 2 decimales
                        self.uv.value = round(self.less_valuesUva, 2)
                        self.total_uva.value = self.uv.value

                    self.uv.update()
                    self.total_uva.update()
                    self.update()
                except Exception as ex:
                    uf_val = "" # por si acaso se mete algo raro
                    print("UF: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                    pass
            else:
                uf_val = "" # si está vacío o solo con ".", lo tratamos como 0
        else:
            self.uv.value = ""
            self.uv.update()
            self.update()

        self.uv.on_change(e)

    #===================================================#
    #     VALIDACION PARA EL TOTAL DE FRUTA VENDIDA     #
    #===================================================#

    # --- Fresa ---

    def values_Fresa(self, e):
        try:
            if self.fv.value != "":
                self.fruven.value = self.fv.value
                self.total_fruta.value = self.fruven.value

            self.venta_totalFruta()
            self.fruven.update()
            self.total_fruta.update()
        except Exception as ex:
            print("Error en funcion values_Fresa - Error:", ex)

        # print("validation_totales_bg fresa")
        # print("validation_totales_bg fresa")

    # --- Uva ---

    def values_Uva(self, e):
        try:
            if self.uv.value != "" and self.uv.value != "---":
                self.fruven.value = self.uv.value
                self.total_fruta.value = self.fruven.value

            self.venta_totalFruta()
            self.fruven.update()
            self.total_fruta.update()
        except Exception as ex:
            print("Error en funcion values_Uva - Error:", ex)

        # print("validation_totales_bg uva")
        # print("validation_totales_bg uva")

    #========================================================================#
    #     VENTA TOTAL FRUTA DESPUES DE LA VALIDACION DE DATOS INGRESADOS     #
    #========================================================================#

    def venta_totalFruta(self):
        self.num_fruven = 0
        if type(self.uv.value) == str:
            self.fruven.value = self.fv.value
            self.total_fruta.value = self.fruven.value
        elif type(self.fv.value) == str:
            self.fruven.value = self.uv.value
            self.total_fruta.value = self.fruven.value
        else:
            try:
                self.num_fruven = self.fv.value + self.uv.value

                if self.num_fruven % 2 == 0 or self.num_fruven % 2 == 1:
                    self.num_fruven = int(self.num_fruven)
                else:
                    self.num_fruven = round(self.num_fruven, 2)

                self.fruven.value = self.num_fruven
                self.total_fruta.value = self.fruven.value
                self.fruven.update()
                self.total_fruta.update()
            except Exception as ex:
                print("Error en funcion venta_totalFruta - Error:", ex)
                pass

    #===================================================================#
    #     CONVERSION Y CAPTURA DEL TIPO DE DATO INGRESADO EN CREMAS     #
    #===================================================================#

    def conversion_n_capture_co(self, e):
        self.values_co = [self.coi, self.co1s, self.co2s, self.co3s, self.cov]

        if all(co.value == "" for co in self.values_co):
            self.cov.value = ""
            self.cov.update()
            if self.cov.value == "" and self.cchv.value != "" and self.ccav.value != "":
                self.creven.value = self.cchv.value + self.ccav.value
                self.creven.update()
            elif self.cov.value == "" and self.cchv.value != "" and self.ccav.value == "":
                self.creven.value = self.cchv.value
                self.creven.update()
            else:
                self.creven.value = self.ccav.value
                self.creven.update()
            return

        self.supply_co = [self.coi, self.co1s, self.co2s, self.co3s]
        self.float_arrayValues = []
        self.int_arrayValues = []
        self.float_values = 0
        self.int_values = 0

        for sf in self.supply_co:
            if sf.value.strip() != "":
                if sf.value not in ("", "."):
                    try:
                        float_num = float(sf.value)
                        self.float_arrayValues.append(float_num)
                        self.float_values = self.float_values + float_num
                    except Exception as ex:
                        print("SF FLOAT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass
                else:
                    try:
                        int_num = int(sf.value)
                        self.int_arrayValues.append(int_num)
                        self.int_values = self.int_values + int_num
                    except Exception as ex:
                        print("SF INT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass

        self.total_supplyValues = self.float_values + self.int_values

        if self.cof.value != "":
            if self.cof.value not in ("", "."):
                try:
                    co_val = float(self.cof.value) # convertir el valor a float
                    self.less_valuesCo = self.total_supplyValues - co_val

                    # Si el valor es un entero (aunque esté en float, o muy, muy cerca de un entero (toleracion o epsilon), ej 5.0 o 4.9999999999898), convertira el numero a entero (5).
                    if abs(self.less_valuesCo - round(self.less_valuesCo)) < 1e-9: # Tolerancia (epsilon)
                        self.less_valuesCo = int(round(self.less_valuesCo))
                        self.cov.value = self.less_valuesCo
                    else:
                        # Mostrar como máximo 2 decimales
                        self.cov.value = round(self.less_valuesCo, 2)

                    self.cov.update()
                    self.update()
                except Exception as ex:
                    co_val = "" # por si acaso se mete algo raro
                    print("FF: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                    pass
            else:
                co_val = "" # si está vacío o solo con ".", lo tratamos como 0
        else:
            self.cov.value = ""
            self.cov.update()
            self.update()

        self.cov.on_change(e)

    def conversion_n_capture_cch(self, e):
        self.values_cch = [self.cchi, self.cch1s, self.cch2s, self.cch3s, self.cchv]

        if all(cch.value == "" for cch in self.values_cch):
            self.cchv.value = ""
            self.cchv.update()
            if self.cchv.value == "" and self.cov.value != "" and self.ccav.value != "":
                self.creven.value = self.cov.value + self.ccav.value
                self.creven.update()
            elif self.cchv.value == "" and self.cov.value != "" and self.ccav.value == "":
                self.creven.value = self.cov.value
                self.creven.update()
            else:
                self.creven.value = self.ccav.value
                self.creven.update()
            return

        self.supply_cch = [self.cchi, self.cch1s, self.cch2s, self.cch3s]
        self.float_arrayValues = []
        self.int_arrayValues = []
        self.float_values = 0
        self.int_values = 0

        for sf in self.supply_cch:
            if sf.value.strip() != "":
                if sf.value not in ("", "."):
                    try:
                        float_num = float(sf.value)
                        self.float_arrayValues.append(float_num)
                        self.float_values = self.float_values + float_num
                    except Exception as ex:
                        print("SF FLOAT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass
                else:
                    try:
                        int_num = int(sf.value)
                        self.int_arrayValues.append(int_num)
                        self.int_values = self.int_values + int_num
                    except Exception as ex:
                        print("SF INT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass

        self.total_supplyValues = self.float_values + self.int_values

        if self.cchf.value != "":
            if self.cchf.value not in ("", "."):
                try:
                    cch_val = float(self.cchf.value) # convertir el valor a float
                    self.less_valuesCch = self.total_supplyValues - cch_val

                    # Si el valor es un entero (aunque esté en float, o muy, muy cerca de un entero (toleracion o epsilon), ej 5.0 o 4.9999999999898), convertira el numero a entero (5).
                    if abs(self.less_valuesCch - round(self.less_valuesCch)) < 1e-9: # Tolerancia (epsilon)
                        self.less_valuesCch = int(round(self.less_valuesCch))
                        self.cchv.value = self.less_valuesCch
                    else:
                        # Mostrar como máximo 2 decimales
                        self.cchv.value = round(self.less_valuesCch, 2)

                    self.cchv.update()
                    self.update()
                except Exception as ex:
                    co_val = "" # por si acaso se mete algo raro
                    print("FF: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                    pass
            else:
                cch_val = "" # si está vacío o solo con ".", lo tratamos como 0
        else:
            self.cchv.value = ""
            self.cchv.update()
            self.update()

        self.cchv.on_change(e)

    def conversion_n_capture_cca(self, e):
        self.values_cca = [self.ccai, self.cca1s, self.cca2s, self.cca3s, self.ccav]

        if all(cca.value == "" for cca in self.values_cca):
            self.ccav.value = ""
            self.ccav.update()
            if self.ccav.value == "" and self.cov.value != "" and self.cchv.value != "":
                self.creven.value = self.cov.value + self.cchv.value
                self.creven.update()
            elif self.cchv.value == "" and self.cov.value != "" and self.ccav.value == "":
                self.creven.value = self.cov.value
                self.creven.update()
            else:
                self.creven.value = self.cchv.value
                self.creven.update()
            return

        self.supply_cca = [self.ccai, self.cca1s, self.cca2s, self.cca3s]
        self.float_arrayValues = []
        self.int_arrayValues = []
        self.float_values = 0
        self.int_values = 0

        for sf in self.supply_cca:
            if sf.value.strip() != "":
                if sf.value not in ("", "."):
                    try:
                        float_num = float(sf.value)
                        self.float_arrayValues.append(float_num)
                        self.float_values = self.float_values + float_num
                    except Exception as ex:
                        print("SF FLOAT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass
                else:
                    try:
                        int_num = int(sf.value)
                        self.int_arrayValues.append(int_num)
                        self.int_values = self.int_values + int_num
                    except Exception as ex:
                        print("SF INT EN ARRAY: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                        pass

        self.total_supplyValues = self.float_values + self.int_values

        if self.ccaf.value != "":
            if self.ccaf.value not in ("", "."):
                try:
                    cca_val = float(self.ccaf.value) # convertir el valor a float
                    self.less_valuesCca = self.total_supplyValues - cca_val

                    # Si el valor es un entero (aunque esté en float, o muy, muy cerca de un entero (toleracion o epsilon), ej 5.0 o 4.9999999999898), convertira el numero a entero (5).
                    if abs(self.less_valuesCca - round(self.less_valuesCca)) < 1e-9: # Tolerancia (epsilon)
                        self.less_valuesCca = int(round(self.less_valuesCca))
                        self.ccav.value = self.less_valuesCca
                    else:
                        # Mostrar como máximo 2 decimales
                        self.ccav.value = round(self.less_valuesCca, 2)

                    self.ccav.update()
                    self.update()
                except Exception as ex:
                    co_val = "" # por si acaso se mete algo raro
                    print("FF: Intento de conversion al momento de ingresar solo el punto (.): ", ex)
                    pass
            else:
                cca_val = "" # si está vacío o solo con ".", lo tratamos como 0
        else:
            self.ccav.value = ""
            self.ccav.update()
            self.update()

        self.ccav.on_change(e)

    #=================================================#c
    #     VALIDACION CAMPOS VENTA TOTAL DE CREMAS     #
    #=================================================#

    # --- Crema Original ---

    def values_cremaOriginal(self, e):
        try:
            if type(self.cov.value) != str:
                self.creven.value = self.cov.value

            self.venta_totalCrema()
            self.creven.update()
        except Exception as ex:
            print("Error en funcion values_cremaOriginal - Error: ", ex)

    # --- Crema Chocolate ---

    def values_cremaChocolate(self, e):
        try:
            if type(self.cchv.value) != str:
                self.creven.value = self.cchv.value

            self.venta_totalCrema()
            self.creven.update()
        except Exception as ex:
            print("Error en funcion values_cremaChocolate - Error: ", ex)

    # --- Crema Cafe ---

    def values_cremaCafe(self, e):
        try:
            if type(self.ccav.value) != str:
                self.creven.value = self.ccav.value

            self.venta_totalCrema()
            self.creven.update()
        except Exception as ex:
            print("Error en funcion values_cremaCafe - Error: ", ex)

    #=====================================#
    #     VENTA TOTAL BOTES DE CREMAS     #
    #=====================================#

    # --- Venta Total Cremas ---

    def venta_totalCrema(self):
        self.num_creven = 0

        if type(self.cov.value) == str and type(self.cchv.value) == str and type(self.ccav.value) == str:
            self.creven.value = ""
        elif type(self.cov.value) == str or type(self.cchv.value) == str or type(self.ccav.value) == str:
            self.valuesFields_cremasVendidas = [self.cov.value, self.cchv.value, self.ccav.value]
            self.values_cremasVendidas = []

            for e in self.valuesFields_cremasVendidas:
                if type(e) != str:
                    self.values_cremasVendidas.append(e)

            if len(self.values_cremasVendidas) == 2:
                self.valuesArray_cremasVendidas = self.values_cremasVendidas[0] + self.values_cremasVendidas[1]
                self.creven.value = self.valuesArray_cremasVendidas
                self.creven.update()
        else:
            try:
                self.num_creven = self.cov.value + self.cchv.value + self.ccav.value

                if self.num_creven % 2 == 0 or self.num_creven % 2 == 1:
                    self.num_creven = int(self.num_creven)
                else:
                    self.num_creven = round(self.num_creven, 2)

                self.creven.value = self.num_creven
                self.creven.update()
            except Exception as ex:
                print("Error en la funcion venta_totalCrema, No se pudieron sumar todos los campos - Error: ", ex)

    """
    ============================================================================
    #     MANEJO CAMPOS DE TEXTO DE LA SECCION DE EXTRAS Y BALANCE GENERAL     #
    ============================================================================
    """

    #==================================================================================#
    #     CONVERSION Y CAPTURA DEL TIPO DE DATO INGRESADO EN EXTRAS Y BALANCE GRAL     #
    #==================================================================================#

    #=========================#
    #     TOPPINGS EXTRAS     #
    #=========================#

    # ---> Validacion de los valores en los campos de toppings extras, conversion del tipo a numeros y sumas totales tanto de toppings extras como al balance general
    def validation_toppingsExtras(self, e):
        try:
            if self.t5.value != "" and self.t10.value != "":
                self.total_t5 = int(self.t5.value) * 5
                self.total_t10 = int(self.t10.value) * 10
                self.tet.value = self.total_t5 + self.total_t10
                # if self.bging.value != str:
                if self.bgtd.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    # self.bging.value = self.vvmt.value + self.tet.value
                    self.bgtd.value = self.vvmt.value + self.tet.value
                self.tet.update()
                # self.bging.update()
                self.bgtd.update()
            elif self.t5.value != "":
                self.tet.value = int(self.t5.value) * 5
                # if self.bging.value != str:
                if self.bgtd.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    # self.bging.value = self.vvmt.value + self.tet.value
                    self.bgtd.value = self.vvmt.value + self.tet.value
                self.tet.update()
                # self.bging.update()
                self.bgtd.update()
            elif self.t10.value != "":
                self.tet.value = int(self.t10.value) * 10
                # if self.bging.value != str:
                if self.bgtd.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    # self.bging.value = self.vvmt.value + self.tet.value
                    self.bgtd.value = self.vvmt.value + self.tet.value
                self.tet.update()
                # self.bging.update()
                self.bgtd.update()
            else:
                self.t5.value == "" and self.t10.value == ""
                self.tet.value = ""
                # self.bging.value = self.vvmt.value
                self.bgtd.value = self.vvmt.value
                self.tet.update()
                # self.bging.update()
                self.bgtd.update()
        except Exception as ex:
            print("Error en funcion de validacion y recalculamiento de te: ", ex)
            pass
        finally:
            self.validation_totales_extras()
            self.tet.on_change(e)
            self.update()

    #===============================#
    #     SERVICIOS A DOMICILIO     #
    #===============================#

    def validation_serviciosDomicilio(self, e):
        try:
            if self.sd20.value != "" and self.sd35.value != "":
                self.total_sd20 = int(self.sd20.value) * 20
                self.total_sd35 = int(self.sd35.value) * 35
                self.sdt.value = self.total_sd20 + self.total_sd35
                # if self.bging.value != str:
                if self.bgtd.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    # self.bging.value = self.vvmt.value + self.sdt.value
                    self.bgtd.value = self.vvmt.value + self.sdt.value
                self.sdt.update()
                # self.bging.update()
                self.bgtd.update()
            elif self.sd20.value != "":
                self.total_sd20 = int(self.sd20.value) * 20
                self.sdt.value = int(self.sd20.value) * 20
                # if self.bging.value != str:
                if self.bgtd.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    # self.bging.value = self.vvmt.value + self.sdt.value
                    self.bgtd.value = self.vvmt.value + self.sdt.value
                self.sdt.update()
                # self.bging.update()
                self.bgtd.update()
            elif self.sd35.value != "":
                self.total_sd35 = int(self.sd35.value) * 35
                self.sdt.value = int(self.sd35.value) * 35
                # if self.bging.value != str:
                if self.bgtd.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    self.bging.value = self.vvmt.value + self.sdt.value
                    self.bgtd.value = self.vvmt.value + self.sdt.value
                self.sdt.update()
                # self.bging.update()
                self.bgtd.update()
            else:
                self.sd20.value == "" and self.sd35.value == ""
                self.total_sd20 = ""
                self.total_sd35 = ""
                self.sdt.value = ""
                # self.bging.value = self.vvmt.value
                self.bgtd.value = self.vvmt.value
                self.sdt.update()
                # self.bging.update()
                self.bgtd.update()
        except Exception as ex:
            print("Error en funcion de validacion y recalculamiento de sd: ", ex)
            pass
        finally:
            self.validation_totales_extras()
            self.sdt.on_change(e)
            self.update()

    def validation_totales_extras(self):
        if self.tet.value and self.sdt.value:
            # self.bging.value = self.vvmt.value + self.tet.value + self.sdt.value
            self.bgtd.value = self.vvmt.value + self.tet.value + self.sdt.value
            # self.bging.update()
            self.bgtd.update()
        elif self.tet.value == "" and self.sdt.value != "":
            # self.bging.value = self.vvmt.value + self.sdt.value
            self.bgtd.value = self.vvmt.value + self.sdt.value
            # self.bging.update()
            self.bgtd.update()
        elif self.tet.value != "" and self.sdt.value == "":
            # self.bging.value = self.vvmt.value + self.tet.value
            self.bgtd.value = self.vvmt.value + self.tet.value
            # self.bging.update()
            self.bgtd.update()
        else:
            # self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            # self.bging.update()
            self.bgtd.update()
            
    #====================================#
    #     SUMA MONTOS TRANSFERENCIAS     #
    #====================================#

    def plus_trans(self, e):
        self.transfers = [self.tr1, self.tr2, self.tr3, self.tr4, self.tr5, self.tr6, self.tr7, self.tr8, self.tr9, self.tr10, self.tr11, self.tr12, self.tr13, self.tr14, self.tr15]

        if all(tr.value == "" for tr in self.transfers):
            self.trt.value = ""
            self.trn.value = ""
            self.trn.update()
            self.trt.update()
        
        self.total_transfers = 0
        self.total_numTransfers = 0

        for tr in self.transfers:
            if tr.value.strip() != "":
                self.total_numTransfers = self.total_numTransfers + 1
                self.total_transfers = self.total_transfers + int(tr.value)
                self.trn.value = self.total_numTransfers
                self.trt.value = self.total_transfers
                self.trn.update()
                self.trt.update()
                # self.bging.update()
        
        self.trt.on_change(e)
        self.update()

    #======================================#
    #     SUMA MONTOS GASTOS | RETIROS     #
    #======================================#

    def plus_gasRes(self, e):
        self.gasret = [self.gr1, self.gr2, self.gr3, self.gr4, self.gr5, self.gr6, self.gr7, self.gr8]

        if all(gr.value == "" for gr in self.gasret):
            self.grt.value = ""
            self.grn.value = ""
            self.grn.update()
            self.grt.update()
        
        self.total_gasret = 0
        self.total_numGasret = 0

        for gr in self.gasret:
            if gr.value.strip() != "":
                self.total_numGasret = self.total_numGasret + 1
                self.total_gasret = self.total_gasret + int(gr.value)
                self.grn.value = self.total_numGasret
                self.grt.value = self.total_gasret
                self.grn.update()
                self.grt.update()

        self.grt.on_change(e)
        self.update()

    #=========================#
    #     BALANCE GENERAL     #
    #=========================#

    def balance_General(self, e):
        if self.grt.value == "" and self.trt.value == "":
            self.bgegr.value = ""
            self.bgte.value = self.bgtd.value
            self.bgegr.update()
            self.bgte.update()
            # self.trt.on_change(e)
            self.update()
        elif self.grt.value == "" and self.trt.value != "":
            self.bgegr.value = self.trt.value
            self.bgte.value = int(self.bgtd.value) - int(self.bgegr.value)
            # self.bging.value = int(self.bgtd.value) - int(self.bgegr.value)
            # self.efectivo_PDV(e)
            # self.bging.update()            
            self.bgegr.update()
            self.bgtd.update()
            self.bgte.update()
            # self.trt.on_change(e)
            self.update()
        elif self.grt.value != "" and self.trt.value == "":
            self.bgegr.value = self.grt.value
            self.bgte.value = int(self.bgtd.value) - int(self.bgegr.value)
            self.bgegr.update()
            self.bgte.update()
            self.update()
        else:
            self.bgegr.value = int(self.trt.value) + int(self.grt.value)
            self.bgte.value = int(self.bgtd.value) - int(self.bgegr.value)
            # self.bging.value = int(self.grt.value) + int(self.bgte.value)
            self.bgegr.update()
            self.bgtd.update()
            self.bgte.update()
            self.update()

        # self.bging.update()
        self.bgegr.update()
        self.bgtd.update()
        self.bgte.update()
        self.update()

    # def efectivo_PDV(self, e):
    #     efectivoPDV = int(self.bging.value) - int(self.trt.value)
    #     self.bging.value = efectivoPDV
    #     self.bging.update()
    #     self.trt.on_change(e)

    """
    =====================================================================
    #     ELIMINACION DE VALORES Y CONTENIDO DE LOS CAMPOS DE TEXTO     #
    =====================================================================
    """

    #===============================================================#
    #     RESET DE TODOS LOS TEXT FIELDS DE LA VENTANA REGISTRO     #
    #===============================================================#

    def reset_Fields(self, e):
        self.variables_vc = [self.tci, self.tcf, self.vci, self.vcf, self.vcven, self.vcvt]
        for element in self.variables_vc:
            element.value = ""

        self.variables_vi = [self.tii, self.tif, self.vii, self.vif, self.viven, self.vivt]
        for element in self.variables_vi:
            element.value = ""

        self.variables_vm = [self.tmi, self.tmf, self.vmi, self.vmf, self.vmven, self.vmvt]
        for element in self.variables_vm:
            element.value = ""

        self.variables_vg = [self.tgi, self.tgf, self.vgi, self.vgf, self.vgven, self.vgvt]
        for element in self.variables_vg:
            element.value = ""

        self.variables_vmg = [self.tmgi, self.tmgf, self.vmgi, self.vmgf, self.vmgven, self.vmgvt]
        for element in self.variables_vmg:
            element.value = ""

        self.variables_frutas = [self.fi, self.f1s, self.f2s, self.f3s, self.f4s, self.ff, self.fv, self.ui, self.u1s, self.u2s, self.u3s, self.u4s, self.uf, self.uv]
        for element in self.variables_frutas:
            element.value = ""

        self.variables_cremas = [self.coi, self.cof, self.co1s, self.co2s, self.co3s, self.cov, self.cchi, self.cchf, self.cch1s, self.cch2s, self.cch3s, self.cchv, self.ccai, self.ccaf, self.cca1s, self.cca2s, self.cca3s, self.ccav]
        for element in self.variables_cremas:
            element.value = ""

        self.extras = [self.t5, self.t10, self.tet, self.sd20, self.sd35, self.sdt, self.trn, self.trt, self.tr1, self.tr2, self.tr3, self.tr4, self.tr5, self.tr6, self.tr7, self.tr8, self.tr9, self.tr10, self.tr11, self.tr12, self.tr13, self.tr14, self.tr15, self.grn, self.grt, self.gr1, self.gr2, self.gr3, self.gr4, self.gr5, self.gr6, self.gr7, self.gr8, self.bgegr, self.bgtd, self.bgte]
        for element in self.extras:
            element.value = ""

        self.variables_ventas = [self.fruven, self.creven, self.vtv, self.vvmt]
        for element in self.variables_ventas:
            element.value = ""

        self.encSuc.value = ""

        self.pdv.value = ""
        self.pdv_suc = ""

        self.pdv.update()
        self.update()

    #===============================================#
    #     HABILITAR EDICION EN CAMPO DE REPORTE     #
    #===============================================#

    def enable_Edition_Button(self, e):
        self.report_field.read_only = False
        self.report_field.update()

    #===========================#
    #     RESET TEXT FIELDS     #
    #===========================#

    def reset_textFields(self, e):
        self.report_field.value = ""
        self.sales_field.value = ""
        self.report_field.read_only = True
        self.update()

    """
    ================================
    #     FUNCION CONSTRUCTORA     #
    ================================
    """

    #======================================#
    #     MANEJO DE PAGINAS Y VENTANAS     #
    #======================================#

    # >>>NO ME QUEDA CLARO PARA QUE Y PORQUE SE HACE, TENGO QUE INVESTIGAR A FONDO

    def build(self):
        return self.main_pages

"""
=============================
#     FUNCION PRINCIPAL     #
=============================
"""

#==========================================#
#     CREACION DE LA VENTANA PRINCIPAL     #
#==========================================#

# >>> FUNCIÓN PRINCIPAL PARA CREAR LA VENTANA PRINCIPAL DEL PROGRAMA O APP CON ALGUNAS CONFIGURACIONES EN ELLA COMO ALINEACION EN HORIZONTAL, COLOR DE FONDO, MEDIDA MINIMA EN ALTO Y ANCHO, TEMA PREDETERMINADO Y TÍTULO

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.bgcolor = ft.Colors.BLUE_GREY_900
    page.bgcolor = "#C4C4C4"
    # page.window.min_height = 680
    # page.window.min_width = 920
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Control - Las Fresas con Crema's"
    page.window.maximized = True
    page.window.resizable = True
    page.window.icon = get_resource_path("assets/Images/icon_program_03.ico")
    # page.window_opacity = .95
    page.add(UI(page))

    """
    =============================
    #     FUNCION PRINCIPAL     #
    =============================
    """

    # initial_dialog = ft.CupertinoAlertDialog(
    #     title=ft.Text("Bienvenido Las Fresas con Crema's", italic=True, size=15),
    #     actions=[
    #         ft.CupertinoDialogAction("Cerrar", is_destructive_action=True, on_click=lambda e: (page.close(e.control.parent), page.update()))
    #     ]
    # )

    # page.open(initial_dialog)
    page.update()
    
# ***** Web Mode *****
# ft.app(target=main, view=ft.WEB_BROWSER)

# ***** Desktop Mode *****
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
ft.app(target=main)