#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.gardener import Gardener
from models.plant import Plant

print("Resetting tables...")
Plant.drop_table()
Gardener.drop_table()

Gardener.create_table()
Plant.create_table()

# Create gardeners
print("\nCreating gardeners...")
g1 = Gardener("Alice", 12345)
g1.save()

g2 = Gardener("Bob", 67890)
g2.save()

print("Gardeners in database:")
for g in Gardener.get_all():
    print(f" - {g.id}: {g.name}, phone={g.phone}")

# Create plants for Alice
print("\nAdding plants for Alice...")
p1 = Plant("Rose", 15, g1.id)
p1.save()

p2 = Plant("Tulip", 10, g1.id)
p2.save()

print("Plants in database:")
for p in Plant.get_all():
    print(f" - {p.id}: {p.name}, height={p.height}, gardener_id={p.gardener_id}")

# Test find_by_id
print("\nTesting find_by_id:")
gardener = Gardener.find_by_id(g1.id)
print(f"Found gardener: {gardener.name}, phone={gardener.phone}")

plant = Plant.find_by_id(p1.id)
print(f"Found plant: {plant.name}, height={plant.height}")

# Test update
print("\nUpdating Bob's phone number...")
g2.phone = 55555
g2.save()

print("Gardeners after update:")
for g in Gardener.get_all():
    print(f" - {g.id}: {g.name}, phone={g.phone}")

# Test delete
print("\nDeleting Rose plant...")
p1.delete()

print("Plants after deletion:")
for p in Plant.get_all():
    print(f" - {p.id}: {p.name}, height={p.height}, gardener_id={p.gardener_id}")

print("\n✅ Debug script finished successfully!")