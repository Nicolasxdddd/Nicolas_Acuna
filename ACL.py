ACLnum = int(input("Cual es el numero de ACL: "))
if ACLnum >= 1 and ACLnum <=99:
    print("Este es un ACL IPV4 estandar. ")
elif ACLnum >= 100 and ACLnum <=199:
    print("Este es una ACL IPV4 extendida. ")
else:
    print("Esta ACL IPV4 no es extendida o estandar. ")
    
