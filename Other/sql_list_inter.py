list_test = ["PSA Peugeot Citroen","Suzuki","Fiat Chrysler Automobiles","Honda","Ford", "Hyundai-Kia", "General Motors", "Renault-Nissan","Toyota","VW"]
count = 0
while count < (len(list_test)):
    # Create SQL statement to get gene_identifiers
    sql = '''SELECT * FROM dna_seq WHERE accession_id ="%s" ''' %str(list_test[count])
    identifier = str(list_test[count])
#    cursor = db.cursor()
#    cursor.execute(sql,identifier)
#    seq_info = cursor.fetchall()
#    print(sql)
#    print(isinstance(sql, str))
#    print(" This is my SQL test,",list_test[count])
#    print(count)
    count += 1


list_test2 = ['1','324', '23552', '241', '14', '161', '981']

seq_info = ["PSA Peugeot Citroen","Suzuki","Fiat Chrysler Automobiles","Honda","Ford", "Hyundai-Kia", "General Motors", "Renault-Nissan","Toyota","VW"]

splicesites     =   ""
    ##acc is short for accession, seq is short for sequence
for acc in seq_info:
   # splicesites.append(a[0])
    splicesites +=  (acc[1].replace("..",","))
    print("ACC;", acc[0:])
#    print("1st For:", splicesites)
#    for i in splicesites.split(','):
 #       print("FOR LOOP:",i)


#splices         =   [int(i) for i in splicesites.split(',')] 
#print(splices)
print("END")