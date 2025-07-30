# TEXT COUNT ANALYSIS
""" Calculates the amount of words, chars, sentences, and paragraphs in a .pdf/.docx/.txt """

import os
import re
import pymupdf
import docx

def user_guide():
    current_working_directory = os.getcwd()
    
    print("\nWelcome!")
    print(f"The current working directory is: {current_working_directory}")
    print("This program will only work on .pdf/.docx/.txt file extensions, please keep in mind.")
    print("Use for rough approximations only.\n")
    


def detect_file_path(file_path):
    ext = os.path.splitext(file_path)[1]

    try:
        match ext:
            case ".pdf":
                pdf_doc = pymupdf.open(file_path)
                pdf_full_text = ""

                for page in pdf_doc:
                    pdf_full_text += page.get_text("text") + "\n"

                pdf_doc.close()
                counting_algorithm(pdf_full_text)    
            

            case ".docx":
                document = docx.Document(file_path)
                docs_full_text = ""

                for paragraph in document.paragraphs:
                    docs_full_text += paragraph.text + "\n"
                
                counting_algorithm(docs_full_text) 


            case ".txt":
                with open(file_path, "r", encoding="utf-8") as txt_full_text:
                    txt_full_text = txt_full_text.read()
                    counting_algorithm(txt_full_text)


            case _:
                print("Please use only valid file extensions. Make sure the path is clear too.")
    
    except (pymupdf.FileNotFoundError, docx.opc.exceptions.PackageNotFoundError, FileNotFoundError):
        print(f"'{file_path}' cannot be found. Make sure to enter the right path\\file name")

    except Exception:
        print(f"Something went wrong. Please report this bug.")
        



def counting_algorithm(text):
    get_word_count = len(re.findall(r"\w+", text))
    get_character_count = len(re.findall(r"\S", text))
    get_sentence_count = len(re.split(r"(?<=[.!?])\s+", text))
    get_paragraph_count = len(re.split(r"\n\n", text))
    
    
                              
    result = {"Word count" : get_word_count,
              "Character count" : get_character_count,
              "Sentence count" : get_sentence_count,
              "Paragraph count" : get_paragraph_count}
    
    display_results(result)



def display_results(results):
    print("\nThe results are as follows...")
    for count_category, total_amount in results.items():
        print(f"{count_category} : {total_amount}")
    print()



user_guide()
detect_file_path(str(input("Enter the path of the file you want to analyse -> ")))