from fruitmand import fruitmand

extra = {
    'name' : 'watermeloen',
    'weight' : 2130,
    'color' : 'green',
    'round' : True
}

fruitmandNew = fruitmand | extra

print(fruitmandNew)