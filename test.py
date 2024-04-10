import pdfkit
import io
import base64

# Set options including orientation
options = {
    'orientation': 'Landscape',
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
    'encoding': "UTF-8",
}
report = pdfkit.from_file('testing.html', 'testing.pdf', options=options)
print(report)
