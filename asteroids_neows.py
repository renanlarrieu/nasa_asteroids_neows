import requests
import sys
import matplotlib.pyplot as plt

api_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=OvTHbfDPvJCjyvVIaw0ucxVGlOo6Bmij4yoReqDs'

  
class Asteroide():
    def __init__(self, self_links, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object):
        
        self.idd = idd
        self.self_links = self_links
        self.neo_reference_id = neo_reference_id
        self.name = name
        self.designation = designation
        self.nasa_jpl_url = nasa_jpl_url
        self.absolute_magnitude_h = absolute_magnitude_h
        self.estimated_diameter_km_min = estimated_diameter_km_min
        self.estimated_diameter_km_max = estimated_diameter_km_max
        self.estimated_diameter_m_min = estimated_diameter_m_min
        self.estimated_diameter_m_max = estimated_diameter_m_max
        self.estimated_diameter_ml_min = estimated_diameter_ml_min
        self.estimated_diameter_ml_max = estimated_diameter_ml_min
        self.estimated_diameter_ft_min = estimated_diameter_ft_min
        self.estimated_diameter_ft_max = estimated_diameter_ft_max
        self.is_sentry_object = is_sentry_object 
        
        
class Pagina():
    def __init__(self, size, total_elements, total_pages, number):
        self.size_pg = size
        self.total_elements_pg = total_elements
        self.total_pages_pg = total_pages
        self.number_pg = number


class Links():
    def __init__(self, next_lin, self_lin):
        self.next_lin = next_lin
        self.self_lin = self_lin
        
        
req_url = requests.get(api_url)

if req_url.status_code == 200:
    
    dados = req_url.json()
    
    caps = []
    
    for item in dados:
        caps.append(dados[item])
    
else:
    sys.exit()

# =-=-=-=-=-=- Criação dos super-links do API =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-         

links = []
page = []
near_earth_objects = []

# =-=-=-=-=-=- Atribuição de valor dos super-links -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

links = caps[0]
page = caps[1]
near_earth_objects = caps[2]

# =-=-=-=- Criação do Objeto Links (Primeiro super-link) =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

next_lin = links['next']
self_lin = links['self']

links_obj = Links(next_lin, self_lin)                                           

# =-=-=-=- Criação do Objeto Page (Segundo super-link) =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

size_pg = page['size']
total_elements_pg = page['total_elements']
total_pages_pg = page['total_pages']
number_pg = page['number']

page_obj = Pagina(size_pg, total_elements_pg, total_pages_pg, number_pg)

# =-=-=-=- Criação do Objeto Asteroid [sub-links de near_earth_object(Terceiro super-link)] =-=-=-=-=-=-=-=-

for i in range(len(near_earth_objects)):
    obj = near_earth_objects[i]
    self_link_obj = obj['links']['self']
    idd = obj['id']
    neo_reference_id = obj['neo_reference_id']
    name = obj['name']
    designation = obj['designation']
    nasa_jpl_url = obj['nasa_jpl_url']
    absolute_magnitude_h = obj['absolute_magnitude_h']
    estimated_diameter_km_min = obj['estimated_diameter']['kilometers']['estimated_diameter_min']
    estimated_diameter_km_max = obj['estimated_diameter']['kilometers']['estimated_diameter_max']
    estimated_diameter_m_min  = obj['estimated_diameter']['meters']['estimated_diameter_min']
    estimated_diameter_m_max  = obj['estimated_diameter']['meters']['estimated_diameter_max']
    estimated_diameter_ml_min = obj['estimated_diameter']['miles']['estimated_diameter_min']
    estimated_diameter_ml_max = obj['estimated_diameter']['miles']['estimated_diameter_max']
    estimated_diameter_ft_min = obj['estimated_diameter']['feet']['estimated_diameter_min']
    estimated_diameter_ft_max = obj['estimated_diameter']['feet']['estimated_diameter_max']
    is_potentially_hazadours_asteroid = obj['is_potentially_hazardous_asteroid']
    is_sentry_object = obj['is_sentry_object']
    
    
    if i == 0:
        obj_zero = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 1:
        obj_um = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 2:
        obj_dois = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 3:
        obj_tres = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 4:
        obj_quatro = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 5:
        obj_cinco = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 6:
        obj_seis = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 7:
        obj_sete = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)    
    elif i == 8:
        obj_oito = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 9:
        obj_nove = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 10:
        obj_dez = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 11:
        obj_onze = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 12:
        obj_doze = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 13:
        obj_treze = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 14:
        obj_quatorze = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 15:
        obj_quinze = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 16:
        obj_dezesseis = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 17:
        obj_dezessete = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 18:
        obj_dezoito = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
    elif i == 19:
        obj_dezenove = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)

objeto_dez = [obj_dez.estimated_diameter_m_min, obj_dez.estimated_diameter_m_max]
objeto_tres = [obj_tres.estimated_diameter_m_min, obj_tres.estimated_diameter_m_max]

width = 0.35

labels = ['Diâmetro mínimo', 'Diâmetro máximo']

fig, ax = plt.subplots()

ax.bar(labels, objeto_tres, (-width/2), label='{}'.format(obj_tres.name), color='green')
ax.bar(labels, objeto_dez, (-width/2), label = '{}'.format(obj_dez.name)) 


ax.set_title('Comparativo diâmetro em Metros(m)')
ax.legend()
plt.ylabel("Diâmetro (m)")
plt.savefig("Dmax_e_Dmin.png")
plt.show()









