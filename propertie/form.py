from django import forms

class ContactForm(forms.Form):
    """
        Clase para crear formulario

        Atributos:
            name
            phone
            email
            message
            source
            property_id
    """
    name = forms.CharField(label = "Nombre", initial = "John Smith" ,required = True)
    phone = forms.CharField(label = "Contacto", initial = "5559090909",required = True)
    email = forms.EmailField(label = "Email", initial = "mail@example.com" ,required = True)
    message = forms.CharField(label = "Mensaje", initial = "I'm interested in this property. Please contact me." ,required = True)
    source = forms.CharField(label = "source", initial = "mydomain.com", required = True)
    property_id = forms.CharField(disabled = True, label = 'Id', required = True, widget=forms.TextInput(attrs = {
        'hidden': 'true'
    }))
    




