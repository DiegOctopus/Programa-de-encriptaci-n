alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "codificar":
    shift_amount *= -1
  for char in start_text:
    
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Aqui está su resultado al {cipher_direction}: {end_text}")
logo = '''
    _______
---'   ____)____
Encripte su contraseña_)
       ____)
      (____)
---.__(_DS_)
'''

print(logo)

should_end = False
while not should_end:

  direction = input("Teclee 'codificar' para encriptar, teclee 'decodificar' para desencriptar:\n")
  text = input("Teclee su mensaje:\n").lower()
  shift = int(input("Teclee un numero de encriptacion:\n"))

  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Teclee 'si' si quiere encriptar de nuevo. Si quiere terminar teclee 'no'.\n")
  if restart == "no":
    should_end = True
    print("Hasta pronto !")
