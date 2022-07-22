from pygeocoder import Geocoder

endereco = "1222, Lins de Vasconcelos, Sao Paulo, SP"
print(Geocoder("AIzaSyDFUK4jzEUzQ5lf67nbsyFdJ2aF3i79MkA").geocode(endereco).coordinates)

