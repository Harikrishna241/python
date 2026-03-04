from fpdf import FPDF
import pandas as pd
df=pd.read_csv('/Users/macos/Desktop/Python/OOPS/topics.csv')
print(df)

pdf = FPDF(orientation="p",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
for index,row in df.iterrows():
    # Set the font: helvetica bold 12
    pdf.add_page()
    pdf.set_font(family="helvetica",style= "B", size=12)
    pdf.set_text_color(0,0,254)

    # Add a cell (content area)
    pdf.cell(w=0, h=10, txt=row["Topic"],align='L',ln=1,border=0)

    pdf.line(10,20,270,20)
    pdf.cell(w=0, h=10, txt="",align='L',ln=2,border=0)
    for i in range(0,290,5):
        pdf.line(10,25+i,200,25+i)

    pdf.ln(258)
    pdf.cell(w=0, h=10, txt=row["Topic"],align='R',border=0)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        for i in range(0,290,5):
            pdf.line(10,25+i,200,25+i)
        pdf.ln(275)
        pdf.cell(w=0, h=10, txt=row["Topic"],align='R',border=0)
pdf.output("/Users/macos/Desktop/Python/OOPS/hari.pdf")
