import pandas as pd
import numpy as np
class Tablica:

    def Lista(Lista):
        List = []
        List_zapas = Lista
        for i in range(0, len(List_zapas)):
            LS = List_zapas[i]
            List.append(LS)
        
        Unique = pd.unique(List)
        
        List_np_u = []
        List_df = pd.DataFrame(List_zapas)
        for i in range(0, len(Unique)):
            npU = np.where(List_df == Unique[i])
            List_np_u.append(npU)
        
        List_Len = []
        for i in range(0, len(Unique)):
            len_list = len(List_np_u[i][0])
            List_Len.append(len_list)
        
        name_index = []
        for i in range(0, len(Unique)):
            names_Unique = Unique[i]
            name_index.append(names_Unique)
            
        Table_Print = pd.DataFrame(List_Len)
        Table_Print.index = name_index
        Table_Print.columns = ["Counts"]
        Table_Print.sort_values('Counts', ascending = False)
        return(Table_Print)

