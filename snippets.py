#######################
# Getting data
#######################

# import the stix2 library and the taxii2client libraries
from stix2 import TAXIICollectionSource, Filter
from taxii2client import Collection

# establish TAXII2 Collection instance
collection = Collection("https://limo.anomali.com/api/v1/taxii2/feeds/collections/107/", user="guest", password="guest")

# supply the TAXII2 collection to TAXIICollection
tc_source = TAXIICollectionSource(collection)

# build your filter -- kinda seems broken now
# f1 = Filter("type","=", "indicator")

#retrieve the STIX objects
results = tc_source.query()

print("Retrieving...")
print("Got {} results".format(len(results)))

#######################
# Adding Data Back
#######################

# Note that the password below is incorrect. You can find the real password in the Google Doc
collection = Collection('https://ubertaxii.com/scratch/collections/4a26ee4a-924c-4d5e-8519-5d87efe7f6a8/', user='guest', password='guest')

status = collection.add_objects(str(Bundle(sighting)))