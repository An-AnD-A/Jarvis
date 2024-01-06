from DrMime import FileProcessing, PDFProcessing
import os

test_file_baseloc = r"C:\Users\anand\Projects\Enefit\Reference Materials"
curr_file_name = r"Machine_Learning_Based_Energy_Management_Model_for_Smart_Grid_and_Renewable_Energy_Districts"
extension=r".pdf"
meta_info = PDFProcessing.metadata_extraction(os.path.join(test_file_baseloc,curr_file_name+extension))

FileProcessing.rename_file(base_path=test_file_baseloc, curr_name=curr_file_name, new_name=meta_info.title, extension=".pdf")