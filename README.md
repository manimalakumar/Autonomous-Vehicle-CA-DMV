# Autonomous-Vehicle-CA-DMV
CA DMV Autonomous Vehicle (AV) Test Result Data Pipeline

### What problem does the CA DMV AV Test Result Data Pipeline solve?
California DMV is the only DMV in the USA publishing AV road test data. However, the data is not readily ingestible for data analysis. 
The DMV data lies in hundreds of forms. The data pipeline processes the form data using primarily Optical Chracter Recognition (OCR) and some Natural Language Processing (NLP).
A neat excel file is generated at the outset. You could also check the article for additional context.

### Setup
1. Install Python 3.9
2. Install Pillow-8.1.0
3. Install pdfminer.six-20201018
4. Install pytesseract-0.3.7-py3.9
5. Install pdf2image-1.14.0
6. Install spacy-3.0
7. Install Visual Studio Community Edition or use Jupyter Notebook or use Google Colab (your preferred environment)
8. Note: The code is tested on the above verisons of libraries. 

### Run the code
1. Input directory: Create a directory named "pdf_files" at the same level as the Python files. 
2. Input file: In the "pdf_files" directory, place all the pdf files. Get the pdf files (i.e. collision reports) from https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-collision-reports/
3. Create four empty directories parallel to "pdf-files" directory: a) "image_to_ocr_text", b) "images", c) "output_text_data" and d) "output_csv_data".
4. Make sure that spacy english is downloaded by running "python -m spacy download en" from the code file. 
5. Run the "invoke" method of "FormFields.py".
6. Check the results in "output_csv_data/master_ca_av_data.csv".
7. Note: The code is tested on the 2019 collision reports on Windows 10.

### Known issues and troubleshooting
1. Creating the pdf to image file is an interim step. Creating the image file programmatically on the fly creates the image files. However, OCR can't extract the data from the image files. It is possibly a resolution issue. As a workaround, a) Convert pdf file to jpeg image by using an online coverter. Use the batch mode rather than individually processing. b) Name the image file as "<pdf file's name>-2.jpg". c) Place the image file(s) under the "images" directory. d) In FormFields.py, comment "convert_pdf_to_img" call and uncomment image flie load. You will see the instructions in the code under "HACK".
2. After the final consolidated CSV file is generated, there could be a few fields misplaced. Just open the excel file and look for any misplacements. Minor corrections and you will be all set.

### Directory structure

#### Top level directory structure
![image](https://user-images.githubusercontent.com/34682445/111552702-45557680-8759-11eb-9439-0e140957929f.png)

#### Input directory content (sample)
![image](https://user-images.githubusercontent.com/34682445/111552846-8d749900-8759-11eb-8ed0-9ce3726953d2.png)

#### If troubleshooting by creating images manually from pdf, place the images like this (follow the file naming convention)
![image](https://user-images.githubusercontent.com/34682445/111552975-cc0a5380-8759-11eb-8020-a635f53aac36.png)

#### Output directory content
![image](https://user-images.githubusercontent.com/34682445/111553090-0a077780-875a-11eb-9776-3c52c866a876.png)
![image](https://user-images.githubusercontent.com/34682445/111553112-155aa300-875a-11eb-8f41-618d3c4c6fb9.png)

### Sample of the generated CSV file (a subset of columns and rows)
![image](https://user-images.githubusercontent.com/34682445/111553243-56eb4e00-875a-11eb-893f-a83b657aea4f.png)






