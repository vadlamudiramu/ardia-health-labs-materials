#!/usr/bin/env python3
"""
Convert ArdiA Health Labs Business Development Guide to PDF format
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, PageBreak, SimpleDocTemplate
from reportlab.lib.units import inch
from reportlab.lib import colors
import os

# Read the markdown content
input_file = "/workspace/ardia_health_labs_business_development_guide.md"
output_file = "/workspace/ardia_health_labs_business_development_guide.pdf"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse markdown into sections
def parse_markdown_to_platypus(content):
    """Convert markdown content to ReportLab Platypus elements"""
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1a365d')
    )
    
    heading1_style = ParagraphStyle(
        'Heading1',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        spaceBefore=30,
        textColor=colors.HexColor('#2c5282')
    )
    
    heading2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.HexColor('#2b6cb0')
    )
    
    heading3_style = ParagraphStyle(
        'Heading3',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=10,
        spaceBefore=15,
        textColor=colors.HexColor('#3182ce')
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        alignment=TA_JUSTIFY,
        leading=14
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        leftIndent=20,
        firstLineIndent=-20,
        leading=14
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=8,
        fontName='Courier',
        leftIndent=20,
        backColor=colors.HexColor('#f7fafc')
    )
    
    elements = []
    
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Skip empty lines
        if not line.strip():
            i += 1
            continue
        
        # Headers
        if line.startswith('# '):
            title = line[2:].strip()
            elements.append(Paragraph(title, title_style))
            elements.append(Spacer(1, 20))
        elif line.startswith('## '):
            heading = line[3:].strip()
            elements.append(Paragraph(heading, heading1_style))
        elif line.startswith('### '):
            heading = line[4:].strip()
            elements.append(Paragraph(heading, heading2_style))
        elif line.startswith('#### '):
            heading = line[5:].strip()
            elements.append(Paragraph(heading, heading3_style))
        
        # Code blocks
        elif line.strip().startswith('```'):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().endswith('```'):
                if not lines[i].strip().startswith('#'):
                    code_lines.append(lines[i])
                i += 1
            if code_lines:
                code_text = '\n'.join(code_lines)
                elements.append(Paragraph(code_text.strip(), code_style))
                elements.append(Spacer(1, 10))
            continue
        
        # Regular text (but not list items)
        elif not line.strip().startswith('- ') and not line.strip().startswith('* ') and not line.strip().startswith('1.'):
            # Check if line might be continuation of previous paragraph
            if line.strip() and not line.startswith('---'):
                # Clean up markdown formatting
                text = line.strip()
                text = text.replace('**', '')
                text = text.replace('*', '')
                text = text.replace('_', '')
                text = text.replace('`', '')
                text = text.replace('[', '')
                text = text.replace('](', ' - ')
                text = text.replace(')', '')
                
                if text:
                    elements.append(Paragraph(text, body_style))
        
        # List items
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:].strip()
            # Clean up markdown
            text = text.replace('**', '')
            text = text.replace('*', '')
            text = text.replace('_', '')
            elements.append(Paragraph(f"• {text}", bullet_style))
        elif line.strip().startswith('1.') or line.strip().startswith('2.') or line.strip().startswith('3.'):
            # Numbered lists
            text = line.strip()[3:].strip()
            text = text.replace('**', '')
            elements.append(Paragraph(f"{text}", bullet_style))
        
        # Horizontal rules
        elif line.strip() == '---':
            elements.append(Spacer(1, 20))
        
        i += 1
    
    return elements

# Create the PDF
def create_pdf():
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    elements = parse_markdown_to_platypus(content)
    
    # Add title page
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitlePage',
        parent=styles['Title'],
        fontSize=28,
        spaceAfter=40,
        alignment=1,  # Center
        textColor=colors.HexColor('#1a365d')
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitlePage',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=20,
        alignment=1,
        textColor=colors.HexColor('#4a5568')
    )
    
    date_style = ParagraphStyle(
        'DatePage',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=60,
        alignment=1,
        textColor=colors.HexColor('#718096')
    )
    
    elements.insert(0, Paragraph("ArdiA Health Labs", title_style))
    elements.insert(1, Paragraph("Comprehensive Business Development Guide", subtitle_style))
    elements.insert(2, Paragraph("December 2025", date_style))
    elements.insert(3, PageBreak())
    
    doc.build(elements)
    print(f"PDF created successfully: {output_file}")

if __name__ == "__main__":
    create_pdf()
