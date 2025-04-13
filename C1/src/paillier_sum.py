from phe import paillier

def generar_claves(bits=2048):
    return paillier.generate_paillier_keypair(n_length=bits)

def cifrar_lista(public_key, valores):
    return [public_key.encrypt(v) for v in valores]

def sumar_cifrados(valores_cifrados):
    return sum(valores_cifrados)

def descifrar(private_key, valor_cifrado):
    return private_key.decrypt(valor_cifrado)
