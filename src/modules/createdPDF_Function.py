from fpdf import FPDF
import os

def cells_basicas_FPDF(text1, sl1, text2, sl2, text3, sl3, text4, sl4):
    pdf.cell(15, 10, text1, 1, sl1, 'C')
    pdf.cell(15, 10, text2, 1, sl2, 'C')
    pdf.cell(15, 10, text3, 1, sl3, 'C')
    pdf.cell(15, 10, text4, 1, sl4, 'C')

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font("Arial", "", 10)

pdf.image("../../assets/Images/FresaReporte.png", 10, 7, 20)
pdf.cell(187, 5, f'FECHA', 0, 1, "R")

# Titulo
pdf.cell(0, 23, f'Reporte SUCURSAL'.upper(), 0, 1, 'C')
pdf.line(70, 30, 140, 30)

# pdf.cell(0, 5, '', 0, 1)

# Vasos
pdf.cell(70, 10, 'VASOS', 1, 0, "C")
cells_basicas_FPDF("TI", 0, "TF", 0, "VI", 0, "VF", 0)
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

pdf.cell(0, 1, f'* FIN REPORTE *'.upper(), 0, 1, 'C')

pdf.output(f"../../...Reportes/Reporte.pdf")