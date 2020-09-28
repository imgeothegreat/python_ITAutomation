#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment_path, title,paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment_path)
    report_title = Paragraph(title, styles["h1"])
    paragraph = "<br/>".join(paragraph)
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info])
