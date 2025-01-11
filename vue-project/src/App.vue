<template>
  <div class="form-container">
    <h1 class="form-title">Formulaire de Commande</h1>
    <form @submit.prevent="envoyerCommande" class="form">
      <!-- Client -->
      <div class="form-group">
        <label for="client">Client :</label>
        <select v-model="formulaire.client" class="form-control" required>
          <option value="" disabled>Sélectionnez un client</option>
          <option v-for="client in clients" :key="client.id" :value="client.id">
            {{ client.nom_client }}:{{ client.prenom_client }}-{{ client.adresse_client }}-{{ client.cp_client }}-{{ client.phone_client }}
          </option>
        </select>
      </div>

      <!-- Benne -->
      <div class="form-group">
        <label for="benne">Benne :</label>
        <select v-model="formulaire.benne" class="form-control" required>
          <option value="" disabled>Sélectionnez une benne</option>
          <option v-for="benne in bennes" :key="benne.id" :value="benne.id">
            {{ benne.id_benne }}:{{ benne.nom_benne }}-{{ benne.poids_benne }}-{{ benne.tps_montage_standard }}-{{ benne.tps_peinture_standard }}
          </option>
        </select>
      </div>

      <!-- Camion -->
      <div class="form-group">
        <label for="camion">Camion :</label>
        <select v-model="formulaire.camion" class="form-control" required>
          <option value="" disabled>Sélectionnez un camion</option>
          <option v-for="camion in camions" :key="camion.id" :value="camion.id">
            {{ camion.id_camion }}:{{ camion.marque }}-{{ camion.modele }}-{{ camion.ptc }}-{{ camion.longueur }}-{{ camion.empattement }}
          </option>
        </select>
      </div>

      <!-- Option -->
      <div class="form-group">
        <label for="option">Option :</label>
        <select v-model="formulaire.option" class="form-control" required>
          <option value="" disabled>Sélectionnez une option</option>
          <option v-for="option in options" :key="option.id" :value="option.id">
            {{ option.id_option }}:{{ option.nom_option }}-{{ option.tps_option_standard }}
          </option>
        </select>
      </div>

      <!-- Date de commande -->
      <div class="form-group">
        <label for="date_commande">Date Commande :</label>
        <input v-model="formulaire.date_commande" placeholder="Date Commande" type="date" class="form-control" required>
      </div>

      <!-- Date de livraison prévue -->
      <div class="form-group">
        <label for="date_livraison_prevue">Date Livraison Prévue :</label>
        <input v-model="formulaire.date_livraison_prevue" placeholder="Date Livraison Prévue" type="date" class="form-control" required>
      </div>

      <!-- Date de début de montage -->
      <div class="form-group">
        <label for="date_debut_montage">Date Début Montage :</label>
        <input v-model="formulaire.date_debut_montage" placeholder="Date Début Montage" type="date" class="form-control" required>
      </div>

      <button type="submit" class="btn-submit">Envoyer la commande</button>
    </form>

    <!-- Add Client Form -->
    <h1 class="form-title">Ajouter un Client</h1>
    <form @submit.prevent="addClient">
      <label for="nom_client">Nom</label>
      <input v-model="client.nom_client" type="text" id="nom_client" required>

      <label for="prenom_client">Prénom</label>
      <input v-model="client.prenom_client" type="text" id="prenom_client" required>

      <label for="adresse_client">Adresse</label>
      <textarea v-model="client.adresse_client" id="adresse_client" required></textarea>

      <label for="cp_client">Code Postal</label>
      <input v-model="client.cp_client" type="text" id="cp_client" required>

      <label for="phone_client">Téléphone</label>
      <input v-model="client.phone_client" type="tel" id="phone_client">

      <button type="submit">Ajouter le client</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

// Client Form Data
const client = ref({
  nom_client: '',
  prenom_client: '',
  adresse_client: '',
  cp_client: '',
  phone_client: ''
});

// Command Form Data
const formulaire = ref({
  client: "",
  benne: "",
  camion: "",
  option: "",
  date_commande: "",
  date_livraison_prevue: "",
  date_debut_montage: ""
});

// Data for Select Options
const clients = ref([]);
const bennes = ref([]);
const camions = ref([]);
const options = ref([]);

// Fetch data for dropdowns
const chargerDonnees = async () => {
  try {
    const clientsResponse = await fetch("http://127.0.0.1:8000/api/clients/");
    clients.value = await clientsResponse.json();

    const bennesResponse = await fetch("http://127.0.0.1:8000/api/bennes/");
    bennes.value = await bennesResponse.json();

    const camionsResponse = await fetch("http://127.0.0.1:8000/api/camions/");
    camions.value = await camionsResponse.json();

    const optionsResponse = await fetch("http://127.0.0.1:8000/api/options/");
    options.value = await optionsResponse.json();
  } catch (error) {
    console.error("Erreur lors du chargement des données :", error);
  }
};

// Add a new client
const addClient = async () => {
  try {
    console.log("Données client envoyées :", client.value);
    const response = await axios.post('http://localhost:8000/api/clients/', client.value);
    alert('Client ajouté avec succès !');
    // Reset client form
    client.value = { nom_client: '', prenom_client: '', adresse_client: '', cp_client: '', phone_client: '' };
  } catch (error) {
    console.error('Erreur lors de l\'ajout du client', error);
    alert(`Erreur lors de l'ajout du client: ${error.response ? error.response.data : error.message}`);
  }
};

// Submit the order form
const envoyerCommande = async () => {
  try {
    // Vérification du client sélectionné
    console.log("Client sélectionné :", formulaire.value.client);
    console.log("Données commande envoyées :", formulaire.value);

    const response = await fetch("http://127.0.0.1:8000/api/commandes/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formulaire.value)
    });

    const data = await response.json();
    console.log("Réponse du serveur :", data);

    if (response.ok) {
      alert("Commande envoyée avec succès !");
    } else {
      alert("Erreur lors de l'envoi de la commande : " + (data.error || "Inconnue"));
    }
  } catch (error) {
    console.error("Erreur lors de l'envoi de la commande :", error);
  }
};



// Call the function to load data on mount
chargerDonnees();
</script>

<style scoped>
.form-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #000000;
  border-radius: 5px;
  background-color: #000000;
}

.form-title {
  text-align: center;
  font-size: 1.5em;
  margin-bottom: 30px; /* Espacement avant le titre */
  color: #fff;
}

.form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px; /* Espacement entre les champs */
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #fff;
}

.form-control {
  width: 100%;
  padding: 12px; /* Plus de padding pour plus d'espace dans les champs */
  font-size: 1em;
  border: 1px solid #0a0808;
  border-radius: 5px;
  margin: 0; /* Supprime toute marge supplémentaire */
}

.form-control:focus {
  outline: none;
  border-color: #007bff;
}

textarea.form-control {
  resize: vertical;
}

.btn-submit, button[type="submit"] {
  background-color: #007bff;
  color: rgb(0, 0, 0);
  border: none;
  padding: 12px 15px; /* Ajuster le padding du bouton pour l'uniformité */
  font-size: 1em;
  border-radius: 10px;
  cursor: pointer;
  text-align: center;
  margin-top: 10px; /* Ajouter un petit espacement au-dessus du bouton */
}

.btn-submit:hover, button[type="submit"]:hover {
  background-color: #0fb300;
}
.form-container {
  max-width: 0 auto;
  margin: 0 auto;
  padding: 200px;
  border: 1px solid #fffefe;
  border-radius: 5px;
  background-color: #000000;
}

.form-title {
  text-align: center;
  font-size: 1.5em;
  margin-bottom: 20px;
}

.form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 10px;
  font-size: 1em;
  border: 1px solid #050404;
  border-radius: 5px;
}

.form-control:focus {
  outline: none;
  border-color: #007bff;
}

.btn-submit {
  background-color: #007bff;
  color: rgb(0, 0, 0);
  border: none;
  padding: 10px 15px;
  font-size: 1em;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
}

.btn-submit:hover {
  background-color: #0fb300;
}
</style>
