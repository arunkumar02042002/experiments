import os
import io
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.conf import settings


class GeneratePDF():

    @staticmethod
    def generate_pdf(template_path, context, custom_name=None):
        html = render_to_string(template_path, context)
        print(context)

        result = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), result)

        if not pdf.err:
            if custom_name:
                with open(custom_name, 'wb') as f:
                    f.write(result.getvalue())
                return custom_name
            else:
                # You can set a default name here if no custom name is provided
                pdf_name = "default_name.pdf"
                with open(pdf_name, 'wb') as f:
                    f.write(result.getvalue())
                return pdf_name
        return None


if __name__ == '__main__':
    context = {
        'name': "Arun Kumar",
        "admin_email": "ar@gmail.com",
        "admin_mobile": "1234",
        "order_id": "qwer",
        "firstName": "Dheeraj",
        "lastName": "Kumar",
        "age": "23",
        "mobile": 234,
        "relation": "Brother",
        "total_amount": "200",
        "plan": "plan5"
    }
