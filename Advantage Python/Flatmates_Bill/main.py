from fpdf import FPDF

class Bill:
    '''
    Object that contains data about a bill, such as total amout and period of the bill
    '''

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    '''
    Create a flatmate person who lives in the flat and pays a share of the bill.
    '''

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PDFReport:
    '''
    Generate a PDF withe the name of the flatemates, the period and how much have to pay
    '''

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=1, align='C', ln=1)

        #insert period label and value
        pdf.cell(w=100, h=40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        #insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=100, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=1)

        pdf.output(self.filename)



a_bill = Bill(amount=200, period='March 2020')
john = Flatmate(name='John', days_in_house=20)
marry = Flatmate(name='Marry', days_in_house=25)

print('John pays: ', john.pays(bill=a_bill, flatmate2=marry))
print('Marry pays: ', marry.pays(a_bill, john))

pdf_report = PDFReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=a_bill)