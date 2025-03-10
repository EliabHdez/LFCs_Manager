import flet as ft
import sys
import os
ruta_raiz = os.path.join(os.path.dirname(__file__), "..", "../Main_Code")
sys.path.append(ruta_raiz)
import
import datetime as dt
from fpdf import FPDF

# class UI(ft.ResponsiveRow):
#     def __init__(, page):
#         pass

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

    # pdv = ""
    # selected_index = 0

    # .color_teal = "teal"
    color_teal = "#00ebab"
    color_teal_2 = "#11b78a"

    tci = created_Functions.create_textfield(Label="Iniciales", suffix_Text="Tapas Iniciales", on_Focus=created_Functions.Focus, on_Change=None)
    tcf = created_Functions.create_textfield(Label="Finales", suffix_Text="Tapas Finales", on_Focus=created_Functions.Focus, on_Change=None)
    vci = created_Functions.create_textfield(Label="Iniciales", suffix_Text="Vasos Iniciales", on_Focus=created_Functions.Focus, on_Change=None)
    vcf = created_Functions.create_textfield(Label="Finales", suffix_Text="Vasos Finales", on_Focus=created_Functions.Focus, on_Change=None)
    vcven = created_Functions.create_textfield(Label="Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True)
    vcvt = created_Functions.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24,label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=2, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)
    # tcdif = created_Functions.create_textfield("Diferencia de...", suffix_Text="Tapas", read_Only=True)
    # vcdif = created_Functions.create_textfield("Diferencia", suffix_Text="Vasos", read_Only=True)
    # vcsv = created_Functions.create_textfield("Sin vender", suffix_Text="Vasos", Color="#ffffff", read_Only=True)

    # Variables Vasos Medianos

    # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

    tmi = created_Functions.create_textfield(Label="Iniciales", suffix_Text="Tapas Iniciales", on_Focus=created_Functions.Focus, on_Change=None)
    tmf = created_Functions.create_textfield(Label="Finales", suffix_Text="Tapas Finales", on_Focus=created_Functions.Focus, on_Change=None)
    vmi = created_Functions.create_textfield(Label="Iniciales", suffix_Text="Vasos Iniciales", on_Focus=created_Functions.Focus, on_Change=None)
    vmf = created_Functions.create_textfield(Label="Finales", suffix_Text=" Vasos Finales", on_Focus=created_Functions.Focus, on_Change=None)
    vmven = created_Functions.create_textfield(Label="Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True)
    vmvt = created_Functions.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)
    # tmdif = created_Functions.create_textfield("Diferencia", read_Only=True)
    # vmdif = created_Functions.create_textfield("Diferencia", read_Only=True)
    # vmsv = created_Functions.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)

    # Variables Vasos Grandes

    # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

    tgi = created_Functions.create_textfield(Label="Iniciales", suffix_Text="Tapas Iniciales", on_Focus=created_Functions.Focus, on_Change=None)
    tgf = created_Functions.create_textfield(Label="Finales", suffix_Text="Tapas Finales", on_Focus=created_Functions.Focus, on_Change=None)
    vgi = created_Functions.create_textfield(Label="Iniciales", suffix_Text="Vasos Iniciales", on_Focus=created_Functions.Focus, on_Change=None)
    vgf = created_Functions.create_textfield(Label="Finales", suffix_Text="Vasos Finales", on_Focus=created_Functions.Focus, on_Change=None)
    vgven = created_Functions.create_textfield(Label="Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True)
    vgvt = created_Functions.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)
    # tgdif = created_Functions.create_textfield("Diferencia", read_Only=True)
    # vgdif = created_Functions.create_textfield("Diferencia", read_Only=True)
    # vgsv = created_Functions.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)

    # Variables Venta Total Vasos

    # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

    vtv = created_Functions.create_textfield_WB(Label="Vendidos", Color="#ffffff", text_Size=24, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", suffix_Text="Vasos ", read_Only=True)
    vvmt = created_Functions.create_textfield_WB(Label="Venta Total", Color="#ffffff", text_Size=24, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), suffix_Text="MX ", read_Only=True)

    # ***** VARIABLES FRUTAS *****

    # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

    # Fresa

    # tgi = created_Functions.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=created_Functions.Focus, on_Change=conversion_n_capture_vg)
    fpi = created_Functions.create_textfield(Label="Picada Inicial", suffix_Text="Botes", on_Change=None)
    fpf = created_Functions.create_textfield(Label="Picada Final", suffix_Text="Botes", on_Change=None)
    fei = created_Functions.create_textfield(Label="Entera Inicial", suffix_Text="Botes", on_Change=None)
    fef = created_Functions.create_textfield(Label="Entera Final", suffix_Text="Botes", on_Change=None)
    fv = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", read_Only=True, on_Change=None)
    # fr = created_Functions.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

    # Uva

    upi = created_Functions.create_textfield(Label="Picada Inicial", suffix_Text="Botes", on_Change=None)
    upf = created_Functions.create_textfield(Label="Picada Final", suffix_Text="Botes", on_Change=None)
    uei = created_Functions.create_textfield(Label="Entera Inicial", suffix_Text="Botes", on_Change=None)
    uef = created_Functions.create_textfield(Label="Entera Final", suffix_Text="Botes", on_Change=None)
    uv = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000",read_Only=True, on_Change=None)
    # ur = created_Functions.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

    # ***** VARIABLES CREMAS *****

    # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

    # Crema Original

    coi = created_Functions.create_textfield(Label="Inicial", suffix_Text="Botes", on_Change=None)
    cof = created_Functions.create_textfield(Label="Final", suffix_Text="Botes", on_Change=None)
    cov = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000",read_Only=True)

    # Crema Chocolate

    cchi = created_Functions.create_textfield(Label="Inicial", suffix_Text="Botes", on_Change=None)
    cchf = created_Functions.create_textfield(Label="Final", suffix_Text="Botes", on_Change=None)
    cchv = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000",read_Only=True)

    # Crema Cafe

    ccai = created_Functions.create_textfield(Label="Inicial", suffix_Text="Botes", on_Change=None)
    ccaf = created_Functions.create_textfield(Label="Final", suffix_Text="Botes", on_Change=None)
    ccav = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000",read_Only=True)

    # Variables Venta Total Vasos

    # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

    fruven = created_Functions.create_textfield_WB(Label="Fruta", Height=25, Color="#ffffff", text_Size=24, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", suffix_Text="Botes ", read_Only=True)
    creven = created_Functions.create_textfield_WB(Label="Cremas", Height=25, Color="#ffffff", text_Size=24, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", suffix_Text="Botes ", read_Only=True)
        
    # ***** VARIABLES ADICIONALES Y EXTRAS *****

    # Opciones a configurar en la funcion create_textfield_Extras: Width, Height, Color="#d3d3d3", text_Size=12, border_Color=None, read_Only=False, on_Change=False

    # Toppings Extras

    t5 = created_Functions.create_textField_Extras(40, 25, on_Change=None)
    t10 = created_Functions.create_textField_Extras(40, 25, on_Change=None)
    tt = created_Functions.create_textField_Extras(55, 25, "#ffffff", 15, border_Color="#fd0000", read_Only=True)

    # Servicios a Domicilio

    sd25 = created_Functions.create_textField_Extras(40, 25, on_Change=None)
    sd35 = created_Functions.create_textField_Extras(40, 25, on_Change=None)
    sdt = created_Functions.create_textField_Extras(50, 25, "#ffffff", 15, border_Color="#fd0000", read_Only=True)

    # Transferencias

    trn = created_Functions.create_textField_Extras(50, 25)
    trt = created_Functions.create_textField_Extras(50, 25, "#ffffff", 15, border_Color="#fd0000")

    # Gastos / Retiros

    grn = created_Functions.create_textField_Extras(50, 25)
    grt = created_Functions.create_textField_Extras(50, 25, "#ffffff", 15, border_Color="#fd0000", on_Change=None)

    # Balance

    bgi = created_Functions.create_textField_Extras(50, 25)
    bgd = created_Functions.create_textField_Extras(50, 25)
    bgt = created_Functions.create_textField_Extras(70, 25, "#ffffff", 15, border_Color="#fd0000", read_Only=True)

    # ***** VARIABLES VENTANA VENTAS *****

    # *** Variables Campos de texto y Botones ***

    # Campos de texto

    report_field = created_Functions.create_textField_RyV("REPORTE")
    sales_field = created_Functions.create_textField_RyV("EXTRAS", False)

    # *** Variable Boton cambio de tema ***

    mode_switch = created_Functions.create_Boton_Switch()
    
    # *** Variables Iconos Inferiores Barra de Navegacion Lateral ***

    profiles = ft.IconButton(# Ventana Perfiles / Cuentas
        icon=ft.Icons.ACCOUNT_CIRCLE_SHARP,
        icon_color="white",
        tooltip="Cuenta",
        on_click=lambda e: page.open(
            ft.CupertinoAlertDialog(
                # title=ft.Text("Cuentas"),
                content=ft.Text('Sección no disponible por el momento'),
                actions=[
                    ft.CupertinoDialogAction("Ok", is_destructive_action=True, on_click=lambda e: page.close(e.control.parent))
                ]
            ),
        )
    )
    configuration = ft.IconButton(# Ventana Configuraciones
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

    # Variables sucursales

    glorieta = created_Functions.create_radio("glorieta", "Glorieta")

    sanmiguel = created_Functions.create_radio("sanmiguel", "San Miguel")

    vips = created_Functions.create_radio("vips", "Vips")

    cofradia2 = created_Functions.create_radio("cofradia2", "Cofradía 2")

    ensuenos = created_Functions.create_radio("ensueños", "Ensueños")

    operagua = created_Functions.create_radio("operagua", "Operagua")

    sanantonio = created_Functions.create_radio("sanantonio", "San Antonio")

    lapiedad = created_Functions.create_radio("lapiedad", "La Piedad")

    # -------------------------------------------------------------------

    ##### +++++ COMIENZO DEL MAQUETADO DE LA INTERFAZ GRAFICA ***++ #####

    # -------------------------------------------------------------------

    # ***** BARRA DE NAVEGACION LATERAL IZQUIERDA *****

    navigation_bar = ft.Container(# Barra lateral de navegacion principal
        col=.8,
        # height=page.height,
        # bgcolor=.color_teal,
        bgcolor=ft.Colors.BLUE_GREY_900,
        border_radius=10,
        content=ft.Column(
            # expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    expand=True,
                    # height=500,
                    # alignment=ft.alignment.center,
                    content=ft.NavigationRail(
                        bgcolor=ft.Colors.BLUE_GREY_900,
                        # on_change=change_page,
                        selected_index=0,
                        indicator_color=color_teal_2,
                        # selected_label_text_style=ft.TextStyle(color=.color_teal_2),
                        destinations=[
                            ft.NavigationRailDestination(
                                icon = ft.Icons.HOME,
                                label_content=ft.Text("INICIO", size=8),
                                selected_icon=ft.Icon(ft.Icons.HOME, color="#2e2e2e")
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
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            profiles,
                            configuration,
                            mode_switch
                        ]
                    )
                ),
            ]
        )
    )

    pdv = ft.RadioGroup(# Grupo de Botones tipo Radio de las Sucursales
        # on_change=pdv_selection,
        content=ft.Container(
            bgcolor=ft.Colors.BLUE_GREY_900,
            alignment=ft.alignment.center,
            border_radius=10,
            padding=ft.Padding(top=2, bottom=2, left=2, right=4),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                # expand=True,
                controls=[
                    glorieta,
                    sanmiguel,
                    vips,
                    cofradia2,
                    ensuenos,
                    operagua,
                    sanantonio,
                    lapiedad 
                ]
            )
        )
    )

    home = ft.Container(# Ventana Inicio
        bgcolor=ft.Colors.BLUE_GREY_900,
        height=578,
        width=1500,
        # padding=10,
        border_radius=10,
        # alignment=ft.alignment.center,
        content=ft.Tabs(
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
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Container(# Frutas
                                content=ft.ResponsiveRow(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.Container(# Frutas
                                            col=12,
                                            margin=ft.Margin(top=15, bottom=5, left=30, right=30),
                                            # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                # horizontal_alignment="center",
                                                controls=[
                                                    ft.Container(# Frutas
                                                        # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                        # height=250,
                                                        # width=600,
                                                        # margin=5,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="#292929",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        padding=ft.Padding(top=7, bottom=10, left=0, right=2),
                                                        # shadow=ft.BoxShadow(
                                                        #     spread_radius=1,
                                                        #     blur_radius=15,
                                                        #     color=ft.Colors.BLUE_GREY_100,
                                                        #     offset=ft.Offset(0, 0),
                                                        #     blur_style=ft.ShadowBlurStyle.OUTER,
                                                        # ),
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            controls=[
                                                                ft.Container(# Titulo Fresa
                                                                    alignment=ft.alignment.center,
                                                                    padding=ft.padding.symmetric(horizontal=0, vertical=3),
                                                                    # height=15,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(# Titulo
                                                                        # horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* FRESA *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="white",
                                                                            #     thickness=.5,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                    ft.Container(# Fresa
                                                                    alignment=ft.alignment.center,
                                                                    margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=fpi
                                                                                )
                                                                            ),
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=fpf
                                                                                ),
                                                                            ),
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=fei
                                                                                )
                                                                            ),
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=fef
                                                                                ),
                                                                            ),
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=fv
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Titulo Uva
                                                                    alignment=ft.alignment.center,
                                                                    padding=ft.padding.symmetric(horizontal=0, vertical=3),
                                                                    # height=15,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        # horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* UVA *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="white",
                                                                            #     thickness=.5,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Uva
                                                                    alignment=ft.alignment.center,
                                                                    # margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=upi
                                                                                )
                                                                            ),
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=upf
                                                                                ),
                                                                            ),
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=uei
                                                                                )
                                                                            ),
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=uef
                                                                                ),
                                                                            ),
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=uv
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
                            ),
                            ft.Container(# Cremas
                                content=ft.ResponsiveRow(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.Container(# Crema Original
                                            col=4,
                                            margin=ft.Margin(top=12, bottom=0, left=30, right=2),
                                            # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                # horizontal_alignment="center",
                                                controls=[
                                                    ft.Container(
                                                        # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                        # height=250,
                                                        # width=600,
                                                        # margin=5,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="#292929",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        padding=ft.Padding(top=7, bottom=10, left=0, right=0),
                                                        # shadow=ft.BoxShadow(
                                                        #     spread_radius=1,
                                                        #     blur_radius=15,
                                                        #     color=ft.Colors.BLUE_GREY_100,
                                                        #     offset=ft.Offset(0, 0),
                                                        #     blur_style=ft.ShadowBlurStyle.OUTER,
                                                        # ),
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            controls=[
                                                                ft.Container(# Titulo
                                                                    alignment=ft.alignment.center,
                                                                    padding=ft.padding.symmetric(horizontal=0, vertical=3),
                                                                    # height=15,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        # horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* CREMA ORIGINAL *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="white",
                                                                            #     thickness=.5,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                    ft.Container(# Botes Dia
                                                                    alignment=ft.alignment.center,
                                                                    # margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Botes Iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=4,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=coi
                                                                                )
                                                                            ),
                                                                            ft.Container(# Botes Finales
                                                                                alignment=ft.alignment.center,
                                                                                col=4,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=cof
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Venta Botes
                                                                    alignment=ft.alignment.center,
                                                                    # margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=6,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=cov
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
                                            margin=ft.Margin(top=12, bottom=0, left=4, right=4),
                                            # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                # horizontal_alignment="center",
                                                controls=[
                                                    ft.Container(
                                                        # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                        # height=250,
                                                        # width=600,
                                                        # margin=5,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="#292929",
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        padding=ft.Padding(top=7, bottom=10, left=0, right=0),
                                                        # shadow=ft.BoxShadow(
                                                        #     spread_radius=1,
                                                        #     blur_radius=15,
                                                        #     color=ft.Colors.BLUE_GREY_100,
                                                        #     offset=ft.Offset(0, 0),
                                                        #     blur_style=ft.ShadowBlurStyle.OUTER,
                                                        # ),
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            controls=[
                                                                ft.Container(# Titulo
                                                                    alignment=ft.alignment.center,
                                                                    padding=ft.padding.symmetric(horizontal=0, vertical=3),
                                                                    # height=15,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        # horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* CREMA CHOCOLATE *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="white",
                                                                            #     thickness=.5,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Botes Dia
                                                                    alignment=ft.alignment.center,
                                                                    # margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Botes Iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=4,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=cchi
                                                                                )
                                                                            ),
                                                                            ft.Container(# Botes Finales
                                                                                alignment=ft.alignment.center,
                                                                                col=4,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=cchf
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Venta Botes
                                                                    alignment=ft.alignment.center,
                                                                    # margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=6,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=cchv
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
                                            margin=ft.Margin(top=12, bottom=0, left=2, right=30),
                                            # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                # horizontal_alignment="center",
                                                controls=[
                                                    ft.Container(
                                                        # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                        # height=250,
                                                        # width=600,
                                                        # margin=5,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="#292929",
                                                        # bgcolor=ft.Colors.BLUE_GREY_900,
                                                        border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        border_radius=5,
                                                        padding=ft.Padding(top=7, bottom=10, left=0, right=0),
                                                        # shadow=ft.BoxShadow(
                                                        #     spread_radius=1,
                                                        #     blur_radius=15,
                                                        #     color=ft.Colors.BLUE_GREY_100,
                                                        #     offset=ft.Offset(0, 0),
                                                        #     blur_style=ft.ShadowBlurStyle.OUTER,
                                                        # ),
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            controls=[
                                                                ft.Container(# Titulo
                                                                    alignment=ft.alignment.center,
                                                                    padding=ft.padding.symmetric(horizontal=0, vertical=3),
                                                                    # height=15,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        # horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* CREMA CAFE *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="white",
                                                                            #     thickness=.5,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Botes Dia
                                                                    alignment=ft.alignment.center,
                                                                    # margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Botes Iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=4,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=ccai
                                                                                )
                                                                            ),
                                                                            ft.Container(# Botes Finales
                                                                                alignment=ft.alignment.center,
                                                                                col=4,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=ccaf
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Venta Botes
                                                                    alignment=ft.alignment.center,
                                                                    # margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=6,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=ccav
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
                            ),
                            ft.Container(# Venta General
                                content=ft.ResponsiveRow(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    vertical_alignment="center",
                                    controls=[
                                        
                                        ft.Container(# Venta General Frutas y Cremas
                                            col=7,
                                            # margin=ft.Margin(top=2, bottom=0, left=0, right=0),
                                            # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                # horizontal_alignment="center",
                                                controls=[
                                                    ft.Container(
                                                        # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                        # height=250,
                                                        # width=600,
                                                        margin=5,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="#292929",
                                                        # border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                                        # border_radius=5,
                                                        padding=ft.Padding(top=2, bottom=5, left=3, right=3),
                                                        # shadow=ft.BoxShadow(
                                                        #     spread_radius=1,
                                                        #     blur_radius=15,
                                                        #     color=ft.Colors.BLUE_GREY_100,
                                                        #     offset=ft.Offset(0, 0),
                                                        #     blur_style=ft.ShadowBlurStyle.OUTER,
                                                        # ),
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            controls=[
                                                                ft.Container(# Titulo
                                                                    alignment=ft.alignment.center,
                                                                    padding=ft.Padding(top=10, bottom=10, left=0, right=0),
                                                                    # height=40,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        # horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("VENTA GENERAL FRUTAS Y CREMAS", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="white",
                                                                            #     thickness=.5,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Venta Total Frutas y Cremas
                                                                    alignment=ft.alignment.center,
                                                                    margin=ft.margin.only(top=5),
                                                                    padding=ft.Padding(top=5, bottom=5, left=0, right=0),
                                                                    # margin=ft.margin.only(bottom=20),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Fruta total vendida (botes)
                                                                                col=3.5,
                                                                                alignment=ft.alignment.center,
                                                                                bgcolor="#292929",
                                                                                padding=2.5,
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
                                                                                content=fruven
                                                                            ),
                                                                            ft.Container(# Crema total vendida (botes)
                                                                                col=3.5,
                                                                                alignment=ft.alignment.center,
                                                                                bgcolor="#292929",
                                                                                padding=2.5,
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
                                                                                content=creven
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
                                        
                                    ]
                                )
                            ),
                        ]
                    )
                ),
                ft.Tab(# Vasos
                    text="Vasos",
                    content=ft.ResponsiveRow(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Container(# Vasos
                                col=12,
                                margin=ft.Margin(top=30, bottom=0, left=30, right=30),
                                # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                # bgcolor="blue",
                                content=ft.Column(
                                    # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    # horizontal_alignment="center",
                                    controls=[
                                        ft.Container(# Vasos
                                            # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                            # height=540,
                                            # width=1300,
                                            # margin=5,
                                            alignment=ft.alignment.center,
                                            # bgcolor="#292929",
                                            border=ft.border.all(width=.75, color=ft.Colors.BLUE_GREY_800),
                                            border_radius=5,
                                            padding=ft.Padding(top=15, bottom=15, left=0, right=0),
                                            # shadow=ft.BoxShadow(
                                            #     spread_radius=1,
                                            #     blur_radius=15,
                                            #     color=ft.Colors.BLUE_GREY_100,
                                            #     offset=ft.Offset(0, 0),
                                            #     blur_style=ft.ShadowBlurStyle.OUTER,
                                            # ),
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                controls=[
                                                    ft.Container(# Vasos Chicos
                                                        alignment=ft.alignment.center,
                                                        height=15,
                                                        # padding=7,
                                                        # bgcolor="blue",
                                                        # border_radius=20,
                                                        # width=180,
                                                        content=ft.Column(
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Text("* VASOS CHICOS *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                # ft.Divider(# Separador de seccion con Divider
                                                                #     height=1,
                                                                #     color="white",
                                                                #     thickness=.5,
                                                                #     leading_indent=400,
                                                                #     trailing_indent=400
                                                                # ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Vasos Chicos
                                                        alignment=ft.alignment.center,
                                                        margin=ft.margin.only(bottom=25),
                                                        # bgcolor="pink",
                                                        # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                        # border_radius=20,
                                                        content=ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            vertical_alignment="center",
                                                            controls=[
                                                                ft.Container(# Tapas chicas iniciales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=tci
                                                                    )
                                                                ),
                                                                ft.Container(# Tapas chicos finales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        # padding=2.5,
                                                                        border_radius=5,
                                                                        content=tcf
                                                                    ),
                                                                ),
                                                                ft.Container(# Vasos chicos inciales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=vci
                                                                    ),
                                                                ),
                                                                ft.Container(# Vasos chicos finales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(# Vasos Chicos
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=vcf
                                                                    ),
                                                                ),
                                                                ft.Container(# Vasos chicos vendidos
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        padding=2.5,
                                                                        border_radius=5,
                                                                        content=vcven
                                                                    ),
                                                                ),
                                                                ft.Container(# Venta total vasos chicos
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor="#f00000",
                                                                        border_radius=5,
                                                                        content=vcvt
                                                                    ),
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Vasos Medianos
                                                        alignment=ft.alignment.center,
                                                        height=15,
                                                        # padding=7,
                                                        # bgcolor="blue",
                                                        # border_radius=20,
                                                        # width=180,
                                                        content=ft.Column(
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Text("* VASOS MEDIANOS *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                # ft.Divider(# Separador de seccion con Divider
                                                                #     height=1,
                                                                #     color="#ff1765",
                                                                #     thickness=1,
                                                                #     leading_indent=400,
                                                                #     trailing_indent=400
                                                                # ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Vasos Medianos
                                                        alignment=ft.alignment.center,
                                                        margin=ft.margin.only(bottom=25),
                                                        # bgcolor="pink",
                                                        # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                        # border_radius=20,
                                                        content=ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            vertical_alignment="center",
                                                            controls=[
                                                                ft.Container(# Tapas medianas iniciales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=tmi
                                                                    )
                                                                ),
                                                                ft.Container(# Tapas medianas finales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=tmf
                                                                    ),
                                                                ),
                                                                ft.Container(# vasos medianos iniciales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=vmi
                                                                    ),
                                                                ),
                                                                ft.Container(# Vasos medianos finales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(# Vasos Chicos
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=vmf
                                                                    ),
                                                                ),
                                                                ft.Container(# Vasos medianos vendidos
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=vmven
                                                                    ),
                                                                ),
                                                                ft.Container(# Venta total vasos medianos
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor="#f00000",
                                                                        border_radius=5,
                                                                        content=vmvt
                                                                    ),
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Vasos Grandes
                                                        alignment=ft.alignment.center,
                                                        height=15,
                                                        # padding=7,
                                                        # bgcolor="blue",
                                                        # border_radius=20,
                                                        # width=180,
                                                        content=ft.Column(
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.Text("* VASOS GRANDES *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                # ft.Divider(# Separador de seccion con Divider
                                                                #     height=1,
                                                                #     color="#ff1765",
                                                                #     thickness=1,
                                                                #     leading_indent=400,
                                                                #     trailing_indent=400
                                                                # ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Vasos Grandes
                                                        alignment=ft.alignment.center,
                                                        # margin=ft.margin.only(bottom=25),
                                                        # bgcolor="pink",
                                                        # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                        # border_radius=20,
                                                        content=ft.ResponsiveRow(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            vertical_alignment="center",
                                                            controls=[
                                                                ft.Container(# Tapas grandes iniciales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=tgi
                                                                    )
                                                                ),
                                                                ft.Container(# Tapas grandes finales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=tgf
                                                                    ),
                                                                ),
                                                                ft.Container(# Vasos grandes inciales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=vgi
                                                                    ),
                                                                ),
                                                                ft.Container(# Vasos grandes finales
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(# Vasos Chicos
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=vgf
                                                                    ),
                                                                ),
                                                                ft.Container(# Vasos grandes vendidos
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor=color_teal_2,
                                                                        border_radius=5,
                                                                        content=vgven
                                                                    ),
                                                                ),
                                                                ft.Container(# Venta total vasos grandes
                                                                    alignment=ft.alignment.center,
                                                                    col=2,
                                                                    # bgcolor="yellow",
                                                                    content=ft.Container(
                                                                        # bgcolor="#f00000",
                                                                        border_radius=5,
                                                                        content=vgvt
                                                                    ),
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    
                                                ]
                                            )
                                        ),
                                        ft.Container(# Venta Total Vasos en General
                                            alignment=ft.alignment.center,
                                            height=45,
                                            margin=ft.margin.only(top=10),
                                            # padding=7,
                                            # bgcolor="blue",
                                            # border_radius=20,
                                            # width=180,
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                controls=[
                                                    ft.Text("VENTA GENERAL VASOS", color="#bfc244", weight=ft.FontWeight.BOLD, size=20, style=ft.TextStyle(letter_spacing=10)),
                                                    # ft.Divider(# Separador de seccion con Divider
                                                    #     height=1,
                                                    #     color="#ff1765",
                                                    #     thickness=1,
                                                    #     leading_indent=400,
                                                    #     trailing_indent=400
                                                    # ),
                                                ]
                                            )
                                        ),
                                        ft.Container(# Venta Total Vasos en General
                                            alignment=ft.alignment.center,
                                            margin=ft.margin.only(bottom=5),
                                            # margin=ft.margin.only(bottom=20),
                                            # bgcolor="pink",
                                            # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                            # border_radius=20,
                                            content=ft.ResponsiveRow(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                vertical_alignment="center",
                                                controls=[
                                                    ft.Container(# Total Vasos Vendidos
                                                        col=2.5,
                                                        alignment=ft.alignment.center,
                                                        bgcolor="#292929",
                                                        padding=2.5,
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
                                                        content=vtv
                                                    ),
                                                    ft.Container(# Total Vasos Vendidos
                                                        col=2.5,
                                                        alignment=ft.alignment.center,
                                                        bgcolor="#292929",
                                                        padding=2.5,
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
                                                        content=vvmt
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
                ft.Tab(# Extras y Adicionales
                    text="Extras y Adicionales",
                )
            ]
        ),
    )

    # ***** BARRA DE SELECCION DE SUCURSALES *****

    # select_Bar_Sucursales = ft.Container(# Puntos de venta
    #     alignment=ft.alignment.center,
    #     bgcolor=ft.Colors.BLUE_GREY_900,
    #     border_radius=10,
    #     content=ft.Column(
    #         horizontal_alignment="center",
    #         alignment="center",
    #         # controls=[
    #         #     pdv,
    #         # ]
    #     )
    # )

    page.add(
        ft.ResponsiveRow(
            expand=True,
            controls=[
                navigation_bar,
                ft.Container(
                    col=11.20,
                    bgcolor="pink",
                    content=ft.Column(
                        controls=[
                            pdv,
                            home
                        ]
                    )
                )
            ]
        )
    )

    # ***** FUNCIONES *****

    #  *** Funcion para el manejo del cambio de ventanas mediante la barra lateral de navegacion ***

    # def change_page( e):
    #     selected_index = e.control.selected_index
    #     main_container.content = pages_containers[selected_index]
    #     page.update()

    # *** Funcion para el manejo de los radios boton's y la seleccion de las sucursales ***

    # def pdv_selection( e):
    #     if e.control.value == "glorieta":
    #         pdv = "Suc. Glorieta"

    #     if e.control.value == "sanmiguel":
    #         pdv = "Suc. San Miguel"

    #     if e.control.value == "vips":
    #         pdv = "Suc. Vips"

    #     if e.control.value == "cofradia2":
    #         pdv = "Suc. Cofradía 2"

    #     if e.control.value == "ensueños":
    #         pdv = "Suc. Ensueños"

    #     if e.control.value == "operagua":
    #         pdv = "Suc. Operagua"

    #     if e.control.value == "sanantonio":
    #         pdv = "Suc. San Antonio"

    #     if e.control.value == "lapiedad":
    #         pdv = "Suc. La Piedad"

    # *** Funcion para el generar el reporte y cargarlo en el textfield de la ventana de ventas ***

    # def generar_Reporte(e):
    #     # print(f"La sucursal seleccionada es: {e.control.value}")
    #     fecha_Actual = dt.datetime.today().date()

    #     fecha_Formateada = fecha_Actual.strftime("%d-%b-%Y")

    #     report_field.value = fecha_Formateada

    #     report_field.value = (
    #         f"                                                   {fecha_Formateada}\n\n"
    #         f"<<< {pdv} >>>\n\n"
    #         f"- VASOS -\n\n"
    #         f"Vasos Chicos: TI-{tci.value} / TP-{tcf.value} / VI-{vci.value} / VF-{vcf.value} / VV-{vcven.value}\n / Venta: ${vcvt.value}\n"
    #         f"Vasos Medianos: TI-{tmi.value} / TP-{tmf.value} / VI-{vmi.value} / VF-{vmf.value} / VV-{vmven.value}\n / Venta: ${vmvt.value}\n"
    #         f"Vasos Grandes: TI-{tgi.value} / TP-{tgf.value} / VI-{vgi.value} / VF-{vgf.value} / VV-{vgven.value}\n / Venta: ${vgvt.value}\n\n"
    #         f"- FRUTA -\n\n"
    #         f"Fresa: PI-{fpi.value} / PF-{fpf.value} / EI-{fei.value} / EF-{fef.value} / Vendida-{fv.value}\n"
    #         f"Uva: PI-{upi.value} / PF-{upf.value} / EI-{uei.value} / EF-{uef.value} / Vendida-{uv.value}\n\n"
    #         f"- CREMAS -\n\n"
    #         f"Crema Original: I-{coi.value} / F-{cof.value} / Vendida-{cov.value}\n\n"
    #         f"Crema Chocolate: I-{cchi.value} / F-{cchf.value} / Vendida-{cchv.value}\n\n"
    #         f"Crema Cafe: I-{ccai.value} / F-{ccaf.value} / Vendida-{ccav.value}\n\n"
    #         f"- TOPPINGS -\n\n"
    #         f"Toppings Extras: TE5-{t5.value} / TE10-{t10.value} / Total: ${tt.value}\n\n"
    #         f"- SERVICIOS A DOMICILIO -\n\n"
    #         f"Servivios a Domicilio: SD25-{sd25.value} / SD35-{sd35.value} / Total: ${sdt.value}\n\n"
    #         f"- TRANSFERENCIAS -\n\n"
    #         f"Transferencias: No TRANSFERENCIAS-{trn.value} / Monto Total: ${trt.value}\n\n"
    #         f"- GASTOS / RETIROS -\n\n"
    #         f"Gastos y/o Retiros: Cantidad-{grn.value} / Monto Total: ${grt.value}\n\n"
    #         f"- INGRESOS / EGRESOS -\n\n"
    #         f"Ingresos: Monto Total: ${bgi.value}\n"
    #         f"Egresos (G/R/T): Monto Total: ${bgd.value}\n\n"
    #         f"- TOTAL DIA PDV -\n\n"
    #         f"Total General: ${bgi.value}\n"
    #         f"Total Efectivo: ${bgt.value}\n\n"

    #         f"<<< FIN DEL REPORTE >>>"
    #     )
        
    # *** Funcion creadora del reporte del dia en formato PDF ***

    # def create_ReportePDF( e):
    #     fecha_Actual = dt.datetime.today().date()

    #     fecha_Formateada = fecha_Actual.strftime("%d-%b-%Y")

    #     fecha_Formateada_RN = fecha_Actual.strftime("%d-%m-%y")

    #     pdf = FPDF(orientation="P", unit="mm", format="A4")
    #     pdf.add_page()
        
    #     pdf.set_font("Arial", "", 10)
        
    #     pdf.image("../Images/Images_Program/FresaReporte.png", 10, 7, 20)
    #     pdf.cell(187, 5, f'{fecha_Formateada}', 0, 1, "R")
        
    #     # Titulo
    #     pdf.cell(0, 25, f'Reporte {pdv}'.upper(), 0, 1, 'C')
    #     pdf.line(70, 30, 140, 30)

    #     # pdf.cell(0, 5, '', 0, 1)
        
    #     # Vasos
    #     pdf.cell(70, 10, 'VASOS', 1, 0, "C")
    #     pdf.cell(15, 10, f'TI', 1, 0, 'C')
    #     pdf.cell(15, 10, f'TF', 1, 0, 'C')
    #     pdf.cell(15, 10, f'VI', 1, 0, 'C')
    #     pdf.cell(15, 10, f'VF', 1, 0, 'C')
    #     pdf.cell(25, 10, f'VENDIDOS', 1, 0, 'C')
    #     pdf.cell(35, 10, f'MONTO VENTA', 1, 1, 'C')
    #     pdf.cell(70, 8, 'VASOS CHICOS', 1, 0)
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(25, 8, f'', 1, 0, 'C')
    #     pdf.cell(35, 8, f'$ ', 1, 1, 'C')
    #     pdf.cell(70, 8, 'VASOS MEDIANOS', 1, 0)
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(25, 8, f'', 1, 0, 'C')
    #     pdf.cell(35, 8, f'$ ', 1, 1, 'C')
    #     pdf.cell(70, 8, 'VASOS GRANDES', 1, 0)
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(15, 8, f'', 1, 0, 'C')
    #     pdf.cell(25, 8, f'', 1, 0, 'C')
    #     pdf.cell(35, 8, f'$ ', 1, 1, 'C')

    #     # Separador con celda
    #     pdf.cell(0, 5, '', 0, 1)

    #     # Frutas Y Cremas
    #     # pdf.cell(100, 10, 'FRUTAS', 1, 0, "C")

    #     # pdf.cell(5, 10, '', 0, 0)

    #     # pdf.cell(85, 10, 'CREMAS', 1, 1, "C")

    #     pdf.cell(30, 10, f'FRUTA', 1, 0, 'C')
    #     pdf.cell(11, 10, f'PI', 1, 0, 'C')
    #     pdf.cell(11, 10, f'PF', 1, 0, 'C')
    #     pdf.cell(11, 10, f'EI', 1, 0, 'C')
    #     pdf.cell(11, 10, f'EF', 1, 0, 'C')
    #     pdf.cell(26, 10, f'VENDIDOS', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(35, 10, f'CREMA', 1, 0, 'C')
    #     pdf.cell(12.5, 10, f'IN', 1, 0, 'C')
    #     pdf.cell(12.5, 10, f'FI', 1, 0, 'C')
    #     pdf.cell(25, 10, f'VENDIDOS', 1, 1, 'C')

    #     pdf.cell(30, 8, 'FRESA', 1, 0)
    #     pdf.cell(11, 8, f'', 1, 0, 'C')
    #     pdf.cell(11, 8, f'', 1, 0, 'C')
    #     pdf.cell(11, 8, f'', 1, 0, 'C')
    #     pdf.cell(11, 8, f'', 1, 0, 'C')
    #     pdf.cell(26, 8, f'', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(35, 8, 'CR ORIGINAL', 1, 0)
    #     pdf.cell(12.5, 8, f'', 1, 0, 'C')
    #     pdf.cell(12.5, 8, f'', 1, 0, 'C')
    #     pdf.cell(25, 8, f'', 1, 1, 'C')

    #     pdf.cell(30, 8, 'UVA', 1, 0)
    #     pdf.cell(11, 8, f'', 1, 0, 'C')
    #     pdf.cell(11, 8, f'', 1, 0, 'C')
    #     pdf.cell(11, 8, f'', 1, 0, 'C')
    #     pdf.cell(11, 8, f'', 1, 0, 'C')
    #     pdf.cell(26, 8, f'', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(35, 8, 'CR CHOCOLATE', 1, 0)
    #     pdf.cell(12.5, 8, f'', 1, 0, 'C')
    #     pdf.cell(12.5, 8, f'', 1, 0, 'C')
    #     pdf.cell(25, 8, f'', 1, 1, 'C')

    #     pdf.cell(30, 8, '', 0, 0)
    #     pdf.cell(10, 8, f'', 0, 0,)
    #     pdf.cell(10, 8, f'', 0, 0,)
    #     pdf.cell(10, 8, f'', 0, 0,)
    #     pdf.cell(10, 8, f'', 0, 0,)
    #     pdf.cell(30, 8, f'', 0, 0,)

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(35, 8, 'CR CAFE', 1, 0)
    #     pdf.cell(12.5, 8, f'', 1, 0, 'C')
    #     pdf.cell(12.5, 8, f'', 1, 0, 'C')
    #     pdf.cell(25, 8, f'', 1, 1, 'C')

    #     # Separador con celda
    #     pdf.cell(0, 5, '', 0, 1)

    #     pdf.cell(45, 10, f'TOPPINGS EXTRA', 1, 0, 'C')
    #     pdf.cell(25, 10, f'CANTIDAD', 1, 0, 'C')
    #     pdf.cell(20, 10, f'TOTAL', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(50, 10, f'SERVICIOS A DOMICILIO', 1, 0, 'C')
    #     pdf.cell(25, 10, f'CANTIDAD', 1, 0, 'C')
    #     pdf.cell(20, 10, f'TOTAL', 1, 1, 'C')

    #     pdf.cell(45, 10, f'TOPPING 5', 1, 0, 'C')
    #     pdf.cell(25, 10, f'', 1, 0, 'C')
    #     pdf.cell(20, 10, f'$ ', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(50, 10, f'SERV DOM 25', 1, 0, 'C')
    #     pdf.cell(25, 10, f'', 1, 0, 'C')
    #     pdf.cell(20, 10, f'$ ', 1, 1, 'C')

    #     pdf.cell(45, 10, f'TOPPING 10', 1, 0, 'C')
    #     pdf.cell(25, 10, f'', 1, 0, 'C')
    #     pdf.cell(20, 10, f'$ ', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(50, 10, f'SERV DOM 35', 1, 0, 'C')
    #     pdf.cell(25, 10, f'', 1, 0, 'C')
    #     pdf.cell(20, 10, f'$ ', 1, 1, 'C')

    #     # Separador con celda
    #     pdf.cell(0, 5, '', 0, 1)

    #     pdf.cell(90, 10, f'TRANSFERENCIAS', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(95, 10, f'GASTOS Y RETIROS', 1, 1, 'C')

    #     # pdf.cell(30, 10, f'MONTOS', 1, 0, 'C')
    #     pdf.cell(60, 10, f'NO. DE TRANSFERENCIAS', 1, 0, 'C')
    #     pdf.cell(30, 10, f'TOTAL', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     # pdf.cell(30, 10, f'MONTOS', 1, 0, 'C')
    #     pdf.cell(60, 10, f'NO. DE GASTOS / RETIROS', 1, 0, 'C')
    #     pdf.cell(35, 10, f'TOTAL', 1, 1, 'C')

    #     pdf.cell(60, 10, f'', 1, 0, 'C')
    #     pdf.cell(30, 10, f'$ ', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(60, 10, f'', 1, 0, 'C')
    #     pdf.cell(35, 10, f'$ ', 1, 1, 'C')

    #     # Separador con celda
    #     pdf.cell(0, 5, '', 0, 1)

    #     pdf.cell(90, 12, f'MONTOS TRANSFERENCIAS Y GASTOS / RETIROS', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(95, 12, f'INGRESOS Y EGRESOS', 1, 1, 'C')

    #     pdf.cell(45, 7, f'TRANSFERENCIAS', 1, 0, 'C')
    #     pdf.cell(45, 7, f'GASTOS / RETIROS', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(47.5, 7, f'CONCEPTO', 1, 0, 'C')
    #     pdf.cell(47.5, 7, f'MONTO', 1, 1, 'C')

    #     pdf.cell(45, 25, f'', 1, 0, 'C')
    #     pdf.cell(45, 25, f'', 1, 0, 'C')

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(47.5, 10, f'INGRESOS', 1, 0, 'C')
    #     pdf.cell(47.5, 10, f'$ ', 1, 1, 'C')

    #     pdf.cell(45, 10, f'', 0, 0)
    #     pdf.cell(45, 10, f'', 0, 0)

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(47.5, 10, f'EGRESOS', 1, 0, 'C')
    #     pdf.cell(47.5, 10, f'$ ', 1, 1, 'C')

    #     # Separador con celda
    #     pdf.cell(0, 5, '', 0, 1)

    #     pdf.cell(45, 10, f'', 0, 0)
    #     pdf.cell(45, 10, f'', 0, 0)

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(95, 14, f'VENTA PDV', 1, 1, 'C')

    #     pdf.cell(45, 10, f'', 0, 0)
    #     pdf.cell(45, 10, f'', 0, 0)

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(47.5, 10, f'TOTAL DIA PDV', 1, 0, 'C')
    #     pdf.cell(47.5, 10, f'$ ', 1, 1, 'C')

    #     pdf.cell(45, 10, f'', 0, 0)
    #     pdf.cell(45, 10, f'', 0, 0)

    #     # Separador vertical con celda
    #     pdf.cell(5, 10, '', 0, 0)

    #     pdf.cell(47.5, 10, f'EFECTIVO DIA PDV', 1, 0, 'C')
    #     pdf.cell(47.5, 10, f'$ ', 1, 1, 'C')

    #     # Separador con celda
    #     pdf.cell(0, 10, '', 0, 1)

    #     pdf.cell(0, 25, f'* FIN REPORTE *'.upper(), 0, 1, 'C')
        
    #     pdf.output(f"../Reportes_PDV's/{fecha_Formateada_RN} - Reporte {pdv}.pdf")
    
    # *** Funciones para el manejo de los campos de texto de la seccion de vasos ***

    # def venta_Total_Vasos():
    #     num_vtv = vcven.value
    #     num_vvmt = vcvt.value
    #     vtv.value = num_vtv
    #     vvmt.value = num_vvmt

    #     num_vtv = num_vtv + vmven.value
    #     num_vvmt = num_vvmt + vmvt.value
    #     vtv.value = num_vtv
    #     vvmt.value = num_vvmt

    #     num_vtv = num_vtv + vgven.value
    #     num_vvmt = num_vvmt + vgvt.value
    #     vtv.value = num_vtv
    #     vvmt.value = num_vvmt
    #     page.update()

    # # ***** Funciones para el manejo de los campos de texto de la seccion de frutas *****

    # def conversion_n_capture_fr(e):
    #     try:
    #         if fpi.value == "" or fpf.value == "" or fei.value == "" or fef.value == "":
    #             fv.value = 0
    #             fv.update()
    #             fv.on_change(e)
    #             return
    #     except:
    #         pass

    #     try:
    #         if "." in fpi.value or "." in fpf.value or "." in fei.value or "." in fef.value:
    #             num_fpi = float(fpi.value)
    #             num_fpf = float(fpf.value)
    #             num_fei = float(fei.value)
    #             num_fef = float(fef.value)
    #         else:
    #             num_fpi = int(fpi.value)
    #             num_fpf = int(fpf.value)
    #             num_fei = int(fei.value)
    #             num_fef = int(fef.value)
            
    #         # num_fr = num_fpf + num_fef
    #         # num_fv = (num_fpi + num_fei) - num_fr
    #         num_fv = (num_fpi + num_fei) - (num_fpf + num_fef)

    #         # if num_fr % 2 == 0 or num_fr % 2 == 1:
    #         #     num_fr = int(num_fr)

    #         if num_fv % 2 == 0 or num_fv % 2 == 1:
    #             num_fv = int(num_fv)

    #         # fr.value = round(num_fr, 2)
    #         fv.value = round(num_fv, 2)
    #         fv.update()
    #         fv.on_change(e)
    #         venta_Total_Fruta_Crema()
    #     except:
    #         pass
    #     finally:
    #         page.update()

    # def conversion_n_capture_uva(e):
    #     try:
    #         if upi.value == "" or upf.value == "" or uei.value == "" or uef.value == "":
    #             uv.value = 0
    #             uv.update()
    #             uv.on_change(e)
    #             return
    #     except:
    #         pass

    #     try:
    #         if "." in upi.value or "." in upf.value or "." in uei.value or "." in uef.value:
    #             num_upi = float(upi.value)
    #             num_upf = float(upf.value)
    #             num_uei = float(uei.value)
    #             num_uef = float(uef.value)
    #         else:
    #             num_upi = int(upi.value)
    #             num_upf = int(upf.value)
    #             num_uei = int(uei.value)
    #             num_uef = int(uef.value)

    #         # num_ur = num_upf + num_uef
    #         # num_uv = (num_upi + num_uei) - num_ur
    #         num_uv = (num_upi + num_uei) - (num_upf + num_uef)

    #         # if num_ur % 2 == 0 or num_ur % 2 == 1:
    #         #     num_ur = int(num_ur)

    #         if num_uv % 2 == 0 or num_uv % 2 == 1:
    #             num_uv = int(num_uv)

    #         # ur.value = round(num_ur, 2)
    #         uv.value = round(num_uv, 2)
    #         uv.update()
    #         uv.on_change(e)
    #         venta_Total_Fruta_Crema()
    #     except:
    #         pass
    #     finally:
    #         page.update()

    # def venta_Total_Fruta_Crema():
    #     try:
    #         if fpi.value == "" or fpf.value == "" or fei.value == "" or fef.value == "":
    #             fv.value = 0
    #             fv.update()
    #     except:
    #         pass

    #     try:
    #         if upi.value == "" or upf.value == "" or uei.value == "" or uef.value == "":
    #             uv.value = 0
    #             uv.update()
    #     except:
    #         pass

    #     try:
    #         if fv.value != 0 and uv.value != 0:
    #             fruven.value = fv.value + uv.value
    #             print("Valores en ambos")
    #             print(fv.value)
    #             print(uv.value)

    #         if fv.value == "0" and uv.value == "0":
    #             fruven.value = "0"
    #             print("SIN Valor en ambos")
    #             print(fv.value)
    #             print(uv.value)
            
    #         if fv.value != "0" and uv.value == "0" or uv.value == "":
    #             fruven.value = fv.value
    #             print("Con Valor en FRESA")
    #             print(fv.value)
    #             print(uv.value)

    #         if fv.value == "0" or fv.value == "" and uv.value != "0":
    #             fruven.value = uv.value
    #             print("Con Valor en UVA")
    #             print(fv.value)
    #             print(uv.value)

    #         fruven.update()
    #     except:
    #         print("Error")
    #         pass
    #     page.update()

    # # ***** Funciones para el manejo de los campos de texto de la seccion de cremas *****

    # def conversion_n_capture_co(e):
    #     try:
    #         if "." in coi.value or "." in cof.value:
    #             num_coi = float(coi.value)
    #             num_cof = float(cof.value)
    #         else:
    #             num_coi = int(coi.value)
    #             num_cof = int(cof.value)

    #         num_cov = num_coi - num_cof

    #         if num_cov % 2 == 0 or num_cov % 2 == 1:
    #             num_cov = int(num_cov)
                
    #         cov.value = round(num_cov, 2)
    #     except ValueError:
    #         pass
    #     finally:
    #         page.update()

    # def conversion_n_capture_cch(e):
    #     try:
    #         if "." in cchi.value or "." in cchf.value:
    #             num_cchi = float(cchi.value)
    #             num_cchf = float(cchf.value)
    #         else:
    #             num_cchi = int(cchi.value)
    #             num_cchf = int(cchf.value)

    #         num_cchv = num_cchi - num_cchf

    #         if num_cchv % 2 == 0 or num_cchv % 2 == 1:
    #             num_cchv = int(num_cchv)

    #         cchv.value = round(num_cchv, 2)
    #     except ValueError:
    #         pass
    #     finally:
    #         page.update()

    # def conversion_n_capture_cca(e):
    #     try:
    #         if "." in ccai.value or "." in ccaf.value:
    #             num_ccaf = float(ccaf.value)
    #             num_ccai = float(ccai.value)
    #         else:
    #             num_ccaf = int(ccaf.value)
    #             num_ccai = int(ccai.value)

    #         num_ccav = num_ccai - num_ccaf

    #         if num_ccav % 2 == 0 or num_ccav % 2 == 1:
    #             num_ccav = int(num_ccav)
            
    #         ccav.value = round(num_ccav, 2)
    #     except ValueError:
    #         pass
    #     finally:
    #         page.update()

    # # ***** Funciones para el manejo de los campos de texto de la seccion de extras y adicionales *****

    # def conversion_n_capture_tE(e):
    #     try:
    #         num_t5 = int(t5.value)
    #         num_t10 = int(t10.value)
    #         total_t5 = num_t5 * 5
    #         total_t10 = num_t10 * 10
    #         num_tt = total_t5 + total_t10
    #         tt.value = num_tt
    #     except:
    #         pass
    #     finally:
    #         page.update()

    # def conversion_n_capture_sD(e):
    #     try:
    #         num_sd25 = int(sd25.value)
    #         num_sd35 = int(sd35.value)
    #         total_sd25 = num_sd25 * 25
    #         total_sd35 = num_sd35 * 35
    #         num_sdt = total_sd25 + total_sd35
    #         sdt.value = num_sdt
    #     except:
    #         pass
    #     finally:
    #         page.update()

    # def balance_General( e):
    #     num_bgi = vcvt.value + vmvt.value + vgvt.value + tt.value + sdt.value
    #     bgi.value = num_bgi
        
    #     try:
    #         num_trt = int(trt.value)
    #         num_grt = int(grt.value)
    #         num_bgd = num_trt + num_grt
    #         bgd.value = num_bgd
    #         num_bgt = bgi.value - bgd.value
    #         bgt.value = num_bgt
    #     except ValueError:
    #         pass
    #     finally:
    #         page.update()

    # def reset_Fields( e):
    #     variables_vc = [tci, tcf, vci, vcf, vcven, vcvt]
    #     for element in variables_vc:
    #         element.value = ""

    #     variables_vm = [tmi, tmf, vmi, vmf, vmven, vmvt]
    #     for element in variables_vm:
    #         element.value = ""

    #     variables_vg = [tgi, tgf, vgi, vgf, vgven, vgvt]
    #     for element in variables_vg:
    #         element.value = ""

    #     variables_frutas = [fpi, fpf, fei, fef, fv, upi, upf, uei, uef, uv]
    #     for element in variables_frutas:
    #         element.value = ""

    #     variables_cremas = [coi, cof, cov, cchi, cchf, cchv, ccai, ccaf, ccav]
    #     for element in variables_cremas:
    #         element.value = ""

    #     extras = [t5, t10, tt, sd25, sd35, sdt, trn, trt, grn, grt, bgi, bgd, bgt]
    #     for element in extras:
    #         element.value = ""

    #     page.update()

    # def reset_textFields(e):
    #     report_field.value = ""
    #     sales_field.value = ""
    #     page.update()

ft.app(main)