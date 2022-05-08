
#Script done by:
#Bruno Lopes 202000210
#Gonçalo Cachado 202000190
#Samuel Correia 202000094
#Turma: Binf21

from Bio import Entrez
import sys


#Searches for the term in the chosen database and returns the database, webenv and query key
def insert_search():
  #Usage: python3 my_script.py email database term
  Entrez.email = sys.argv[1]
  user_database = sys.argv[2]
  user_term = sys.argv[3]

  search_handle = Entrez.esearch(db = user_database, usehistory="y",term = user_term, idtype="acc")
  search_result = Entrez.read(search_handle)
  web_env = search_result["WebEnv"]
  query_key = search_result["QueryKey"]
  search_handle.close()
  return(user_database, web_env, query_key) 
  
#Gets the sequences saved in the history( by using the webenv and query key) and displays corresponding sequences in fasta format
def fetch_show( user_database, web_env, query_key):
  fetch_handle = Entrez.efetch(db = user_database, query_key = query_key, webenv = web_env, rettype="fasta", retmode="text",
    idtype="acc")
  print(fetch_handle.read())
  fetch_handle.close()

user_database, web_env, query_key = insert_search()
fetch_show(user_database, web_env, query_key)





