import emoji

emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

print("Emojis disponíveis:")
for em, code in emojis_disponiveis.items():
    print(f"{em} - {code}")

frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")

frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

print("\nFrase emojizada:")
print(frase_emojizada)