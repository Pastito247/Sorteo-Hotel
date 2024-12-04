<template>
  <div class="choose-winner-container">
    <div class="form-container">
      <h2 class="title">Generar Ganador</h2>
      <button @click="chooseWinner" class="btn choose-winner-btn">
        Generar Ganador
      </button>
      <div v-if="winner" class="winner-message">
        <p><strong>{{ winner }}</strong></p>
      </div>
      <div v-if="error" class="error-message">
        <p>{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      winner: null, // Para almacenar el ganador
      error: "", // Para almacenar cualquier error
    };
  },
  methods: {
    async chooseWinner() {
      try {
        const token = localStorage.getItem("access_token"); // Obtener token del localStorage

        // Si el token no existe, mostrar un mensaje de error
        if (!token) {
          this.error = "No estás autenticado. Por favor inicia sesión.";
          return;
        }

        // Hacer la solicitud POST a la API para elegir al ganador
        const response = await axios.post(
          "http://127.0.0.1:8000/api/users/choose-winner/",
          {}, // El cuerpo de la solicitud está vacío
          {
            headers: {
              Authorization: `Bearer ${token}`,
              "Content-Type": "application/json",
            },
          }
        );

        if (response.status === 200) {
          // Si la respuesta es exitosa, asignar al ganador
          this.winner = response.data.message; // Aquí esperamos que la respuesta contenga el nombre del ganador en `message`
        } else {
          this.error = "Hubo un error al generar el ganador.";
        }
      } catch (error) {
        // Manejo mejorado de errores
        if (error.response) {
          // Error con la respuesta del servidor
          this.error = error.response.data.error || "No esta habilitado para escoger ganador.";
        } else if (error.request) {
          // Error en la solicitud (ej. sin respuesta del servidor)
          this.error = "No se recibió respuesta del servidor.";
        } else {
          // Error en la configuración de la solicitud
          this.error = `Error: ${error.message}`;
        }
      }
    },
  },
};
</script>

<style scoped>
.choose-winner-container {
  height: 100vh;
  background-image: url('../assets/img/winner.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.form-container {
  background-color: rgba(255, 255, 255, 0.8);
  padding: 2rem;
  border-radius: 10px;
  max-width: 400px;
  width: 100%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.title {
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.choose-winner-btn {
  padding: 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.choose-winner-btn:hover {
  background-color: #45a049;
}

.winner-message {
  margin-top: 2rem;
  font-size: 1.2rem;
  color: #333;
}

.error-message {
  margin-top: 1rem;
  color: red;
  font-size: 1rem;
}
</style>
