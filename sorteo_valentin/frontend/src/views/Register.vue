<template>
  <div class="register-container">
    <div class="form-container">
      <h1 class="title">Registro de Usuario</h1>
      <form @submit.prevent="registerUser">
        <!-- Campo de Usuario -->
        <div class="input-group">
          <label for="username">Primer Nombe</label>
          <input v-model="username" type="text" id="username" required />
        </div>

        <!-- Campo de Correo Electrónico -->
        <div class="input-group">
          <label for="email">Correo Electrónico</label>
          <input v-model="email" type="email" id="email" required />
        </div>

        <!-- Campo de Contraseña -->
        <div class="input-group">
          <label for="password">Contraseña</label>
          <input v-model="password" type="password" id="password" required />
        </div>

        <!-- Botón de Registro -->
        <div class="button-container">
          <button type="submit" class="submit-btn">Registrar</button>
        </div>
      </form>

      <!-- Mensaje de estado -->
      <div v-if="message" :class="{'message': true, 'error': message.includes('error')}">
        <p>{{ message }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";

export default {
  name: "Register",
  setup() {
    // Definir las variables de los campos de entrada
    const username = ref("");
    const email = ref("");
    const password = ref("");
    const message = ref("");

    // Método para registrar al usuario
    const registerUser = async () => {
      // Limpiar el mensaje previo
      message.value = "";

      try {
        const response = await axios.post("http://127.0.0.1:8000/api/users/register/", {
          username: username.value,
          email: email.value,
          password: password.value,
        });

        // Si la solicitud fue exitosa, mostrar un mensaje
        message.value = response.data.message;
      } catch (error) {
        // Si hay un error, mostrarlo en el mensaje
          console.log(error);
        if (error.response) {
          message.value = error.response.data.message || "Hubo un error al registrar el usuario.";
        } else {
          message.value = "Error al conectar con el servidor.";
        }
      }
    };

    return {
      username,
      email,
      password,
      message,
      registerUser,
    };
  },
};
</script>

<style scoped>
.register-container {
  height: 100vh;
  background-image: url('../assets/img/register.jpg');
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

.input-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

label {
  display: block;
  font-size: 1rem;
  margin-bottom: 0.5rem;
  color: #333;
}

input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  margin-bottom: 1rem;
}

.submit-btn {
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

.submit-btn:hover {
  background-color: #45a049;
}

.message {
  margin-top: 2rem;
  font-size: 1.2rem;
  color: green;
}

.message.error {
  color: red;
}
</style>
