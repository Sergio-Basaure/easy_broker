from django.shortcuts import render, redirect
from .requests_properties import RequestAPI
from .form import ContactForm

# Se crea objeto de la clase RequestAPI()
requestApi = RequestAPI()
# path o end_point como variable global
url = 'properties'

def home(request):
    """
        Función encargade de renderizar la página de inicio de la aplicación

        Atributos:
            query = variable que contiene la query que se enviara como parámetro para obtener los datos filtrados
    """
    query = {
        "limit" : 15,
        "search[statuses][]" : "published"
    }
    # properties = requestApi.get_all_properties(url = url, query_serch = query)
    response = requestApi.get_request(url = url, query_serch = query)

    # Condicional para evaluar el resultado de la petición
    if response == 200:
        return render(request, 'propertie/index.html', {'properties' : requestApi.get_properties, 'pagination': requestApi.get_pagination})
    else:
        pass
    

def detail_propertie(request, id):
    """
        Funcion que se encargara de renderizar a una propiedad especifica de acuerdo al id

        Atributos:
            form = 
    """
    
    propertie = requestApi.get_detail_propertie(url = url, id = id)

    # Condicional para verificar el método POST
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Validamos que los campos del formulario sean correctos
        if form.is_valid():
            #Separamos las variables para enviarlas como parámetro en la función send_contact_form
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            source = form.cleaned_data['source']
            requestApi.send_contact_form(name = name, phone = phone, email = email, message = message, id = id, source = source)
            return redirect('propertie:index')
    else:
        form = ContactForm()
    return render(request, 'propertie/detail_propertie.html', {'propertie' : propertie, 'form' : form})

