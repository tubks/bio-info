# coding: utf8
'''
Classe DbRef : Genes Uniprot
   Attributs :
      - type : Type de dbref
      - ref : reference dans la base "type"
@author: Sarah Cohen Boulakia
'''
class DbRef:
    
    # Parametre de classe utilise pour dire si les DbRef doivent etre inserees 
    # en base quand insertDB est appele
    DEBUG_INSERT_DB = True

    def __init__(self, typeRef, ref):
        self._ref = ref
        self._typeRef = typeRef
    
    def insertDB (self, curDB, accession):
        
        if DbRef.DEBUG_INSERT_DB:
            #### TODO : Insertion dbref ####
            ####          ####
            curDB.prepare("INSERT INTO DbRef " \
                            + "(accession, db_type, db_ref) " \
                            + "values " \
                            + "(:accession, " \
                            + ":typeRef, :ref)")
            curDB.execute(None, {'accession':accession, 'typeRef': self._typeRef, 'ref':self._ref})
            #### FIN TODO ####
            