
#nesting a list in a dictionary example
american_cities = {
	"West": ["San Francisco", "Los Angeles", "Seattle", "Las Vegas", "San Diego", ],
	"North East": ["New York", "Philadelphia", "Washington DC"],
	"South East": ["Miami", "Orlando", "Charlotte", "Atlanta"],
	"South": ["Dallas", "Austin", "New Orleans"],
	"Mid West": ["Chicago", "Denver"]
	
}
print("American Cities")
for city in american_cities:
	print(city)
	print(american_cities[city])




#Nesting Dictionaries in List
European_cities = [
{
	"country": "France",
	"cities_visited": ["Paris"],
},
{
	"country": "Belgium",
	"cities_visited": ["Brussels"]
},
{
	"country": "Italy",
	"cities_visited": ["Florence", "Rome", "Venice"]
},
{
	"country": "Germany",
	"cities_visited": ["Munich", "Berlin", "Cologne"]
},
{
	"country": "Austria",
	"cities_visited": ["Vienna", "Innsbruck"]
},
{
	"country": "Switzerland",
	"cities_visited": ["Lucerne", "Interlaken"]
},
{
	"country": "Netherlands",
	"cities_visited": ["Amsterdam", "Innsbruck"]
},

]
print("European Cities")
for city in European_cities:
	print(city)

Euro_bucketlist = [
{
	"country": "France",
	"cities_2go": ["Versailles", "Cannes", "Lyon", "Nice"],
},
{
	"country": "Switzerland",
	"cities_2go": ["Geneva", "Zurich"],
},
{
	"country": "Spain",
	"cities_2go": ["Madrid", "Barcelona", ""],
},

]