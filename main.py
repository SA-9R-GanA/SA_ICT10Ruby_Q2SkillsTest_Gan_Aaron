from pyscript import display, document

alkali_metals = {
    "Li":("Lithiun",    3,   6.9410),
    "Na":("Sodium",     11,  22.990),
    "K":("Potassium",   19,  39.098),
    "Rb":("Rubidium",   37,  85.368),
    "Cs":("Caesium",    55,  132.91),
    "Fr":("Francium",   87,  223)

}

def element_checker(e):
    document.getElementById('result').innerHTML = " "
    element1 = document.getElementById('element_name').value.strip().title()

    result = alkali_metals.get(
        element1,
        ("Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
<b>Symbol:</b> {element1}<br>
<b>Element:</b> {result[0]}<br>
<b>Atomic Number:</b> {result[1]}<br>
<b>Atomic Mass:</b> {result[2]}<br>
"""