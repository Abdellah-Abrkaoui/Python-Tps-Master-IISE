# this is a module 

# function for converting dollar to MAD
def dollars_to_dirhams(dollars):
    if dollars < 0 :
        raise ValueError("Le montant doit etre positif")
    return dollars * 10


# functionn for converting m to km
def meters_to_kilometers(meters):
    if meters < 0 :
        raise ValueError("La distance doit etre positive")
    return meters/1000



