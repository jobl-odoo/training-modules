from xmlrpc import client

# Required variables
url = 'https://jobl-odoo-training-modules-16-0-space-mission-2-6855191.dev.odoo.com'
db = 'jobl-odoo-training-modules-16-0-space-mission-2-6855191'
username = 'admin'
password = 'admin'

# Check for connection to url
common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print("VERSION:", common.version())

# Get uid
uid = common.authenticate(db, username, password, {})
print("UID:", uid)

# Check access right of user
models = client.ServerProxy("{}/xmlrpc/2/object".format(url))
model_access = models.execute_kw(db, uid, password,
                                 'space_mission.spaceship', 'check_access_rights',
                                 ['write'], {'raise_exception': False})
print("MODEL ACCESS:", model_access)


# Explore searching with filters
spaceships = models.execute_kw(db, uid, password,
                  'space_mission.spaceship', 'search',
                  [[['ship_type', 'in', ['small', 'large']]]])

# Explore fields of chosen model based on attributes
spaceship_fields = models.execute_kw(db, uid, password,
                                     'space_mission.spaceship', 'fields_get',
                                     [], {'attributes': ['string', 'type', 'required']})
print("FIELDS:", spaceship_fields)


# Add new spaceship (name only required field)
new_spaceship = models.execute(db, uid, password,
                               'space_mission.spaceship', 'create',
                               [
                                   {
                                       'name': 'Model 4'
                                   }
                               ])
print("NEW SHIP:", new_spaceship)                         