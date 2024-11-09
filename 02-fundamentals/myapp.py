import physics

hmotnost = float(input("Zadej svou váhu na planetě Zemi: "))
# Vypsání váhy uživatele na všech planetách sluneční soustavy a na měsíci
for planeta, g in physics.GRAVITIES.items():
    print(f"{planeta}: {physics.vahaNaPlanete(hmotnost, g):.2f} kg")

cas_zem, _ = physics.padVeVakuu(10, physics.EARTH_GRAVITY);
cas_mesic, _ = physics.padVeVakuu(10, physics.MOON_GRAVITY)
print(f"\nNa planetě Zemi bys ve vakuu padal z 10 metrů {cas_zem:.2f} s.")
print(f"Na měsíci bys z 10 metrů padal {cas_mesic:.2f} s.\n")

vzdalenost = float(input("Zadej libovolnou vzdálenost v metrech: "))
print(f"Světlo urazí {vzdalenost:} m za {physics.jak_rychle_urazi_svetlo(vzdalenost):.12f} s.")

cas = float(input("Zadej časovou prodlevu mezi bleskem a hromem v sekundách: "))
print(f"Blesk uhodil {physics.vzdalenostBlesku(cas):.2f} m daleko od místa pozorování.")