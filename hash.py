import sqlite3
import hashlib


def hash_passwords():
	conn = sqlite3.connect('Database/Database.db')
	cursor = conn.cursor()

	cursor.execute('SELECT RepublicOfTurkeyIDCardNo, Password FROM Doctors')
	rows = cursor.fetchall()

	for row in rows:
		republic_of_turkey_id_card_no, password = row
		# Check if the password is not hashed (assuming a hashed password is 64 characters long)
		if len(password) != 64:
			hashed_password = hashlib.sha256(password.encode()).hexdigest()
			cursor.execute('UPDATE Doctors SET Password = ? WHERE RepublicOfTurkeyIDCardNo = ?',
						   (hashed_password, republic_of_turkey_id_card_no))
			print(f"Updated ID: {republic_of_turkey_id_card_no}, Password: {hashed_password}")

	conn.commit()
	conn.close()


if __name__ == "__main__":
	hash_passwords()
