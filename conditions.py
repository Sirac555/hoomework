mubteda = 'Men'
tamamliq = "Python"
xeber = "oyrenirem"

cumle = mubteda + ' ' + tamamliq + ' ' + xeber 
print(cumle)











kredit_miqdari = float(input("Kredit miqdarını daxil edin (AZN): "))

if kredit_miqdari < 2000:
    print("2000 AZN-dan aşağı kredit verilmir.")
elif 2000 <= kredit_miqdari <= 10000:
    faiz_orani = 0.05
elif 10000 < kredit_miqdari <= 50000:
    faiz_orani = 0.04
elif 50000 < kredit_miqdari <= 200000:
    faiz_orani = 0.03
elif 200000 < kredit_miqdari <= 500000:
    faiz_orani = 0.02
else:
    print("500000 AZN-dan yuxarı kredit verilmir.")

if kredit_miqdari >= 2000 and kredit_miqdari <= 500000:
    odeyecegi_borc = kredit_miqdari + (kredit_miqdari * faiz_orani)
    print("Ödəməli olduğunuz ümumi borc: ", odeyecegi_borc, "AZN")


