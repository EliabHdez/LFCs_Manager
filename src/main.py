import datetime as dt
import flet as ft
from fpdf import FPDF
import modules.created_Functions as cf

class UI(ft.ResponsiveRow):
    def __init__(self, page):
        super().__init__(expand=True)

        # ***** VARIABLES SISTEMA *****

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

        # self.color_teal = "teal"
        self.color_teal = "#00ebab"
        self.color_teal_2 = "#11b78a"

        # *** Variable Boton cambio de tema ***

        self.mode_switch = cf.create_Boton_Switch()

        # *** Variables Iconos Inferiores Barra de Navegacion Lateral ***

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

        # *** Variables Ventana Inicio ***

        # Variables Personal Supervision

        self.sup_Pers_PDV = cf.create_textfield_planeador(hint_Text="Ivette Herrera", hint_Style=ft.TextStyle(color="black", size=12, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, italic=True, weight=ft.FontWeight.BOLD))
        self.sup_Ops = cf.create_textfield_planeador(hint_Text="Omar Tovar", hint_Style=ft.TextStyle(color="black", size=12, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, italic=True, weight=ft.FontWeight.BOLD))
        self.sup_CDO = cf.create_textfield_planeador(hint_Text="Uriel Martínez", hint_Style=ft.TextStyle(color="black", size=12, italic=True, weight="bold"), text_Style=ft.TextStyle(color="black", size=12, italic=True, weight=ft.FontWeight.BOLD))

        # Variables Personal Ventas

        self.ven_Glorieta = cf.create_textfield_planeador(hint_Text="Valeria", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Vips = cf.create_textfield_planeador(hint_Text="Donovan Hdez", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_SanMiguel = cf.create_textfield_planeador(hint_Text="Uriel", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_SanAntonio = cf.create_textfield_planeador(hint_Text="Ivette", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Ensuenos = cf.create_textfield_planeador(hint_Text="Alejandra", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Operagua = cf.create_textfield_planeador(hint_Text="Victor", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_LaPiedad = cf.create_textfield_planeador(hint_Text="Isabel", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Cofradia2 = cf.create_textfield_planeador(hint_Text="Karla", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Parques = cf.create_textfield_planeador(hint_Text="Omar", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Cumbria = cf.create_textfield_planeador(hint_Text="Jesús", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Palomas = cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))
        self.ven_Atlanta = cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD), text_Style=ft.TextStyle(color="black", size=12, weight=ft.FontWeight.BOLD))

        # Variables Ventas Promedio

        self.cdo_1 = cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.cdo_2 = cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.cdo_3 = cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))

        # Variables Ventas Minimas

        self.vm_Glorieta = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_Vips = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_SanMiguel = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_SanAntonio = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_Ensuenos = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_Operagua = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_LaPiedad = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_Cofradia2 = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_Parques = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_Cumbria = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_Palomas = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.vm_Atlanta = cf.create_textfield_planeador(Value="$", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))

        # Variables Ventas Promedio

        self.prom_Glorieta = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_Vips = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_SanMiguel = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_SanAntonio = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_Ensuenos = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_Operagua = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_LaPiedad = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_Cofradia2 = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_Parques = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_Cumbria = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_Palomas = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))
        self.prom_Atlanta = cf.create_textfield_planeador(Value="$0", text_Style=ft.TextStyle(color="black", size=12, weight="bold"))

        # Variables sucursales

        self.glorieta = cf.create_radio("glorieta", "Glorieta")

        self.vips = cf.create_radio("vips", "Vips")

        self.sanmiguel = cf.create_radio("sanmiguel", "San Miguel")

        self.sanantonio = cf.create_radio("sanantonio", "San Antonio")

        self.ensuenos = cf.create_radio("ensueños", "Ensueños")

        self.operagua = cf.create_radio("operagua", "Operagua")

        self.lapiedad = cf.create_radio("lapiedad", "La Piedad")

        self.cofradia2 = cf.create_radio("cofradia2", "Cofradía 2")

        self.parques = cf.create_radio("parques", "Parques")

        self.cumbria = cf.create_radio("cumbria", "Cumbria")

        self.palomas = cf.create_radio("palomas", "Palomas")

        self.atlanta = cf.create_radio("atalanta", "Atlanta")

        self.pdv = ft.RadioGroup(# Grupo de Botones tipo Radio de las Sucursales
            on_change=self.pdv_selection,
            content=ft.Container(
                alignment=ft.alignment.center,
                padding=ft.Padding(top=2, bottom=2, left=2, right=4),
                # bgcolor="blue",
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    # expand=True,
                    controls=[
                        self.glorieta,
                        self.vips,
                        self.sanmiguel,
                        self.sanantonio,
                        self.ensuenos,
                        self.operagua,
                        self.lapiedad,
                        self.cofradia2,
                        self.parques,
                        self.cumbria,
                        self.palomas,
                        self.atlanta,
                    ]
                )
            )
        )

        # Variables Vasos Chicos

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tci = cf.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vc)
        self.tcf = cf.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vc)
        # self.tcdif = cf.create_textfield("Diferencia de...", suffix_Text="Tapas", read_Only=True)
        self.vci = cf.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vc)
        self.vcf = cf.create_textfield("Finales", suffix_Text="Vasos Finales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vc)
        # self.vcdif = cf.create_textfield("Diferencia", suffix_Text="Vasos", read_Only=True)
        # self.vcsv = cf.create_textfield("Sin vender", suffix_Text="Vasos", Color="#ffffff", read_Only=True)
        self.vcven = cf.create_textfield("Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True, on_Change=self.field_totalSale_vc)
        self.vcvt = cf.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)

        # Variables Vasos Medianos

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tmi = cf.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vm)
        self.tmf = cf.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vm)
        # self.tmdif = cf.create_textfield("Diferencia", read_Only=True)
        self.vmi = cf.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vm)
        self.vmf = cf.create_textfield("Finales", suffix_Text=" Vasos Finales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vm)
        # self.vmdif = cf.create_textfield("Diferencia", read_Only=True)
        # self.vmsv = cf.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vmven = cf.create_textfield("Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True)
        self.vmvt = cf.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)

        # Variables Vasos Grandes

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tgi = cf.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vg)
        self.tgf = cf.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vg)
        # self.tgdif = cf.create_textfield("Diferencia", read_Only=True)
        self.vgi = cf.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vg)
        self.vgf = cf.create_textfield("Finales", suffix_Text="Vasos Finales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vg)
        # self.vgdif = cf.create_textfield("Diferencia", read_Only=True)
        # self.vgsv = cf.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vgven = cf.create_textfield("Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True)
        self.vgvt = cf.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)

        # Variables Venta Total Vasos

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.vtv = cf.create_textfield_WB(Label="Vendidos", Color="#ffffff", text_Size=24, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", suffix_Text="Vasos ", read_Only=True)
        self.vvmt = cf.create_textfield_WB(Label="Venta Total", Color="#ffffff", text_Size=24, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), suffix_Text="MX ", read_Only=True)

        # ***** VARIABLES FRUTAS *****

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        # Fresa

        # self.tgi = cf.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=cf.Focus, on_Change=self.conversion_n_capture_vg)
        self.fpi = cf.create_textfield("Picada Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fpf = cf.create_textfield("Picada Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fei = cf.create_textfield("Entera Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fef = cf.create_textfield("Entera Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fv = cf.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", read_Only=True, on_Change=self.values_Fresa)
        # self.fr = cf.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

        # Uva

        self.upi = cf.create_textfield("Picada Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.upf = cf.create_textfield("Picada Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uei = cf.create_textfield("Entera Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uef = cf.create_textfield("Entera Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uv = cf.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", read_Only=True, on_Change=self.values_Uva)
        # self.ur = cf.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

        # ***** VARIABLES CREMAS *****

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        # Crema Original

        self.coi = cf.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.cof = cf.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.cov = cf.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaOriginal, read_Only=True)

        # Crema Chocolate

        self.cchi = cf.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_cch)
        self.cchf = cf.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_cch)
        self.cchv = cf.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaChocolate, read_Only=True)

        # Crema Cafe

        self.ccai = cf.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_cca)
        self.ccaf = cf.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_cca)
        self.ccav = cf.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", on_Change=self.values_cremaCafe, read_Only=True)

        # Variables Venta Total Vasos

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.fruven = cf.create_textfield_WB(Label="Fruta", Height=30, Color="#ffffff", text_Size=24, border_Color="#292929", Width=150, border_Width=.3, focused_Border_Color="#292929", suffix_Text="Botes ", read_Only=True)
        self.creven = cf.create_textfield_WB(Label="Cremas", Height=30, Color="#ffffff", text_Size=24, border_Color="#292929", Width=150, border_Width=.3, focused_Border_Color="#292929", suffix_Text="Botes ", read_Only=True)

        # ***** VARIABLES ADICIONALES Y EXTRAS *****

        # Opciones a configurar en la funcion create_textfield_Extras: Width, Height, Color="#d3d3d3", text_Size=12, border_Color=None, read_Only=False, on_Change=False

        # Toppings Extras

        self.t5 = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.conversion_n_capture_tE)
        self.t10 = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.conversion_n_capture_tE)
        self.tt = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", read_Only=True)

        # Servicios a Domicilio

        self.sd20 = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.conversion_n_capture_sD)
        self.sd35 = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="white", read_Only=False, on_Change=self.conversion_n_capture_sD)
        self.sdt = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", read_Only=True)

        # Transferencias

        self.trn = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=80, Height=35, border_Color="white", read_Only=False)
        self.trt = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=100, Height=35, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", prefix_Text="$", content_Padding=ft.padding.symmetric(horizontal=10, vertical=0), read_Only=False)

        # Gastos / Retiros

        self.grn = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=80, Height=35, border_Color="white", read_Only=False)
        self.grt = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=100, Height=35, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", read_Only=False)

        # Balance

        self.bging = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", read_Only=True)
        self.bgegr = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", read_Only=True)
        self.bgtd = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", read_Only=True, on_Change=self.balance_General)
        self.bgte = cf.create_textField_Extras(text_Size=15, text_Style=None, Color="white", Width=None, Height=40, border_Color="#ff0b0b", border_Width=1.5, focused_Border_Color="#750000", read_Only=True)

        # ***** VARIABLES VENTANA VENTAS *****

        # *** Variables Campos de texto y Botones ***

        # Campos de texto

        self.report_field = cf.create_textField_RyV("REPORTE", min_Lines=25, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=5, size=10))
        self.sales_field = cf.create_textField_RyV("EXTRAS", min_Lines=25, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=5, size=10), read_Only=False)

        self.transf_field = cf.create_textField_RyV("MONTOS TRANSFERENCIAS", min_Lines=10, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=3, size=8), read_Only=False)
        self.gastos_field = cf.create_textField_RyV("MONTOS GASTOS / RETIROS", min_Lines=10, counter_Style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=3, size=8), read_Only=False)

        # ***** BARRA DE NAVEGACION LATERAL IZQUIERDA *****

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

        # ***** BARRA DE SELECCION DE SUCURSALES *****

        self.select_Bar_Sucursales = ft.Container(# Puntos de venta
            alignment=ft.alignment.center,
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

        # ***** BARRA DE BOTONOS DE ACCION *****

        self.actions_Buttons = ft.Container(# Puntos de venta
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.BLUE_GREY_900,
            border_radius=10,
            content=ft.ResponsiveRow(
                vertical_alignment="center",
                alignment="center",
                controls=[
                    ft.Container(# Reset Button
                        col=3,
                        padding=ft.padding.symmetric(horizontal=60, vertical=10),
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
                            content=cf.created_Button(Text="Limpiar Campos", bgColor=self.color_teal, Icon=ft.Icons.CLEAR_ALL, on_Click=self.reset_Fields)
                        ),
                    ),
                    ft.Container(# Borrar Seccion especifica
                        col=3,
                        # bgcolor=ft.Colors.BLUE_GREY_900,
                        padding=ft.padding.symmetric(horizontal=60, vertical=10),
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
                            content=cf.created_Button(Text="Borrado puntual", bgColor=self.color_teal, Icon=ft.Icons.CLEAR, on_Click=self.reset_Fields)
                        ),
                    ),
                    ft.Container(# Preview View Button
                        col=3,
                        bgcolor=ft.Colors.BLUE_GREY_900,
                        border_radius=10,
                        padding=ft.padding.symmetric(horizontal=60, vertical=10),
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
                            content=cf.created_Button(Text="Vista previa", bgColor=self.color_teal, Icon=ft.Icons.DOCUMENT_SCANNER_OUTLINED, on_Click=self.generar_Reporte)
                        ),
                    ),
                    ft.Container(# Report Button
                        col=3,
                        bgcolor=ft.Colors.BLUE_GREY_900,
                        border_radius=10,
                        padding=ft.padding.symmetric(horizontal=60, vertical=10),
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
                            content=cf.created_Button(Text="Añadir a Reporte", bgColor=self.color_teal, Icon=ft.Icons.NOTE_ADD_OUTLINED, on_Click=self.generar_Reporte)
                        ),
                    ),
                ]
            )
        )

        # ***** PAGINA INICIO *****

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
                                    thickness=3,
                                    # leading_indent=50,
                                    # trailing_indent=10
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
                                                        expand=True,
                                                        # bgcolor="blue",
                                                        alignment=ft.alignment.center,
                                                        col=4,
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Container(# Supervisores
                                                                    expand=True,
                                                                    # bgcolor="yellow",
                                                                    alignment=ft.alignment.center,
                                                                    content=ft.ResponsiveRow(
                                                                        spacing=0,
                                                                        controls=[
                                                                            ft.Container(
                                                                                col=1,
                                                                                border_radius=ft.border_radius.only(top_left=3),
                                                                                # expand=True,
                                                                                # height=142,
                                                                                bgcolor="#6adb00",
                                                                                alignment=ft.alignment.center,
                                                                                border=ft.border.all(color="black", width=.5),
                                                                                content=ft.Column(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    horizontal_alignment="center",
                                                                                    spacing=0,
                                                                                    controls=[
                                                                                        ft.Text("S", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("U", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("P", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("E", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("R", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("V", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("I", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("S", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("I", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("O", color="black", size=6.5, weight="bold"),
                                                                                        ft.Text("N", color="black", size=6.5, weight="bold"),
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
                                                                                        content=ft.Text("Supervisor de Personal y PDV", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        padding=5,
                                                                                        # height=45,
                                                                                        bgcolor="#6adb00",
                                                                                        content=ft.Text("Supervisor de Operaciones", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        padding=5,
                                                                                        # height=45,
                                                                                        bgcolor="#6adb00",
                                                                                        content=ft.Text("Supervisor de CDO", color="black", size=10)
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
                                                                    ),
                                                                ),
                                                                ft.Container(# Supervisores
                                                                    # expand=True,
                                                                    height=300,
                                                                    alignment=ft.alignment.center,
                                                                    content=ft.ResponsiveRow(
                                                                        spacing=0,
                                                                        controls=[
                                                                            ft.Container(
                                                                                col=1,
                                                                                border_radius=ft.border_radius.only(bottom_left=3),
                                                                                bgcolor="#fe0f7c",
                                                                                alignment=ft.alignment.center,
                                                                                border=ft.border.all(color="black", width=.5),
                                                                                content=ft.Column(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    horizontal_alignment="center",
                                                                                    spacing=0,
                                                                                    controls=[
                                                                                        ft.Text("S", color="black", size=14, weight="bold"),
                                                                                        ft.Text("U", color="black", size=14, weight="bold"),
                                                                                        ft.Text("C", color="black", size=14, weight="bold"),
                                                                                        ft.Text("U", color="black", size=14, weight="bold"),
                                                                                        ft.Text("R", color="black", size=14, weight="bold"),
                                                                                        ft.Text("S", color="black", size=14, weight="bold"),
                                                                                        ft.Text("A", color="black", size=14, weight="bold"),
                                                                                        ft.Text("L", color="black", size=14, weight="bold"),
                                                                                        ft.Text("E", color="black", size=14, weight="bold"),
                                                                                        ft.Text("S", color="black", size=14, weight="bold"),
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            ft.Column(
                                                                                col=6,
                                                                                horizontal_alignment="center",
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("1 - VP Glorieta", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("2 - VP Vips", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("3 - VP San Miguel", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("4 - VP San Antonio", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("5 - VP Ensueños", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("6 - VP Operagua", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("7 - VP La Piedad", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("8 - VP Cofradía 2", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("9 - VP Parques", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("10 - VP Cumbria", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("11 - VP Palomas", color="black", size=10)
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center_left,
                                                                                        border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="#fe0f7c",
                                                                                        padding=ft.padding.only(left=5),
                                                                                        content=ft.Text("12 - VP Atlanta", color="black", size=10)
                                                                                    )
                                                                                ]
                                                                            ),
                                                                            ft.Column(
                                                                                col=5,
                                                                                horizontal_alignment="center",
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Glorieta
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Vips
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_SanMiguel
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_SanAntonio
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Ensuenos
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Operagua
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_LaPiedad
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Cofradia2
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Parques
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Cumbria
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Palomas
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=25,
                                                                                        bgcolor="white",
                                                                                        content=self.ven_Atlanta
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    ft.Container(# Ventas mínimas
                                                        alignment=ft.alignment.center,
                                                        col=2,
                                                        
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Column(
                                                                    expand=True,
                                                                    spacing=0,
                                                                    controls=[
                                                                        ft.Container(
                                                                            expand=True,
                                                                            border=ft.border.all(width=.5, color="black"),
                                                                            bgcolor="white",
                                                                            alignment=ft.alignment.center,
                                                                            content=ft.Text("Ventas mínimas\ndel día", size=20, color="black", text_align="center"),
                                                                        ),
                                                                    ]
                                                                ),
                                                                ft.Column(
                                                                    spacing=0,
                                                                    controls=[
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Glorieta
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Vips
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_SanMiguel
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_SanAntonio
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Ensuenos
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Operagua
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_LaPiedad
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Cofradia2
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Parques
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Cumbria
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Palomas
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.vm_Atlanta
                                                                        ),
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Promedio
                                                        alignment=ft.alignment.center,
                                                        col=1,
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Column(
                                                                    expand=True,
                                                                    controls=[
                                                                        ft.Container(
                                                                            expand=True,
                                                                            border=ft.border.all(width=.5, color="black"),
                                                                            alignment=ft.alignment.center,
                                                                            bgcolor="white",
                                                                            content=ft.Text("Promedio", color="black")
                                                                        )
                                                                    ]
                                                                ),
                                                                ft.Column(
                                                                    spacing=0,
                                                                    controls=[
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Glorieta
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Vips
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_SanMiguel
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_SanAntonio
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Ensuenos
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Operagua
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_LaPiedad
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Cofradia2
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Parques
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Cumbria
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Palomas
                                                                        ),
                                                                        ft.Container(
                                                                            height=25,
                                                                            alignment=ft.alignment.center,
                                                                            # border=ft.border.all(color="black", width=1),
                                                                            bgcolor="white",
                                                                            content=self.prom_Atlanta
                                                                        ),
                                                                    ]
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
                                                                                        content=cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
                                                                                    ),
                                                                                    ft.Container(
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        height=30,
                                                                                        bgcolor="white",
                                                                                        content=cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand=True,
                                                                                        alignment=ft.alignment.center,
                                                                                        # border=ft.border.all(color="black", width=.5),
                                                                                        bgcolor="white",
                                                                                        content=cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
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
                                                                                        content=cf.create_textfield_planeador(hint_Text="---", hint_Style=ft.TextStyle(color="black", size=12, weight="bold"))
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
                        ft.Container(# Botones parte inferior planeador
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
                                        content=cf.created_Button(Text="Personal", bgColor=self.color_teal, Icon=None, on_Click=self.personal)
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
                                        content=cf.created_Button(Text="Lunes", bgColor=self.color_teal, Icon=None, on_Click=None)
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
                                        content=cf.created_Button(Text="Martes", bgColor=self.color_teal, Icon=None, on_Click=None)
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
                                        content=cf.created_Button(Text="Miércoles", bgColor=self.color_teal, Icon=None, on_Click=None)
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
                                        content=cf.created_Button(Text="Jueves", bgColor=self.color_teal, Icon=None, on_Click=None)
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
                                        content=cf.created_Button(Text="Viernes", bgColor=self.color_teal, Icon=None, on_Click=None)
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
                                        content=cf.created_Button(Text="Sábado", bgColor=self.color_teal, Icon=None, on_Click=None)
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
                                        content=cf.created_Button(Text="Domingo", bgColor=self.color_teal, Icon=None, on_Click=None)
                                    ),
                                ]
                            ),
                        )
                    ]
                )
            )
        )

        # ***** PAGINA DE REGISTRO *****

        self.register = ft.Container(# Ventana Inicio
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
                                            ft.ResponsiveRow(
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
                                                    ft.Container(# Vasos
                                                        expand=True,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="#292929",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        padding=ft.Padding(top=5, bottom=20, left=0, right=0),
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            controls=[
                                                                ft.Container(# Vasos Chicos
                                                                    alignment=ft.alignment.center,
                                                                    # bgcolor="blue",
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                        horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* VASOS CHICOS *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            ft.Container(# Vasos Chicos
                                                                                alignment=ft.alignment.center,
                                                                                margin=ft.margin.only(bottom=15),
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Tapas chicas iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.tci
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Tapas chicos finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.tcf
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Vasos chicos inciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.vci
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Vasos chicos finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(# Vasos Chicos
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.vcf
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Vasos chicos vendidos
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.vcven
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Venta total vasos chicos
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor="#f00000",
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
                                                                    alignment=ft.alignment.center,
                                                                    # bgcolor="blue",
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                        horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* VASOS MEDIANOS *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            ft.Container(# Vasos Medianos
                                                                                alignment=ft.alignment.center,
                                                                                margin=ft.margin.only(bottom=15),
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Tapas medianas iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.tmi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Tapas medianas finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.tmf
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# vasos medianos iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.vmi
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Vasos medianos finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(# Vasos Chicos
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.vmf
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Vasos medianos vendidos
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.vmven
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Venta total vasos medianos
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor="#f00000",
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
                                                                    alignment=ft.alignment.center,
                                                                    # bgcolor="blue",
                                                                    content=ft.Column(
                                                                        horizontal_alignment="center",
                                                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                        controls=[
                                                                            ft.Text("* VASOS GRANDES *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            ft.Container(# Vasos Grandes
                                                                                alignment=ft.alignment.center,
                                                                                # bgcolor="pink",
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Tapas grandes iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.tgi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Tapas grandes finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.tgf
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Vasos grandes inciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.vgi
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Vasos grandes finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(# Vasos Chicos
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.vgf
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Vasos grandes vendidos
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                border_radius=5,
                                                                                                content=self.vgven
                                                                                            ),
                                                                                        ),
                                                                                        ft.Container(# Venta total vasos grandes
                                                                                            alignment=ft.alignment.center,
                                                                                            col=2,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor="#f00000",
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
                                                        )
                                                    ),
                                                    ft.Container(# Venta Total Vasos en General
                                                        # bgcolor="yellow",
                                                        padding=10,
                                                        alignment=ft.alignment.center,
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Container(# Venta Total Vasos en General
                                                                    alignment=ft.alignment.center,
                                                                    padding=ft.padding.only(bottom=7),
                                                                    # bgcolor="blue",
                                                                    content=ft.Text("VENTA GENERAL VASOS", color="#bfc244", weight=ft.FontWeight.BOLD, size=20, style=ft.TextStyle(letter_spacing=10)),
                                                                ),
                                                                ft.Container(# Venta Total Vasos en General
                                                                    alignment=ft.alignment.center,
                                                                    padding=ft.padding.only(bottom=3),
                                                                    # bgcolor="pink",
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Total Vasos Vendidos
                                                                                col=2.5,
                                                                                alignment=ft.alignment.center,
                                                                                bgcolor="#292929",
                                                                                padding=3,
                                                                                border=ft.border.all(width=1, color="#292929"),
                                                                                border_radius=5,
                                                                                margin=ft.margin.only(right=60),
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
                                                                                col=2.5,
                                                                                alignment=ft.alignment.center,
                                                                                bgcolor="#292929",
                                                                                padding=3,
                                                                                border=ft.border.all(width=1, color="#292929"),
                                                                                border_radius=5,
                                                                                margin=ft.margin.only(left=60),
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
                                                                                    content=ft.Text("TOPPINGS", style=ft.TextStyle(letter_spacing=5))
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
                                                                                            content=self.tt
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
                                                                                    content=ft.Text("SERVICIOS A DOMICILIO", style=ft.TextStyle(letter_spacing=3.5))
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
                                                                                                        content=ft.Text("INGRESOS"),
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
                                                                                                        content=ft.Text("EGRESOS"),
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
                                                                                                        padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                                                                                        content=ft.Column(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    expand=True,
                                                                                                                    col=5,
                                                                                                                    alignment=ft.alignment.center,
                                                                                                                    # bgcolor="blue",
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
                                                                                                                        content=self.transf_field
                                                                                                                    )
                                                                                                                ),
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
                                                                                    content=ft.Text("GASTOS / RETIROS", style=ft.TextStyle(letter_spacing=5))
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
                                                                                                                                content=ft.Text("NO. GASTOS / RETIROS"),
                                                                                                                            ),
                                                                                                                            ft.Container(
                                                                                                                                content=self.grn
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
                                                                                                                                content=ft.Text("TOTAL GASTOS / RETIROS"),
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
                                                                                                        padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                                                                                        content=ft.Column(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    expand=True,
                                                                                                                    col=5,
                                                                                                                    alignment=ft.alignment.center,
                                                                                                                    # bgcolor="blue",
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
                                                                                                                        content=self.gastos_field
                                                                                                                    )
                                                                                                                ),
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

        # ***** PAGINA VENTAS *****

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
                                ft.Column(# Dropdowns para fecha
                                    col=12,
                                    controls=[
                                        ft.Container(
                                            # bgcolor="pink",
                                            margin=ft.margin.only(top=20),
                                            padding=ft.padding.symmetric(horizontal=50, vertical=0),
                                            content=ft.ResponsiveRow(
                                                # spacing=30,
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                vertical_alignment="center",
                                                controls=[
                                                    ft.Container(
                                                        col=3,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="black",
                                                        content=ft.Dropdown(
                                                            width=180,
                                                            bgcolor="black",
                                                            color="white",
                                                            fill_color="#555555",
                                                            # fill_color=self.color_teal,
                                                            filled=True,
                                                            label_style=ft.TextStyle(color="white"),
                                                            border_color=self.color_teal,
                                                            border_width=1.5,
                                                            focused_border_color=self.color_teal_2,
                                                            focused_border_width=3,
                                                            label="Ventas / Reportes",
                                                            hint_text="Selecciona una opción",
                                                            options=[
                                                                ft.dropdown.Option("Ventas"),
                                                                ft.dropdown.Option("Reportes"),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Dias
                                                        col=3,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="black",
                                                        content=ft.Dropdown(
                                                            width=180,
                                                            bgcolor="black",
                                                            color="white",
                                                            fill_color="#555555",
                                                            # fill_color=self.color_teal,
                                                            filled=True,
                                                            label_style=ft.TextStyle(color="white"),
                                                            border_color=self.color_teal,
                                                            border_width=1.5,
                                                            focused_border_color=self.color_teal_2,
                                                            focused_border_width=3,
                                                            label="Dia",
                                                            hint_text="Selecciona el día",
                                                            options=[
                                                                ft.dropdown.Option("1"),
                                                                ft.dropdown.Option("2"),
                                                                ft.dropdown.Option("3"),
                                                                ft.dropdown.Option("4"),
                                                                ft.dropdown.Option("5"),
                                                                ft.dropdown.Option("6"),
                                                                ft.dropdown.Option("7"),
                                                                ft.dropdown.Option("8"),
                                                                ft.dropdown.Option("9"),
                                                                ft.dropdown.Option("10"),
                                                                ft.dropdown.Option("11"),
                                                                ft.dropdown.Option("12"),
                                                                ft.dropdown.Option("13"),
                                                                ft.dropdown.Option("14"),
                                                                ft.dropdown.Option("15"),
                                                                ft.dropdown.Option("16"),
                                                                ft.dropdown.Option("17"),
                                                                ft.dropdown.Option("18"),
                                                                ft.dropdown.Option("19"),
                                                                ft.dropdown.Option("20"),
                                                                ft.dropdown.Option("21"),
                                                                ft.dropdown.Option("22"),
                                                                ft.dropdown.Option("23"),
                                                                ft.dropdown.Option("24"),
                                                                ft.dropdown.Option("25"),
                                                                ft.dropdown.Option("26"),
                                                                ft.dropdown.Option("27"),
                                                                ft.dropdown.Option("28"),
                                                                ft.dropdown.Option("29"),
                                                                ft.dropdown.Option("30"),
                                                                ft.dropdown.Option("31"),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Meses
                                                        col=3,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="black",
                                                        content=ft.Dropdown(
                                                            width=180,
                                                            bgcolor="black",
                                                            color="white",
                                                            fill_color="#555555",
                                                            # fill_color=self.color_teal,
                                                            filled=True,
                                                            label_style=ft.TextStyle(color="white"),
                                                            border_color=self.color_teal,
                                                            border_width=1.5,
                                                            focused_border_color=self.color_teal_2,
                                                            focused_border_width=3,
                                                            label="Mes",
                                                            hint_text="Selecciona el Mes",
                                                            options=[
                                                                ft.dropdown.Option("Enero"),
                                                                ft.dropdown.Option("Febrero"),
                                                                ft.dropdown.Option("Marzo"),
                                                                ft.dropdown.Option("Abril"),
                                                                ft.dropdown.Option("Mayo"),
                                                                ft.dropdown.Option("Junio"),
                                                                ft.dropdown.Option("Julio"),
                                                                ft.dropdown.Option("Agosto"),
                                                                ft.dropdown.Option("Septiembre"),
                                                                ft.dropdown.Option("Octubre"),
                                                                ft.dropdown.Option("Noviembre"),
                                                                ft.dropdown.Option("Diciembre"),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Años
                                                        col=3,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor=self.color_teal,
                                                        content=ft.Dropdown(
                                                            width=180,
                                                            bgcolor="black",
                                                            color="white",
                                                            fill_color="#555555",
                                                            # fill_color=self.color_teal,
                                                            filled=True,
                                                            label="Año",
                                                            label_style=ft.TextStyle(color="white"),
                                                            border_color=self.color_teal,
                                                            border_width=1.5,
                                                            focused_border_color=self.color_teal_2,
                                                            focused_border_width=3,
                                                            hint_text="Selecciona el Año",
                                                            options=[
                                                                ft.dropdown.Option("2024"),
                                                                ft.dropdown.Option("2025"),
                                                                ft.dropdown.Option("2026"),
                                                                ft.dropdown.Option("2027"),
                                                                ft.dropdown.Option("2028"),
                                                                ft.dropdown.Option("2029"),
                                                                ft.dropdown.Option("2030"),
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        )
                                    ]
                                ),
                            ]
                        ),
                         ft.Column(# Campos de texto y archivos
                            expand=True,
                            controls=[
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
                                                                        content=cf.created_Button(Text="Crear Reporte PDF", bgColor=self.color_teal, Icon=ft.Icons.ADD)
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=cf.created_Button(Text="Exportar Archivo", bgColor=self.color_teal, Icon=ft.Icons.UPLOAD, on_Click=self.create_ReportePDF)
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=cf.created_Button(Text="Borrar Archivo", bgColor=self.color_teal, Icon=ft.Icons.DELETE)
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=cf.created_Button(Text="Limpiar Campos", bgColor=self.color_teal, Icon=ft.Icons.CLEAR_ALL, on_Click=self.reset_textFields)
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
                    ]
                )
            )
        )

        # ***** PAGINA PUNTOS DE VENTAS *****

        self.pos = ft.Row(
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

        # ***** PAGINA INVENTARIO *****

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

        # ***** Paginas de los respectivos elementos laterales encerrados en una lista para el control de estas con los elementos laterales *****


        self.pages_containers = [self.home, ft.Column(controls=[self.select_Bar_Sucursales, self.register, self.actions_Buttons]), self.sales, self.pos, self.stock]

        # ***** Seleccion de la pagina a mostrar mediante el index relacionado con el NavigationRail *****

        self.main_container = ft.Container(content=self.pages_containers[0], expand=True)

        # ***** Variable principal encargada de almacenar las diferentes paginas relacionadas con los elementos laterales *****

        self.pages = ft.Container(
            col=11.25,
            # expand=True,
            content=ft.Column(
                controls=[
                    self.main_container,
                ]
            )
        )

        # ***** FILA PRINCIPAL DE LA PAGINA (ABARCA TODA LA VENTANA Y ES DONDE SE PONE CADA UNA DE LAS SECCIONES QUE VAN A VERSE EN LA PAGINA) *****

        self.main_pages = ft.ResponsiveRow(
            controls=[
                self.navigation_bar,
                self.pages
            ]
        )

        self.controls.append(self.main_pages)

    # ***** FUNCIONES *****

    #  *** Funcion para el manejo del cambio de ventanas mediante la barra lateral de navegacion ***

    def change_page(self, e):
        index = e.control.selected_index
        self.main_container.content = self.pages_containers[index]
        self.update()

    # *** Funcion para el manejo de los radios boton's y la seleccion de las sucursales ***

    def pdv_selection(self, e):
        if e.control.value == "glorieta":
            self.pdv = "Suc. Glorieta"
        elif e.control.value == "sanmiguel":
            self.pdv = "Suc. San Miguel"
        elif e.control.value == "vips":
            self.pdv = "Suc. Vips"
        elif e.control.value == "cofradia2":
            self.pdv = "Suc. Cofradía 2"
        elif e.control.value == "ensueños":
            self.pdv = "Suc. Ensueños"
        elif e.control.value == "operagua":
            self.pdv = "Suc. Operagua"
        elif e.control.value == "sanantonio":
            self.pdv = "Suc. San Antonio"
        elif e.control.value == "lapiedad":
            self.pdv = "Suc. La Piedad"

    # *** Funcion para el generar el reporte y cargarlo en el textfield de la ventana de ventas ***

    def generar_Reporte(self, e):
        # print(f"La sucursal seleccionada es: {e.control.value}")
        self.fecha_Actual = dt.datetime.today().date()

        self.fecha_Formateada = self.fecha_Actual.strftime("%d-%b-%Y")

        self.report_field.value = (
                                f"                                                   {self.fecha_Formateada}\n\n"
                                f"<<< {self.pdv} >>>\n\n"
                                f"- VASOS -\n\n"
                                f"Vasos Chicos: TI-{self.tci.value} / TP-{self.tcf.value} / VI-{self.vci.value} / VF-{self.vcf.value} / VV-{self.vcven.value}\n / Venta: ${self.vcvt.value}\n"
                                f"Vasos Medianos: TI-{self.tmi.value} / TP-{self.tmf.value} / VI-{self.vmi.value} / VF-{self.vmf.value} / VV-{self.vmven.value}\n / Venta: ${self.vmvt.value}\n"
                                f"Vasos Grandes: TI-{self.tgi.value} / TP-{self.tgf.value} / VI-{self.vgi.value} / VF-{self.vgf.value} / VV-{self.vgven.value}\n / Venta: ${self.vgvt.value}\n\n"
                                f"- FRUTA -\n\n"
                                f"Fresa: PI-{self.fpi.value} / PF-{self.fpf.value} / EI-{self.fei.value} / EF-{self.fef.value} / Vendida-{self.fv.value}\n"
                                f"Uva: PI-{self.upi.value} / PF-{self.upf.value} / EI-{self.uei.value} / EF-{self.uef.value} / Vendida-{self.uv.value}\n\n"
                                f"- CREMAS -\n\n"
                                f"Crema Original: I-{self.coi.value} / F-{self.cof.value} / Vendida-{self.cov.value}\n\n"
                                f"Crema Chocolate: I-{self.cchi.value} / F-{self.cchf.value} / Vendida-{self.cchv.value}\n\n"
                                f"Crema Cafe: I-{self.ccai.value} / F-{self.ccaf.value} / Vendida-{self.ccav.value}\n\n"
                                f"- TOPPINGS -\n\n"
                                f"Toppings Extras: TE5-{self.t5.value} / TE10-{self.t10.value} / Total: ${self.tt.value}\n\n"
                                f"- SERVICIOS A DOMICILIO -\n\n"
                                f"Servivios a Domicilio: SD25-{self.sd25.value} / SD35-{self.sd35.value} / Total: ${self.sdt.value}\n\n"
                                f"- TRANSFERENCIAS -\n\n"
                                f"Transferencias: No TRANSFERENCIAS-{self.trn.value} / Monto Total: ${self.trt.value}\n\n"
                                f"- GASTOS / RETIROS -\n\n"
                                f"Gastos y/o Retiros: Cantidad-{self.grn.value} / Monto Total: ${self.grt.value}\n\n"
                                f"- INGRESOS / EGRESOS -\n\n"
                                f"Ingresos: Monto Total: ${self.bgi.value}\n"
                                f"Egresos (G/R/T): Monto Total: ${self.bgd.value}\n\n"
                                f"- TOTAL DIA PDV -\n\n"
                                f"Total General: ${self.bgi.value}\n"
                                f"Total Efectivo: ${self.bgt.value}\n\n"

                                f"<<< FIN DEL REPORTE >>>"
                            )

    # *** Funcion creadora del reporte del dia en formato PDF ***

    def create_ReportePDF(self, e):
        self.fecha_Actual = dt.datetime.today().date()

        self.fecha_Formateada = self.fecha_Actual.strftime("%d-%b-%Y")

        self.fecha_Formateada_RN = self.fecha_Actual.strftime("%d-%m-%y")

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font("Arial", "", 10)

        pdf.image("assets/Images/FresaReporte.png", 10, 7, 20)
        pdf.cell(187, 5, f'{self.fecha_Formateada}', 0, 1, "R")

        # Titulo
        pdf.cell(0, 25, f'Reporte {self.pdv}'.upper(), 0, 1, 'C')
        pdf.line(70, 30, 140, 30)

        # pdf.cell(0, 5, '', 0, 1)

        # Vasos
        pdf.cell(70, 10, 'VASOS', 1, 0, "C")
        pdf.cell(15, 10, f'TI', 1, 0, 'C')
        pdf.cell(15, 10, f'TF', 1, 0, 'C')
        pdf.cell(15, 10, f'VI', 1, 0, 'C')
        pdf.cell(15, 10, f'VF', 1, 0, 'C')
        pdf.cell(25, 10, f'VENDIDOS', 1, 0, 'C')
        pdf.cell(35, 10, f'MONTO VENTA', 1, 1, 'C')
        pdf.cell(70, 8, 'VASOS CHICOS', 1, 0)
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(25, 8, f'', 1, 0, 'C')
        pdf.cell(35, 8, f'$ ', 1, 1, 'C')
        pdf.cell(70, 8, 'VASOS MEDIANOS', 1, 0)
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(25, 8, f'', 1, 0, 'C')
        pdf.cell(35, 8, f'$ ', 1, 1, 'C')
        pdf.cell(70, 8, 'VASOS GRANDES', 1, 0)
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(15, 8, f'', 1, 0, 'C')
        pdf.cell(25, 8, f'', 1, 0, 'C')
        pdf.cell(35, 8, f'$ ', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        # Frutas Y Cremas
        # pdf.cell(100, 10, 'FRUTAS', 1, 0, "C")

        # pdf.cell(5, 10, '', 0, 0)

        # pdf.cell(85, 10, 'CREMAS', 1, 1, "C")

        pdf.cell(30, 10, f'FRUTA', 1, 0, 'C')
        pdf.cell(11, 10, f'PI', 1, 0, 'C')
        pdf.cell(11, 10, f'PF', 1, 0, 'C')
        pdf.cell(11, 10, f'EI', 1, 0, 'C')
        pdf.cell(11, 10, f'EF', 1, 0, 'C')
        pdf.cell(26, 10, f'VENDIDOS', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(35, 10, f'CREMA', 1, 0, 'C')
        pdf.cell(12.5, 10, f'IN', 1, 0, 'C')
        pdf.cell(12.5, 10, f'FI', 1, 0, 'C')
        pdf.cell(25, 10, f'VENDIDOS', 1, 1, 'C')

        pdf.cell(30, 8, 'FRESA', 1, 0)
        pdf.cell(11, 8, f'', 1, 0, 'C')
        pdf.cell(11, 8, f'', 1, 0, 'C')
        pdf.cell(11, 8, f'', 1, 0, 'C')
        pdf.cell(11, 8, f'', 1, 0, 'C')
        pdf.cell(26, 8, f'', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(35, 8, 'CR ORIGINAL', 1, 0)
        pdf.cell(12.5, 8, f'', 1, 0, 'C')
        pdf.cell(12.5, 8, f'', 1, 0, 'C')
        pdf.cell(25, 8, f'', 1, 1, 'C')

        pdf.cell(30, 8, 'UVA', 1, 0)
        pdf.cell(11, 8, f'', 1, 0, 'C')
        pdf.cell(11, 8, f'', 1, 0, 'C')
        pdf.cell(11, 8, f'', 1, 0, 'C')
        pdf.cell(11, 8, f'', 1, 0, 'C')
        pdf.cell(26, 8, f'', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(35, 8, 'CR CHOCOLATE', 1, 0)
        pdf.cell(12.5, 8, f'', 1, 0, 'C')
        pdf.cell(12.5, 8, f'', 1, 0, 'C')
        pdf.cell(25, 8, f'', 1, 1, 'C')

        pdf.cell(30, 8, '', 0, 0)
        pdf.cell(10, 8, f'', 0, 0,)
        pdf.cell(10, 8, f'', 0, 0,)
        pdf.cell(10, 8, f'', 0, 0,)
        pdf.cell(10, 8, f'', 0, 0,)
        pdf.cell(30, 8, f'', 0, 0,)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(35, 8, 'CR CAFE', 1, 0)
        pdf.cell(12.5, 8, f'', 1, 0, 'C')
        pdf.cell(12.5, 8, f'', 1, 0, 'C')
        pdf.cell(25, 8, f'', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        pdf.cell(45, 10, f'TOPPINGS EXTRA', 1, 0, 'C')
        pdf.cell(25, 10, f'CANTIDAD', 1, 0, 'C')
        pdf.cell(20, 10, f'TOTAL', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(50, 10, f'SERVICIOS A DOMICILIO', 1, 0, 'C')
        pdf.cell(25, 10, f'CANTIDAD', 1, 0, 'C')
        pdf.cell(20, 10, f'TOTAL', 1, 1, 'C')

        pdf.cell(45, 10, f'TOPPING 5', 1, 0, 'C')
        pdf.cell(25, 10, f'', 1, 0, 'C')
        pdf.cell(20, 10, f'$ ', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(50, 10, f'SERV DOM 25', 1, 0, 'C')
        pdf.cell(25, 10, f'', 1, 0, 'C')
        pdf.cell(20, 10, f'$ ', 1, 1, 'C')

        pdf.cell(45, 10, f'TOPPING 10', 1, 0, 'C')
        pdf.cell(25, 10, f'', 1, 0, 'C')
        pdf.cell(20, 10, f'$ ', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(50, 10, f'SERV DOM 35', 1, 0, 'C')
        pdf.cell(25, 10, f'', 1, 0, 'C')
        pdf.cell(20, 10, f'$ ', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        pdf.cell(90, 10, f'TRANSFERENCIAS', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(95, 10, f'GASTOS Y RETIROS', 1, 1, 'C')

        # pdf.cell(30, 10, f'MONTOS', 1, 0, 'C')
        pdf.cell(60, 10, f'NO. DE TRANSFERENCIAS', 1, 0, 'C')
        pdf.cell(30, 10, f'TOTAL', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        # pdf.cell(30, 10, f'MONTOS', 1, 0, 'C')
        pdf.cell(60, 10, f'NO. DE GASTOS / RETIROS', 1, 0, 'C')
        pdf.cell(35, 10, f'TOTAL', 1, 1, 'C')

        pdf.cell(60, 10, f'', 1, 0, 'C')
        pdf.cell(30, 10, f'$ ', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(60, 10, f'', 1, 0, 'C')
        pdf.cell(35, 10, f'$ ', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        pdf.cell(90, 12, f'MONTOS TRANSFERENCIAS Y GASTOS / RETIROS', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(95, 12, f'INGRESOS Y EGRESOS', 1, 1, 'C')

        pdf.cell(45, 7, f'TRANSFERENCIAS', 1, 0, 'C')
        pdf.cell(45, 7, f'GASTOS / RETIROS', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(47.5, 7, f'CONCEPTO', 1, 0, 'C')
        pdf.cell(47.5, 7, f'MONTO', 1, 1, 'C')

        pdf.cell(45, 25, f'', 1, 0, 'C')
        pdf.cell(45, 25, f'', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(47.5, 10, f'INGRESOS', 1, 0, 'C')
        pdf.cell(47.5, 10, f'$ ', 1, 1, 'C')

        pdf.cell(45, 10, f'', 0, 0)
        pdf.cell(45, 10, f'', 0, 0)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(47.5, 10, f'EGRESOS', 1, 0, 'C')
        pdf.cell(47.5, 10, f'$ ', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        pdf.cell(45, 10, f'', 0, 0)
        pdf.cell(45, 10, f'', 0, 0)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(95, 14, f'VENTA PDV', 1, 1, 'C')

        pdf.cell(45, 10, f'', 0, 0)
        pdf.cell(45, 10, f'', 0, 0)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(47.5, 10, f'TOTAL DIA PDV', 1, 0, 'C')
        pdf.cell(47.5, 10, f'$ ', 1, 1, 'C')

        pdf.cell(45, 10, f'', 0, 0)
        pdf.cell(45, 10, f'', 0, 0)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(47.5, 10, f'EFECTIVO DIA PDV', 1, 0, 'C')
        pdf.cell(47.5, 10, f'$ ', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 10, '', 0, 1)

        pdf.cell(0, 25, f'* FIN REPORTE *'.upper(), 0, 1, 'C')

        pdf.output(f"...Reportes/Reportes_PDV's/{self.fecha_Formateada_RN} - Reporte {self.pdv}.pdf")

    # *** Funciones para el manejo de los campos de texto del Planeador ***

    def personal(self, e):
        self.sup_Pers_PDV.hint_text = "Ivette Herrera"
        self.sup_Ops.hint_text = "Omar Tovar"
        self.sup_CDO.hint_text = "Uriel Martínez"
        self.ven_Glorieta.hint_text = "Valeria"
        self.ven_Vips.hint_text = "Donovan Hdez"
        self.ven_SanMiguel.hint_text = "Uriel"
        self.ven_SanAntonio.hint_text = "Ivette"
        self.ven_Ensuenos.hint_text = "Alejandra"
        self.ven_Operagua.hint_text = "Victor"
        self.ven_LaPiedad.hint_text = "Isabel"
        self.ven_Cofradia2.hint_text = "Karla"
        self.ven_Parques.hint_text = "Omar"
        self.ven_Cumbria.hint_text = "Jesús"
        self.ven_Palomas.hint_text = "--"
        self.ven_Atlanta.hint_text = "--"
        self.update()

    # *** Funciones para el manejo de los campos de texto de la seccion de vasos ***

    # Vasos Chicos

    def conversion_n_capture_vc(self, e):
        if self.vci.value == "" or self.vcf.value == "":
            self.vcven.value = "---"
            self.vcvt.value = ""
            self.vcven.update()
            self.vcvt.update()
            if self.vcven.value == "---":
                if type(self.vmven.value) != str and type(self.vgven.value) != str:
                    try:
                        self.vtv.value = self.vmven.value + self.vgven.value
                        self.vvmt.value = self.vmvt.value + self.vgvt.value
                        self.vtv.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        self.vvmt.value = ""
                        print("Error en suma: vasos medianos totales + vasos grandes totales (funcion cac crema vasos chicos) - Error:", ex)
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
        
        try:
            self.num_tci = int(self.tci.value)
            self.num_tcf = int(self.tcf.value)
            self.num_vci = int(self.vci.value)
            self.num_vcf = int(self.vcf.value)
            # self.vcven.update()
            # self.vcvt.update()
            self.vcven.on_change(e)
            self.vcven.update()
        except Exception as ex:
            print("Error en funcion conversion y captura vasos chicos: ", ex)
        finally:
            self.update()

    # Vasos Medianos

    def conversion_n_capture_vm(self, e):
        if self.vmi.value == "" or self.vmf.value == "":
            self.vmven.value = "---"
            self.vmvt.value = ""
            self.vmven.update()
            self.vmvt.update()
            if self.vmven.value == "---":
                self.vmvt.value = ""
                if type(self.vcven.value) != str and type(self.vgven.value) != str:
                    try:
                        self.vtv.value = self.vcven.value + self.vgven.value
                        self.vvmt.value = self.vcvt.value + self.vgvt.value
                        self.vtv.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        print("Error en suma: vasos medianos totales + vasos grandes totales (funcion cac crema vasos chicos) - Error:", ex)
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

        try:
            self.num_tmi = int(self.tmi.value)
            self.num_tmf = int(self.tmf.value)
            self.num_vmi = int(self.vmi.value)
            self.num_vmf = int(self.vmf.value)
            self.vmven.on_change(e)
            self.vmven.update()
        except ValueError:
            pass
        finally:
            self.update()

    # Vasos Grandes

    def conversion_n_capture_vg(self, e):
        if self.vgi.value == "" or self.vgf.value == "":
            self.vgven.value = "---"
            self.vgvt.value = ""
            self.vgven.update()
            self.vgvt.update()
            if self.vgven.value == "---":
                self.vgvt.value = ""
                if type(self.vmven.value) != str and type(self.vcven.value) != str:
                    try:
                        self.vtv.value = self.vmven.value + self.vcven.value
                        self.vvmt.value = self.vmvt.value + self.vcvt.value
                        self.vtv.update()
                        self.vvmt.update()
                    except Exception as ex:
                        self.vtv.value = ""
                        print("Error en suma: vasos medianos totales + vasos chicos (funcion cac crema vasos grandes) - Error:", ex)
                    return
                elif type(self.vmven.value) != str:
                    self.vtv.value = self.vmven.value
                    self.vvmt.value = self.vmvt.value
                elif type(self.vcven.value) != str:
                    self.vtv.value = self.vcven.value
                    self.vvmt.value = self.vcvt.value
                else:
                    self.vtv.value = ""
                    self.vvmt.value = ""

                self.vtv.update()
                self.vvmt.update()
            return
        
        try:
            self.num_tgi = int(self.tgi.value)
            self.num_tgf = int(self.tgf.value)
            self.num_vgi = int(self.vgi.value)
            self.num_vgf = int(self.vgf.value)
            # self.num_tgdif = self.num_tgi - self.num_tgf
            # self.tgdif.value = self.num_tgdif
            # self.num_vgdif = self.num_vgi - self.num_vgf
            # self.vgdif.value = self.num_vgdif
            self.field_totalSale_vg()
            self.venta_totalVasos()
            self.vgven.update()
            self.vgvt.update()
            self.vgven.on_change(e)
            self.vgven.update()
        except ValueError:
            pass
        finally:
            self.update()

    # Vasos Chicos

    def field_totalSale_vc(self, e):
        self.num_vcven = self.num_vci - self.num_vcf
        self.num_vcvt = self.num_vcven * 50
        self.vcven.value = self.num_vcven
        self.vcvt.value = self.num_vcvt
        self.vcven.update()
        self.vcvt.update()
        self.venta_totalVasos()

    # Vasos Medianos

    def field_totalSale_vm(self):
        self.num_vmven = self.num_vmi - self.num_vmf
        self.vmven.value = self.num_vmven
        self.num_vmvt = self.num_vmven * 70
        self.vmvt.value = self.num_vmvt

    # Vasos Grandes
    def field_totalSale_vg(self):
        self.num_vgven = self.num_vgi - self.num_vgf
        self.vgven.value = self.num_vgven
        self.num_vgvt = self.num_vgven * 150
        self.vgvt.value = self.num_vgvt

    # Venta Total Vasos
    def venta_totalVasos(self):
        self.num_vtv = 0
        self.num_vvmt = 0

        self.bloque_or_1 = (type(self.vcven.value) == str or type(self.vmven.value) == str or type(self.vgven.value) == str)
        self.bloque_or_2 = (type(self.vcvt.value) == str or type(self.vmvt.value) == str or type(self.vgvt.value) == str)

        if type(self.vcven.value) == str and type(self.vmven.value) == str and type(self.vgven.value) == str and type(self.vcvt.value) == str and type(self.vmvt.value) == str and type(self.vgvt.value) == str:
            self.vtv.value = ""
            self.vvmt.value = ""
            self.vtv.update()
            self.vvmt.update()
        elif self.bloque_or_1 and self.bloque_or_2:
            self.values_bloque1 = [self.vcven.value, self.vmven.value, self.vgven.value]
            self.values_bloque2 = [self.vcvt.value, self.vmvt.value, self.vgvt.value]
            self.values_numericos_bloque1 = []
            self.values_numericos_bloque2 = []

            for e1, e2 in zip(self.values_bloque1, self.values_bloque2):
                if type(e1) != str and type(e2) != str:
                    self.values_numericos_bloque1.append(e1)
                    self.values_numericos_bloque2.append(e2)

            if (len(self.values_numericos_bloque1) == 2) and (len(self.values_numericos_bloque2) == 2):
                self.values_numericos_1 = self.values_numericos_bloque1[0] + self.values_numericos_bloque1[1]
                self.values_numericos_2 = self.values_numericos_bloque2[0] + self.values_numericos_bloque2[1]
                self.vtv.value = self.values_numericos_1
                self.vvmt.value = self.values_numericos_2
                self.vtv.update()
                self.vvmt.update()
        else:
            try:
                self.num_vtv = self.vcven.value + self.vmven.value + self.vgven.value
                self.num_vvmt = self.vcvt.value + self.vmvt.value + self.vgvt.value
                self.vtv.value = self.num_vtv
                self.vvmt.value = self.num_vvmt
                self.vtv.update()
                self.vvmt.update()
                self.update()
            except Exception as ex:
                print("Error: ", ex)

    # ***** Funciones para el manejo de los campos de texto de la seccion de frutas *****

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

    # ------------------------ CAMPOS FRUTA ------------------------

    # FRESA

    def values_Fresa(self, e):
        try:
            if self.fv.value != "" and self.fv.value != "---":
                self.fruven.value = self.fv.value

            self.venta_totalFruta()
            self.fruven.update()
        except Exception as ex:
            print("Error en funcion values_Fresa - Error:", ex)

        # print("prueba fresa")
        # print("prueba fresa")

    # UVA
        
    def values_Uva(self, e):
        try:
            if self.uv.value != "" and self.uv.value != "---":
                self.fruven.value = self.uv.value

            self.venta_totalFruta()
            self.fruven.update()
        except Exception as ex:
            print("Error en funcion values_Uva - Error:", ex)

        # print("prueba uva")
        # print("prueba uva")

    # VENTA TOTAL FRUTA

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

    # ***** Funciones para el manejo de los campos de texto de la seccion de cremas *****

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

    # ------------------------ CAMPOS CREMA ------------------------

    # CREMA ORIGINAL

    def values_cremaOriginal(self, e):
        try:
            if (self.cov.value) != str:
                self.creven.value = self.cov.value

            self.venta_totalCrema()
            self.creven.update()
        except Exception as ex:
            print("Error en funcion values_cremaOriginal - Error: ", ex)

    # CREMA CHOCOLATE

    def values_cremaChocolate(self, e):
        try:
            if type(self.cchv.value) != str:
                self.creven.value = self.cchv.value

            self.venta_totalCrema()
            self.creven.update()
        except Exception as ex:
            print("Error en funcion values_cremaChocolate - Error: ", ex)

    # CREMA CAFE

    def values_cremaCafe(self, e):
        try:
            if type(self.ccav.value) != str:
                self.creven.value = self.ccav.value

            self.venta_totalCrema()
            self.creven.update()
        except Exception as ex:
            print("Error en funcion values_cremaCafe - Error: ", ex)

    # VENTA TOTAL CREMAS

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


    # ***** Funciones para el manejo de los campos de texto de la seccion de extras y adicionales *****

    def conversion_n_capture_tE(self, e):
        try:
            self.num_t5 = int(self.t5.value)
            self.num_t10 = int(self.t10.value)
            self.total_t5 = self.num_t5 * 5
            self.total_t10 = self.num_t10 * 10
            self.num_tt = self.total_t5 + self.total_t10
            self.tt.value = self.num_tt
        except:
            pass
        finally:
            self.update()

    def conversion_n_capture_sD(self, e):
        try:
            self.num_sd20 = int(self.sd20.value)
            self.num_sd35 = int(self.sd35.value)
            self.total_sd20 = self.num_sd20 * 20
            self.total_sd35 = self.num_sd35 * 35
            self.num_sdt = self.total_sd20 + self.total_sd35
            self.sdt.value = self.num_sdt
        except:
            pass
        finally:
            self.update()

    def balance_General(self, e):
        # self.num_bging = self.vcvt.value + self.vmvt.value + self.vgvt.value + self.tt.value + self.sdt.value + self.trt
        # self.bging.value = self.num_bging
        # self.num_bgte = self.trt + self.grt
        # self.num_bgte = self.bgtd.value - self.num_bgte

        try:
            self.num_trt = int(self.trt.value)
            self.num_grt = int(self.grt.value)
            self.num_bging = self.vcvt.value + self.vmvt.value + self.vgvt.value + self.tt.value + self.sdt.value + self.num_trt
            self.bging.value = self.num_bging
            self.num_bgegr = self.num_trt + self.num_grt
            self.bgegr.value = self.num_bgegr
            self.bgtd.value = self.bging.value
            self.bgte.value = self.bgtd.value - self.bgegr.value
        except ValueError:
            pass
        finally:
            self.update()

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

        self.extras = [self.t5, self.t10, self.tt, self.sd20, self.sd35, self.sdt, self.trn, self.trt, self.grn, self.grt, self.bging, self.bgegr, self.bgtd, self.bgte]
        for element in self.extras:
            element.value = ""

        self.variables_ventas = [self.fruven, self.creven, self.vtv, self.vvmt]
        for element in self.variables_ventas:
            element.value = ""

        self.update()

    def reset_textFields(self, e):
        self.report_field.value = ""
        self.sales_field.value = ""
        self.update()

    # ***** FUNCTION CONSTRUCTORA (NO ME QUEDA CLARO PARA QUE Y PORQUE SE HACE, TENGO QUE INVESTIGAR A FONDO) *****

    def build(self):
        return self.main_pages

# ***** FUNCIÓN PRINCIPAL PARA CREAR LA VENTANA PRINCIPAL DE NUESTRO PROGRAMA O APP CON ALGUNAS CONFIGURACIONES EN ELLA COMO ALINEACION EN HORIZONTAL, COLOR DE FONDO, MEDIDA MINIMA EN ALTO Y ANCHO, TEMA PREDETERMINADO Y TÍTULO *****

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

# ***** Web Mode *****
# ft.app(target=main, view=ft.WEB_BROWSER)

# ***** Desktop Mode *****
ft.app(target=main)