def palindromo(sentencia):
    sent = sentencia.replace(' ','').lower()

    if sent == sent[::-1]:
        return True
    return False
