# Definicion de la base de conocimineto
KB = [ X? ]     # =================================================================

# Funcion que resuelve las clausulas individuales
def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            if li == '~'+lj or lj == '~'+li:
                resolvent = [x for x in set(ci) | set(cj) if x != li and x != lj]
                resolvents.append(resolvent)
    return X?	#===================================================================

# Resuelve toda la base de conocimiento
def resolution(X?):	#===========================================================
    clauses = [set(c) for c in KB]
    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1,n)]
        for (ci, cj) in pairs:
            resolvents = X?(ci, cj)      #===========================================
            if [] in resolvents:
                return X?	#====================================================
            new |= set([tuple(c) for c in resolvents])
        if new.issubset(set([tuple(c) for c in clauses])):
            return X?		#====================================================
        for c in new:
            if tuple(c) not in [tuple(x) for x in clauses]:
                clauses.append(list(c))

# Llamado al metodo
result = X?(X?)		#============================================================
print(result)

a=input('\n presionar para terminar')