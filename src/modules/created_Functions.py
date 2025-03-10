import flet as ft

color_teal = "#00ebab"
color_teal_2 = "#11b78a"

# ***** Función creadora de boton para cambio de tema (Modo Claro / Oscuro) *****

def create_Boton_Switch():
    return ft.Switch(
        adaptive=True,
        tooltip="Modo Nocturno",
        value=True,
        thumb_color="#222222",
        active_track_color=ft.Colors.CYAN,
        # active_color="red",
        inactive_thumb_color=ft.Colors.BLUE,
        inactive_track_color=ft.Colors.BLUE_GREY_500,
        thumb_icon={
            ft.ControlState.HOVERED: ft.Icons.DARK_MODE_SHARP,
            ft.ControlState.SELECTED: ft.Icons.DARK_MODE
        }
    )

# ***** Función creadora de radios para la selección de sucursales *****

def create_radio(Value, Label):
    return ft.Radio(
        value=Value,
        label=Label,
        label_style=ft.TextStyle(size=12),
        visual_density=ft.VisualDensity.STANDARD,
        fill_color={
            ft.ControlState.DEFAULT: ft.Colors.PINK,
            ft.ControlState.SELECTED: color_teal,
        },
    )

# ***** Función creadora de campos de texto para las secciones de vasos, frutas y cremas *****

def create_textfield(Label, label_Style=ft.TextStyle(color="#a2a2a2", size=10), Color="#d3d3d3", text_Size=20, Width=110, border_Color=ft.Colors.WHITE, border_Width=1.5, focused_Border_Color="#08f5a9", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, suffix_Text=None, suffix_Style=ft.TextStyle(color="#a2a2a2", size=9), on_Focus=None, read_Only=False, on_Change=None):
    return ft.TextField(
        # height=30,
        width=Width,
        # color="#dc0000", # rojo
        text_align="center",
        # label_style=ft.TextStyle(color="#545454", size=10), # color = gris claro
        # label_style=ft.TextStyle(color="#c1c1c1", size=10), # color = gris claro
        label_style=label_Style, # color = gris claro
        # content_padding=2,
        # bgcolor="white",
        # bgcolor=ft.Colors.BLUE_GREY_900,
        cursor_height=22,
        # cursor_color="#747474", # gris oscuro
        cursor_color="#a8a8a8", # gris oscuro
        focused_border_color=focused_Border_Color,
        # focused_border_color="#00ebab",
        focused_border_width=2,
        on_focus=on_Focus,
        label=Label,
        color=Color,
        text_size=text_Size,
        prefix_text=prefix_Text,
        prefix_style=prefix_Style,
        border=ft.InputBorder.UNDERLINE,
        border_color=border_Color,
        border_width=border_Width,
        hint_text=hint_Text,
        hint_style=hint_Style,
        suffix_text=suffix_Text,
        suffix_style=suffix_Style,
        read_only=read_Only,
        # filled=True,
        on_change=on_Change
    )

def create_textfield_WB(Label, Height=30, Color="#d3d3d3", text_Size=25, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, suffix_Text=None, suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=False, on_Change=None):
    return ft.TextField(
        height=Height,
        # width=200,
        # color="#dc0000", # rojo
        text_align="center",
        # label_style=ft.TextStyle(color="#545454", size=10), # color = gris claro
        # label_style=ft.TextStyle(color="#c1c1c1", size=10), # color = gris claro
        label_style=ft.TextStyle(color="#a2a2a2", size=14), # color = gris claro
        content_padding=3,
        # bgcolor="white",
        bgcolor="#292929",
        cursor_height=18,
        # cursor_color="#747474", # gris oscuro
        cursor_color="#a8a8a8", # gris oscuro
        focused_border_color=focused_Border_Color,
        focused_border_width=.5,
        label=Label,
        color=Color,
        text_size=text_Size,
        prefix_text=prefix_Text,
        prefix_style=prefix_Style,
        border_color=border_Color,
        border_width=border_Width,
        suffix_text=suffix_Text,
        suffix_style=suffix_Style,
        hint_text=hint_Text,
        hint_style=hint_Style,
        read_only=read_Only,
        on_change=on_Change
    )

# ***** Función creadora de campos de texto para la seccion de extra y adicionales *****

def create_textField_Extras(Width, Height, Color="#d3d3d3", text_Size=12, border_Color=None, read_Only=False, on_Change=False):
    return ft.TextField(
        text_size=text_Size,
        color=Color,
        width=Width,
        height=Height,
        border_color=border_Color,
        # "#0c52ff" # Color del border_Color a aplicar en una actualizacion a posteriori como predeterminado en lugar del None
        bgcolor=ft.Colors.BLUE_GREY_900,
        cursor_height=15,
        cursor_color="#a8a8a8", # gris oscuro
        content_padding=0,
        text_align="center",
        focused_border_color="black",
        focused_border_width=1.5,
        read_only=read_Only,
        on_change=on_Change
    )

def create_textField_RyV(counter_Text, read_Only=True):
    return ft.TextField(
        #  bgcolor=ft.Colors.BLUE_GREY_700,
         bgcolor="#292929",
         color="white",
         multiline=True,
         min_lines=25,
         text_size=12,
         cursor_height=15,
         cursor_color="white",
        #  border_color="#0c52ff",
         border_color="white",
         border_width=1,
         counter_text=counter_Text,
         counter_style=ft.TextStyle(weight=ft.FontWeight.BOLD, italic=True, letter_spacing=5, size=10),
         read_only=read_Only
        #  content_padding=ft.Padding(top=50, bottom=5, left=20, right=5)
    )

def created_Button(Text, bgColor, Icon, on_Click=None):
    return ft.ElevatedButton(
        text=Text,
        bgcolor=bgColor,
        color="black",
        icon=Icon,
        icon_color="black",
        width=150,
        style=ft.ButtonStyle(text_style={
            ft.ControlState.DEFAULT: ft.TextStyle(size=12),
            ft.ControlState.PRESSED: ft.TextStyle(size=10)
            }
        ),
        on_click=on_Click
    )


# Funciones de control para los elementos creados

def Focus(e):
    e.control.label = "Cantidad"
    e.control.update()

# def onHover_Containers(e):
#     print(f"{e.data}")
#     if e.data == "true":
#         e.control.bgcolor = ft.Colors.with_opacity(0.2, "#cdcdcd")
#     else:
#         e.control.bgcolor = ft.Colors.TRANSPARENT

#     e.control.bgcolor = e.control.bgcolor
#     e.control.update()

# def onHover_Containers(e):
#     e.control.bgcolor = ft.Colors.with_opacity(0.2, "#cdcdcd") if e.data == "true" else ft.Colors.TRANSPARENT
#     e.control.update()

# def onFocus_Containers(e):
#     e.control.bgcolor = "#29926f" if e.data == "true" else ft.Colors.TRANSPARENT
#     e.control.update()