import emoji

# Lista de emojis disponíveis
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Apresenta os emojis disponíveis
print("Emojis disponíveis:")
for em, code in emojis_disponiveis.items():
    print(f"{em} - {code}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")

# Emojiza a frase
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

# Apresenta a frase emojizada
print("\nFrase emojizada:")
print(frase_emojizada)