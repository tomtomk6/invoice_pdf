from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_margins(25.0, 5.0, 25.0)
        self.set_line_width(0.0)
        self.set_xy(25.0, 10.0)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'U', 8)
        self.cell(w=210.0, h=40.0, align='L', txt="Tom Klaube - Beratung Online Marketing | Straße Hausnummer | 12345 Frankfurt", border=0)

    def logo(self):
        self.set_xy(155.0, 20.0)
        self.image("logo.png",  link="", w=40, h=40)

    def address(self):
        self.set_xy(25.0, 25.0)
        self.set_font('Arial', "", 12)
        self.cell(w=30.0, h=40.0, align='L', txt="Rechnungsempfänger", border=0)
        self.set_xy(25.0, 30.0)
        self.cell(w=30.0, h=40.0, align='L', txt="Straße Hausnummer", border=0)
        self.set_xy(25.0, 35.0)
        self.cell(w=30.0, h=40.0, align='L', txt="12345 Frankfurt", border=0)

    def date(self):
        self.set_xy(155.0, 45.0)
        self.cell(w=30.0, h=40.0, align='L', txt="Datum: 17.04.2021", border=0)

    def invoice_number(self):
        self.set_xy(25.0, 85.0)
        self.set_font('Arial', "B", 12)
        self.write(5,"Rechnung Nr. XX-X-XXXXXXXX")

    def introduction(self):
        self.set_xy (25.0, 95.0)
        self.set_font('Arial', "", 12)
        self.write(5,"Sehr geehrte Damen und Herren,")

    def introduction_text(self):
        self.set_xy (25.0, 105.0)
        self.set_font('Arial', "", 12)
        self.write(5, "für meine freie Mitarbeit darf ich Ihnen für den Zeitraum 01.01. - 31.01.2021 folgenden Betrag in Rechnung stellen:")

    def table_header(self):
        self.set_xy (25.0, 110.0)
        self.set_font("Arial", "BU", 10)
        self.cell(w=200.0, h=40.0, align='L', txt="Nr.                  Bezeichnung                         Menge                   Einheit in EUR                  Gesamt in EUR", border=0)

    def table_entries(self):
        self.set_font("Arial", "", 12)
        self.set_xy (25.0, 135.0)
        top = self.y

        self.multi_cell(10,5,'1',0,0)
        self.y = top
        self.x = self.x + 10
        self.multi_cell(60,5,'Mitarbeit Online Marketing',0,0)

        self.y = top 
        self.x = self.x + 70
        self.multi_cell(40,5,'XX,XX',0,0)

        self.y = top 
        self.x = self.x + 110
        self.multi_cell(40,5,'XX,XX',0,0)

        self.y = top 
        self.x = self.x + 150
        self.multi_cell(40,5,'XX,XX',0,0)

    def sum_net(self):
        self.set_xy (90.0, 150.0)
        top = self.y
        self.multi_cell(65,5,'Summe netto:',0,0)
        self.y = top
        self.x = self.x + 135
        self.multi_cell(35,5,'XX,XX EUR',0,'R')

    def sum_vat(self):
        self.set_xy (90.0, 160.0)
        top = self.y
        self.multi_cell(65,5,'Umsatzsteuer 19%:',0,0)
        self.y = top
        self.x = self.x + 135
        self.multi_cell(35,5,'XX,XX EUR',0,'R')

    def sum_total(self):
        self.set_font("Arial", "B", 12)
        self.set_xy (90.0, 170.0)
        top = self.y
        self.multi_cell(65,5,'Gesamtbetrag;',0,0)
        self.y = top
        self.x = self.x + 135
        self.multi_cell(35,5,'XX,XX EUR',0,'R')

    def outroduction_text(self):
        self.set_xy (25.0, 190.0)
        self.set_font('Arial', "", 12)
        self.write(5, "Bitte überweisen Sie den Rechnungsbetrag innerhalb von 30 Tagen auf das untenstehende Konto.")

    def greeting_text(self):
        self.set_xy (25.0, 210.0)
        self.write(5, "Mit freundlichen Grüßen")

    def greeting(self):
        self.set_xy (25.0, 220.0)
        self.write(5, "Tom Klaube")

    def footer(self):
        self.set_font("Arial", "", 10)
        self.set_xy (25.0, 255.0)
        top = self.y

        self.multi_cell(30,5,'Anschrift:',0,0)
        self.y = top
        self.x = self.x + 20
        self.multi_cell(110,5,'Straße Hausnummer, 12345 Frankfurt',0,0)

        self.set_xy (25.0, 260.0)
        top = self.y
        self.multi_cell(30,5,'Telefon:',0,0)
        self.y = top
        self.x = self.x + 20
        self.multi_cell(60,5,'XXXX XXX XX XXX',0,0)

        self.y = top
        self.x = self.x + 60
        self.multi_cell(60,5,'Umsatzsteuer-ID:',0,0)
        self.y = top
        self.x = self.x + 90
        self.multi_cell(60,5,'DEXXXXXXXX',0,0)

        self.set_xy (25.0, 265.0)
        top = self.y
        self.multi_cell(30,5,'E-Mail:',0,0)
        self.y = top
        self.x = self.x + 20
        self.multi_cell(60,5,'tk@tomklaube.de',0,0)

        self.y = top
        self.x = self.x + 60
        self.multi_cell(60,5,'IBAN:',0,0)
        self.y = top
        self.x = self.x + 90
        self.multi_cell(60,5,'DEXX XXXX XXXX XXXX XXXX XX',0,0)

        self.set_xy (25.0, 270.0)
        top = self.y
        self.multi_cell(30,5,'Web:',0,0)
        self.y = top
        self.x = self.x + 20
        self.multi_cell(60,5,'www.tomklaube.de',0,0)

        self.y = top
        self.x = self.x + 60
        self.multi_cell(60,5,'BIC:',0,0)
        self.y = top
        self.x = self.x + 90
        self.multi_cell(60,5,'XXXXXXXXXX',0,0)

    

        

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.header()
pdf.logo()
pdf.address()
pdf.date()
pdf.invoice_number()
pdf.introduction()
pdf.introduction_text()
pdf.table_header()
pdf.table_entries()
pdf.sum_net()
pdf.sum_vat()
pdf.sum_total()
pdf.outroduction_text()
pdf.greeting_text()
pdf.greeting()
pdf.footer()
pdf.output("test.pdf", "F")
