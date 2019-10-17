if __name__ == '__main__':
    s = 'aA2' #input()
    #s = 'aA'
    #s = '213'
    print(s.isalnum())
    print(s.isalnum() and not s.isdigit())
    print(s.isalnum() and not s.isalpha())
    print(s.isalnum() and not s.isupper())
    print(s.isalnum() and not s.islower())
