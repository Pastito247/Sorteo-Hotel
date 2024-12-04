<template>
  <div class="verify-email">
    <div class="form-container">
      <h1 class="title">Verificación de Correo</h1>
      <p v-if="loading" class="message">Verificando tu correo...</p>
      <p v-else-if="message" class="message">{{ message }}</p>
      <p v-else class="error">Hubo un problema verificando tu correo.</p>
      <button v-if="verified" @click="goToChangePassword" class="change-password-btn">Cambiar Contraseña</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      loading: true, // Estado inicial de carga
      message: "", // Mensaje de éxito o error
      verified: false, // Bandera para mostrar el botón de cambiar contraseña
    };
  },
  async created() {
    const { uidb64, token } = this.$route.params; // Capturar parámetros desde la URL
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/users/verify-email/${uidb64}/${token}/`
      );
      this.message = response.data.message; // Mensaje del servidor
      this.verified = true; // Marca como verificado
    } catch (error) {
      console.error("Error al verificar el correo:", error);
      this.message = "Hubo un error al verificar tu correo.";
    } finally {
      this.loading = false; // Detiene el estado de carga
    }
  },
  methods: {
    goToChangePassword() {
      this.$router.push("/change-password"); // Redirige a la vista de cambiar contraseña
    },
  },
};
</script>

<style scoped>
.verify-email {
  height: 100vh;
  background-image: url('../assets/img/verify.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.form-container {
  background-color: rgba(255, 255, 255, 0.9);
  padding: 2rem;
  border-radius: 10px;
  max-width: 400px;
  width: 100%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.title {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.message {
  font-size: 1.2rem;
  color: green;
  margin-bottom: 1rem;
}

.error {
  color: red;
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.change-password-btn {
  padding: 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s;
  width: 100%;
}

.change-password-btn:hover {
  background-color: #45a049;
}
</style>
