import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("tkinter-42267.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def add_client(address, name, email, phone_number, company, surname):
    client_data = {
        'nom': name,
        'prenom': surname,
        'adresse': address,
        'email': email,
        'numero': phone_number,
        'entreprise': company
    }
    db.collection('clients').add(client_data)
    print("Client added successfully!")

# Example usage
add_client(
    address="123 Main St, Anytown, USA",
    name="John Doe",
    surname="Doe",
    email="johndoe@example.com",
    phone_number="+1234567890",
    company="Doe Enterprises"
)