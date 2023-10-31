import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheet:
    
    def __init__(self, secret_key_path, sheet_key):
        
        scope = [
            "https://spreadsheets.google.com/feeds", 
            "https://www.googleapis.com/auth/drive", 
            "https://www.googleapis.com/auth/spreadsheets", 
            "https://www.googleapis.com/auth/drive.file", 
            "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name(secret_key_path, scope)
        self.client = gspread.authorize(creds)
        self.sheet_key = sheet_key
        
    def get_all_data(self, tab):
        sheet = self.client.open_by_key(self.sheet_key)
        worksheet = sheet.worksheet(tab)
        return worksheet.get_all_values()
    
    
    def insert_data(self, tab, new_row):
        sheet = self.client.open_by_key(self.sheet_key)
        worksheet = sheet.worksheet(tab)
        worksheet.append_row(new_row)

        
        



