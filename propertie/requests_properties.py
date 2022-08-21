from logging import Filter
from typing import Dict, List, Optional
from urllib import response
import requests

class RequestAPI():
    """ 
        Clase encargada de realizar las peticiones al servidor
    
        Atributos:
            BASE_URL : Dirección de la API.
            API_KEY : Llave para poder acceder a los datos de la API.
            HEADER : Contenedora de la cabecera de la petición a realizar (credenciales).
            properties: Encargada de almacenar la información de las propiedades.
            pagination: Encargada de almacenar la información de la paginación de la web.

     """


    BASE_URL : str = 'https://api.stagingeb.com/v1/'

    API_KEY : str = 'l7u502p8v46ba3ppgvj5y2aad50lb9'

    HEADER : Dict = {'X-Authorization' : API_KEY, 'content-type': 'application/json'}

    properties : Dict = {}

    pagination : Dict = {}


    # Decorador para mejor manejo de los getters y setters
    @property
    def get_properties(self) -> Dict:
        """  
            Función encargada de almacenar las propiedades en el atributo de clase properties

            Retorna:
                Data que se va a almacenar como diccionario en properties
        """
        return self.properties
    

    # Decorador setter de la propiedad properties
    @get_properties.setter
    def set_properties(self, properties: Dict) -> Dict:
        """
            función decoradora para setear o dar valor a al atributo properties
            
            Parámetros:
                self: Hace referencia al objeto de la clase
                properties: Diccionario con la información de las propiedades
        """
        self.properties = properties  


    @property
    def get_pagination(self) -> Dict:
        return self.pagination


    def set_pagination(self, paginatio: Dict) -> Dict:
        self.pagination = paginatio


    def get_request(self, url : str, query_serch : Optional[str] = None) -> Dict:
        """
            función que se encarga de realizar la petición a la API

            Parámetros: 
                self.BASE_URL: Hace referencia al atributo de la clase que contiene la dirección a la cual se realiza la petición
                url: Path o endpoint de la consulta
                query_serch: Parámetros para obtener datos específicos en la petición
                self.HEADER: Referencia al atributo de clase que contiene las credenciales para la petición

            Retorna:
                response.status_code: En caso de que la petición sea exitosa
                response.raise_for_status(): En caso de obtener un error en la petición
        """

        # Variable response que contendrá el resultado y datos de la petición
        response = requests.get(f'{self.BASE_URL}{url}',params = query_serch , headers = self.HEADER)
         
        # condición con la que verificamos el resultado de la petición
        if response.status_code == 200:
            # .jon() para guardar o cambiar el tipo de variable a diccionario
            response_to_dict = response.json()
            # Almacenamos el valor de las propiedades en el atributo de la clase
            self.properties = response_to_dict.get('content')
            # Almacenamos el valor de la paginación en el atributo de la clase
            self.pagination = response_to_dict.get('pagination')

            # Retorna código del resultado de la petición
            return response.status_code
        else:
            # Retorna error al en la petición
            return response.raise_for_status()

    
    def get_detail_propertie(self, url: str, id: str) -> Dict:
        """
            función que se ejecutara siempre y cuando el id a buscar no se encuentre en el atributo de clase properties

            Parámetros:
                self.BASE_URL: Hace referencia al atributo de la clase que contiene la dirección a la cual se realiza la petición
                url: Path o endpoint de la consulta
                id: Referencia al id de la propiedad a buscar
                self.HEADER: Referencia al atributo de clase que contiene las credenciales para la petición

            Retorna:
                response: En caso de que la petición sea exitosa con los datos de la propiedad de forma de diccionario
                response.raise_for_status(): En caso de obtener un error en la petición
        """

        # Variable response que contendrá el resultado y datos de la petición
        response = requests.get(f'{self.BASE_URL}{url}/{id}', headers = self.HEADER)
        # Condición con la que verificamos el resultado de la petición
        if response.status_code == 200:
            # .jon() para guardar o cambiar el tipo de variable a diccionario
            response = response.json()
            # Retorna los datos de la propiedad
            return response
        else:
            # Retorna error al en la petición
            response.raise_for_status()

    
    def send_contact_form(self, name: str, phone: str, email: str, message: str, id: str, source: str) -> None:
        """
            función que se encargara de enviar los datos del formulario web.

            Parámetros:
                name: Nombre registrado en el formulario
                phone: Teléfono registrado en el formulario
                email: Email registrado en el formulario
                message: Mensaje registrado en el formulario
                id: Id de la propiedad

        """
        
        # Variable contenedora de los parámetros
        data = {
            'name' : name,
            'phone' : phone,
            'email' : email,
            'message' : message,
            'property_id' : id,
            "source": source
        }

        # Variable response que contendrá el resultado y datos de la petición
        response = requests.post('https://api.stagingeb.com/v1/contact_requests', data = data, headers = self.HEADER)

        if response.status_code == 200:

            return response.status_code
        else:
            response.raise_for_status()
