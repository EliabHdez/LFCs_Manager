import flet as ft
from fpdf import FPDF
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        # Cuando es .exe
        base_path = sys._MEIPASS
    else:
        # Cuando estás en desarrollo
        base_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..")
        )

    return os.path.join(base_path, relative_path)

logo_path = resource_path(os.path.join("assets", "Images", "LogoReporte.png"))

#====================================================#
#     CREACION DE REPORTE EXTERNO EN FORMATO PDF     #
#====================================================#

def create_ReportPDF(ui):
        print("GENERANDO REPORTE...")
        # fecha_Actual_PDF = dt.datetime.today().date()
        # fecha_Formateada = fecha_Actual_PDF.strftime("%d-%b-%Y")
        # fecha_Formateada_RN = fecha_Actual_PDF.strftime("%d-%m-%y")
        # f_pdv = ui.pdv

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(True, margin=5)
        pdf.add_page()

        pdf.set_font("Arial", "", 10)

        pdf.image(logo_path, 10, 7, 40)
        pdf.cell(187, 5, f'{ui.date_receiver}', 0, 1, "R")
        pdf.cell(187, 5, f'Encargado(a): {ui.encSuc.value.upper()}', 0, 1, "R")

        # Titulo
        pdf.cell(0, 25, f'Reporte {ui.pdv_suc}'.upper(), 0, 1, 'C')
        pdf.line(75, 35, 135, 35)

        # Vasos
        pdf.cell(70, 10, 'VASOS', 1, 0, "C")
        pdf.cell(15, 10, 'TI', 1, 0, 'C')
        pdf.cell(15, 10, 'TF', 1, 0, 'C')
        pdf.cell(15, 10, 'VI', 1, 0, 'C')
        pdf.cell(15, 10, 'VF', 1, 0, 'C')
        pdf.cell(25, 10, 'VENDIDOS', 1, 0, 'C')
        pdf.cell(35, 10, 'MONTO VENTA', 1, 1, 'C')
        pdf.cell(70, 8, 'VASOS CHICOS', 1, 0)
        pdf.cell(15, 8, f'{ui.tci.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.tcf.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vci.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vcf.value}', 1, 0, 'C')
        pdf.cell(25, 8, f'{ui.vcven.value}', 1, 0, 'C')
        pdf.cell(35, 8, f'${ui.vcvt.value}', 1, 1, 'C')
        pdf.cell(70, 8, 'VASOS INDIVIDUALES', 1, 0)
        pdf.cell(15, 8, f'{ui.tii.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.tif.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vii.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vif.value}', 1, 0, 'C')
        pdf.cell(25, 8, f'{ui.viven.value}', 1, 0, 'C')
        pdf.cell(35, 8, f'${ui.vivt.value}', 1, 1, 'C')
        pdf.cell(70, 8, 'VASOS MEDIANOS', 1, 0)
        pdf.cell(15, 8, f'{ui.tmi.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.tmf.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vmi.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vmf.value}', 1, 0, 'C')
        pdf.cell(25, 8, f'{ui.vmven.value}', 1, 0, 'C')
        pdf.cell(35, 8, f'${ui.vmvt.value}', 1, 1, 'C')
        pdf.cell(70, 8, 'VASOS GRANDES', 1, 0)
        pdf.cell(15, 8, f'{ui.tgi.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.tgf.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vgi.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vgf.value}', 1, 0, 'C')
        pdf.cell(25, 8, f'{ui.vgven.value}', 1, 0, 'C')
        pdf.cell(35, 8, f'${ui.vgvt.value}', 1, 1, 'C')
        pdf.cell(70, 8, 'VASOS MEGAS', 1, 0)
        pdf.cell(15, 8, f'{ui.tmgi.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.tmgf.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vmgi.value}', 1, 0, 'C')
        pdf.cell(15, 8, f'{ui.vmgf.value}', 1, 0, 'C')
        pdf.cell(25, 8, f'{ui.vmgven.value}', 1, 0, 'C')
        pdf.cell(35, 8, f'${ui.vmgvt.value}', 1, 1, 'C')    

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)    
        pdf.cell(20, 10, 'FRUTA', 1, 0, 'C')
        pdf.cell(9, 10, 'FI', 1, 0, 'C')
        pdf.cell(9, 10, '1S', 1, 0, 'C')
        pdf.cell(9, 10, '2S', 1, 0, 'C')
        pdf.cell(9, 10, '3S', 1, 0, 'C')
        pdf.cell(9, 10, '4S', 1, 0, 'C')
        pdf.cell(9, 10, 'FF', 1, 0, 'C')
        pdf.cell(23, 10, 'VENDIDA', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(20, 10, 'CREMA', 1, 0, 'C')
        pdf.cell(9, 10, 'CI', 1, 0, 'C')
        pdf.cell(9, 10, '1S', 1, 0, 'C')
        pdf.cell(9, 10, '2S', 1, 0, 'C')
        pdf.cell(9, 10, '3S', 1, 0, 'C')
        pdf.cell(9, 10, 'CF', 1, 0, 'C')
        pdf.cell(23, 10, 'VENDIDA', 1, 1, 'C')

        pdf.cell(20, 8, 'FRESA', 1, 0)
        pdf.cell(9, 8, f'{ui.fi.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.f1s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.f2s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.f3s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.f4s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.ff.value}', 1, 0, 'C')
        pdf.cell(23, 8, f'{ui.fv.value}', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(20, 8, 'CR ORIG', 1, 0)
        pdf.cell(9, 8, f'{ui.coi.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.co1s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.co2s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.co3s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.cof.value}', 1, 0, 'C')
        pdf.cell(23, 8, f'{ui.cov.value}', 1, 1, 'C')

        pdf.cell(20, 8, 'UVA', 1, 0)
        pdf.cell(9, 8, f'{ui.ui.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.u1s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.u2s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.u3s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.u4s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.uf.value}', 1, 0, 'C')
        pdf.cell(23, 8, f'{ui.uv.value}', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(20, 8, 'CR CHOC', 1, 0)
        pdf.cell(9, 8, f'{ui.cchi.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.cch1s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.cch2s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.cch3s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.cchf.value}', 1, 0, 'C')
        pdf.cell(23, 8, f'{ui.cchv.value}', 1, 1, 'C')

        pdf.cell(20, 8, '', 0, 0)
        pdf.cell(9, 8, '', 0, 0,)
        pdf.cell(9, 8, '', 0, 0,)
        pdf.cell(9, 8, '', 0, 0,)
        pdf.cell(9, 8, '', 0, 0,)
        pdf.cell(9, 8, '', 0, 0,)
        pdf.cell(9, 8, '', 0, 0,)
        pdf.cell(23, 8, '', 0, 0,)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(20, 8, 'CR CAFE', 1, 0)
        pdf.cell(9, 8, f'{ui.ccai.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.cca1s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.cca2s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.cca3s.value}', 1, 0, 'C')
        pdf.cell(9, 8, f'{ui.ccaf.value}', 1, 0, 'C')
        pdf.cell(23, 8, f'{ui.ccav.value}', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        pdf.cell(32, 10, 'TOPPS EXTRA', 1, 0, 'C')
        pdf.cell(15, 10, 'CANT', 1, 0, 'C')
        pdf.cell(23, 10, 'SUBTOTAL', 1, 0, 'C')
        pdf.cell(20, 10, 'TOTAL', 1, 0, 'C')
        # pdf.multi_cell(25, 10, 'TOTAL GRAL', 1, "C")

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)
        # pdf.multi_cell(5, 10, '', 0, 0)

        pdf.cell(37, 10, 'SERV DOMICILIO', 1, 0, 'C')
        pdf.cell(15, 10, 'CANT', 1, 0, 'C')
        pdf.cell(23, 10, 'SUBTOTAL', 1, 0, 'C')
        pdf.cell(20, 10, 'TOTAL', 1, 1, 'C')
        # pdf.multi_cell(25, 10, 'TOTAL GRAL', 1, "C")

        x, y = pdf.get_x(), pdf.get_y()

        pdf.cell(32, 10, 'TOPPING 5', 1, 0, 'C')
        pdf.cell(15, 10, f'{ui.t5.value}', 1, 0, 'C')
        pdf.cell(23, 10, f'${ui.total_t5}', 1, 0, 'C')
        x2 = pdf.get_x()
        pdf.set_xy(x2, y)
        pdf.cell(20, 20, f'${ui.tet.value}', 1, 0, "C")

        # Separador vertical con celda
        pdf.set_xy(x2+20, y)
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(37, 10, f'SERV DOM 20', 1, 0, 'C')
        pdf.cell(15, 10, f'{ui.sd20.value}', 1, 0, 'C')
        pdf.cell(23, 10, f'${ui.total_sd20}', 1, 0, 'C')
        x2 = pdf.get_x()
        pdf.set_xy(x2, y)
        pdf.cell(20, 20, f'${ui.sdt.value}', 1, 1, "C")

        pdf.set_xy(x, y+10)
        pdf.cell(32, 10, f'TOPPING 10', 1, 0, 'C')
        pdf.cell(15, 10, f'{ui.t10.value}', 1, 0, 'C')
        pdf.cell(23, 10, f'${ui.total_t10}', 1, 0, 'C')
        pdf.cell(20, 10, "", 0, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(37, 10, f'SERV DOM 35', 1, 0, 'C')
        pdf.cell(15, 10, f'{ui.sd35.value}', 1, 0, 'C')
        pdf.cell(23, 10, f'${ui.total_sd35}', 1, 0, 'C')
        pdf.cell(20, 10, "", 0, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        pdf.cell(90, 10, 'TRANSFERENCIAS', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(95, 10, 'GASTOS Y RETIROS', 1, 1, 'C')

        pdf.cell(60, 10, 'NO. DE TRANSFERENCIAS', 1, 0, 'C')
        pdf.cell(30, 10, 'TOTAL', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(60, 10, 'NO. DE GASTOS | RETIROS', 1, 0, 'C')
        pdf.cell(35, 10, 'TOTAL', 1, 1, 'C')

        pdf.cell(60, 10, f'{ui.trn.value}', 1, 0, 'C')
        pdf.cell(30, 10, f'${ui.trt.value}', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(60, 10, f'{ui.grn.value}', 1, 0, 'C')
        pdf.cell(35, 10, f'${ui.grt.value}', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        pdf.cell(90, 12, 'MONTOS TRANSFERENCIAS Y GASTOS | RETIROS', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(95, 12, 'INGRESOS Y DEDUCCIONES', 1, 1, 'C')

        pdf.cell(45, 8, 'TRANSFERENCIAS', 1, 0, 'C')
        pdf.cell(45, 8, 'GASTOS | RETIROS', 1, 0, 'C')

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(47.5, 8, f'INGRESOS TOTALES PDV', 1, 0, 'C')
        pdf.cell(47.5, 8, f'${ui.bgtd.value}', 1, 1, 'C')

        x, y = pdf.get_x(), pdf.get_y()
        pdf.multi_cell(22.5, 6.85, f'  - ${ui.tr1.value}\n  - ${ui.tr2.value}\n  - ${ui.tr3.value}\n  - ${ui.tr4.value}\n  - ${ui.tr5.value}\n  - ${ui.tr6.value}\n', border="LTB", align="L")

        pdf.set_xy(x+22.5, y)
        pdf.multi_cell(22.5, 6.85, f'  - ${ui.tr7.value}\n  - ${ui.tr8.value}\n  - ${ui.tr9.value}\n  - ${ui.tr10.value}\n  - ${ui.tr11.value}\n  - ${ui.tr12.value}\n', border="TRB", align="L")

        pdf.set_xy(x+45, y)
        pdf.multi_cell(45, 6.85, f'- ${ui.gr1.value}\n- ${ui.gr2.value}\n- ${ui.gr3.value}\n- ${ui.gr4.value}\n- ${ui.gr5.value}\n- ${ui.gr6.value}\n', 1, "C")

        # Separador vertical con celda
        # pdf.cell(5, 10, '', 0, 0)
        pdf.set_xy(x+95, y)

        pdf.cell(47.5, 8, 'DEDUCCIONES (TR/GR)', 1, 0, 'C')
        pdf.cell(47.5, 8, f'${ui.bgegr.value}', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 5, '', 0, 1)

        pdf.cell(45, 10, '', 0, 0)
        pdf.cell(45, 10, '', 0, 0)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(95, 12, 'VENTA PDV', 1, 1, 'C')

        pdf.cell(45, 10, '', 0, 0)
        pdf.cell(45, 10, '', 0, 0)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(47.5, 8, f'TOTAL DIA PDV', 1, 0, 'C')
        pdf.cell(47.5, 8, f'${ui.bgtd.value}', 1, 1, 'C')

        pdf.cell(45, 10, '', 0, 0)
        pdf.cell(45, 10, '', 0, 0)

        # Separador vertical con celda
        pdf.cell(5, 10, '', 0, 0)

        pdf.cell(47.5, 8, 'EFECTIVO DIA PDV', 1, 0, 'C')
        pdf.cell(47.5, 8, f'${ui.bgte.value}', 1, 1, 'C')

        # Separador con celda
        pdf.cell(0, 10, '', 0, 1)

        pdf.cell(0, 10, '* FIN REPORTE *'.upper(), 0, 1, 'C')

        # Condicional para definir la ruta según el sistema
        if os.name == "posix":  # Linux o Mac
            ruta = os.path.join(os.environ['HOME'], "Dropbox", "Las_Fresas_con_Cremas", "App", "Reportes_PDVs")
        else:  # Windows
            ruta = os.path.join(os.environ['USERPROFILE'], "Dropbox", "Las_Fresas_con_Cremas", "App", "Reportes_PDVs")

        pdf.output(f"{ruta}/{ui.date_receiver} - Reporte {ui.pdv_suc}.pdf")
        # pdf.output(f"../Reportes_PDV's/{ui.date_receiver} - Reporte {ui.pdv}.pdf")

        print("GENERACIÓN DE REPORTE FINALIZADA")

        report_confirmation_succesfully = ft.AlertDialog(
            modal=True,
            # title=ft.Text("Cuentas"),
            content=ft.Text('PDF generado con éxito'),
            actions=[
                ft.TextButton("OK", on_click=lambda e: ui.page.close(e.control.parent))
            ]
        )

        ui.page.open(report_confirmation_succesfully)

#===================================================================================#
#     CARGA DE INFORMACION REPORTE EN EL CAMPO DE TEXTO DE LA VENTANA DE VENTAS     #
#===================================================================================#

def generar_Reporte(ui): # Reporte para pagina de ventas y reporte
        # print(f"La sucursal seleccionada es: {e.control.value}")
        # fecha_Actual_TF = dt.datetime.today().date()
        # fecha_Formateada = fecha_Actual_TF.strftime("%d-%b-%Y")
        if ui.pdv_suc != "":
            try:
                ui.report_field.value = (
                                f"                                                                                                             {ui.date_receiver}\n\n"
                                f"{ui.pdv_suc.upper()}\n"
                                f"Encargado(a): {ui.encSuc.value.upper()}\n\n"
                                f"→  VASOS\n"
                                f"     •  Chicos - TI: {ui.tci.value} | TP: {ui.tcf.value} | VI: {ui.vci.value} | VF: {ui.vcf.value} | VV: {ui.vcven.value} | VENTA: $ {ui.vcvt.value}\n"
                                f"     •  Individuales - TI: {ui.tii.value} | TP: {ui.tif.value} | VI: {ui.vii.value} | VF: {ui.vif.value} | VV: {ui.viven.value} | VENTA: $ {ui.vivt.value}\n"
                                f"     •  Medianos - TI: {ui.tmi.value} | TP: {ui.tmf.value} | VI: {ui.vmi.value} | VF: {ui.vmf.value} | VV: {ui.vmven.value} | VENTA: $ {ui.vmvt.value}\n"
                                f"     •  Grandes - TI: {ui.tgi.value} | TP: {ui.tgf.value} | VI: {ui.vgi.value} | VF: {ui.vgf.value} | VV: {ui.vgven.value} | VENTA: $ {ui.vgvt.value}\n"
                                f"     •  Megas - TI: {ui.tmgi.value} | TP: {ui.tmgf.value} | VI: {ui.vmgi.value} | VF: {ui.vmgf.value} | VV: {ui.vmgven.value} | VENTA: $ {ui.vmgvt.value}\n\n"
                                f"→  FRUTA\n"
                                f"     •  Fresa - FI: {ui.fi.value} | 1S: {ui.f1s.value} | 2S: {ui.f2s.value} | 3S: {ui.f3s.value} | 4S: {ui.f4s.value} | FF: {ui.ff.value} | FV: {ui.fv.value} bote(s)\n"
                                f"     •  Uva - UI: {ui.ui.value} | 1S: {ui.u1s.value} | 2S: {ui.u2s.value} | 3S: {ui.u3s.value} | 4S: {ui.u4s.value} | UF: {ui.uf.value} | UV: {ui.uv.value} bote(s)\n\n"
                                f"→  CREMAS\n"
                                f"     •  Original - In: {ui.coi.value} | 1S: {ui.co1s.value} | 2S: {ui.co2s.value} | 3S: {ui.co3s.value} | Fi: {ui.cof.value} | COV: {ui.cov.value} bote(s)\n"
                                f"     •  Chocolate - In: {ui.cchi.value} | 1S: {ui.cch1s.value} | 2S: {ui.cch2s.value} | 3S: {ui.cch3s.value} | Fi: {ui.cchf.value} | CCHV: {ui.cchv.value} bote(s)\n"
                                f"     •  Cafe - In: {ui.ccai.value} | 1S: {ui.cca1s.value} | 2S: {ui.cca2s.value} | 3S: {ui.cca3s.value} | Fi: {ui.ccaf.value} | CCV: {ui.ccav.value} bote(s)\n\n"
                                f"→  TOPPINGS EXTRAS\n"
                                f"     •  TE5: {ui.t5.value} | TE10: {ui.t10.value} | Total: $ {ui.tet.value}\n\n"
                                f"→  SERVICIOS A DOMICILIO\n"
                                f"     •  SD20: {ui.sd20.value} | SD35: {ui.sd35.value} | Total: $ {ui.sdt.value}\n\n"
                                f"→  TRANSFERENCIAS\n"
                                f"     •  No Transferencias: {ui.trn.value} | Total: $ {ui.trt.value}\n\n"
                                f"→  GASTOS | RETIROS\n"
                                f"     •  Cantidad: {ui.grn.value} | Total: $ {ui.grt.value}\n\n"
                                f"→  INGRESOS | DEDUCCIONES\n"
                                f"     •  Ingresos PDV: $ {ui.bgtd.value}\n"
                                f"     •  Deducciones: $ {ui.bgegr.value}\n\n"
                                f"→  TOTAL DIA PDV\n"
                                f"     •  Efectivo: $ {ui.bgte.value}\n"
                                f"     •  Venta Total: $ {ui.bgtd.value}\n\n"

                                f"<<< FIN DEL REPORTE >>>"
                            )
            except Exception as ex:
                print(ex)

        else:
            noSelectPDV_dialog = ft.CupertinoAlertDialog(
                modal=True,
                title=ft.Text("Por favor, selecciona un Punto de Venta", size=13),
                actions=[
                    ft.CupertinoDialogAction("Aceptar", is_destructive_action=True, on_click=lambda e: (ui.page.close(e.control.parent), ui.page.update()))
                ]
            )

            ui.page.open(noSelectPDV_dialog)

            # noSelectPDV = ft.AlertDialog(
            #     modal=True,
            #     # title=ft.Text("Cuentas"),
            #     content=ft.Container(
            #         width=800,
            #         padding=10,
            #         content=ft.Text('Por favor seleccione un PDV')
            #     ),
            #     actions=[
            #         ft.TextButton("Ok", on_click=lambda e: ui.page.close(e.control.parent))
            #     ]
            # )

            # ui.page.open(noSelectPDV)