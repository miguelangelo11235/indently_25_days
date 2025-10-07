adjective_1: str = input("Enter Adjective 1: ")
adjective_2: str = input("Enter Adjective 2: ")
object_1: str = input("Enter Object 1: ")
animal_1: str = input("Enter Animal 1: ")
animal_2: str = input("Enter Animal 2: ")
verb_1: str = input("Enter Verb 1: ")
verb_2: str = input("Enter Verb 2: ")
place: str = input("Enter Place: ")
food: str = input("Enter Food: ")

story: str = f"""
Un día {adjective_1} el {animal_1} escapó del zoológico y decidió {verb_1} por toda la {place}.
En el camino encontró un {object_1}, lo olfateó y gritó: "¡Qué {adjective_2} sorpresa!"
De pronto, apareció el {animal_2}, que comenzó a {verb_2} sin razón alguna.
Al final, ambos se rieron tanto que terminaron comiendo {food} juntos bajo el sol. 
"""
print("Madlibs")
print(story)