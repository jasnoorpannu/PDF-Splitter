import PyPDF2
import os

def split_pdf(input_pdf, output_dir, ranges_and_names):
    print(f'Splitting PDF: {input_pdf}')
    print(f'Saving to directory: {output_dir}')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(input_pdf, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            total_pages = len(reader.pages)

            for range_and_name in ranges_and_names:
                range_str, name = range_and_name
                start, end = map(int, range_str.split('-'))
                start -= 1
                end -= 1 

                writer = PyPDF2.PdfWriter()
                for page_num in range(start, end + 1):
                    if page_num < total_pages:
                        writer.add_page(reader.pages[page_num])
                    else:
                        print(f"Warning: Page {page_num + 1} is out of range.")

                output_filename = os.path.join(output_dir, f'{name}.pdf')
                with open(output_filename, 'wb') as output_pdf:
                    writer.write(output_pdf)

                print(f'Saved: {output_filename}')
    except Exception as e:
        print(f'Error: {e}')

def get_ranges_and_names():
    ranges_and_names = []
    while True:
        range_str = input("Enter the range (e.g., 1-3) or 'done' to finish: ")
        if range_str.lower() == 'done':
            break
        name = input("Enter the name for this range: ")
        ranges_and_names.append((range_str, name))
    return ranges_and_names

if __name__ == "__main__":
    input_pdf = input("Enter the path to the input PDF file: ")
    output_dir = input("Enter the directory to save the split pages: ")

    ranges_and_names = get_ranges_and_names()

    split_pdf(input_pdf, output_dir, ranges_and_names)
