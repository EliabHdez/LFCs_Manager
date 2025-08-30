import flet as ft
from fpdf import FPDF
import datetime as dt
import os
# import os

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
    pdf.add_page()

    pdf.set_font("Arial", "", 10)

    pdf.image("../assets/Images/LogoReporte.png", 10, 7, 40)
    pdf.cell(187, 10, f'{ui.date_receiver}', 0, 1, "R")

    # Titulo
    pdf.cell(0, 25, f'Reporte {ui.pdv}'.upper(), 0, 1, 'C')
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

    # Separador con celda
    pdf.cell(0, 5, '', 0, 1)    
    pdf.cell(30, 10, 'FRUTA', 1, 0, 'C')
    pdf.cell(11, 10, 'PI', 1, 0, 'C')
    pdf.cell(11, 10, 'PF', 1, 0, 'C')
    pdf.cell(11, 10, 'EI', 1, 0, 'C')
    pdf.cell(11, 10, 'EF', 1, 0, 'C')
    pdf.cell(26, 10, 'VENDIDOS', 1, 0, 'C')

    # Separador vertical con celda
    pdf.cell(5, 10, '', 0, 0)

    pdf.cell(35, 10, 'CREMA', 1, 0, 'C')
    pdf.cell(12.5, 10, 'IN', 1, 0, 'C')
    pdf.cell(12.5, 10, 'FI', 1, 0, 'C')
    pdf.cell(25, 10, 'VENDIDOS', 1, 1, 'C')

    pdf.cell(30, 8, 'FRESA', 1, 0)
    pdf.cell(11, 8, f'{ui.fpi.value}', 1, 0, 'C')
    pdf.cell(11, 8, f'{ui.fpf.value}', 1, 0, 'C')
    pdf.cell(11, 8, f'{ui.fei.value}', 1, 0, 'C')
    pdf.cell(11, 8, f'{ui.fef.value}', 1, 0, 'C')
    pdf.cell(26, 8, f'{ui.fv.value}', 1, 0, 'C')

    # Separador vertical con celda
    pdf.cell(5, 10, '', 0, 0)

    pdf.cell(35, 8, 'CR ORIGINAL', 1, 0)
    pdf.cell(12.5, 8, f'{ui.coi.value}', 1, 0, 'C')
    pdf.cell(12.5, 8, f'{ui.cof.value}', 1, 0, 'C')
    pdf.cell(25, 8, f'{ui.cov.value}', 1, 1, 'C')

    pdf.cell(30, 8, 'UVA', 1, 0)
    pdf.cell(11, 8, f'{ui.upi.value}', 1, 0, 'C')
    pdf.cell(11, 8, f'{ui.upf.value}', 1, 0, 'C')
    pdf.cell(11, 8, f'{ui.uei.value}', 1, 0, 'C')
    pdf.cell(11, 8, f'{ui.uef.value}', 1, 0, 'C')
    pdf.cell(26, 8, f'{ui.uv.value}', 1, 0, 'C')

    # Separador vertical con celda
    pdf.cell(5, 10, '', 0, 0)

    pdf.cell(35, 8, 'CR CHOCOLATE', 1, 0)
    pdf.cell(12.5, 8, f'{ui.cchi.value}', 1, 0, 'C')
    pdf.cell(12.5, 8, f'{ui.cchf.value}', 1, 0, 'C')
    pdf.cell(25, 8, f'{ui.cchv.value}', 1, 1, 'C')

    pdf.cell(30, 8, '', 0, 0)
    pdf.cell(10, 8, '', 0, 0,)
    pdf.cell(10, 8, '', 0, 0,)
    pdf.cell(10, 8, '', 0, 0,)
    pdf.cell(10, 8, '', 0, 0,)
    pdf.cell(30, 8, '', 0, 0,)

    # Separador vertical con celda
    pdf.cell(5, 10, '', 0, 0)

    pdf.cell(35, 8, 'CR CAFE', 1, 0)
    pdf.cell(12.5, 8, f'{ui.ccai.value}', 1, 0, 'C')
    pdf.cell(12.5, 8, f'{ui.ccaf.value}', 1, 0, 'C')
    pdf.cell(25, 8, f'{ui.ccav.value}', 1, 1, 'C')

    # Separador con celda
    pdf.cell(0, 5, '', 0, 1)

    pdf.cell(45, 10, 'TOPPINGS EXTRA', 1, 0, 'C')
    pdf.cell(25, 10, 'CANTIDAD', 1, 0, 'C')
    pdf.cell(20, 10, 'TOTAL', 1, 0, 'C')

    # Separador vertical con celda
    pdf.cell(5, 10, '', 0, 0)

    pdf.cell(50, 10, 'SERVICIOS A DOMICILIO', 1, 0, 'C')
    pdf.cell(25, 10, 'CANTIDAD', 1, 0, 'C')
    pdf.cell(20, 10, 'TOTAL', 1, 1, 'C')

    pdf.cell(45, 10, 'TOPPING 5', 1, 0, 'C')
    pdf.cell(25, 10, f'{ui.t5.value}', 1, 0, 'C')
    pdf.cell(20, 10, f'${ui.total_t5}', 1, 0, 'C')

    # Separador vertical con celda
    pdf.cell(5, 10, '', 0, 0)

    pdf.cell(50, 10, f'SERV DOM 20', 1, 0, 'C')
    pdf.cell(25, 10, f'{ui.sd20.value}', 1, 0, 'C')
    pdf.cell(20, 10, f'${ui.total_sd20}', 1, 1, 'C')

    pdf.cell(45, 10, f'TOPPING 10', 1, 0, 'C')
    pdf.cell(25, 10, f'{ui.t10.value}', 1, 0, 'C')
    pdf.cell(20, 10, f'${ui.total_t10}', 1, 0, 'C')

    # Separador vertical con celda
    pdf.cell(5, 10, '', 0, 0)

    pdf.cell(50, 10, f'SERV DOM 35', 1, 0, 'C')
    pdf.cell(25, 10, f'{ui.sd35.value}', 1, 0, 'C')
    pdf.cell(20, 10, f'${ui.total_sd35}', 1, 1, 'C')

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

    pdf.cell(95, 12, 'INGRESOS Y EGRESOS', 1, 1, 'C')

    pdf.cell(45, 8, 'TRANSFERENCIAS', 1, 0, 'C')
    pdf.cell(45, 8, 'GASTOS | RETIROS', 1, 0, 'C')

    # Separador vertical con celda
    pdf.cell(5, 10, '', 0, 0)

    pdf.cell(47.5, 8, f'INGRESOS', 1, 0, 'C')
    pdf.cell(47.5, 8, f'${ui.bging.value}', 1, 1, 'C')

    x, y = pdf.get_x(), pdf.get_y()
    pdf.multi_cell(22.5, 6.85, f'  - ${ui.tr1.value}\n  - ${ui.tr2.value}\n  - ${ui.tr3.value}\n  - ${ui.tr4.value}\n  - ${ui.tr5.value}\n  - ${ui.tr6.value}\n', border="LTB", align="L")

    pdf.set_xy(x+22.5, y)
    pdf.multi_cell(22.5, 6.85, f'  - ${ui.tr7.value}\n  - ${ui.tr8.value}\n  - ${ui.tr9.value}\n  - ${ui.tr10.value}\n  - ${ui.tr11.value}\n  - ${ui.tr12.value}\n', border="TRB", align="L")

    pdf.set_xy(x+45, y)
    pdf.multi_cell(45, 6.85, f'- ${ui.gr1.value}\n- ${ui.gr2.value}\n- ${ui.gr3.value}\n- ${ui.gr4.value}\n- ${ui.gr5.value}\n- ${ui.gr6.value}\n', 1, "C")

    # Separador vertical con celda
    # pdf.cell(5, 10, '', 0, 0)
    pdf.set_xy(x+95, y)

    pdf.cell(47.5, 8, 'EGRESOS', 1, 0, 'C')
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

    pdf.cell(0, 12, '* FIN REPORTE *'.upper(), 0, 1, 'C')

    # Condicional para definir la ruta según el sistema
    if os.name == "posix":  # Linux o Mac
        ruta = os.path.join(os.environ['HOME'], "Dropbox", "Las_Fresas_con_Crema's", "App", "Reportes_PDVs")
    else:  # Windows
        ruta = os.path.join(os.environ['USERPROFILE'], "Dropbox", "Las_Fresas_con_Crema's", "App", "Reportes_PDVs")

    pdf.output(f"{ruta}/{ui.date_receiver} - Reporte {ui.pdv}.pdf")
    # pdf.output(f"../Reportes_PDV's/{ui.date_receiver} - Reporte {ui.pdv}.pdf")

    print("GENERACIÓN DE REPORTE FINALIZADA")

#===================================================================================#
#     CARGA DE INFORMACION REPORTE EN EL CAMPO DE TEXTO DE LA VENTANA DE VENTAS     #
#===================================================================================#

def generar_Reporte(ui):
        # print(f"La sucursal seleccionada es: {e.control.value}")
        # fecha_Actual_TF = dt.datetime.today().date()
        # fecha_Formateada = fecha_Actual_TF.strftime("%d-%b-%Y")
        ui.report_field.value = (
                                f"                                                                       {ui.date_receiver}\n\n"
                                f"<<< {ui.pdv} >>>\n\n"
                                f"--- VASOS CHICOS ---\n"
                                f"TI: {ui.tci.value} | TP: {ui.tcf.value} | VI: {ui.vci.value} | VF: {ui.vcf.value} | VV: {ui.vcven.value} | VENTA: $ {ui.vcvt.value}\n\n"
                                f"--- VASOS MEDIANOS ---\n"
                                f"TI: {ui.tmi.value} | TP: {ui.tmf.value} | VI: {ui.vmi.value} | VF: {ui.vmf.value} | VV: {ui.vmven.value} | VENTA: $ {ui.vmvt.value}\n\n"
                                f"--- VASOS GRANDES ---\n"
                                f"TI: {ui.tgi.value} | TP: {ui.tgf.value} | VI: {ui.vgi.value} | VF: {ui.vgf.value} | VV: {ui.vgven.value} | VENTA: $ {ui.vgvt.value}\n\n"
                                f"--- FRUTA ---\n"
                                f"Fresa - PI: {ui.fpi.value} | PF: {ui.fpf.value} | EI: {ui.fei.value} | EF: {ui.fef.value} | Vendida: {ui.fv.value} bote(s)\n"
                                f"Uva - PI: {ui.upi.value} | PF: {ui.upf.value} | EI: {ui.uei.value} | EF: {ui.uef.value} | Vendida: {ui.uv.value} bote(s)\n\n"
                                f"--- CREMAS ---\n"
                                f"Crema Original - I: {ui.coi.value} | F: {ui.cof.value} | Vendida: {ui.cov.value} bote(s)\n"
                                f"Crema Chocolate - I: {ui.cchi.value} | F: {ui.cchf.value} | Vendida: {ui.cchv.value} bote(s)\n"
                                f"Crema Cafe - I: {ui.ccai.value} | F: {ui.ccaf.value} | Vendida: {ui.ccav.value} bote(s)\n\n"
                                f"--- TOPPINGS EXTRA ---\n"
                                f"TE5: {ui.t5.value} | TE10: {ui.t10.value} | Total: $ {ui.tet.value}\n\n"
                                f"--- SERVICIOS A DOMICILIO ---\n"
                                f"SD20: {ui.sd20.value} | SD35: {ui.sd35.value} | Total: $ {ui.sdt.value}\n\n"
                                f"--- TRANSFERENCIAS ---\n"
                                f"No Transferencias: {ui.trn.value} | Monto Total: $ {ui.trt.value}\n\n"
                                f"  - $ {ui.tr1.value}   - $ {ui.tr2.value}   - $ {ui.tr3.value}   - $ {ui.tr4.value}\n\n"
                                f"  - $ {ui.tr5.value}   - $ {ui.tr6.value}   - $ {ui.tr7.value}   - $ {ui.tr8.value}\n\n"
                                f"  - $ {ui.tr9.value}   - $ {ui.tr10.value}   - $ {ui.tr11.value}   - $ {ui.tr12.value}\n\n"
                                f"--- GASTOS | RETIROS ---\n"
                                f"Cantidad: {ui.grn.value} | Monto Total: $ {ui.grt.value}\n\n"
                                f"  - $ {ui.gr1.value}   - $ {ui.gr2.value}   - $ {ui.gr3.value}\n\n"
                                f"  - $ {ui.gr4.value}   - $ {ui.gr5.value}   - $ {ui.gr6.value}\n\n"
                                f"--- INGRESOS | EGRESOS ---\n"
                                f"INGRESOS - Monto Total: $ {ui.bging.value}\n"
                                f"EGRESOS - Monto Total: $ {ui.bgegr.value}\n\n"
                                f"--- TOTAL DIA PDV ---\n"
                                f"TOTAL EFECTIVO: $ {ui.bgte.value}\n"
                                f"TOTAL GENERAL: $ {ui.bgtd.value}\n\n"

                                f"<<< FIN DEL REPORTE >>>"
                            )