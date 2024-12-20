from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "", 45)
        self.image("shirtificate.png", 10, 70, 190)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    your_name = input("Name: ")
    make_shirt(your_ename)


def make_shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=22)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 200, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

