# coding: utf8
'''
Classe ProtName : Noms de proteines Uniprot
   Attributs :
      - name : nom de la proteine
      - name_kind : categorie de nom ('alternativeName', 'recommendedName', 'submittedName')
      - name_type : Type de nom ('fullName', 'shortName', 'ecNumber')
@author: Sarah Cohen Boulakia
'''
import cx_Oracle
class ProtName:
    
    # Parametre de classe utilise pour dire si les ProtName doivent etre inseres 
    # en base quand insertDB est appele
    DEBUG_INSERT_DB = True
    
    
    def __init__(self, name, name_kind, name_type):
        self._name = name
        self._name_kind= name_kind
        self._name_type = name_type
    
    '''
    Si le nom de proteine (couple nom/type/categorie) n'existe pas deja, 
    ajout en base
    @param curDb: Curseur sur la base de donnees oracle 
    @return identifiant du gene en base de donnees
    ''' 
    def insertDB(self, curDB):
        prot_name_id=-1
        
        #### TODO : Recuperer l'identifiant de nom de proteine 
        #### s'il existe 
        #### Cf. la classe Gene pour un exemple si besoin
        
        if ProtName.DEBUG_INSERT_DB:
            curDB.prepare ("SELECT prot_name_id " \
                                    + " FROM protein_names " \
                                    + " WHERE prot_name=:prot_name " \
                                            + " AND name_type=:name_type" \
                                            + " AND name_kind=:name_kind")
            curDB.execute (None, {'prot_name': self._name, 'name_type': self._name_type, 'name_kind': self._name_kind})
        ####          ####
        #### FIN TODO ####
        
               
        raw = curDB.fetchone ()
        if raw != None:
            prot_name_id = raw[0]
            print("prot:", prot_name_id)
        else:
            if ProtName.DEBUG_INSERT_DB:
                #### TODO : Inserer le nom de proteine dans la table
                #### en utilisant la séquence oracle seq_prot_names
                #### pour avoir l'identifiant. Affecter le résultat 
                #### a la variable prot_name_id
                #### Cf. classe Gene pour un exemple
                idP =curDB.var(cx_Oracle.NUMBER)
                curDB.prepare("INSERT INTO protein_names " \
                                + "(prot_name_id, prot_name, name_kind, name_type) " \
                                + " values " \
                                + " (seq_prot_names.NEXTVAL, :prot_name, " \
                                + " :name_kind, :name_type) " \
                                + " RETURNING prot_name_id INTO :id")
                curDB.execute (None, {'prot_name': self._name, 'name_kind': self._name_kind, 'name_type': self._name_type, 'id': idP})
                prot_name_id = idP.getvalue()[0]
                ####          ####
                #### FIN TODO ####
        return prot_name_id 