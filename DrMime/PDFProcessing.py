from PyPDF2 import PdfReader
import typing
import os
from DrMime.FileProcessing import list_dir, rename_file


def metadata_extraction(path: str):
    """
    The function collects the metadata for PDF files.
    :param path: The path to the desired PDF file.
    :dtype path: string
    :return: A dictionary element with metadata information for the pdf file.
    """

    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        meta_info = pdf.metadata
        return meta_info


def rename_all_pdffiles(base_path: str,extension: str):
    """
    The function will collect all the files in the given folder that has the desired extension. Currently, works only
    for pdf (as metadata function) is used.
    :param base_path: The desired folder that needs to be checked
    :param extension: the file extension eg: .pdf etc.
    :return: The files are renamed with pdf title.
    """
    files = list_dir(folder_path=base_path, extension=extension)
    file_data = {file: os.path.join(base_path, file) for file in files}
    for file in files:
        file_metadata = metadata_extraction(path=file_data[file])
        curr_filename = file.rstrip(extension)
        new_filename = file_metadata.title
        rename_file(base_path=base_path, curr_name=curr_filename, new_name=new_filename, extension=extension)
        print(f"Old filename : {curr_filename} \n New filename : {new_filename}")
    return


if __name__ == "__main__":

    rename_all_pdffiles(base_path=r"C:\Users\anand\Projects\Enefit\Reference Materials",extension=".pdf")


