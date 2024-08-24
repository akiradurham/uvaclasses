"""
Query factory for making api calls
"""
from typing import List
import requests as rqs

class QueryFactory:
    """
    This class is designed to generate the queries to get class information from UVA API
    
    Attributes:
        clist (List[int]): list of tuples containing course mnemonics and course numbers
        url (str): the prepped string that allows for course lookups
        
    Methods:
        call_api(): use request library to call with the new urls and return json 
    """
    def __init__(self, clist: List[str], url: str):
        self.clist = clist
        self.url = url

    def call_api(self):
        """
        Actual call function using the class list and prepped url
        """
        output = []
        for course in self.clist:
            try:
                prepped_url = self.url + '&subject=' + course[0] + '&catalog_nbr=' + course[1]
                output.append(rqs.get(prepped_url, timeout=5))
            except (rqs.exceptions.ConnectionError, rqs.exceptions.Timeout,
                    rqs.exceptions.HTTPError, rqs.exceptions.TooManyRedirects) as e:
                print(f"Error: {e}")

    def __str___(self) -> str:
        return f"URL: {self.url} \nClass List: {self.clist}"

# USE CASE EXAMPLE
# clist = [('MATH','3100'), ('PSYC','2150'), ('STAT','2120')]
# url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1'

# for c in clist:
#     r = requests.get(url + '&subject=' + c[0] + '&catalog_nbr=' + c[1])
#     for c in r.json():
#         print(c['subject'], c['catalog_nbr'] + '-' + c['class_section'], c['component'], c['descr'], \
#                 c['class_nbr'], c['class_capacity'], c['enrollment_available'])