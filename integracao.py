import os.path

import datetime
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def convert_date(date):
    date = date.replace('/', ' ').split()
    date = datetime.date(day=int(date[0]), month=int(date[1]), year=int(date[2]))
    year = date.strftime('%Y')
    month = date.strftime('%B')
    day = date.strftime('%d')
    week_day = date.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return f'{days[week_day]}, {month} {day}, {year}'

def current_day_br(date, for_text=True):
    days_eng = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months_eng = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
    
    days_br = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado','domingo']
    months_br = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    
    date = convert_date(date).replace(',', '').split()
    
    for index, day in enumerate(days_eng):
      if date[0] == day:
        date[0] = days_br[index]
    
    for index, month in enumerate(months_eng):
      if date[1] == month:
        date[1] = months_br[index]
    
    if for_text:
        return f'{date[0].capitalize()}. {date[2]} de {date[1]} de {date[3]}'
    else:
        return f'{date[0]}, {date[1]} {date[2]}, {date[3]}'
        
def integracao(text, id, range, date):
  
  # If modifying these scopes, delete the file token.json.
  SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

  # The ID and range of a sample spreadsheet.
  SAMPLE_SPREADSHEET_ID = id
  SAMPLE_RANGE_NAME = range
  
  creds = None
  if os.path.exists("data/token.json"):
    creds = Credentials.from_authorized_user_file("data/token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "data/credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("data/token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    data = [r for r in result['values']]
    
    values = []
    
    for i, row in enumerate(data):
        if row[0] == current_day_br(date, for_text=False):
          for value in data[i]:
            values.append(value)
          for index, header in enumerate(data[0]):
            text = text.replace('['+header+']', values[index])
            
    text = text.replace('{current date}', current_day_br(date))
    
    text = text.replace('.', '_')
    text = text.replace(',', '.')
    text = text.replace('_', ',')

    return text
      
  except HttpError as err:
    return err