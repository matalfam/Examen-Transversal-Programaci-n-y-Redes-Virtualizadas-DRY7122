vlan_id = int(input("Ingrese el número de VLAN: "))

print(f"La VLAN {vlan_id} está en el rango {'normal' if 1 <= vlan_id <= 1005 else 'extendido' if 1006 <= vlan_id <= 4094 else 'no válido'}.")
