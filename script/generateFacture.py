from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.utils import ImageReader

def collect_user_input():
    invoice_number = "INV-001"
    created_date = "2022-09-15"
    due_date = "2022-10-15"
    company_name = "ABC Company"
    company_address = "123 Main Street, City, Country"
    company_email = "contact@abccompany.com"
    client_name = "Client Name"
    client_email = "client@email.com"

    items = []
    
    while True:
        item_description = input("Entrez la description de l'article (ou appuyez sur Entrée pour terminer) : ")
        if not item_description:
            break
        item_price = input(f"Entrez le prix de l'article '{item_description}' : ")
        items.append((item_description, item_price))
    
    return {
        "invoice_number": invoice_number,
        "created_date": created_date,
        "due_date": due_date,
        "company_name": company_name,
        "company_address": company_address,
        "company_email": company_email,
        "client_name": client_name,
        "client_email": client_email,
        "items": items,
    }

def generate_invoice(data):
    pdf_file = "facture.pdf"
    document = SimpleDocTemplate(pdf_file, pagesize=A4)
    
    # Conteneur pour les éléments de la facture
    elements = []

    # Logo
    # try:
    #     logo_path = "logo.jpg"
    #     logo = Image(logo_path, width=2*inch, height=2*inch)
    #     elements.append(logo)
    # except FileNotFoundError:
    #     Handle the exception, for example:
    #     elements.append(Paragraph("Logo Not Found", styles['Normal']))
    
    # Informations de l'entreprise et du client
    styles = getSampleStyleSheet()
    company_info = f"""
    <b>{data['company_name']}</b><br/>
    {data['company_address']}<br/>
    {data['company_email']}
    """
    client_info = f"""
    <b>{data['client_name']}</b><br/>
    {data['client_email']}
    """
    
    header_data = [
        [Paragraph(company_info, styles['Normal']), Paragraph(f"Facture #: {data['invoice_number']}<br/>Créée: {data['created_date']}<br/>Échéance: {data['due_date']}", styles['Normal'])],
        [Paragraph(client_info, styles['Normal']), ""]
    ]
    header_table = Table(header_data, colWidths=[4*inch, 2*inch])
    elements.append(header_table)
    elements.append(Spacer(1, 0.5*inch))
    
    # Tableau des articles
    table_data = [
        ["Description", "Prix (€)"]
    ]
    for item_description, item_price in data["items"]:
        table_data.append([item_description, item_price])
    
    # Calculer le total
    total = sum(float(price) for _, price in data['items'])
    table_data.append(["", ""])
    table_data.append(["Total", f"{total:.2f} €"])

    table = Table(table_data, colWidths=[4*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Générer le PDF
    document.build(elements)
    print(f"La facture a été générée avec succès sous forme de {pdf_file}.")

if __name__ == "__main__":
    data = collect_user_input()
    generate_invoice(data)
