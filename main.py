import pdfkit
import matplotlib.pyplot as plt
import io
import base64

# def generate_pdf()
pdfkit.from_file('invoice.html', 'index.pdf')

# pdfkit.from_url('http://127.0.0.1:5501/invoice.html', 'example.pdf')


class GenerateChartUtiity:

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

        # Create bar chart
        plt.figure(figsize=(6, 3))
        bars = plt.bar(categories, values, color='orange', edgecolor='black')

        # Remove top and right spines
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)

        return plt

    @staticmethod
    def make_chart(categories: list, values: list):
        plt = GenerateChartUtiity.get_plot_object(categories, values)
        image_base64 = GenerateChartUtiity.convert_image_to_base64(plt)
        return image_base64

        # def create_planning_emotion_chart(planning: float = 0, emotion: float = 0):
        #     pass
        #     # Data
        #     # categories = ['Planning', 'Emotion']
        #     # values = [planning, emotion]

        #     # plt.figure(figsize=(6, 3))
        #     # bars = plt.bar(categories, values, color='orange', edgecolor='black')

        #     # # Remove top and right spines
        #     # plt.gca().spines['top'].set_visible(False)
        #     # plt.gca().spines['right'].set_visible(False)

        #     @staticmethod
        #     def create_interpersonal_chart(values: list = list):
        #         # Sample data
        #         categories = ['Resoning', 'Numeric', 'Geometry']
        #         values = [33.7247393072851, 44.351858926981, 28.259835915192]

        #         # get the base64 string
        #         image_base64 = convert_image_to_base64(plt)
        #         return image_base64

        # image_base64 = create_interpersonal_chart()
        # print(image_base64)


if __name__ == '__main__':
    # categories = ['Resoning2', 'Numeric', 'Geometry']
    # values = [53.7247393072851, 44.351858926981, 25.259835915192]
    # images_base64 = GenerateChartUtiity.make_chart(categories, values)
    # print(images_base64)
    pdfkit.from_file('invoice.html', 'index.pdf')
