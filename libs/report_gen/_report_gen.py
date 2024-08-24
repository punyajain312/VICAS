"""Load Data"""
import pandas as pd

inspection_df = pd.read_csv('inspection.csv')
tires_df = pd.read_csv('tires.csv')
battery_df = pd.read_csv('battery.csv')
exterior_df = pd.read_csv('exterior.csv')
brakes_df = pd.read_csv('brakes.csv')
engine_df = pd.read_csv('engine.csv')


"""Gen Report"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib import colors

def generate_report(serial_number):     # Primary key = Serial number
    # Data Frames
    inspection_data = inspection_df[inspection_df['TruckSerialNumber'] == serial_number].iloc[0]
    tires_data = tires_df[tires_df['InspectionID'] == inspection_data['InspectionID']].iloc[0]
    battery_data = battery_df[battery_df['InspectionID'] == inspection_data['InspectionID']].iloc[0]
    exterior_data = exterior_df[exterior_df['InspectionID'] == inspection_data['InspectionID']].iloc[0]
    brakes_data = brakes_df[brakes_df['InspectionID'] == inspection_data['InspectionID']].iloc[0]
    engine_data = engine_df[engine_df['InspectionID'] == inspection_data['InspectionID']].iloc[0]

    doc = SimpleDocTemplate(f"Inspection_Report_{serial_number}.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    def create_table(data, headers, title):
        table_data = [headers] + [list(data[header] for header in headers)]
        table = Table(table_data, colWidths=[1.5*inch] * len(headers))
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(Paragraph(title, styles['Title']))
        elements.append(table)
        elements.append(Paragraph("<br/>", styles['Normal']))

    # Table for each form query
    create_table(inspection_data, ['TruckSerialNumber', 'TruckModel', 'InspectorName', 'InspectionEmployeeID', 'DateTime', 'Location', 'GeoCoordinates', 'ServiceMeterHours', 'InspectorSignature', 'CustomerName', 'CatCustomerID'], 'Inspection Details')
    create_table(tires_data, ['TirePressureLeftFront', 'TirePressureRightFront', 'TireConditionLeftFront', 'TireConditionRightFront', 'TirePressureLeftRear', 'TirePressureRightRear', 'TireConditionLeftRear', 'TireConditionRightRear', 'OverallTireSummary'], 'Tires Details')
    create_table(battery_data, ['BatteryMake', 'BatteryReplacementDate', 'BatteryVoltage', 'BatteryWaterLevel', 'ConditionOfBattery', 'AnyLeakRust', 'BatteryOverallSummary'], 'Battery Details')
    create_table(exterior_data, ['RustDentDamage', 'OilLeakSuspension', 'OverallSummary'], 'Exterior Details')
    create_table(brakes_data, ['BrakeFluidLevel', 'BrakeConditionFront', 'BrakeConditionRear', 'EmergencyBrake', 'BrakeOverallSummary'], 'Brakes Details')
    create_table(engine_data, ['RustDentsDamage', 'EngineOilCondition', 'EngineOilColor', 'BrakeFluidCondition', 'BrakeFluidColor', 'AnyOilLeak', 'EngineOverallSummary'], 'Engine Details')

    def add_image(image_path, title):
        try:
            img = Image(image_path)
            img.drawHeight = 2*inch
            img.drawWidth = 3*inch
            elements.append(Paragraph(title, styles['Title']))
            elements.append(img)
            elements.append(Paragraph("<br/>", styles['Normal']))
        except:
            elements.append(Paragraph(f"Image not found: {image_path}", styles['Normal']))
    
    # Images
    add_image(f"images/{serial_number}_tires.jpg", "Tires Images")
    add_image(f"images/{serial_number}_battery.jpg", "Battery Images")
    add_image(f"images/{serial_number}_exterior.jpg", "Exterior Images")
    add_image(f"images/{serial_number}_brakes.jpg", "Brakes Images")
    add_image(f"images/{serial_number}_engine.jpg", "Engine Images")
    
    doc.build(elements)

# generate_report('7301234')
