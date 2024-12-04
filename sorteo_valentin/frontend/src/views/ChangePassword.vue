<template>
  <div class="change-password-container">
    <div class="form-container">
      <h1>Cambiar Contraseña</h1>
      <form @submit.prevent="changePassword">
        <div>
          <label for="email">Correo Electrónico</label>
          <input v-model="email" type="email" id="email" required />
        </div>
        <div>
          <label for="password">Nueva Contraseña</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit">Cambiar Contraseña</button>
      </form>
      <p v-if="message" class="message">{{ message }}</p>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      message: '',
      error: ''
    };
  },
  methods: {
    async changePassword() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/users/set-password/', {
          email: this.email,
          password: this.password
        });
        this.message = response.data.message;
        
        // Redirigir al login después de cambiar la contraseña correctamente
        this.$router.push({ name: 'Login' });
      } catch (error) {
        this.error = error.response.data.error || 'Error al cambiar la contraseña';
      }
    }
  }
};
</script>

<style scoped>
.change-password-container {
  height: 100vh;
  background-image: url('../assets/img/change_p.jpg');
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
}

h1 {
  text-align: center;
  color: #333;
}

form {
  display: flex;
  flex-direction: column;
}

form div {
  margin-bottom: 1rem;
}

label {
  font-size: 1rem;
  color: #555;
}

input {
  padding: 0.8rem;
  margin-top: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

button {
  padding: 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.1rem;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
}

.message {
  color: green;
  text-align: center;
}

.error {
  color: red;
  text-align: center;
}
</style>
