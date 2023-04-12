from sortclass import *
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import random


#Para sincronizar con Google sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'C:\Users\Admin\OneDrive\Imágenes\lester\Algoritmo y Estructura de Datos\GoogleSheet'
SPREADSHEET_ID = '1Pb_J5L49hMJ5Q-FnqT8f658eCbt-JWczVe3KsFzDwa4'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def initArray(size=10, maxValue=150, seed=3.14159):
    Listap = Array(size)                   
    random.seed(seed)                   
    for i in range(size):              
        Listap.insert(random.randrange(maxValue)) 
    return Listap                          

lista = initArray()



#Random list
lista.traverse()
print('La matriz desordenada contiene:\n', lista)
Nueva = [[lista.get(i)] for i in range(len(lista))]
range_ ='A2:A11' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range_,
							valueInputOption='USER_ENTERED',
							body={'values':Nueva}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")



#Bubblesort
lista.bubbleSort()
print('Agregado Bubble Sort')
Nueva = [[lista.get(i)] for i in range(len(lista))]
range2_ ='B2:B11' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range2_,
							valueInputOption='USER_ENTERED',
							body={'values':Nueva}).execute()
print(f"Datos insertados de Bubble.\n{(result.get('updates').get('updatedCells'))}")

#insertion sort
lista.insertionSort()
print('Agregado Insertion sort')
Nueva = [[lista.get(i)] for i in range(len(lista))]
range4_ ='D2:D11' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range4_,
							valueInputOption='USER_ENTERED',
							body={'values':Nueva}).execute()
print(f"Datos insertados de insertion.\n{(result.get('updates').get('updatedCells'))}")

#selection sort
lista.selectionSort()
print('Agregado Insertion sort')
Nueva = [[lista.get(i)] for i in range(len(lista))]
range3_ ='C2:C11' 
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range3_,
							valueInputOption='USER_ENTERED',
							body={'values':Nueva}).execute()
print(f"Datos insertados de Selection.\n{(result.get('updates').get('updatedCells'))}")






