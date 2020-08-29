#!/usr/bin/env python3

#basic PDF Generation
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, para):
	styles = getSampleStyleSheet()
	report = SimpleDocTemplate(filename)
	report_title = Paragraph(title, styles['h1'])
	content  = Paragraph(para, styles['BodyText'])
	new_line = Spacer(1,20)
	report.build([report_title,new_line, content])