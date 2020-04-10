#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 03:36:38 2020
"""
import matplotlib.ticker as tck
import requests
import sys
import matplotlib.pyplot as plt

api_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=tnW5ET0UNTZVpwXcTHUU7AeH6F4jP2A62976GBFa'

  
class Asteroide():
    def __init__(self, self_links, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object):#,close_approach_date):
        
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
        #self.close_approach_date = close_approach_date
        
        
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
obj_=[]
for i in range(len(near_earth_objects)):
    obj_.append(i)
for i in range(len(near_earth_objects)):
    c=0
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
    if i<len(near_earth_objects)+1:
        obj_[i] = Asteroide(self_link_obj, idd, neo_reference_id, name, designation, nasa_jpl_url, absolute_magnitude_h, estimated_diameter_km_min, estimated_diameter_km_max, estimated_diameter_m_min, estimated_diameter_m_max, estimated_diameter_ml_min, estimated_diameter_ml_max, estimated_diameter_ft_min, estimated_diameter_ft_max, is_potentially_hazadours_asteroid, is_sentry_object)
       
        
width = 0.35

labels = ['Minimum diameter', 'Maximum diameter']

fig, ax = plt.subplots()
'''
ax.bar(labels, obj_[2], (-width/2), label='{}'.format(obj_[2].name), color='green')
ax.bar(labels, obj_[9], (-width/2), label = '{}'.format(obj_[9].name)) 
'''
#-------------------------criação de listas para plotagens de graficos-----------------------------
diameter_max_km=[]
diameter_min_km=[]
asteroid_names=[]
sentry_object=[]
for i in range (0,len(near_earth_objects),1):
    diameter_max_km.append(obj_[i].estimated_diameter_km_max)
    diameter_min_km.append(obj_[i].estimated_diameter_km_min)
    asteroid_names.append(obj_[i].name)

plt.rcParams['figure.figsize'] = (70,40) #tamanho do gráfico
plt.bar(asteroid_names, diameter_max_km)
plt.bar(asteroid_names, diameter_min_km)

ax.yaxis.set_minor_locator(tck.AutoMinorLocator())


plt.grid(True)
ax.set_title('Asteroid diameter comparison graph')
ax.legend()
plt.ylabel("Diameter [km]")
plt.xlabel("Asteroid's name")
plt.savefig("Diameter comparison graph.png")
plt.show()



sentry_object_max_diameter=[]
sentry_object_min_diameter=[]
sentry_object_name=[]

print('-----------------------------------------------------------------------------'   )   
for i in range (0,len(near_earth_objects),1):
    if obj_[i].is_sentry_object == False:
        print('The asteroid',obj_[i].name,'\033[32m'+'is not a sentry object'+'\033[32m'+'\033[0;0m')
    elif obj_[i].is_sentry_object == True: 
        print('The asteroid',obj_[i].name,'\033[31m'+'is a sentry object'+'\033[31m'+'\033[0;0m')
        sentry_object_max_diameter.append(obj_[i].estimated_diameter_km_max)
        sentry_object_min_diameter.append(obj_[i].estimated_diameter_km_min)
        sentry_object_name.append(obj_[i].name)
        
width = 0.15        
plt.rcParams['figure.figsize'] = (5,10) #tamanho do gráfico
plt.bar(sentry_object_name, sentry_object_min_diameter, color='blue')
plt.bar(sentry_object_name, sentry_object_max_diameter,color='red')
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
ax.set_title('Diameter of each sentry asteroid')
plt.ylabel("Diameter [km]")
plt.xlabel("Asteroid name")
plt.grid(True)
ax.legend()
plt.savefig("Diameter comparison of sentry asteroids.png")
plt.show()
       
        
        

