import urllib.parse
from passlib.hash import des_crypt

cookie = "HqdJMl%2F6I1GfgHqhC2ke2qOU7YHqeNDbIbDxc5QHqji5sV22J2.wHqKLFRhYE3%2FO2HqkX4ej2sZDekHqImc8H9JehScHqPa1LGqzYGykHq9WEB8EHrp46Hq7YuOn0ni.fYHqDGMiwNcOvS2HqqUBVtyeudXUHqHYrc28%2FGs9EHqAST6yrgGMQAHqPjELkLDNyx2HqIhkBnrz.mrwHqsc8NAtFeYNcHqaFrJBZkLTeYHq9ekI6yqtkTEHqHUnPDHPo9GAHqv07nghgsVyoHqUERZsImGUDQHqbC7GFN3AaisHqNoZWUF3K.dMHqAKKAZvY.DqwHqFrTWcrRClSgHq8pgEkCQ7eJMHqNg1vBJYvJe6HqBKwx1A%2FjfoE"
guest = "guest:Mo"
admin = "admin:Mo"

salt = cookie[:2]

guest_beginning = des_crypt.hash(guest, salt=salt)  
guest_beginning = urllib.parse.quote(guest_beginning, safe ="")

if guest_beginning in cookie:
    print(guest_beginning)
    print(cookie)
    print()
    print(cookie[15:])
    print()
    admin_beginning = des_crypt.hash(admin, salt=salt)
    admin_beginning = urllib.parse.quote(admin_beginning, safe="")
    admin_cookie = admin_beginning + cookie[15:]
    print(admin_beginning)

print(admin_cookie)