import datetime as dt
import flet as ft
from fpdf import FPDF
import modules.create_Elements as ce
import modules.button_Actions as ba
import modules.create_Reports as cr
import asyncio


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

        self.mayus_weekend_day = dt.datetime.now().strftime("%a").upper()
        self.mayus_month = dt.datetime.now().strftime("%b").upper()
        self.today_1 = dt.datetime.today().date()
        self.today_2 = self.today_1.strftime(f"{self.mayus_weekend_day} %d°{self.mayus_month}°%Y")
        self.today_main = self.today_2

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
            icon_color="white",
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
            icon_color="white",
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

        self.sup_Pers_PDV = ce.create_textfield_planeador(hint_Text="Ivette Herrera", hint_Style=ft.TextStyle(color="black", size=12, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, italic=True, weight=ft.FontWeight.BOLD))
        self.sup_Ops = ce.create_textfield_planeador(hint_Text="Efrain Hernandez", hint_Style=ft.TextStyle(color="black", size=12, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, italic=True, weight=ft.FontWeight.BOLD))
        self.sup_CDO = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, italic=True, weight=ft.FontWeight.BOLD))

        #==================================#
        #     VARIABLES PERSONAL PDV'S     #
        #==================================#

        self.ven_Vips = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_SanMiguel = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_SanAntonio = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Ensuenos = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_LaPiedad = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Cofradia2 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Glorieta = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        # self.ven_Parques = ce.create_textfield_planeador(hint_Text="Omar", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        # self.ven_Cumbria = ce.create_textfield_planeador(hint_Text="Nahun", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        # self.ven_Palomas = ce.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        # self.ven_Colinas = ce.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))

        #======================================#
        #     VARIABLES OPERADORES DE RUTA     #
        #======================================#

        self.ruta1_1 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ruta1_2 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ruta1_3 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ruta2_1 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ruta2_2 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ruta2_3 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ruta_com = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))

        #=========================================#
        #     VARIABLES CENTRO DE OPERACIONES     #
        #=========================================#

        self.cdo_1 = ce.create_textfield_planeador(hint_Text="Danna", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.cdo_2 = ce.create_textfield_planeador(hint_Text="Berenice", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.cdo_3 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.cdo_4 = ce.create_textfield_planeador(hint_Text="", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))

        #==========================================#
        #     VARIABLES SECCION VENTAS MINIMAS     #
        #==========================================#

        self.vm_Vips = ce.create_textfield_planeador(hint_Text="$3,900", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.vm_SanMiguel = ce.create_textfield_planeador(hint_Text="$4,800", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.vm_SanAntonio = ce.create_textfield_planeador(hint_Text="$6,500", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.vm_Ensuenos = ce.create_textfield_planeador(hint_Text="$4,800", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.vm_Cofradia2 = ce.create_textfield_planeador(hint_Text="$3,900", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.vm_LaPiedad = ce.create_textfield_planeador(hint_Text="$3,900", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.vm_Glorieta = ce.create_textfield_planeador(hint_Text="$3,500", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        # self.vm_Parques = ce.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        # self.vm_Cumbria = ce.create_textfield_planeador(Value="$3,200", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        # self.vm_Palomas = ce.create_textfield_planeador(Value="$---", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        # self.vm_Colinas = ce.create_textfield_planeador(Value="$---", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))

        #=============================== ====#
        #     VARIABLES SECCION PROMEDIO     #
        #====================================#

        self.prom_Vips = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.prom_SanMiguel = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.prom_SanAntonio = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.prom_Ensuenos = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.prom_LaPiedad = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.prom_Cofradia2 = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.prom_Glorieta = ce.create_textfield_planeador(hint_Text="$0", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        # self.prom_Parques = ce.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        # self.prom_Cumbria = ce.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        # self.prom_Palomas = ce.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        # self.prom_Colinas = ce.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))

        #==============================#
        #     VARIABLES SUCURSALES     #
        #==============================#

        self.vips = ce.create_radio("vips", "Vips")
        self.sanmiguel = ce.create_radio("sanmiguel", "San Miguel")
        self.sanantonio = ce.create_radio("sanantonio", "San Antonio")
        self.ensuenos = ce.create_radio("ensueños", "Ensueños")
        self.lapiedad = ce.create_radio("lapiedad", "La Piedad")
        self.cofradia2 = ce.create_radio("cofradia2", "Cofradía 2")
        self.glorieta = ce.create_radio("glorieta", "Glorieta")
        # self.parques = ce.create_radio("parques", "Parques")
        # self.cumbria = ce.create_radio("cumbria", "Cumbria")
        # self.palomas = ce.create_radio("palomas", "Palomas")
        # self.colinas = ce.create_radio("atalanta", "Colinas")

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
                        self.lapiedad,
                        self.glorieta,
                        # self.cumbria,
                        # self.palomas,
                        # self.colinas,
                    ]
                )
            )
        )

        #=====================================================#
        #     VARIABLE BARRA PARA SELECCION DE SUCURSALES     #
        #=====================================================#

        self.select_Bar_Sucursales = ft.Container(# Puntos de venta
            alignment=ft.alignment.top_center,
            bgcolor=ft.Colors.BLUE_GREY_900,
            border_radius=10,
            content=ft.Column(
                horizontal_alignment="center",
                alignment="center",
                controls=[
                    self.pdv,
                ]
            )
        )

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
        self.vcven = ce.create_textfield(Label="Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="VASOS", suffix_Style=ft.TextStyle(color="#a2a2a2", size=10), focused_Border_Color="#08f5a9", read_Only=True)
        self.vcvt = ce.create_textfield(Label="Venta Total", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="MX", suffix_Style=ft.TextStyle(color="#a2a2a2", size=10), border_Color="#fd0000", focused_Border_Color="#08f5a9", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True, on_Change=self.values_types_comprobation_vc)

        #==================================#
        #     VARIABLES VASOS MEDIANOS     #
        #==================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tmi = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vm)
        self.tmf = ce.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vm)
        # self.tmdif = ce.create_textfield("Diferencia", read_Only=True)
        self.vmi = ce.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vm)
        self.vmf = ce.create_textfield("Finales", suffix_Text=" Vasos Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vm)
        # self.vmdif = ce.create_textfield("Diferencia", read_Only=True)
        # self.vmsv = ce.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vmven = ce.create_textfield(Label="Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="VASOS", suffix_Style=ft.TextStyle(color="#a2a2a2", size=10), focused_Border_Color="#08f5a9", read_Only=True)
        self.vmvt = ce.create_textfield(Label="Venta Total", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="MX", suffix_Style=ft.TextStyle(color="#a2a2a2", size=10), border_Color="#fd0000", focused_Border_Color="#08f5a9", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True, on_Change=self.values_types_comprobation_vm)

        #=================================#
        #     VARIABLES VASOS GRANDES    #
        #=================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tgi = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vg)
        self.tgf = ce.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vg)
        # self.tgdif = ce.create_textfield("Diferencia", read_Only=True)
        self.vgi = ce.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vg)
        self.vgf = ce.create_textfield("Finales", suffix_Text="Vasos Finales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vg)
        # self.vgdif = ce.create_textfield("Diferencia", read_Only=True)
        # self.vgsv = ce.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vgven = ce.create_textfield(Label="Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="VASOS", suffix_Style=ft.TextStyle(color="#a2a2a2", size=10), focused_Border_Color="#08f5a9", read_Only=True)
        self.vgvt = ce.create_textfield(Label="Venta Total", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="MX", suffix_Style=ft.TextStyle(color="#a2a2a2", size=10), border_Color="#fd0000", focused_Border_Color="#08f5a9", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True, on_Change=self.values_types_comprobation_vg)

        #=====================================#
        #     VARIABLES VENTA TOTAL VASOS     #
        #=====================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.vtv = ce.create_textfield_WB(Label="Vendidos", Color="#ffffff", text_Size=20, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", suffix_Text="Vasos ", read_Only=True)
        self.vvmt = ce.create_textfield_WB(Label="Venta Total", Color="#ffffff", text_Size=20, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=14), suffix_Text="MX ", read_Only=True)

        #==========================#
        #     VARIABLES FRUTAS     #
        #==========================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        # --- Fresa ---

        # self.tgi = ce.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=ce.Focus, on_Change=self.conversion_n_capture_vg)
        self.fpi = ce.create_textfield("Picada Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fpf = ce.create_textfield("Picada Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fei = ce.create_textfield("Entera Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fef = ce.create_textfield("Entera Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fv = ce.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", read_Only=True, on_Change=self.values_Fresa)
        # self.fr = ce.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

        # --- Uva ---

        self.upi = ce.create_textfield("Picada Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.upf = ce.create_textfield("Picada Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uei = ce.create_textfield("Entera Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uef = ce.create_textfield("Entera Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uv = ce.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", read_Only=True, on_Change=self.values_Uva)
        # self.ur = ce.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

        #==========================#
        #     VARIABLES CREMAS     #
        #==========================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        # --- Crema Original ---

        self.coi = ce.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.cof = ce.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.cov = ce.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaOriginal, read_Only=True)

        # --- Crema Chocolate ---

        self.cchi = ce.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_cch)
        self.cchf = ce.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_cch)
        self.cchv = ce.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaChocolate, read_Only=True)

        # --- Crema Cafe ---

        self.ccai = ce.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_cca)
        self.ccaf = ce.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_cca)
        self.ccav = ce.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaCafe, read_Only=True)

        #==========================================#
        #     VARIABLES FRUTA Y CREMA VENDIDAS     #
        #==========================================#

        # >>> Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.fruven = ce.create_textfield_WB(Label="Fruta", Height=30, Color="#ffffff", text_Size=24, border_Color="#292929", Width=150, border_Width=.3, focused_Border_Color="#292929", suffix_Text="Botes ", read_Only=True)
        self.creven = ce.create_textfield_WB(Label="Cremas", Height=30, Color="#ffffff", text_Size=24, border_Color="#292929", Width=150, border_Width=.3, focused_Border_Color="#292929", suffix_Text="Botes ", read_Only=True)

        #========================================#
        #     VARIABLES ADICIONALES Y EXTRAS     #
        #========================================#

        # >>> Opciones a configurar en la funcion create_textfield_Extras: Width, Height, Color="#d3d3d3", text_Size=12, border_Color=None, read_Only=False, on_Change=False

        # --- Toppings Extras ---

        self.t5 = ce.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.validation_toppingsExtras)
        self.t10 = ce.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.validation_toppingsExtras)
        self.tet = ce.create_textField_Extras(text_Size=18, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True, on_Change=self.balance_General)

        # --- Servicios a Domicilio ---

        self.sd20 = ce.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.validation_serviciosDomicilio)
        self.sd35 = ce.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.validation_serviciosDomicilio)
        self.sdt = ce.create_textField_Extras(text_Size=18, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True, on_Change=self.balance_General)

        self.total_t5 = ""
        self.total_t10 = ""
        self.total_sd20 = ""
        self.total_sd35 = ""

        # --- Transferencias ---

        self.trn = ce.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=60, Height=35, border_Color="white", read_Only=False)
        self.trt = ce.create_textField_Extras(text_Size=17, text_Style=None, Color="white", Width=100, Height=35, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#252121", prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=12), suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=False, on_Change=self.balance_General)
        
        self.tr1 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr2 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr3 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr4 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr5 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr6 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr7 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr8 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr9 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr10 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr11 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)
        self.tr12 = ce.create_textField_Extras(Value="", text_Size=11, Color="white", Width=60, Height=23, border_Color="white", cursor_Height=12, prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=7, vertical=0), read_Only=False, on_Change=self.plus_trans)

        # --- Gastos / Retiros ---

        self.grn = ce.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=60, Height=35, border_Color="white", read_Only=False)
        self.grt = ce.create_textField_Extras(text_Size=17, text_Style=None, Color="white", Width=100, Height=35, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#252121", prefix_Text="$", prefix_Style=ft.TextStyle(color="#ffffff", size=12), suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=False, on_Change=self.balance_General)
        self.bgtd = ce.create_textField_Extras(text_Size=20, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True)

        self.gr1 = ce.create_textField_Extras(Value="", text_Size=12, Color="white", Width=80, Height=25, border_Color="white", cursor_Height=12, read_Only=False, on_Change=self.plus_gasRes)
        self.gr2 = ce.create_textField_Extras(Value="", text_Size=12, Color="white", Width=80, Height=25, border_Color="white", cursor_Height=12, read_Only=False, on_Change=self.plus_gasRes)
        self.gr3 = ce.create_textField_Extras(Value="", text_Size=12, Color="white", Width=80, Height=25, border_Color="white", cursor_Height=12, read_Only=False, on_Change=self.plus_gasRes)
        self.gr4 = ce.create_textField_Extras(Value="", text_Size=12, Color="white", Width=80, Height=25, border_Color="white", cursor_Height=12, read_Only=False, on_Change=self.plus_gasRes)
        self.gr5 = ce.create_textField_Extras(Value="", text_Size=12, Color="white", Width=80, Height=25, border_Color="white", cursor_Height=12, read_Only=False, on_Change=self.plus_gasRes)
        self.gr6 = ce.create_textField_Extras(Value="", text_Size=12, Color="white", Width=80, Height=25, border_Color="white", cursor_Height=12, read_Only=False, on_Change=self.plus_gasRes)

        # --- Balance ---

        self.bging = ce.create_textField_Extras(text_Size=20, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True)
        self.bgegr = ce.create_textField_Extras(text_Size=20, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True)
        self.bgtd = ce.create_textField_Extras(text_Size=20, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True)
        self.bgte = ce.create_textField_Extras(text_Size=20, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", suffix_Text="MX ", suffix_Style=ft.TextStyle(color="#ffffff", size=10), content_Padding=ft.padding.symmetric(horizontal=5, vertical=0), read_Only=True)

        #========================================================================#
        #     VARIABLE BARRA BOTONES INFERIORES DE ACCIONES VENTANA REGISTRO     #
        #========================================================================#

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

        self.actions_Buttons = ft.Container(# Botones inferiores interactivos campos ventana registro
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.BLUE_GREY_900,
            border_radius=10,
            content=ft.ResponsiveRow(
                vertical_alignment="center",
                alignment="center",
                controls=[
                    ft.Container(# Calendary Button
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
                    ft.Container(# Report Button
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
                    ft.Container(# Preview Button
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
                                    ft.CupertinoAlertDialog(
                                        title=ft.Text(f"Reporte  {self.pdv}\n"),
                                        content=ft.Text(color="white", size=9, value=(
                                                f"--- VASOS CHICOS ---\n"
                                                f"   TI: {self.tci.value} | TP: {self.tcf.value} | VI: {self.vci.value} | VF: {self.vcf.value} | VV: {self.vcven.value} | VENTA: $ {self.vcvt.value}\n\n"
                                                f"--- VASOS MEDIANOS ---\n"
                                                f"   TI: {self.tmi.value} | TP: {self.tmf.value} | VI: {self.vmi.value} | VF: {self.vmf.value} | VV: {self.vmven.value} | VENTA: $ {self.vmvt.value}\n\n"
                                                f"--- VASOS GRANDES ---\n"
                                                f"   TI: {self.tgi.value} | TP: {self.tgf.value} | VI: {self.vgi.value} | VF: {self.vgf.value} | VV: {self.vgven.value} | VENTA: $ {self.vgvt.value}\n\n"
                                                f"--- FRUTA ---\n"
                                                f"   Fresa -> PI: {self.fpi.value} | PF: {self.fpf.value} | EI: {self.fei.value} | EF: {self.fef.value} | Vendida: {self.fv.value} bote(s)\n"
                                                f"   Uva -> PI: {self.upi.value} | PF: {self.upf.value} | EI: {self.uei.value} | EF: {self.uef.value} | Vendida: {self.uv.value} bote(s)\n\n"
                                                f"--- CREMAS ---\n"
                                                f"   Crema Original -> I: {self.coi.value} | F: {self.cof.value} | Vendida: {self.cov.value} bote(s)\n"
                                                f"   Crema Chocolate -> I: {self.cchi.value} | F: {self.cchf.value} | Vendida: {self.cchv.value} bote(s)\n"
                                                f"   Crema Cafe -> I: {self.ccai.value} | F: {self.ccaf.value} | Vendida: {self.ccav.value} bote(s)\n\n"
                                                f"--- TOPPINGS EXTRAS ---\n"
                                                f"   TE5: {self.t5.value} | TE10: {self.t10.value} | Total: $ {self.tet.value}\n\n"
                                                f"--- SERVICIOS A DOMICILIO ---\n"
                                                f"   SD20: {self.sd20.value} | SD35: {self.sd35.value} | Total: $ {self.sdt.value}\n\n"
                                                f"--- TRANSFERENCIAS ---\n"
                                                f"   No Transferencias: {self.trn.value} | Total: $ {self.trt.value}\n\n"
                                                f"--- GASTOS | RETIROS ---\n"
                                                f"   Cantidad: {self.grn.value} | Total: $ {self.grt.value}\n\n"
                                                f"--- INGRESOS | DEDUCCIONES ---\n"
                                                f"   Ingresos: $ {self.bging.value}\n"
                                                f"   Deducciones: $ {self.bgegr.value}\n\n"
                                                f"--- TOTAL DIA PDV ---\n"
                                                f"   Efectivo: $ {self.bgte.value}\n"
                                                f"   Venta Total: $ {self.bgtd.value}\n\n"
                                            ),
                                        ),
                                        actions=[
                                            ft.CupertinoDialogAction("Ok",
                                                is_destructive_action=True,
                                                on_click=lambda e: page.close(e.control.parent)
                                            )
                                        ]
                                    )
                                )
                            )
                        ),
                    ),
                    ft.Container(# Reset Button
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
                    ft.Container(# Borrar Seccion especifica
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

        self.report_field = ce.create_textField_RyV("REPORTE", text_Size=10, min_Lines=35, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=5, size=10), read_Only=True)
        self.sales_field = ce.create_textField_RyV("EXTRAS", text_Size=10, min_Lines=35, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=5, size=10), read_Only=False)

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

        self.navigation_bar = ft.Container(# Barra lateral de navegacion principal
            col=.75,
            # bgcolor=self.color_teal,
            bgcolor=ft.Colors.BLUE_GREY_900,
            # border=ft.border.all(width=2, color=ft.Colors.BLUE_GREY_900),
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        border_radius=10,
                        expand=True,
                        content=ft.NavigationRail(
                            bgcolor=ft.Colors.BLUE_GREY_900,
                            # bgcolor="#181818",
                            expand=True,
                            on_change=self.change_page,
                            selected_index=0,
                            indicator_color=self.color_teal_2,
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

        self.home = ft.Container(# Ventana Inicio Planeador
            col=12,
            bgcolor=ft.Colors.BLUE_GREY_900,
            border_radius=10,
            content=ft.Container(
                margin=3,
                # bgcolor="pink",
                content=ft.Column(
                    controls=[
                        ft.ResponsiveRow(# Titulo ventana
                            controls=[
                                ft.Column(# Titulo ventana
                                    col=12,
                                    horizontal_alignment="center",
                                    controls=[
                                        ft.Container(
                                            padding=10,
                                            # bgcolor="black",
                                            content=ft.Text("PLANEADOR", size=30, color="#ff1765", weight=ft.FontWeight.BOLD)
                                        )
                                    ]
                                ),
                                ft.Divider(# Separador de seccion con Divider
                                    height=1,
                                    color=self.color_teal,
                                    thickness=1,
                                    leading_indent=10,
                                    trailing_indent=10,
                                ),

                            ]
                        ),
                        ft.ResponsiveRow(# Planeador del dia
                            expand=True,
                            controls=[
                                ft.Container(# Contenedor Principal
                                    col=12,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.symmetric(horizontal=50, vertical=10),
                                    padding=20,
                                    # bgcolor="yellow",
                                    border=ft.border.all(width=2, color=ft.Colors.BLUE_GREY_700),
                                    border_radius=10,
                                    content=ft.Column(
                                        alignment=ft.alignment.center,
                                        controls=[
                                            ft.Container(# Fecha
                                                border_radius=3,
                                                bgcolor="#1b89ff",
                                                alignment=ft.alignment.center,
                                                padding=5,
                                                content=ft.Text(value="PLANEACIÓN Y ESTRUCTURA LABORAL", size=20, color="black", weight=ft.FontWeight.BOLD, style=ft.TextStyle(letter_spacing=15))
                                                # content=ft.Text(self.today_main, size=32,style=ft.TextStyle(letter_spacing=20), color="black")
                                            ),
                                            ft.ResponsiveRow(# Fila Principal
                                                expand=True,
                                                controls=[
                                                    ft.Container(# Fecha vertical
                                                        col=.5,
                                                        padding=ft.padding.symmetric(horizontal=5, vertical=20),
                                                        border_radius=3,
                                                        alignment=ft.alignment.center,
                                                        expand=True,
                                                        bgcolor="#1b89ff",
                                                        content=ft.Column(
                                                            spacing=0,
                                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Text(value=self.date_onList[0], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[1], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[2], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[3], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[4], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[5], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[6], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[7], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[8], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[9], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[10], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[11], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[12], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[13], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                                ft.Text(value=self.date_onList[14], color="black", weight=ft.FontWeight.BOLD, size=11),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Supervisores y Sucursales
                                                        # expand=True,
                                                        # height=300,
                                                        # bgcolor="blue",
                                                        alignment=ft.alignment.center,
                                                        col=4,
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
                                                                                bgcolor="#6adb00",
                                                                                alignment=ft.alignment.center,
                                                                                border=ft.border.all(color="black", width=.5),
                                                                                content=ft.Column(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    horizontal_alignment="center",
                                                                                    spacing=0,
                                                                                    controls=[
                                                                                        ft.Text("S", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("U", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("P", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("E", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("R", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("V", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("I", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("S", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("I", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("O", color="black", size=7.5, weight="bold"),
                                                                                        ft.Text("N", color="black", size=7.5, weight="bold"),
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
                                                                                        bgcolor="#6adb00",
                                                                                        content=ft.Text("Supervisor de Personal y PDV", color="black", size=10, weight="bold")
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        padding=5,
                                                                                        # height=45,
                                                                                        bgcolor="#6adb00",
                                                                                        content=ft.Text("Supervisor de Operaciones", color="black", size=10, weight="bold")
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        padding=5,
                                                                                        # height=45,
                                                                                        bgcolor="#6adb00",
                                                                                        content=ft.Text("Supervisor de CDO", color="black", size=10, weight="bold")
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
                                                                                    spacing=0,
                                                                                    controls=[
                                                                                        ft.Text("S", color="white", size=12, weight="bold"),
                                                                                        ft.Text("U", color="white", size=12, weight="bold"),
                                                                                        ft.Text("C", color="white", size=12, weight="bold"),
                                                                                        ft.Text("U", color="white", size=12, weight="bold"),
                                                                                        ft.Text("R", color="white", size=12, weight="bold"),
                                                                                        ft.Text("S", color="white", size=12, weight="bold"),
                                                                                        ft.Text("A", color="white", size=12, weight="bold"),
                                                                                        ft.Text("L", color="white", size=12, weight="bold"),
                                                                                        ft.Text("E", color="white", size=12, weight="bold"),
                                                                                        ft.Text("S", color="white", size=12, weight="bold"),
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
                                                                                                    content=ft.Text("2 - VP Vips", color="white", size=10, weight="bold")
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center_left,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    # height=25,
                                                                                                    bgcolor="#fe0f7c",
                                                                                                    padding=ft.padding.only(left=5),
                                                                                                    content=ft.Text("3 - VP San Miguel", color="white", size=10, weight="bold")
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center_left,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    # height=25,
                                                                                                    bgcolor="#fe0f7c",
                                                                                                    padding=ft.padding.only(left=5),
                                                                                                    content=ft.Text("4 - VP San Antonio", color="white", size=10, weight="bold")
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center_left,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    # height=25,
                                                                                                    bgcolor="#fe0f7c",
                                                                                                    padding=ft.padding.only(left=5),
                                                                                                    content=ft.Text("5 - VP Ensueños", color="white", size=10, weight="bold")
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center_left,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    # height=25,
                                                                                                    bgcolor="#fe0f7c",
                                                                                                    padding=ft.padding.only(left=5),
                                                                                                    content=ft.Text("6 - VP Cofradía 2", color="white", size=10, weight="bold")
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center_left,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    # height=25,
                                                                                                    bgcolor="#fe0f7c",
                                                                                                    padding=ft.padding.only(left=5),
                                                                                                    content=ft.Text("7 - PL La Piedad", color="white", size=10, weight="bold")
                                                                                                ),
                                                                                                ft.Container(
                                                                                                    expand=True,
                                                                                                    alignment=ft.alignment.center_left,
                                                                                                    border=ft.border.all(color="black", width=.5),
                                                                                                    # height=25,
                                                                                                    bgcolor="#fe0f7c",
                                                                                                    padding=ft.padding.only(left=5),
                                                                                                    content=ft.Text("8 - FS Glorieta", color="white", size=10, weight="bold")
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
                                                                                        # height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_LaPiedad
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
                                                                        content=ft.Text("Ventas mínimas\ndel día", size=20, color="black", text_align="center"),
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
                                                                                content=self.vm_LaPiedad
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
                                                    ft.Container(# Promedio
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
                                                                        content=ft.Text("Promedio", color="black")
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
                                                                                content=self.prom_LaPiedad
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
                                                    ft.Container(# Rutas y CDO
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
                                                                                content=ft.Text("Operaciones\ny Transporte", color="black",size=20)
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
                                                                                        content=ft.Text("Ruta 1", color="black")
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=90,
                                                                                        bgcolor="#ff1919",
                                                                                        content=ft.Text("Ruta 2", color="black")
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        alignment=ft.alignment.center,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        bgcolor="#ff1919",
                                                                                        content=ft.Text("Comodines", color="black")
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
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=self.ruta1_1
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=self.ruta1_2
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=self.ruta1_3
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=self.ruta2_1
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=self.ruta2_2
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=self.ruta2_3
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        bgcolor="white",
                                                                                        content=self.ruta_com
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                                ft.Container(# CDO
                                                                    height=150,
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
                                                                                content=ft.Text("Centro de Operaciones", color="black",size=20)
                                                                            ),
                                                                            ft.Column(
                                                                                col=4,
                                                                                horizontal_alignment="center",
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=self.cdo_1
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=self.cdo_2
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
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
        )

        #==========================================================#
        #     VENTANA DE REGISTRO / SECCION CONTROL DE INSUMOS     #
        #==========================================================#

        self.register = ft.Container(
            bgcolor=ft.Colors.BLUE_GREY_900,
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
                        selected_index=1,
                        label_text_style=ft.TextStyle(size=16, italic=True),
                        label_color="#08f5a9",
                        unselected_label_color="white",
                        unselected_label_text_style=ft.TextStyle(size=12, italic=False),
                        animation_duration=150,
                        scrollable=False,
                        indicator_tab_size=True,
                        indicator_color="#08f5a9",
                        overlay_color={
                            ft.ControlState.HOVERED: "#181818",
                            ft.ControlState.PRESSED: "#181818"
                        },
                        # indicator_color="#ff1765",
                        # indicator_thickness=10,
                        tabs=[
                            ft.Tab(# Frutas y Cremas
                                text="Frutas y Cremas",
                                content=ft.Container(
                                    expand=True,
                                    # bgcolor="red",
                                    margin=ft.Margin(top=20, bottom=20, left=30, right=30),
                                    content=ft.Column(
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        controls=[
                                            ft.ResponsiveRow(
                                                expand=True,
                                                controls=[
                                                    ft.Container(
                                                        col=9,
                                                        # bgcolor="yellow",
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(# Fresa
                                                                    expand=True,
                                                                    alignment=ft.alignment.center,
                                                                    # bgcolor="#292929",
                                                                    border_radius=5,
                                                                    margin=ft.margin.only(bottom=2),
                                                                    border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                    padding=ft.Padding(top=15, bottom=15, left=0, right=0),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo Fresa
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="blue",
                                                                                content=ft.Column(# Titulo
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* FRESA *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Fresa
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.fpi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.fpf
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.fei
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.fef
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.fv
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Uva
                                                                    expand=True,
                                                                    alignment=ft.alignment.center,
                                                                    # bgcolor="#292929",
                                                                    border_radius=5,
                                                                    margin=ft.margin.only(top=2),
                                                                    border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                    padding=ft.Padding(top=15, bottom=15, left=0, right=0),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo Uva
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="blue",
                                                                                content=ft.Column(# Titulo
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* UVA *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Uva
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.upi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.upf
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.uei
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.uef
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.uv
                                                                                            )
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
                                                    ft.Container(
                                                        col=3,
                                                        margin=ft.margin.only(left=4),
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        # bgcolor="yellow",
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(# Titulo
                                                                    # bgcolor="blue",
                                                                    alignment=ft.alignment.center,
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("VENTA", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            ft.Text("GENERAL", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Fruta total vendida (botes)
                                                                    alignment=ft.alignment.center,
                                                                    width=150,
                                                                    bgcolor="#292929",
                                                                    border=ft.border.all(width=1, color="#292929"),
                                                                    border_radius=5,
                                                                    padding=5,
                                                                    shadow=ft.BoxShadow(
                                                                        spread_radius=.5,
                                                                        blur_radius=5,
                                                                        color="#0042e8",
                                                                        offset=ft.Offset(0, 0),
                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                    ),
                                                                    content=self.fruven
                                                                ),
                                                                ft.Container(# Crema total vendida (botes)
                                                                    alignment=ft.alignment.center,
                                                                    width=150,
                                                                    bgcolor="#292929",
                                                                    border=ft.border.all(width=1, color="#292929"),
                                                                    border_radius=5,
                                                                    padding=5,
                                                                    shadow=ft.BoxShadow(
                                                                        spread_radius=.5,
                                                                        blur_radius=5,
                                                                        color="#ff0707",
                                                                        offset=ft.Offset(0, 0),
                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                    ),
                                                                    content=self.creven
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            ft.ResponsiveRow(# Cremas
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    ft.Container(# Crema Original
                                                        col=4,
                                                        margin=ft.Margin(top=8, bottom=0, left=0, right=0),
                                                        # bgcolor="blue",
                                                        content=ft.Column(
                                                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    alignment=ft.alignment.center,
                                                                    # bgcolor="#292929",
                                                                    border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                    border_radius=5,
                                                                    padding=ft.Padding(top=20, bottom=20, left=0, right=0),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="blue",
                                                                                content=ft.Column(
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* CREMA ORIGINAL *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                                ft.Container(# Botes Dia
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Botes Iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.coi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Botes Finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.cof
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Venta Botes
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=6,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.cov
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Crema Chocolate
                                                        col=4,
                                                        margin=ft.Margin(top=8, bottom=0, left=4, right=4),
                                                        # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                        # bgcolor="blue",
                                                        content=ft.Column(
                                                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    alignment=ft.alignment.center,
                                                                    # bgcolor="#292929",
                                                                    border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                    border_radius=5,
                                                                    padding=ft.Padding(top=20, bottom=20, left=0, right=0),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="blue",
                                                                                content=ft.Column(
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* CREMA CHOCOLATE *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Botes Dia
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Botes Iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.cchi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Botes Finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.cchf
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Venta Botes
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=6,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.cchv
                                                                                            )
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
                                                    ft.Container(# Crema Cafe
                                                        col=4,
                                                        margin=ft.Margin(top=8, bottom=0, left=0, right=0),
                                                        # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                        # bgcolor="blue",
                                                        content=ft.Column(
                                                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(
                                                                    alignment=ft.alignment.center,
                                                                    # bgcolor="#292929",
                                                                    border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                    border_radius=5,
                                                                    padding=ft.Padding(top=20, bottom=20, left=0, right=0),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="blue",
                                                                                content=ft.Column(
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* CREMA CAFE *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Botes Dia
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Botes Iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.ccai
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Botes Finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.ccaf
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Venta Botes
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=6,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.ccav
                                                                                            )
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
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ),
                            ft.Tab(# Vasos
                                text="Vasos",
                                content=ft.ResponsiveRow(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.Container(# Vasos
                                            col=12,
                                            margin=ft.Margin(top=20, bottom=20, left=30, right=30),
                                            # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                # horizontal_alignment="center",
                                                controls=[
                                                    ft.ResponsiveRow(
                                                        expand=True,
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        vertical_alignment="center",
                                                        controls=[
                                                            ft.Container(# Vasos Chicos
                                                                col=4,
                                                                # expand=True,
                                                                alignment=ft.alignment.center,
                                                                # bgcolor="#292929",
                                                                border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                border_radius=5,
                                                                padding=ft.Padding(top=10, bottom=10, left=0, right=0),
                                                                content=ft.Column(
                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                    horizontal_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="red",
                                                                            content=ft.Text("VASOS CHICOS", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Tapas chicas iniciales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.tci
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(# Tapas chicas finales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.tcf
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Vasos chicos iniciales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vci
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(# Vasos chicos finales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vcf
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Vasos chicos vendidos
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vcven
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(# Vasos chicos venta total
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vcvt
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(# Vasos Medianos
                                                                col=4,
                                                                expand=True,
                                                                alignment=ft.alignment.center,
                                                                # bgcolor="#292929",
                                                                border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                border_radius=5,
                                                                padding=ft.Padding(top=10, bottom=10, left=0, right=0),
                                                                content=ft.Column(
                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                    controls=[
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="red",
                                                                            content=ft.Text("VASOS MEDIANOS", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Tapas medianas iniciales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.tmi
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(# Tapas medianas finales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.tmf
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Vasos medianos iniciales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vmi
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(# Vasos medianos finales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vmf
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Vasos medianos vendidos
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vmven
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(# Vasos medianos venta total
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vmvt
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(# Vasos Grandes
                                                                col=4,
                                                                expand=True,
                                                                alignment=ft.alignment.center,
                                                                # bgcolor="#292929",
                                                                border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                border_radius=5,
                                                                padding=ft.Padding(top=10, bottom=10, left=0, right=0),
                                                                content=ft.Column(
                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                    controls=[
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="red",
                                                                            content=ft.Text("VASOS GRANDES", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Tapas grandes iniciales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.tgi
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(# Tapas grandes finales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.tgf
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Vasos grnades iniciales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vgi
                                                                                        )
                                                                                    ),
                                                                                    ft.Container(# Vasos grandes finales
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vgf
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            # bgcolor="blue",
                                                                            content=ft.ResponsiveRow(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                vertical_alignment="center",
                                                                                controls=[
                                                                                    ft.Container(# Vasos grandes vendidos
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vgven
                                                                                        ),
                                                                                    ),
                                                                                    ft.Container(# Vasos grandes venta total
                                                                                        alignment=ft.alignment.center,
                                                                                        col=6,
                                                                                        # bgcolor="yellow",
                                                                                        content=ft.Container(
                                                                                            # bgcolor=self.color_teal_2,
                                                                                            border_radius=5,
                                                                                            content=self.vgvt
                                                                                        ),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    ft.Container(# Venta Total Vasos en General
                                                        # bgcolor="yellow",
                                                        padding=25,
                                                        alignment=ft.alignment.center,
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        content=ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            vertical_alignment="center",
                                                            controls=[
                                                                ft.Container(# Venta Total Vasos en General
                                                                    col=6,
                                                                    alignment=ft.alignment.center,
                                                                    # padding=ft.padding.only(bottom=7),
                                                                    # bgcolor="blue",
                                                                    content=ft.Text("VENTA TOTAL DE VASOS", color="#bfc244", weight=ft.FontWeight.BOLD, size=24, style=ft.TextStyle(letter_spacing=10)),
                                                                ),
                                                                ft.Container(# Venta Total Vasos en General
                                                                    col=6,
                                                                    alignment=ft.alignment.center,
                                                                    # padding=ft.padding.only(bottom=3),
                                                                    # bgcolor="pink",
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Total Vasos Vendidos
                                                                                col=4.5,
                                                                                alignment=ft.alignment.center,
                                                                                bgcolor="#292929",
                                                                                padding=3,
                                                                                border=ft.border.all(width=1, color="#292929"),
                                                                                border_radius=5,
                                                                                margin=ft.margin.only(right=50),
                                                                                shadow=ft.BoxShadow(
                                                                                    spread_radius=.5,
                                                                                    blur_radius=5,
                                                                                    color="#0042e8",
                                                                                    offset=ft.Offset(0, 0),
                                                                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                ),
                                                                                content=self.vtv
                                                                            ),
                                                                            ft.Container(# Total Vasos Vendidos
                                                                                col=4.5,
                                                                                alignment=ft.alignment.center,
                                                                                bgcolor="#292929",
                                                                                padding=3,
                                                                                border=ft.border.all(width=1, color="#292929"),
                                                                                border_radius=5,
                                                                                margin=ft.margin.only(left=50),
                                                                                shadow=ft.BoxShadow(
                                                                                    spread_radius=.5,
                                                                                    blur_radius=5,
                                                                                    color="#ff0707",
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
                                            )
                                        ),
                                    ]
                                )
                            ),
                            ft.Tab(# Extras y Adicionales
                                text="Extras y Adicionales",
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.ResponsiveRow(
                                            expand=True,
                                            controls=[
                                                ft.Container(
                                                    col=12,
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
                                                                expand=True,
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                vertical_alignment=ft.alignment.center,
                                                                controls=[
                                                                    ft.Container(# Toppings
                                                                        col=3,
                                                                        padding=ft.padding.symmetric(horizontal=30, vertical=10),
                                                                        alignment=ft.alignment.center,
                                                                        # bgcolor="red",
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                        border_radius=5,
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Container(
                                                                                    margin=ft.margin.symmetric(horizontal=0, vertical=10),
                                                                                    alignment=ft.alignment.center,
                                                                                    content=ft.Text("TOPPINGS EXTRAS", style=ft.TextStyle(letter_spacing=5))
                                                                                ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            alignment=ft.alignment.center_left,
                                                                                            # bgcolor="blue",
                                                                                            height=40,
                                                                                            content=ft.Text("$5"),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            content=self.t5
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            alignment=ft.alignment.center_left,
                                                                                            # bgcolor="blue",
                                                                                            height=40,
                                                                                            content=ft.Text("$10"),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            content=self.t10
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            col=5,
                                                                                            alignment=ft.alignment.center_left,
                                                                                            # bgcolor="blue",
                                                                                            height=40,
                                                                                            content=ft.Text("TOTAL"),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=1,
                                                                                            alignment=ft.alignment.center_right,
                                                                                            # bgcolor="blue",
                                                                                            height=40,
                                                                                            content=ft.Text("$", size=16),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            content=self.tet
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(# Servicios a Domicilio
                                                                        col=3,
                                                                        alignment=ft.alignment.center,
                                                                        padding=ft.padding.symmetric(horizontal=30, vertical=10),
                                                                        # bgcolor="red",
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                        border_radius=5,
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Container(
                                                                                    margin=ft.margin.symmetric(horizontal=0, vertical=10),
                                                                                    alignment=ft.alignment.center,
                                                                                    content=ft.Text("SERVICIOS A DOMICILIO", style=ft.TextStyle(letter_spacing=3))
                                                                                ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            alignment=ft.alignment.center_left,
                                                                                            # bgcolor="blue",
                                                                                            height=40,
                                                                                            content=ft.Text("$20"),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            content=self.sd20
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            alignment=ft.alignment.center_left,
                                                                                            # bgcolor="blue",
                                                                                            height=40,
                                                                                            content=ft.Text("$35"),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            content=self.sd35
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            col=5,
                                                                                            alignment=ft.alignment.center_left,
                                                                                            # bgcolor="blue",
                                                                                            height=40,
                                                                                            content=ft.Text("TOTAL"),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=1,
                                                                                            alignment=ft.alignment.center_right,
                                                                                            # bgcolor="blue",
                                                                                            height=40,
                                                                                            content=ft.Text("$", size=16),
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            content=self.sdt
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(# Balance General
                                                                        col=6,
                                                                        alignment=ft.alignment.center,
                                                                        padding=ft.padding.symmetric(horizontal=30, vertical=10),
                                                                        # bgcolor="red",
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                        border_radius=5,
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Container(
                                                                                    alignment=ft.alignment.center,
                                                                                    content=ft.Text("BALANCE GENERAL", style=ft.TextStyle(letter_spacing=3.5))
                                                                                ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            margin=ft.margin.only(right=10),
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.ResponsiveRow(
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        col=5,
                                                                                                        alignment=ft.alignment.center_left,
                                                                                                        # bgcolor="blue",
                                                                                                        height=40,
                                                                                                        content=ft.Text("INGRESOS", size=13),
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=1,
                                                                                                        alignment=ft.alignment.center_right,
                                                                                                        # bgcolor="blue",
                                                                                                        height=40,
                                                                                                        content=ft.Text("$", size=16),
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=6,
                                                                                                        content=self.bging
                                                                                                    )
                                                                                                ]
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            margin=ft.margin.only(left=10),
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.ResponsiveRow(
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        col=5,
                                                                                                        alignment=ft.alignment.center_left,
                                                                                                        # bgcolor="blue",
                                                                                                        height=40,
                                                                                                        content=ft.Text("DEDUCCIONES", size=13),
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=1,
                                                                                                        alignment=ft.alignment.center_right,
                                                                                                        # bgcolor="blue",
                                                                                                        height=40,
                                                                                                        content=ft.Text("$", size=16),
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=6,
                                                                                                        content=self.bgegr
                                                                                                    )
                                                                                                ]
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            margin=ft.margin.only(right=10),
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.ResponsiveRow(
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        col=5,
                                                                                                        alignment=ft.alignment.center_left,
                                                                                                        # bgcolor="blue",
                                                                                                        height=40,
                                                                                                        content=ft.Text("TOTAL DÍA"),
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=1,
                                                                                                        alignment=ft.alignment.center_right,
                                                                                                        # bgcolor="blue",
                                                                                                        height=40,
                                                                                                        content=ft.Text("$", size=16),
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=6,
                                                                                                        content=self.bgtd
                                                                                                    )
                                                                                                ]
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            col=6,
                                                                                            margin=ft.margin.only(left=10),
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.ResponsiveRow(
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        col=5,
                                                                                                        alignment=ft.alignment.center_left,
                                                                                                        # bgcolor="blue",
                                                                                                        height=40,
                                                                                                        content=ft.Text("TOTAL EFECTIVO"),
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=1,
                                                                                                        alignment=ft.alignment.center_right,
                                                                                                        # bgcolor="blue",
                                                                                                        height=40,
                                                                                                        content=ft.Text("$", size=16),
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=6,
                                                                                                        content=self.bgte
                                                                                                    ),
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
                                                            ft.ResponsiveRow(
                                                                expand=True,
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                vertical_alignment=ft.alignment.center,
                                                                controls=[
                                                                    ft.Container(# Transferencias
                                                                        col=6,
                                                                        padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                                                        alignment=ft.alignment.center,
                                                                        # bgcolor="red",
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                        border_radius=5,
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Container(
                                                                                    alignment=ft.alignment.center,
                                                                                    content=ft.Text("TRANSFERENCIAS", style=ft.TextStyle(letter_spacing=5))
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
                                                                                                        col=5.5,
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
                                                                                                        col=6,
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
                                                                                                                                border=ft.border.all(width=.75, color=ft.Colors.WHITE),
                                                                                                                                border_radius=5,
                                                                                                                                # bgcolor="blue",
                                                                                                                                # bgcolor="#292929",
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
                                                                                                                                                    self.tr2,
                                                                                                                                                    self.tr3,
                                                                                                                                                    self.tr4,
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
                                                                                                                                                    self.tr5,
                                                                                                                                                    self.tr6,
                                                                                                                                                    self.tr7,
                                                                                                                                                    self.tr8,
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
                                                                                                                                                    self.tr9,
                                                                                                                                                    self.tr10,
                                                                                                                                                    self.tr11,
                                                                                                                                                    self.tr12,
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
                                                                                                                                content=ft.Text("M O N T O S     T R A N S F E R E N C I A S", size=8, italic=True, weight=ft.FontWeight.BOLD)
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
                                                                        # bgcolor="red",
                                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                                        border_radius=5,
                                                                        content=ft.Column(
                                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                            horizontal_alignment="center",
                                                                            controls=[
                                                                                ft.Container(
                                                                                    alignment=ft.alignment.center,
                                                                                    content=ft.Text("GASTOS | RETIROS", style=ft.TextStyle(letter_spacing=5))
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
                                                                                                        col=5.5,
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
                                                                                                        col=6,
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
                                                                                                                                border=ft.border.all(width=.75, color=ft.Colors.WHITE),
                                                                                                                                border_radius=5,
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
                                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                                                                                horizontal_alignment="center",
                                                                                                                                                controls=[
                                                                                                                                                    ft.Text("$", size=12, color="#ffffff"),
                                                                                                                                                    ft.Text("$", size=12, color="#ffffff"),
                                                                                                                                                    ft.Text("$", size=12, color="#ffffff")
                                                                                                                                                ]
                                                                                                                                            ),
                                                                                                                                        ),
                                                                                                                                        ft.Container(
                                                                                                                                            expand=True,
                                                                                                                                            col=5,
                                                                                                                                            alignment=ft.alignment.center,
                                                                                                                                            # bgcolor="red",
                                                                                                                                            content=ft.Column(
                                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                                                                                horizontal_alignment="center",
                                                                                                                                                controls=[
                                                                                                                                                    self.gr1,
                                                                                                                                                    self.gr2,
                                                                                                                                                    self.gr3,
                                                                                                                                                ]
                                                                                                                                            ),
                                                                                                                                        ),
                                                                                                                                        ft.Container(
                                                                                                                                            expand=True,
                                                                                                                                            col=1,
                                                                                                                                            alignment=ft.alignment.center_right,
                                                                                                                                            # bgcolor="red",
                                                                                                                                            content=ft.Column(
                                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                                                                                horizontal_alignment="center",
                                                                                                                                                controls=[
                                                                                                                                                    ft.Text("$", size=12, color="#ffffff"),
                                                                                                                                                    ft.Text("$", size=12, color="#ffffff"),
                                                                                                                                                    ft.Text("$", size=12, color="#ffffff")
                                                                                                                                                ]
                                                                                                                                            ),
                                                                                                                                        ),
                                                                                                                                        ft.Container(
                                                                                                                                            expand=True,
                                                                                                                                            col=5,
                                                                                                                                            alignment=ft.alignment.center,
                                                                                                                                            # bgcolor="red",
                                                                                                                                            content=ft.Column(
                                                                                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                                                                                horizontal_alignment="center",
                                                                                                                                                controls=[
                                                                                                                                                    self.gr4,
                                                                                                                                                    self.gr5,
                                                                                                                                                    self.gr6,
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
                                                                                                                                    content=ft.Text("M O N T O S     G A S T O S   |   R E T I R O S", size=8, italic=True, weight=ft.FontWeight.BOLD)
                                                                                                                                )
                                                                                                                        ]
                                                                                                                    )
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    )
                                                                                                    # ft.Container(
                                                                                                    #     col=6,
                                                                                                    #     # bgcolor="blue",
                                                                                                    #     padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                                                                                    #     content=ft.Column(
                                                                                                    #         controls=[
                                                                                                    #             ft.Container(
                                                                                                    #                 expand=True,
                                                                                                    #                 col=5,
                                                                                                    #                 alignment=ft.alignment.center,
                                                                                                    #                 # bgcolor="blue",
                                                                                                    #                 content=ft.Container(
                                                                                                    #                     # bgcolor=self.color_teal,
                                                                                                    #                     alignment=ft.alignment.center,
                                                                                                    #                     border_radius=5,
                                                                                                    #                     padding=1,
                                                                                                    #                     shadow=ft.BoxShadow(
                                                                                                    #                         spread_radius=1,
                                                                                                    #                         blur_radius=15,
                                                                                                    #                         color=ft.Colors.BLUE_GREY_100,
                                                                                                    #                         offset=ft.Offset(0, 0),
                                                                                                    #                         blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                                    #                     ),
                                                                                                    #                     content=ft.Column(
                                                                                                    #                         spacing=0,
                                                                                                    #                         controls=[
                                                                                                    #                             ft.Container(
                                                                                                    #                                 expand=True,
                                                                                                    #                                 alignment=ft.alignment.center,
                                                                                                    #                                 padding=10,
                                                                                                    #                                 border=ft.border.all(width=.75, color=ft.Colors.WHITE),
                                                                                                    #                                 border_radius=5,
                                                                                                    #                                 # bgcolor="blue",
                                                                                                    #                                 # bgcolor="#292929",
                                                                                                    #                                 content=ft.Column(
                                                                                                    #                                     expand=True,
                                                                                                    #                                     alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                                    #                                     horizontal_alignment=ft.alignment.center,
                                                                                                    #                                     controls=[
                                                                                                    #                                         ft.Container(
                                                                                                    #                                             # expand=True,
                                                                                                    #                                             col=12,
                                                                                                    #                                             alignment=ft.alignment.center,
                                                                                                    #                                             # bgcolor="red",
                                                                                                    #                                             content=ft.Text("G A S T O S", size=10, italic=True, weight=ft.FontWeight.BOLD),
                                                                                                    #                                         ),
                                                                                                    #                                         ft.ResponsiveRow(
                                                                                                    #                                             alignment=ft.MainAxisAlignment.CENTER,
                                                                                                    #                                             vertical_alignment=ft.alignment.center,
                                                                                                    #                                             controls=[
                                                                                                    #                                                 ft.Container(
                                                                                                    #                                                     expand=True,
                                                                                                    #                                                     col=4,
                                                                                                    #                                                     alignment=ft.alignment.center,
                                                                                                    #                                                     # bgcolor="red",
                                                                                                    #                                                     content=self.gr1
                                                                                                    #                                                 ),
                                                                                                    #                                                 ft.Container(
                                                                                                    #                                                     expand=True,
                                                                                                    #                                                     col=4,
                                                                                                    #                                                     alignment=ft.alignment.center,
                                                                                                    #                                                     # bgcolor="red",
                                                                                                    #                                                     content=self.gr2
                                                                                                    #                                                 ),
                                                                                                    #                                                 ft.Container(
                                                                                                    #                                                     expand=True,
                                                                                                    #                                                     col=4,
                                                                                                    #                                                     alignment=ft.alignment.center,
                                                                                                    #                                                     # bgcolor="red",
                                                                                                    #                                                     content=self.gr3
                                                                                                    #                                                 ),
                                                                                                    #                                             ]
                                                                                                    #                                         ),
                                                                                                    #                                         ft.Container(
                                                                                                    #                                             # expand=True,
                                                                                                    #                                             col=12,
                                                                                                    #                                             alignment=ft.alignment.center,
                                                                                                    #                                             # bgcolor="red",
                                                                                                    #                                             content=ft.Text("R E T I R O S", size=10, italic=True, weight=ft.FontWeight.BOLD),
                                                                                                    #                                         ),
                                                                                                    #                                         ft.ResponsiveRow(
                                                                                                    #                                             alignment=ft.MainAxisAlignment.CENTER,
                                                                                                    #                                             vertical_alignment=ft.alignment.center,
                                                                                                    #                                             controls=[
                                                                                                    #                                                 ft.Container(
                                                                                                    #                                                     expand=True,
                                                                                                    #                                                     col=4,
                                                                                                    #                                                     alignment=ft.alignment.center,
                                                                                                    #                                                     # bgcolor="red",
                                                                                                    #                                                     content=self.gr4
                                                                                                    #                                                 ),
                                                                                                    #                                                 ft.Container(
                                                                                                    #                                                     expand=True,
                                                                                                    #                                                     col=4,
                                                                                                    #                                                     alignment=ft.alignment.center,
                                                                                                    #                                                     # bgcolor="red",
                                                                                                    #                                                     content=self.gr5
                                                                                                    #                                                 ),
                                                                                                    #                                                 ft.Container(
                                                                                                    #                                                     expand=True,
                                                                                                    #                                                     col=4,
                                                                                                    #                                                     alignment=ft.alignment.center,
                                                                                                    #                                                     # bgcolor="red",
                                                                                                    #                                                     content=self.gr6
                                                                                                    #                                                 ),
                                                                                                    #                                             ]
                                                                                                    #                                         ),
                                                                                                    #                                     ]
                                                                                                    #                                 )
                                                                                                    #                             ),
                                                                                                    #                             ft.Container(
                                                                                                    #                                 alignment=ft.alignment.center_right,
                                                                                                    #                                 padding=ft.Padding(top=5, right=10, bottom=0, left=0),
                                                                                                    #                                 # bgcolor="blue",
                                                                                                    #                                 bgcolor="#292929",
                                                                                                    #                                 content=ft.Text("M O N T O S     G A S T O S   |   R E T I R O S", size=8, italic=True, weight=ft.FontWeight.BOLD)
                                                                                                    #                             )
                                                                                                    #                         ]
                                                                                                    #                     )
                                                                                                    #                 )
                                                                                                    #             ),
                                                                                                    #         ]
                                                                                                    #     )
                                                                                                    # )
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
                                            ]
                                        )
                                    ]
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

        self.sales = ft.Container(# Ventana Ventas
            col=12,
            bgcolor=ft.Colors.BLUE_GREY_900,
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
                                            padding=10,
                                            # bgcolor="black",
                                            content=ft.Text("VENTAS Y REPORTES", size=30, color="#ff1765", weight=ft.FontWeight.BOLD)
                                        )
                                    ]
                                ),
                                ft.Divider(# Separador de seccion con Divider
                                    height=1,
                                    color=self.color_teal,
                                    thickness=3,
                                    # leading_indent=50,
                                    # trailing_indent=10
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
                                        col=4,
                                        # bgcolor=self.color_teal,
                                        content=ft.Container(
                                            # bgcolor=self.color_teal,
                                            alignment=ft.alignment.center,
                                            border_radius=5,
                                            padding=1,
                                            shadow=ft.BoxShadow(
                                                spread_radius=1,
                                                blur_radius=15,
                                                color=ft.Colors.BLUE_GREY_100,
                                                offset=ft.Offset(0, 0),
                                                blur_style=ft.ShadowBlurStyle.OUTER,
                                            ),
                                            content=self.report_field
                                        )
                                    ),
                                    ft.Container(# Botones interactivos para archivos
                                        col=4,
                                        # bgcolor="black",
                                        alignment=ft.alignment.center,
                                        content=ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container(
                                                    # bgcolor=self.color_teal,
                                                    # border_radius=10,
                                                    # padding=20,
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
                                                )
                                            ]
                                        )
                                    ),
                                    ft.Container(# Campo de texto para ventas
                                        padding=20,
                                        alignment=ft.alignment.center,
                                        col=4,
                                        # bgcolor=self.color_teal,
                                        content=ft.Container(
                                            # bgcolor=self.color_teal,
                                            alignment=ft.alignment.center,
                                            border_radius=5,
                                            padding=1,
                                            shadow=ft.BoxShadow(
                                                spread_radius=1,
                                                blur_radius=15,
                                                color=ft.Colors.BLUE_GREY_100,
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

        self.sp = ft.Row(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    border_radius=10,
                    content=ft.Container(
                        expand=True,
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
                                            ft.Text("En proceso...", size=25),
                                            ft.Container(
                                                bgcolor="#ff2525",
                                                width=200,
                                                height=2
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                )
            ]
        )

        #=======================================#
        #     VENTANA SECCION DE INVENTARIO     #
        #=======================================#

        self.stock = ft.Row(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    border_radius=10,
                    content=ft.Container(
                        expand=True,
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
                                            ft.Text("En proceso...", size=25),
                                            ft.Container(
                                                bgcolor="#ff2525",
                                                width=200,
                                                height=2
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                )
            ]
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
        if e.control.value == "glorieta":
            self.pdv = "Suc. Glorieta"
        if e.control.value == "sanmiguel":
            self.pdv = "Suc. San Miguel"
        elif e.control.value == "vips":
            self.pdv = "Suc. Vips"
        elif e.control.value == "cofradia2":
            self.pdv = "Suc. Cofradía 2"
        elif e.control.value == "ensueños":
            self.pdv = "Suc. Ensueños"
        elif e.control.value == "sanantonio":
            self.pdv = "Suc. San Antonio"
        elif e.control.value == "lapiedad":
            self.pdv = "Suc. La Piedad"

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
            self.vvmt.value = self.vcvt.value
            self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            self.vtv.update()
            self.vvmt.update()
            self.bging.update()
            self.bgtd.update()
            self.venta_totalVasos()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos chicos: ", ex)
            pass
        finally:
            self.update()


    # ---> Comprobacion del tipo de valor en los campos
    def values_types_comprobation_vc(self):
        if self.vci.value == "" or self.vcf.value == "":
            self.vcven.value = ""
            self.vcvt.value = ""
            self.vcven.update()
            self.vcvt.update()
            if self.vcven.value == "":
                if type(self.vmven.value) != str and type(self.vgven.value) != str:
                    try:
                        self.vtv.value = self.vmven.value + self.vgven.value
                        self.vvmt.value = self.vmvt.value + self.vgvt.value
                        self.vtv.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma: vasos medianos totales + vasos grandes totales - Error:", ex)
                    return
                elif type(self.vmven.value) != str:
                    self.vtv.value = self.vmven.value
                    self.vvmt.value = self.vmvt.value
                elif type(self.vgven.value) != str:
                    self.vtv.value = self.vgven.value
                    self.vvmt.value = self.vgvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
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
            self.vmvt.value = int(self.vmven.value * 70)
            self.vtv.value = self.vmven.value
            self.vvmt.value = self.vmvt.value
            self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            self.vtv.update()
            self.vvmt.update()
            self.bging.update()
            self.bgtd.update()
            self.venta_totalVasos()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos medianos: ", ex)
            pass
        finally:
            self.update()

    # ---> Comprobacion del tipo de valor en los campos
    def values_types_comprobation_vm(self):
        if self.vmi.value == "" or self.vmf.value == "":
            self.vmven.value = ""
            self.vmvt.value = ""
            self.vmven.update()
            self.vmvt.update()
            if self.vmven.value == "":
                if type(self.vcven.value) != str and type(self.vgven.value) != str:
                    try:
                        self.vtv.value = self.vcven.value + self.vgven.value
                        self.vvmt.value = self.vcvt.value + self.vgvt.value
                        self.vtv.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma: vasos chicos totales + vasos grandes totales - Error:", ex)
                    return
                elif type(self.vcven.value) != str:
                    self.vtv.value = self.vcven.value
                    self.vvmt.value = self.vcvt.value
                elif type(self.vgven.value) != str:
                    self.vtv.value = self.vgven.value
                    self.vvmt.value = self.vgvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
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
            self.vvmt.value = self.vgvt.value
            self.bging.value = self.vvmt.value
            self.bgtd.value = self.vvmt.value
            self.vtv.update()
            self.vvmt.update()
            self.bging.update()
            self.bgtd.update()
            self.venta_totalVasos()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos grandes: ", ex)
            pass
        finally:
            self.update()

    # ---> Comprobacion del tipo de valor en los campos
    def values_types_comprobation_vg(self):
        if self.vgi.value == "" or self.vgf.value == "":
            self.vgven.value = ""
            self.vgvt.value = ""
            self.vgven.update()
            self.vgvt.update()
            if self.vgven.value == "":
                if type(self.vcven.value) != str and type(self.vmven.value) != str:
                    try:
                        self.vtv.value = self.vcven.value + self.vmven.value
                        self.vvmt.value = self.vcvt.value + self.vmvt.value
                        self.vtv.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma: vasos chicos totales + vasos medianos totales - Error:", ex)
                    return
                elif type(self.vcven.value) != str:
                    self.vtv.value = self.vcven.value
                    self.vvmt.value = self.vcvt.value
                elif type(self.vmven.value) != str:
                    self.vtv.value = self.vmven.value
                    self.vvmt.value = self.vmvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
                self.vvmt.update()
            return

    # --- Venta Total Vasos ---

    def venta_totalVasos(self):
        self.num_vtv = 0
        self.num_vvmt = 0

        # Bloques: verificar si hay al menos una cadena en cada grupo
        self.bloque_or_1 = (type(self.vcven.value) == str or type(self.vmven.value) == str or type(self.vgven.value) == str)
        self.bloque_or_2 = (type(self.vcvt.value) == str or type(self.vmvt.value) == str or type(self.vgvt.value) == str)

        # Caso 1: todos los valores son cadenas -> limpiar salidas
        if type(self.vcven.value) == str and type(self.vmven.value) == str and type(self.vgven.value) == str and type(self.vcvt.value) == str and type(self.vmvt.value) == str and type(self.vgvt.value) == str:
            self.vtv.value = ""
            self.vvmt.value = ""
            self.vtv.update()
            self.vvmt.update()

        # Caso 2: en ambos bloques hay al menos una cadena
        elif self.bloque_or_1 and self.bloque_or_2:
            self.values_bloque1 = [self.vcven.value, self.vmven.value, self.vgven.value]
            self.values_bloque2 = [self.vcvt.value, self.vmvt.value, self.vgvt.value]
            self.values_numericos_bloque1 = []
            self.values_numericos_bloque2 = []

            # Emparejar y filtrar solo si ambos no son str
            for e1, e2 in zip(self.values_bloque1, self.values_bloque2):
                if type(e1) != str and type(e2) != str:
                    self.values_numericos_bloque1.append(e1)
                    self.values_numericos_bloque2.append(e2)

            # Si hay exactamente dos pares válidos, sumarlos
            if (len(self.values_numericos_bloque1) == 2) and (len(self.values_numericos_bloque2) == 2):
                self.values_numericos_1 = self.values_numericos_bloque1[0] + self.values_numericos_bloque1[1]
                self.values_numericos_2 = self.values_numericos_bloque2[0] + self.values_numericos_bloque2[1]
                self.vtv.value = self.values_numericos_1
                self.vvmt.value = self.values_numericos_2
                self.bging.value = self.vvmt.value
                self.bgtd.value = self.vvmt.value
                self.vtv.update()
                self.vvmt.update()
                self.bging.update()
                self.bgtd.update()
                self.update()

        # Caso general: intentar sumar todos los valores
        else:
            try:
                self.num_vtv = self.vcven.value + self.vmven.value + self.vgven.value
                self.num_vvmt = self.vcvt.value + self.vmvt.value + self.vgvt.value
                self.vtv.value = self.num_vtv
                self.vvmt.value = self.num_vvmt
                self.bging.value = self.vvmt.value
                self.bgtd.value = self.vvmt.value
                self.vtv.update()
                self.vvmt.update()
                self.bging.update()
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
        if self.fpi.value == "" or self.fpf.value == "" or self.fei.value == "" or self.fef.value == "":
            self.fv.value = "---"
            self.fv.update()
            if self.fv.value == "---":
                self.fruven.value = self.uv.value
                self.fruven.update()
            return

        try:
            if "." in self.fpi.value or "." in self.fpf.value or "." in self.fei.value or "." in self.fef.value:
                self.num_fpi = float(self.fpi.value)
                self.num_fpf = float(self.fpf.value)
                self.num_fei = float(self.fei.value)
                self.num_fef = float(self.fef.value)
            else:
                self.num_fpi = int(self.fpi.value)
                self.num_fpf = int(self.fpf.value)
                self.num_fei = int(self.fei.value)
                self.num_fef = int(self.fef.value)

            # self.num_fr = self.num_fpf + self.num_fef
            # self.num_fv = (self.num_fpi + self.num_fei) - self.num_fr
            self.num_fv = (self.num_fpi + self.num_fei) - (self.num_fpf + self.num_fef)

            # if self.num_fr % 2 == 0 or self.num_fr % 2 == 1:
            #     self.num_fr = int(self.num_fr)

            if self.num_fv % 2 == 0 or self.num_fv % 2 == 1:
                self.num_fv = int(self.num_fv)

            # self.fr.value = round(self.num_fr, 2)
            self.fv.value = round(self.num_fv, 2)

            self.fv.update()
            self.fv.on_change(e)
            self.fruven.update()
        except Exception as ex:
            print("Error en funcion conversion y captura fresa - Error:", ex)
        finally:
            self.update()

    def conversion_n_capture_uva(self, e):
        if self.upi.value == "" or self.upf.value == "" or self.uei.value == "" or self.uef.value == "":
            self.uv.value = "---"
            self.uv.update()
            if self.uv.value == "---":
                self.fruven.value = self.fv.value
                self.fruven.update()
            return

        try:
            if "." in self.upi.value or "." in self.upf.value or "." in self.uei.value or "." in self.uef.value:
                self.num_upi = float(self.upi.value)
                self.num_upf = float(self.upf.value)
                self.num_uei = float(self.uei.value)
                self.num_uef = float(self.uef.value)
            else:
                self.num_upi = int(self.upi.value)
                self.num_upf = int(self.upf.value)
                self.num_uei = int(self.uei.value)
                self.num_uef = int(self.uef.value)

            # self.num_ur = self.num_upf + self.num_uef
            # self.num_uv = (self.num_upi + self.num_uei) - self.num_ur
            self.num_uv = (self.num_upi + self.num_uei) - (self.num_upf + self.num_uef)

            # if self.num_ur % 2 == 0 or self.num_ur % 2 == 1:
            #     self.num_ur = int(self.num_ur)

            if self.num_uv % 2 == 0 or self.num_uv % 2 == 1:
                self.num_uv = int(self.num_uv)

            # self.ur.value = round(self.num_ur, 2)
            self.uv.value = round(self.num_uv, 2)

            self.uv.update()
            self.uv.on_change(e)
            self.fruven.update()
        except Exception as ex:
            print("Error en funcion conversion y captura uva - Error:", ex)
        finally:
            self.update()

    #===================================================#
    #     VALIDACION PARA EL TOTAL DE FRUTA VENDIDA     #
    #===================================================#

    # --- Fresa ---

    def values_Fresa(self, e):
        try:
            if self.fv.value != "" and self.fv.value != "---":
                self.fruven.value = self.fv.value

            self.venta_totalFruta()
            self.fruven.update()
        except Exception as ex:
            print("Error en funcion values_Fresa - Error:", ex)

        # print("validation_totales_bg fresa")
        # print("validation_totales_bg fresa")

    # --- Uva ---

    def values_Uva(self, e):
        try:
            if self.uv.value != "" and self.uv.value != "---":
                self.fruven.value = self.uv.value

            self.venta_totalFruta()
            self.fruven.update()
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
        elif type(self.fv.value) == str:
            self.fruven.value = self.uv.value
        else:
            try:
                self.num_fruven = self.fv.value + self.uv.value

                if self.num_fruven % 2 == 0 or self.num_fruven % 2 == 1:
                    self.num_fruven = int(self.num_fruven)

                self.fruven.value = self.num_fruven
                self.fruven.update()
            except Exception as ex:
                print("Error en funcion venta_totalFruta - Error:", ex)
                pass

    #===================================================================#
    #     CONVERSION Y CAPTURA DEL TIPO DE DATO INGRESADO EN CREMAS     #
    #===================================================================#

    def conversion_n_capture_co(self, e):
        if self.coi.value == "" or self.cof.value == "":
            self.cov.value = "---"
            self.cov.update()
            if self.cov.value == "---":
                if type(self.cchv.value) != str and type(self.ccav.value) != str:
                    try:
                        self.creven.value = self.cchv.value + self.ccav.value
                        self.creven.update()
                    except Exception as ex:
                        self.creven.value = ""
                        print("Error en suma: crema chocolate vendida + crema cafe vendida (funcion cac crema original) - Error:", ex)
                    return
                elif self.cchv.value != "" or self.cchv.value != "---":
                    self.creven.value = self.cchv.value
                elif self.ccav.value != "" or self.ccav.value != "---":
                    self.creven.value = self.ccav.value
                else:
                    self.creven.value = ""
                self.creven.update()
            return

        try:
            if "." in self.coi.value or "." in self.cof.value:
                self.num_coi = float(self.coi.value)
                self.num_cof = float(self.cof.value)
            else:
                self.num_coi = int(self.coi.value)
                self.num_cof = int(self.cof.value)

            self.num_cov = self.num_coi - self.num_cof

            if self.num_cov % 2 == 0 or self.num_cov % 2 == 1:
                self.num_cov = int(self.num_cov)

            self.cov.value = round(self.num_cov, 2)
            self.cov.update()
            self.cov.on_change(e)
            self.creven.update()
        except Exception as ex:
            print("Error en funcion conversion y captura crema original - Error:", e)
        finally:
            self.update()

    def conversion_n_capture_cch(self, e):
        if self.cchi.value == "" or self.cchf.value == "":
            self.cchv.value = "---"
            self.cchv.update()
            if self.cchv.value == "---":
                if type(self.cov.value) != str and type(self.ccav.value) != str:
                    try:
                        self.creven.value = self.cov.value + self.ccav.value
                        self.creven.update()
                    except Exception as ex:
                        self.creven.value = ""
                        print("Error en suma: crema original vendida + crema cafe vendida (funcion cac crema chocolate) - Error:", ex)
                        pass
                        print("Sigue ejecutando despues del pass")
                elif self.cov.value != "" or self.cov.value != "---":
                    self.creven.value = self.cov.value
                elif self.ccav.value != "" or self.ccav.value != "---":
                    self.creven.value = self.ccav.value
                else:
                    self.creven.value = ""
                self.creven.update()
            return

        try:
            if "." in self.cchi.value or "." in self.cchf.value:
                self.num_cchi = float(self.cchi.value)
                self.num_cchf = float(self.cchf.value)
            else:
                self.num_cchi = int(self.cchi.value)
                self.num_cchf = int(self.cchf.value)

            self.num_cchv = self.num_cchi - self.num_cchf

            if self.num_cchv % 2 == 0 or self.num_cchv % 2 == 1:
                self.num_cchv = int(self.num_cchv)

            self.cchv.value = round(self.num_cchv, 2)
            self.cchv.update()
            self.cchv.on_change(e)
            self.creven.update()
        except Exception as ex:
            print("Error en funcion conversion y captura crema chocolate: ", ex)
        finally:
            self.update()

    def conversion_n_capture_cca(self, e):
        if self.ccai.value == "" or self.ccaf.value == "":
            self.ccav.value = "---"
            self.ccav.update()
            if self.ccav.value == "---":
                if type(self.cov.value) != str and type(self.cchv.value) != str:
                    try:
                        self.creven.value = self.cov.value + self.cchv.value
                        self.creven.update()
                    except Exception as ex:
                        self.creven.value = ""
                        print("Error en suma: crema chocolate vendida + crema original vendida (funcion cac crema cafe) - Error:", ex)
                    return
                elif self.cchv.value != "" or self.cchv.value != "---":
                    self.creven.value = self.cchv.value
                elif self.cov.value != "" or self.cov.value != "---":
                    self.creven.value = self.cov.value
                else:
                    self.creven.value = ""
                self.creven.update()
            return

        try:
            if "." in self.ccai.value or "." in self.ccaf.value:
                self.num_ccaf = float(self.ccaf.value)
                self.num_ccai = float(self.ccai.value)
            else:
                self.num_ccaf = int(self.ccaf.value)
                self.num_ccai = int(self.ccai.value)

            self.num_ccav = self.num_ccai - self.num_ccaf

            if self.num_ccav % 2 == 0 or self.num_ccav % 2 == 1:
                self.num_ccav = int(self.num_ccav)

            self.ccav.value = round(self.num_ccav, 2)
            self.ccav.update()
            self.ccav.on_change(e)
            self.creven.update()
        except Exception as ex:
            print("Error en funcion conversion y captura crema cafe: ", ex)
        finally:
            self.update()

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
                if self.bging.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    self.bging.value = self.vvmt.value + self.tet.value
                    self.bgtd.value = self.bging.value
                self.tet.update()
                self.bging.update()
                self.bgtd.update()
            elif self.t5.value != "":
                self.tet.value = int(self.t5.value) * 5
                if self.bging.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    self.bging.value = self.vvmt.value + self.tet.value
                    self.bgtd.value = self.bging.value
                self.tet.update()
                self.bging.update()
                self.bgtd.update()
            elif self.t10.value != "":
                self.tet.value = int(self.t10.value) * 10
                if self.bging.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    self.bging.value = self.vvmt.value + self.tet.value
                    self.bgtd.value = self.bging.value
                self.tet.update()
                self.bging.update()
                self.bgtd.update()
            else:
                self.t5.value == "" and self.t10.value == ""
                self.tet.value = ""
                self.bging.value = self.vvmt.value
                self.bgtd.value = self.bging.value
                self.tet.update()
                self.bging.update()
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
                if self.bging.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    self.bging.value = self.vvmt.value + self.sdt.value
                    self.bgtd.value = self.bging.value
                self.sdt.update()
                self.bging.update()
                self.bgtd.update()
            elif self.sd20.value != "":
                self.sdt.value = int(self.sd20.value) * 20
                if self.bging.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    self.bging.value = self.vvmt.value + self.sdt.value
                    self.bgtd.value = self.bging.value
                self.sdt.update()
                self.bging.update()
                self.bgtd.update()
            elif self.sd35.value != "":
                self.sdt.value = int(self.sd35.value) * 35
                if self.bging.value != str:
                    self.vvmt.value = int(self.vvmt.value)
                    self.bging.value = self.vvmt.value + self.sdt.value
                    self.bgtd.value = self.bging.value
                self.sdt.update()
                self.bging.update()
                self.bgtd.update()
            else:
                self.sd20.value == "" and self.sd35.value == ""
                self.sdt.value = ""
                self.bging.value = self.vvmt.value
                self.bgtd.value = self.bging.value
                self.sdt.update()
                self.bging.update()
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
            self.bging.value = self.vvmt.value + self.tet.value + self.sdt.value
            self.bgtd.value = self.bging.value
            self.bging.update()
            self.bgtd.update()
        elif self.tet.value == "" and self.sdt.value != "":
            self.bging.value = self.vvmt.value + self.sdt.value
            self.bgtd.value = self.bging.value
            self.bging.update()
            self.bgtd.update()
        elif self.tet.value != "" and self.sdt.value == "":
            self.bging.value = self.vvmt.value + self.tet.value
            self.bgtd.value = self.bging.value
            self.bging.update()
            self.bgtd.update()
        else:
            self.bging.value = self.vvmt.value
            self.bgtd.value = self.bging.value
            self.bging.update()
            self.bgtd.update()
            
    #====================================#
    #     SUMA MONTOS TRANSFERENCIAS     #
    #====================================#

    def plus_trans(self, e):
        self.transfers = [self.tr1, self.tr2, self.tr3, self.tr4, self.tr5, self.tr6, self.tr7, self.tr8, self.tr9, self.tr10, self.tr11, self.tr12]

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
                # self.bgegr.value = self.trt.value
                self.trn.update()
                self.trt.update()
                # self.bgegr.update()

        self.trt.on_change(e)
        self.update()

    #======================================#
    #     SUMA MONTOS GASTOS | RETIROS     #
    #======================================#

    def plus_gasRes(self, e):
        self.gasret = [self.gr1, self.gr2, self.gr3, self.gr4, self.gr5, self.gr6]

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
                # self.bgegr.value = self.grt.value
                self.grn.update()
                self.grt.update()
                # self.bgegr.update()

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
            self.update()
        elif self.grt.value == "" and self.trt.value != "":
            self.bgegr.value = self.trt.value
            self.bgte.value = int(self.bgtd.value) - int(self.bgegr.value)
            self.bgegr.update()
            self.bgte.update()
            self.update()
        elif self.grt.value != "" and self.trt.value == "":
            self.bgegr.value = self.grt.value
            self.bgte.value = int(self.bgtd.value) - int(self.grt.value)
            self.bgegr.update()
            self.bgte.update()
            self.update()
        else:
            self.bgegr.value = int(self.trt.value) + int(self.grt.value)
            self.bgte.value = int(self.bgtd.value) - int(self.bgegr.value)
            self.bgegr.update()
            self.bgte.update()
            self.update()

        self.bging.update()
        self.bgegr.update()
        self.bgtd.update()
        self.bgte.update()
        self.update()

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

        self.variables_vm = [self.tmi, self.tmf, self.vmi, self.vmf, self.vmven, self.vmvt]
        for element in self.variables_vm:
            element.value = ""

        self.variables_vg = [self.tgi, self.tgf, self.vgi, self.vgf, self.vgven, self.vgvt]
        for element in self.variables_vg:
            element.value = ""

        self.variables_frutas = [self.fpi, self.fpf, self.fei, self.fef, self.fv, self.upi, self.upf, self.uei, self.uef, self.uv]
        for element in self.variables_frutas:
            element.value = ""

        self.variables_cremas = [self.coi, self.cof, self.cov, self.cchi, self.cchf, self.cchv, self.ccai, self.ccaf, self.ccav]
        for element in self.variables_cremas:
            element.value = ""

        self.extras = [self.t5, self.t10, self.tet, self.sd20, self.sd35, self.sdt, self.trn, self.trt, self.grn, self.grt, self.bging, self.bgegr, self.bgtd, self.bgte]
        for element in self.extras:
            element.value = ""

        self.variables_ventas = [self.fruven, self.creven, self.vtv, self.vvmt]
        for element in self.variables_ventas:
            element.value = ""

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
    page.bgcolor = "#181818"
    page.window.min_height = 680
    page.window.min_width = 920
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Control PDV's"
    page.window.maximized = True
    page.window.resizable = True
    # page.window_opacity = .95
    page.add(UI(page))

    """
    =============================
    #     FUNCION PRINCIPAL     #
    =============================
    """

    """ initial_dialog = ft.CupertinoAlertDialog(
        title=ft.Text("Bienvenido Gordillooouu"),
        actions=[
            ft.CupertinoDialogAction("Cerrar", is_destructive_action=True, on_click=lambda e: (page.close(e.control.parent), page.update()))
        ]
    ) """

    # page.open(initial_dialog)
    # page.update()
    
# ***** Web Mode *****
# ft.app(target=main, view=ft.WEB_BROWSER)

# ***** Desktop Mode *****
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
ft.app(target=main)