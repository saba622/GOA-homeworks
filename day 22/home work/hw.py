vegetables = ["კარტოფილი", "სტაფილო", "ბადრიჯანი", "კომბოსტო"]

unwanted = ["კარტოფილი", "ბადრიჯანი"]

replacements = ["ბროკოლი", "ყაბაყი"]

for i in range(len(vegetables)):
    if vegetables[i] in unwanted:
        vegetables[i] = replacements.pop(0)


print(vegetables)