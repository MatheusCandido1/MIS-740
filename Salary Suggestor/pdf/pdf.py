# Python program to create
# a pdf file
from fpdf import FPDF
from fpdf.html import hex2dec
from datetime import date

today = date.today()
date = today.strftime("%B %d, %Y")
recipientName = 'Sweastik Pokhrel'
jobTitle = 'Manager'
companyName = 'XYZ Company'
companyAddress = '1234 ABZ Street'
city = 'Las Vegas'
salary = '100,000'
startDate = '11/25/2022'
colorCode = "#F6546A"

class PDF(FPDF):
    def header(self):
        #font
        self.set_font('times', 'B', 18)
        #set left margin
        self.set_left_margin(15)
        #Title
        self.cell(0,15,"JOB OFFER LETTER", border= False, ln=1, align='L')
        #line break
        self.ln(10)
        
    def body(self, name):
        #read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        #set font    
        self.set_font('times','',12)
        #insert text
        self.multi_cell(180,5,txt)
        #line break
        self.ln(6)
        

def generate_pdf():
    # save FPDF() class into a
    # variable pdf
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("times", size = 12)
    #set the color for the line
    pdf.set_draw_color(*hex2dec(colorCode))
    #set the width of the line
    pdf.set_line_width(2)
    #set the line
    pdf.line(x1 = 15, y1 = 23, x2 = 190, y2 = 23)
    #set margin
    pdf.set_left_margin(15)

    pdf.set_font("times", size = 12)
    # create a cell
    pdf.cell(180, 6, txt = "Date : " + str(date) ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "Recipient Name : " + recipientName ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "Title : " + jobTitle ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "Company Name : " + companyName ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "Address : " + companyAddress ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "City : " + city ,ln = 1)
    # add another cell
    pdf.cell(180, 15, txt = "Dear " + recipientName + "," ,ln = 1)


    pdf.multi_cell(180,5, txt= companyName + "is pleased to offer you the position of " + jobTitle + ". Your skills and experience will be ideal fit for our company." )
    pdf.ln(4)
    pdf.multi_cell(180,5, txt="As we discussed, your starting date will be" + startDate + ". The starting salary is $" +salary+" per year and is paid on a weekly basis. Direct deposit is available." )
    pdf.ln(4)
    pdf.body('body.txt')
    pdf.ln(6)
    pdf.cell(180, 5, txt = "Sincerely, " ,ln = 2)
    pdf.cell(180, 5, txt = companyName ,ln = 2)
    pdf.cell(180, 5, txt = companyAddress + ", " + city ,ln = 2)
    # save the pdf with name .pdf
    pdf.output("Proposal.pdf")
