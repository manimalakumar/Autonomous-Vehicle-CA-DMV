##########################################################################################################
### Extracts pdf form fields and field values and puts in text. Then generates csv from text.  ###
##########################################################################################################

### Install the required libraries  ###

#! pip install pdfminer.six
#! pip install spaCy
#! python -m spacy download en
#! pip install pytesseract
#! pip install pdf2image
#! pip install Pillow

### Import dependencies ###

### pdfminer extraction ###
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
from pdfminer.psparser import PSLiteral, PSKeyword
from pdfminer.utils import decode_text

### pdf to image converison ### 
import tempfile
from pdf2image import convert_from_path

### OCR ###
from PIL import Image
import pytesseract

### NLP related ###
import spacy
import re
from spacy import displacy
from spacy.symbols import nsubj, VERB

### System related ###
import glob
import os
from pathlib import Path 

### Other user defined utility files ###
import TextToCSV
#import CAdmvDataAnalysis
#import DisengagementAnalysis

### Load spacy ###
nlp = spacy.load("en_core_web_sm")

### Declare variables ###

# Input pdf directory where original pdf files are kept
p = Path('pdf_files')

# Image directory where pdf to image converted files are kept
img_dir = 'images'

# OCR directory where image to text converted files are kept
img_ocr_text_dir = 'image_to_ocr_text'

# Output directory where text (from pdf form processed and jpg img/ocr processed) files are kept
output_dir = 'output_text_data'

# Final output csv directory and file (after text to csv conversion)
dir = 'output_csv_data'
file_name = 'master_ca_av_data.csv'

# Output csv file header
header = ['Company', 'Date', 'Time', 'Vehicle Damage', 'Weather Veh1', 'Weather Veh2', 'Lighting Veh1', 'Lighting Veh2', 'Road Surface Veh1', 'Road Surface Veh2',
              'Raod Condition Veh1', 'Raod Condition Veh2', 'Movement before Collision Veh1', 'Movement before Collision Veh2', 'Type of Collision Veh1', 
              'Type of Collision Veh2', 'CVC Section Violation Citation', 'Vision Obscurement', 'Inattention', 'Stop n Go Traffic', 'Entering Leaving Ramp', 
              'Previous Collision', 'Unfamiliar with road', 'Defective WEH Equipment', 'Uninvolved Vehicle', 'Other Associated Factor', 'No Factor Apparent',
             'Runaway Vehicle', 'Veh2 condition', 'Mode of Veh1', 'Speed1', 'Context1', 'Speed2', 'Context2', 'Speed3', 'Context3', 'Speed4', 'Context4']

### pdfminer helper method ###
### @param      value       string       pdf field value ###
def decode_value(value):
    # decode PSLiteral, PSKeyword
    if isinstance(value, (PSLiteral, PSKeyword)):
        value = value.name
    # decode bytes
    if isinstance(value, bytes):
        value = decode_text(value)
    return value

### Processes the big text i.e. accident description section n extract info from OCR processed file ###       
### @param1     output_file     string     to which extracted result is appended ### 
### @param2     filename        string     OCR processed file ###
def process_big_text(output_file, filename):    
    btf = open( os.path.join( img_ocr_text_dir, filename ), "r", encoding='utf-8' )
    fcontent = btf.read()

    end_big_text_section = "OL 316"
    pos_x_from_target = 3
    mark = "x"
    mode1 = "Autonomous Mode"
    mode2 = "Conventional Mode"
    mode1_val = "autonomy" 
    mode2_val ="non-autonomy"
    mode_present = "yes"    
    veh2_condtn = "Vehicle2 "
    veh2_default = "no info"
    veh2_condtn1 = "Moving"
    veh2_condtn2 = "Stopped in traffic"
    str_speed = "Speed"
    context = "Context"
    # Speed, Context are new fields created. Values are extracted from accident description. 
    # Autonomy and non-autonomy are new indicators created for driving mode.
    
    #other vehicle state
    condtn1_index = fcontent.find(veh2_condtn1)   
    condtn2_index = fcontent.find(veh2_condtn2)  
    output_file.write(veh2_condtn)
    if mark in fcontent[ :condtn1_index]:
        output_file.write(veh2_condtn1)
    elif mark in fcontent[condtn2_index - pos_x_from_target:condtn2_index]:
        output_file.write(veh2_condtn2)
    if mark not in fcontent[ :condtn1_index] and mark not in fcontent[condtn2_index - pos_x_from_target:condtn2_index]:
        output_file.write(veh2_default)
    output_file.write("\n")
        
    av_mode_index = fcontent.find(mode1)
    phrase_len = len(mode1)   
    #av vs non-av mode: conventional mode contains x after autonomous mode, autonomous mode contains x before autonomous mode after OCR extraction    
    #if mark in fcontent[av_mode_index + phrase_len + 2 : av_mode_index + phrase_len + 3]:
    if mark in fcontent[av_mode_index - pos_x_from_target : av_mode_index + phrase_len]:
        output_file.write(mode1_val)
        output_file.write(' ' + mode_present)
    else:        
        output_file.write(mode2_val)
        output_file.write(' ' + mode_present)
    output_file.write("\n")
        
    start_index = fcontent.find(mode2)
    phrase_len = len(mode2)
    end_index = fcontent.find(end_big_text_section) 
    
    #big text of accident description
    extract_text = fcontent[start_index + phrase_len: end_index]
    #take sentences from the big paragraph where mph is present
    wantTxt = re.findall(r"([^.]*?mph[^.]*\.)",extract_text.lower())
    count = 0
    for sentence in wantTxt:
        count = count+1
        strings = []   
        index = sentence.index('mph')
        speed = sentence[index-3:index]       
        output_file.write(str_speed + str(count))
        output_file.write(speed)        
    
        doc = nlp(sentence)
        
        output_file.write("\n"+context+str(count)+' ')
        for noun_chunk in list(doc.noun_chunks):                      
            output_file.write(str(noun_chunk))            
            output_file.write(":")
        output_file.write("\n") 

### Converts a pdf file to image file. Only page 2 of CA DMV PDF files is converted. ###
### @param1     pdf_filename        string    original pdf file name ### 
### @param2     pdffile             file      original pdf file ###
### @return     <pdf's name>-2.jpg  file ###
def convert_pdf_to_img(pdf_filename,pdffile):     
    image_filename = pdf_filename[0:-4] + "-2.jpg"
    image_file = os.path.join(img_dir, image_filename) 
    pages = convert_from_path(pdffile, 500)
    for idx, page in enumerate(pages, start = 1):
        if idx == 2:
            page.save(image_file, 'JPEG')
    return image_file

### Converts an image file to text file using OCR ###
### @param       image_file     string      image file name
### @output      written to img_ocr_text_dir/img_to_txt_file_name ###
def convert_jpg_to_text(image_file):
    img_to_txt_file_name = os.path.basename(image_file) + ".txt"       
    output_img_to_txt_file = open(os.path.join(img_ocr_text_dir, img_to_txt_file_name), "w", encoding='utf-8')     
   
    str_text = pytesseract.image_to_string(Image.open(image_file))    
    output_img_to_txt_file.write( str_text )
    
    return img_to_txt_file_name

### Extracts form values. Generates CA DMV Form to CSV file. ###
### @output      written to csv file ###
def extract_form_values():
    csv_file = open(os.path.join(dir,file_name), "w") 
    for entry in header:
        csv_file.write("%s , " % entry)
    csv_file.write("\n")
    
    for f in p.glob('*.pdf'):  
        filename = os.path.basename(f)     
        #print ("filename ", filename)  
        
        ### HACK. From web converted file - x sign marks on the field gets extracted! x sign does not work via programmatic method. ### 
        ### In case you face the same issue: ###
        ### Uncomment the below two lines and comment the call to convert_pdf_to_img. ###
        ### Manually convert pdf to image file. Name per the naming convention i.e. filename-2.jpg. Place in the image directory. ###
        #image_filename = filename[0:-4] + "-2.jpg"  
        #image_file = os.path.join(img_dir, image_filename) 

        #Call pdf to image convert
        image_file = convert_pdf_to_img(filename,f)

        #Call OCR
        img_ocr_txt_file = convert_jpg_to_text(image_file)
    
        #It will be the txt file output created from pdf and jpg image files by extracting field values
        form_to_txt_file_name = filename[0:-3] + "txt"
        #print (form_to_txt_file_name)    
        output_file = open(os.path.join(output_dir, form_to_txt_file_name), "w")   

        #Open the pdf file
        with open(f, 'rb') as fp:
            parser = PDFParser(fp)
            doc = PDFDocument(parser)
            res = resolve1(doc.catalog)
            if 'AcroForm' not in res:
                raise ValueError("No AcroForm Found")

            data = {}
            fields = resolve1(doc.catalog['AcroForm'])['Fields']
            #Extract field n value using pdfminer
            for f in fields:
                field = resolve1(f)
                name, values = field.get('T'), field.get('V')
                # decode name
                name = decode_text(name)
                # resolve indirect obj
                values = resolve1(values)
                # decode value(s)
                if isinstance(values, list):
                    values = [decode_value(v) for v in values]
                else:
                    values = decode_value(values)
            
                data.update({name: values})
                #print(name)
                #print ("\n")
                #print (values)
                output_file.write(name)            
                if values is not None:
                   output_file.write(values)
                output_file.write("\n")
            
        process_big_text(output_file, img_ocr_txt_file)    
        output_file.close()
        fp.close()
        TextToCSV.write_CSV(csv_file, output_dir, form_to_txt_file_name)

    csv_file.close()

### Invokes the method(s) ###
def invoke():
    extract_form_values() 
    #CAdmvDataAnalysis.analyze_ca_dmv_data( os.path.join(dir,file_name) ) #CA DMV data analysis using the CSV file generated
    #DisengagementAnalysis.analyze_disengagement() #disengagement data analysis

invoke()
