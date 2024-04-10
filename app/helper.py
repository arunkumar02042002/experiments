from django.conf import settings
import pdfkit
import io
import base64
import matplotlib.pyplot as plt

from django.template.loader import render_to_string

import boto3

import logging

logger = logging.getLogger(__file__)

# Create a formatter object
default_formattor = logging.Formatter(
    fmt='%(name)s:%(asctime)s: %(levelname)s: %(module)s: %(filename)s: %(pathname)s - %(message)s')
file_handler = logging.FileHandler(filename='error.logs')
file_handler.setFormatter(default_formattor)

logger.addHandler(file_handler)


class GenerateReportUtility():

    @staticmethod
    def convert_image_to_base64(plt):
        '''
            function to convert the plot object to base64 

            params: plot object
            returns: base64 of plot object
        '''

        # Creates an in-memory binary stream, which behaves like a file object but operates entirely in memory.
        buffer = io.BytesIO()

        # Is a Matplotlib function that saves the current figure to a file or file-like object.
        plt.savefig(buffer, format='png')

        # After saving the plot to the buffer, we use buffer.seek(0) to move the "file pointer" back to the beginning of the buffer.
        buffer.seek(0)

        # buffer.read() reads the contents of the buffer, which now contains the PNG image data.
        # base64.b64encode() takes the binary image data and encodes it as a base64 string.
        # .decode('utf-8') converts the binary-encoded base64 string to a UTF-8 encoded string.
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        return image_base64

    @staticmethod
    def get_plot_object(categories: list, values: list):
        '''
        function to create plot images

        params:
        categories: list
        values: list

        returns: plot object
        '''

        # Create bar graph
        plt.figure(figsize=(6, 3))
        plt.bar(categories, values, color='orange', edgecolor='black')

        # Remove top and right spines
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)

        return plt

    @ staticmethod
    def generate_report(context: dict, report_name: str):
        # Set options including orientation
        options = {
            'orientation': 'Landscape',
            'margin-top': '0',
            'margin-right': '0',
            'margin-bottom': '0',
            'margin-left': '0',
            'encoding': "UTF-8",
        }

        string = render_to_string('app/testing.html', context=context)
        try:
            report = pdfkit.from_string(string, report_name,
                                        options=options)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def upload_report_to_s3(name: str, pdf):
        try:
            # session = boto3.Session(
            #     aws_access_key_id='AKIAZH33IXRU6G6VZTM3',
            #     aws_secret_access_key='FXMHnEtilFlvaLX78xDLJmnGrroT61ebY6e2fJX',
            #     region_name='ap-south-1'
            # )

            filename = str(name).strip()+'_report.pdf'
            pdf_data = pdf
            s3_client = boto3.client('s3', region_name=settings.AWS_S3_REGION,
                                     aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

            s3_client.upload_file('report.pdf', settings.AWS_STORAGE_BUCKET_NAME, 'report.pdf', ExtraArgs={
                'ACL': 'public-read'})

            return True
        except Exception as e:
            logger.error(msg=e)
            print(e)
            return False
        # try:
        #     object = s3.Object('gtgt65', filename)try:
        #     object = s3.Object('gtgt65', filename)
        #     object.put(ACL='public-read', Body=pdf_data, Key=filename)
        #     return True
        # except Exception as e:
        #     print(e)
        #     return False
        #     object.put(ACL='public-read', Body=pdf_data, Key=filename)
        #     return True
        # except Exception as e:
        #     print(e)
        #     return False


def make_report(data: dict = None):
    # Data
    categories = ['Planning', 'Emotion']
    values = [23.456, 678.23]
    plt = GenerateReportUtility.get_plot_object(
        categories=categories, values=values)
    image_base64 = GenerateReportUtility.convert_image_to_base64(plt)

    context = {
        'firstName': 'Arun',
        'lastName': 'Kumar',
        'url': image_base64,
    }

    reponse = GenerateReportUtility.generate_report(
        context=context, report_name='report.pdf')

    r2 = GenerateReportUtility.upload_report_to_s3('arun', 'report.pdf')

    print(reponse, r2)
