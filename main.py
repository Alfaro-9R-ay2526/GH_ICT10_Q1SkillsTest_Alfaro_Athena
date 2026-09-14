from pyscript import display, document

def create_order(e):

    prod1 = document.getElementById('Menu1')
    prod2 = document.getElementById('Menu2')
    prod3 = document.getElementById('Menu3')
    prod4 = document.getElementById('Menu4')

    # Addition: adds the numbers.
    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked

    display(subtotal,target="result")
