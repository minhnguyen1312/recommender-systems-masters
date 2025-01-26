from src.utils.logging import get_logger
import re

def get_admission_criteria(html_content):
    logger = get_logger("Get Admission Criteria")
  
    admission_block = html_content.find("li", attrs={"id": "acc-zulassungsvoraussetzungen"})

    admission_data_list = admission_block.find_all("span", attrs={"class":"status"})
    if admission_data_list is not None:
      admissionModus = admission_block.find("span", attrs={"class":"status zulassungsmodus"}).get_text(strip=True)
      # admissionSem = html_content.find("span", attrs={"class": "status zulassungssemester"}).get_text(strip=True)
      admissionReq = None

      admissionReq = '. '.join(admission_data_list[i].get_text(strip=True) for i in range (2, len(admission_data_list)))
      admissionReq = re.sub(r'\s+', ' ', admissionReq).strip()
      # print(admissionReq)
      return {
          "admission_Modus": admissionModus,
          "admission_Requirements": admissionReq
          }
    else:
      logger.warning("Admission Criteria is missing for this")
      return {
          "admission_Modus": None,
          "admission_Requirements": None
          }