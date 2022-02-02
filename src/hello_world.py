import random

random.seed(69420)

print(
  ''.join(
    chr(random.randrange(256) ^ c)
    for c in
    bytes.fromhex('EA8760D97CD68CB754E490D68D37606E97BBC1BD2B25C605CDC0D532BE')
    if random.randrange(2)
  )
)
