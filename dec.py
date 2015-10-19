#!/user/bin/env python3
import itertools
import sys
import os

# db = SqliteDatabase('perms.db')
# class Perms(Model):
# 	msg = CharField()
# 	key = CharField()
# 	class Meta:
# 		database = db

# def initialize():
# 	"""Create the database and table"""
# 	db.connect()
# 	db.create_tables([Perms], safe=True)

def d(c,k):
	alphabet = "abcdefghijklmnopqrstuvwxyz1234567890 ."
	decrypters = list(k)
	output = ""
	kletter = 0
	for char in c:
		charnum = alphabet.find(char)
		charnum -= alphabet.find(decrypters[kletter])
		charnum = charnum % len(alphabet)
		output += alphabet[charnum]
		kletter = (kletter + 1) % len(k)
	return output


def main_loop1():
	"""Show the menu"""
	i = 0
	alpha = list('abcdefghijklmnopqrstuvwxyz1234567890 .')
	listperm = list(itertools.permutations(alpha, 3))
	while i < len(listperm):
		string_key = ''.join(listperm[i])
		# print(string_key)
		decrypted_message = d('2vy9xq7vg0g6upfgtamtw2ilhgwwtau0s9uptvfvu0tcegtazg3 tmog8hflgptgnmrvvm3xhr.jxehtav wp3rehmbpfsds2pn0w6dcaguw103 s9gq7gg03  .fq7ifs2v dbkaa1gu  wp3ryvmbpetfzrdl0uslc.28ayduu riq.a2m6vsq.qrflb3ue9uwruonepir.28a6ncpsm.78wfv95t9gq7ffnc  uiiaap0aribag7q10byar.78wfrctk9b2revc35g9cmvc2ryptfb2.ahm86ygoo', string_key)
		if decrypted_message.find('fuck') != -1:
			print (decrypted_message)
			print (string_key)
		

		i += 1
		


if __name__ == '__main__':
	# initialize()
	main_loop1()
